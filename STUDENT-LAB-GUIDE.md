# Student Lab Guide

Use this guide during an instructor-led workshop. You do not need to write code.
Your job is to run one step at a time, observe the result, and stop before any
cleanup step.

## Golden rules

1. Use your assigned group id whenever a name is requested.
2. Run notebook cells one at a time.
3. Do not edit code unless the instructor asks you to.
4. Do not run sections named `Cleanup`.
5. Do not delete anything in the Foundry portal.
6. If you see a red error, stop and ask for help.

## Start checklist

Before starting either path:

1. Open `WORKSHOP-QUICKSTART.md`.
2. Confirm `labs\notebooks\.env` exists.
3. Confirm your `.env` includes `WORKSHOP_GROUP_ID`.
4. Run the VS Code task **Workshop: Check readiness**.
5. Continue only when the instructor says the environment is ready.

## Path A: Foundry Skills

Use this path when the instructor wants Copilot Chat to drive the
observe-optimize loop.

Open Copilot Chat and paste this prompt. Replace the placeholders first:

```text
Use the Microsoft Foundry observe skill for this prepared workshop.

Project endpoint: <PASTE_PROJECT_ENDPOINT>
Group id: <PASTE_GROUP_ID>

Evaluate the Contoso Travel agent and help me understand the results.
Prefix every dataset, evaluation, run, and version you create with my group id.
Do not delete, replace, or clean up shared resources unless I explicitly ask.
Before taking an action that changes Foundry resources, briefly tell me what you will create or update.
```

When Copilot responds:

| If Copilot asks... | Do this |
| --- | --- |
| To confirm the project endpoint | Check it matches the instructor-provided endpoint |
| To choose or create names | Use your group id prefix |
| To delete or replace resources | Stop and ask the instructor |
| To run a long evaluation | Ask the instructor if this is part of the current exercise |

Observe these outcomes:

1. Copilot identifies the Foundry project and agent context.
2. Copilot proposes an evaluation or observe loop.
3. Results include quality, safety, or agent-performance findings.
4. The created assets use your group id prefix.

## Path B: SDK notebooks

Use this path when the instructor wants you to run notebook cells.

Open `labs\notebooks\1-prompt-agents\README.sdk.md`, then follow this short
sequence.

| Step | Open | Run | Observe | Stop before |
| --- | --- | --- | --- | --- |
| 1 | `lab-01-setup.ipynb` | All validation cells | Environment variables, model, and data checks are green | None |
| 2 | `lab-02-agent.ipynb` | Cells through multi-turn chat | A basic travel concierge responds | `Cleanup` |
| 3 | `lab-03a-tools.ipynb` | Cells through the tool-backed response | The agent uses travel data tools instead of guessing | `Cleanup` |
| 4 | `lab-04-tracing.ipynb` | Cells through traced queries | Trace output appears and spans can be discussed | `Cleanup` |
| 5 | `lab-05-evaluation.ipynb` | Cells through result display | Evaluation runs complete and show scores | `Cleanup` |

Optional, instructor-led only:

| Notebook | Why optional |
| --- | --- |
| `lab-03b-workflow.ipynb` | Multi-agent workflow is more complex and uses preview functionality |
| `lab-06-redteam.ipynb` | Red-team scans are supported in the prepared project, but they are slower and should be run instructor-led |

## What success looks like

By the end of the main path, you should be able to explain:

1. How a basic travel agent answers customer questions.
2. Why tools reduce hallucinations by grounding answers in data.
3. How traces help diagnose what happened during an agent run.
4. How evaluations measure quality, safety, and task performance.
5. Why shared workshop resources need group-specific names.

## If you finish early

Ask the instructor before starting optional labs. Good next activities are:

1. Compare a traced response with its evaluation score.
2. Ask Foundry portal **Ask AI** to explain a trace.
3. Review the optional workflow notebook without running cleanup.
4. Read pre-run red-team results instead of launching a new scan.
