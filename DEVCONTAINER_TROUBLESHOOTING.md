# Devcontainer and Jupyter troubleshooting

This note documents the issue we hit during the workshop setup and the steps that fixed or isolated it.

## Symptoms

Participants may see one or more of these issues:

- VS Code / Jupyter shows: `Failed to start the Kernel. Missing required @injectable annotation in: Rv.`
- The notebook package install cell does not behave as expected:

  ```python
  %pip install azure-ai-projects>=2.0.0 azure-identity python-dotenv opentelemetry-sdk azure-core-tracing-opentelemetry azure-monitor-opentelemetry pandas --quiet
  ```

- Running the full project dependency install fails:

  ```bash
  pip install -r requirements.txt
  ```

  with a dependency resolution error involving `azure-ai-projects`.

## What was wrong

There were three separate things to separate:

1. The Devcontainer itself was running, but the Python/Jupyter kernel packages were missing in the container.
2. In a normal shell, `azure-ai-projects>=2.0.0` can be parsed incorrectly because `>` is a shell redirection operator. In notebooks, `%pip` usually handles it, but quoting the requirement is safer and works in both contexts.
3. The repository `requirements.txt` used to mix incompatible package requirements:

   ```text
   azure-ai-projects>=2.0.0
   azure-ai-agentserver-agentframework>=1.0.0b16
   ```

   The Agent Framework dependency chain currently pulls `agent-framework-core`, which requires an exact beta version of `azure-ai-projects` such as `2.0.0b3` or `2.0.0b4`. That conflicts with `azure-ai-projects>=2.0.0`, which asks for the stable 2.x release.

   The fix is to align the top-level package pins:

   ```text
   azure-ai-projects==2.0.0b4
   azure-ai-agentserver-agentframework==1.0.0b17
   azure-ai-agentserver-langgraph==1.0.0b17
   ```

## How we fixed the immediate kernel problem

First, confirm that the Devcontainer is running:

```powershell
docker ps -a --filter "name=sad_robinson"
```

Then install and register the Python kernel inside the running container:

```powershell
docker exec sad_robinson /bin/sh -lc "python -m pip install ipykernel jupyter_client --quiet && python -m ipykernel install --user --name python3 --display-name 'Python 3.12 (devcontainer)'"
```

After that, reload VS Code and select the kernel named:

```text
Python 3.12 (devcontainer)
```

## Safer package install command for notebooks in this workshop

Use the same `azure-ai-projects` pin as `requirements.txt`:

```python
%pip install "azure-ai-projects==2.0.0b4" azure-identity python-dotenv opentelemetry-sdk azure-core-tracing-opentelemetry azure-monitor-opentelemetry pandas --quiet
```

If running the same install command in a terminal, use:

```bash
python -m pip install "azure-ai-projects==2.0.0b4" azure-identity python-dotenv opentelemetry-sdk azure-core-tracing-opentelemetry azure-monitor-opentelemetry pandas --quiet
```

## If `pip install -r requirements.txt` fails

This is a dependency conflict, not a Docker problem. Do not mix the stable `azure-ai-projects>=2.0.0` requirement with the current beta Agent Framework packages unless the package versions are aligned.

For the early Foundry SDK / telemetry labs, install only the packages needed by the notebook, but keep the same `azure-ai-projects` pin if this environment will also run the hosted-agent labs:

```bash
python -m pip install "azure-ai-projects==2.0.0b4" azure-identity python-dotenv opentelemetry-sdk azure-core-tracing-opentelemetry azure-monitor-opentelemetry pandas ipykernel jupyter_client --quiet
```

For hosted-agent labs that require the Agent Framework beta packages, use a compatible beta pin set instead of `azure-ai-projects>=2.0.0`, or update the repository requirements once compatible stable package versions are available:

```bash
python -m pip install "azure-ai-projects==2.0.0b4" "azure-ai-agentserver-agentframework==1.0.0b17" "azure-ai-agentserver-langgraph==1.0.0b17"
```
