"""Preflight checks for the prepared workshop environment.

The script intentionally avoids printing secret values. It validates local files,
Python packages, and required environment variables. Use --online for lightweight
network and Azure CLI checks.
"""

from __future__ import annotations

import argparse
import importlib
import os
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


NOTEBOOKS_DIR = Path(__file__).resolve().parent
REPO_ROOT = NOTEBOOKS_DIR.parents[1]
ENV_FILE = NOTEBOOKS_DIR / ".env"

REQUIRED_ENV = (
    "AZURE_AI_PROJECT_ENDPOINT",
    "AZURE_AI_MODEL_DEPLOYMENT_NAME",
)

RECOMMENDED_ENV = (
    "WORKSHOP_GROUP_ID",
    "AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED",
    "AZURE_LOG_LEVEL",
)

PACKAGE_CHECKS = (
    ("python-dotenv", "dotenv"),
    ("azure-ai-projects", "azure.ai.projects"),
    ("azure-identity", "azure.identity"),
    ("pandas", "pandas"),
    ("opentelemetry-sdk", "opentelemetry.sdk"),
    ("azure-monitor-opentelemetry", "azure.monitor.opentelemetry"),
    ("ipykernel", "ipykernel"),
    ("ipywidgets", "ipywidgets"),
    ("jupyter", "jupyter"),
    ("openai", "openai"),
)

REQUIRED_PATHS = (
    "WORKSHOP-QUICKSTART.md",
    "STUDENT-LAB-GUIDE.md",
    "INSTRUCTOR-GUIDE.md",
    "labs/notebooks/sample.env",
    "labs/notebooks/1-prompt-agents/README.skills.md",
    "labs/notebooks/1-prompt-agents/README.sdk.md",
    "labs/notebooks/1-prompt-agents/workshop_utils.py",
    "labs/notebooks/1-prompt-agents/lab-01-setup.ipynb",
    "labs/notebooks/1-prompt-agents/lab-02-agent.ipynb",
    "labs/data/contoso-travel/flights.csv",
    "labs/data/contoso-travel/hotels.csv",
    "labs/data/contoso-travel/car_rentals.csv",
    "labs/data/contoso-travel/evaluation_data.jsonl",
)


class Reporter:
    def __init__(self) -> None:
        self.failures = 0
        self.warnings = 0

    def pass_(self, message: str) -> None:
        print(f"PASS  {message}")

    def warn(self, message: str) -> None:
        self.warnings += 1
        print(f"WARN  {message}")

    def info(self, message: str) -> None:
        print(f"INFO  {message}")

    def fail(self, message: str) -> None:
        self.failures += 1
        print(f"FAIL  {message}")

    def finish(self) -> int:
        print()
        if self.failures:
            print(f"Workshop readiness: FAIL ({self.failures} failure(s), {self.warnings} warning(s))")
            return 1
        if self.warnings:
            print(f"Workshop readiness: PASS with warnings ({self.warnings} warning(s))")
            return 0
        print("Workshop readiness: PASS")
        return 0


def read_env_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            values[key] = value
    return values


def get_value(key: str, env_values: dict[str, str]) -> str:
    return os.environ.get(key, "").strip() or env_values.get(key, "").strip()


def mask_value(value: str) -> str:
    if not value:
        return "<empty>"
    if len(value) <= 12:
        return "<set>"
    return f"{value[:6]}...{value[-4:]}"


def check_paths(reporter: Reporter) -> None:
    for relative_path in REQUIRED_PATHS:
        path = REPO_ROOT / relative_path
        if path.exists():
            reporter.pass_(f"Found {relative_path}")
        else:
            reporter.fail(f"Missing {relative_path}")


def check_packages(reporter: Reporter) -> None:
    for package_name, module_name in PACKAGE_CHECKS:
        try:
            importlib.import_module(module_name)
        except Exception as exc:  # noqa: BLE001 - preflight should report any import failure.
            reporter.fail(f"Python package not ready: {package_name} ({exc.__class__.__name__})")
        else:
            reporter.pass_(f"Python package ready: {package_name}")


def check_env(reporter: Reporter) -> dict[str, str]:
    if ENV_FILE.exists():
        reporter.pass_(r"Found labs\notebooks\.env")
    else:
        reporter.fail(r"Missing labs\notebooks\.env. Ask the instructor for the prepared file.")

    env_values = read_env_file(ENV_FILE)

    for key in REQUIRED_ENV:
        value = get_value(key, env_values)
        if value:
            reporter.pass_(f"{key} is set ({mask_value(value)})")
        else:
            reporter.fail(f"{key} is not set")

    for key in RECOMMENDED_ENV:
        value = get_value(key, env_values)
        if value:
            reporter.pass_(f"{key} is set ({mask_value(value)})")
        else:
            reporter.warn(f"{key} is not set")

    endpoint = get_value("AZURE_AI_PROJECT_ENDPOINT", env_values)
    if endpoint and not endpoint.startswith("https://"):
        reporter.fail("AZURE_AI_PROJECT_ENDPOINT must start with https://")
    if endpoint and "/api/projects/" not in endpoint:
        reporter.warn("AZURE_AI_PROJECT_ENDPOINT does not look like a Foundry project endpoint")

    if get_value("MODEL_API_KEY", env_values):
        reporter.warn("MODEL_API_KEY is set. Do not share the .env file or screenshots containing it.")
    if get_value("WORKSHOP_ALLOW_CLEANUP", env_values) == "1":
        reporter.warn("WORKSHOP_ALLOW_CLEANUP=1. Cleanup cells can delete Foundry resources.")

    return env_values


def run_command(command: list[str], timeout: int = 60) -> subprocess.CompletedProcess[str] | None:
    try:
        return subprocess.run(
            command,
            capture_output=True,
            check=False,
            encoding="utf-8",
            timeout=timeout,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None


def check_online(reporter: Reporter, env_values: dict[str, str]) -> None:
    az_path = shutil.which("az")
    if not az_path:
        reporter.warn("Azure CLI not found. Skip online Azure account check.")
    else:
        account = run_command([az_path, "account", "show", "--query", "id", "--output", "tsv"])
        if account and account.returncode == 0:
            reporter.pass_("Azure CLI is logged in")
        else:
            reporter.warn("Azure CLI is not logged in or cannot read the active account")

    endpoint = get_value("AZURE_AI_PROJECT_ENDPOINT", env_values)
    if not endpoint:
        reporter.warn("Skip endpoint reachability check because AZURE_AI_PROJECT_ENDPOINT is missing")
        return

    try:
        request = Request(endpoint, method="GET")
        with urlopen(request, timeout=10):
            pass
    except HTTPError as exc:
        if exc.code in {401, 403, 404, 405}:
            reporter.pass_(f"Foundry endpoint is reachable (HTTP {exc.code}; auth not validated)")
        else:
            reporter.warn(f"Foundry endpoint returned HTTP {exc.code}")
    except URLError as exc:
        reporter.warn(f"Foundry endpoint was not reachable ({exc.reason})")
    else:
        reporter.pass_("Foundry endpoint is reachable")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check prepared workshop readiness.")
    parser.add_argument(
        "--online",
        action="store_true",
        help="Also check Azure CLI login and endpoint reachability.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    reporter = Reporter()

    print("Checking prepared workshop environment")
    print(f"Repository: {REPO_ROOT}")
    print()

    check_paths(reporter)
    check_packages(reporter)
    env_values = check_env(reporter)

    if args.online:
        check_online(reporter, env_values)
    else:
        reporter.info("Online checks skipped. Run with --online for Azure CLI and endpoint checks.")

    return reporter.finish()


if __name__ == "__main__":
    sys.exit(main())
