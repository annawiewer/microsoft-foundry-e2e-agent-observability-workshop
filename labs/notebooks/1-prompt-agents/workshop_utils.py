"""Small helpers for instructor-led workshop runs."""

from __future__ import annotations

import os
import re


def _group_prefix() -> str:
    raw_group_id = os.environ.get("WORKSHOP_GROUP_ID", "").strip()
    if not raw_group_id:
        return ""
    return re.sub(r"[^A-Za-z0-9-]+", "-", raw_group_id).strip("-")


def workshop_name(base_name: str) -> str:
    """Prefix shared Foundry resource names with the assigned workshop group id."""
    prefix = _group_prefix()
    if not prefix:
        return base_name
    if base_name.lower().startswith(f"{prefix}-"):
        return base_name
    return f"{prefix}-{base_name}"


def print_workshop_context() -> None:
    group_id = os.environ.get("WORKSHOP_GROUP_ID", "").strip()
    if group_id:
        print(f"   Workshop group: {group_id}")
    else:
        print("   Workshop group: not set; using unprefixed resource names")


def require_cleanup_enabled() -> None:
    if os.environ.get("WORKSHOP_ALLOW_CLEANUP", "").strip() == "1":
        return
    raise RuntimeError(
        "Cleanup is disabled for prepared shared-project workshops. "
        "Set WORKSHOP_ALLOW_CLEANUP=1 only if your instructor tells you to run cleanup."
    )
