# Instructor Guide: Prepared Workshop Mode

Use this guide to run the workshop without asking participants to create
infrastructure or configure their environment during the session.

## Chosen operating model

This repository is currently prepared for:

| Decision | Value |
| --- | --- |
| Foundry resources | One shared Foundry project for the class |
| Environments | GitHub Codespaces and local VS Code dev containers |
| Lab paths | Foundry Skills and Foundry SDK notebooks |
| Branching | Changes are made on the current branch |

The shared-project model is the easiest to explain, but it is also the easiest
to break accidentally. Use group ids, avoid cleanup cells, and keep an instructor
account ready to repair or reset resources.

## Prepare Foundry before the workshop

Create and validate these resources before participants join:

1. Azure resource group for the workshop.
2. Microsoft Foundry project in a region that supports cloud red teaming.
3. Model deployment with enough quota for all participants.
4. Application Insights connected to the Foundry project.
5. Project-connected storage that Foundry Evaluations can reach.
6. A baseline Contoso Travel prompt agent for portal demonstrations.
7. Participant access to the Foundry project and related resources.
8. Optional: pre-run traces, evaluations, and red-team outputs for demo fallback.

This workshop has been validated with one universal project for every lab:

| Setting | Value |
| --- | --- |
| Resource group | `Hackathon-labs` |
| Foundry account | `foundry-ifm-ai-academy-hackathon` |
| Foundry project | `hackathon-labs` |
| Region | `swedencentral` |
| Project endpoint | `https://foundry-ifm-ai-academy-hackathon.services.ai.azure.com/api/projects/hackathon-labs` |
| Model deployment | `gpt-5.4` |
| Storage connection | `foundry-ifm-ai-academy-hackathon-userowned` |
| App Insights connection | `hackathon-labs-appinsights` |

Cloud red teaming is region-dependent. Use a supported region such as
Sweden Central for a live `lab-06-redteam.ipynb` run.

Recommended shared-resource naming pattern:

| Asset | Pattern |
| --- | --- |
| Group id | `G01`, `G02`, `G03` |
| Agents | `G01-contoso-travel` |
| Evaluations | `G01-quality-eval` |
| Datasets | `G01-travel-dataset` |
| Prompt versions | `G01-v1`, `G01-v2` |

## Prepare environment values

Each participant environment needs a `labs\notebooks\.env` file. Do not commit
this file to source control.

Minimum values:

```env
AZURE_AI_PROJECT_ENDPOINT=https://foundry-ifm-ai-academy-hackathon.services.ai.azure.com/api/projects/hackathon-labs
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5.4
WORKSHOP_GROUP_ID=<group or seat id>
WORKSHOP_ALLOW_CLEANUP=
AZURE_TRACING_GEN_AI_CONTENT_RECORDING_ENABLED=true
AZURE_LOG_LEVEL=error
```

Leave `WORKSHOP_ALLOW_CLEANUP` empty during normal shared-project delivery.
Only set it to `1` in an instructor-controlled environment when cleanup cells
should delete resources created by that notebook run.

Do not distribute API keys. The current SDK notebooks, including red teaming,
use Microsoft Entra ID authentication.

## Required access

Use groups instead of assigning roles to individual participants one by one.

| Identity | Scope | Role | Why |
| --- | --- | --- | --- |
| Participant group | Foundry project | `Azure AI User` | Build prompt agents, run conversations, evaluations, and red-team scans in the project |
| Participant group | Foundry account | `Reader` | See the account/project context in Azure/Foundry without managing infrastructure |
| Project managed identity | Foundry project | `Azure AI User` | Required by Foundry project data-plane operations |
| Project managed identity | Foundry account | `Cognitive Services OpenAI User` | Lets evaluation services call the model deployment |
| Project managed identity | Connected storage account | `Storage Blob Data Contributor` | Lets Foundry Evaluations read/write evaluation artifacts |
| Foundry account managed identity | Connected storage account | `Storage Blob Data Contributor` | Supports account/project storage connection flows |
| Instructor/admin group | Subscription or resource group | `Owner` or `Azure AI Owner` plus role assignment rights | Create resources, deploy models, assign roles, and recover the workshop |

Do not give participants broad Azure `Contributor` or `Owner` access unless the
workshop intentionally includes infrastructure provisioning. They do not need
`Cognitive Services OpenAI Contributor` for the prepared labs.

## Codespaces setup

Before the session:

1. Test a fresh Codespace from this repository.
2. Confirm that the devcontainer installs Python dependencies.
3. Place or generate `labs\notebooks\.env` using a secure process.
4. Run the **Workshop: Check readiness** VS Code task.
5. Open `lab-01-setup.ipynb` and run the validation cells.
6. Open Copilot Chat and confirm Foundry Skills are available if using Path A.

For instructor validation, you can also run the readiness script with online
checks from a terminal:

```bash
python labs/notebooks/check-workshop-ready.py --online
```

If participants use personal GitHub accounts, do not assume you can preload
their Codespaces secrets. Have a simple secure fallback for distributing the
prepared `.env` values.

## Local dev container setup

Before the session, tell local participants to install:

1. VS Code.
2. Docker Desktop.
3. VS Code Dev Containers extension.
4. Git.

During validation, test on a machine that is not already configured as the
instructor machine. This catches missing Docker, proxy, and extension issues.

## Participant flow

Use `WORKSHOP-QUICKSTART.md` as the only participant-facing start page.
After readiness checks pass, route participants to `STUDENT-LAB-GUIDE.md` for
the exact click path and copy/paste prompts.

Suggested sequence:

1. Confirm everyone can open the repository.
2. Confirm everyone has a group id.
3. Confirm `labs\notebooks\.env` exists.
4. Run the **Workshop: Check readiness** task.
5. Open `STUDENT-LAB-GUIDE.md`.
6. Start with Path A or Path B based on your agenda.
7. Run red-team scans instructor-led because they are slower and quota-sensitive.

## Shared-project guardrails

Announce these rules at the start:

1. Use the assigned group id in every name.
2. Do not run cleanup cells.
3. Do not delete anything in the Foundry portal.
4. Do not change another group's agent, evaluation, dataset, or prompt version.
5. If something fails, stop and ask for help instead of repeatedly rerunning cells.

## Known risks and mitigations

| Risk | Mitigation |
| --- | --- |
| Name collisions | Use group ids and update notebooks to support prefixes |
| Cleanup cells delete shared assets | Gate cleanup cells or keep them instructor-only |
| Participants lack Azure access | Validate each identity before the session |
| Red-team scans are slow or quota-sensitive | Run instructor-led and keep pre-run output as fallback |
| API keys leak through screenshots | Avoid distributing keys; remind participants not to share secrets |
| Local environments vary | Prefer Codespaces for non-coders |
| Copilot Skills unavailable | Validate Copilot entitlement and extensions before choosing Path A |
| Evaluation runs fail with `ProjectMIUnauthorized` | Confirm the project managed identity has access and the connected storage network allows Foundry Evaluations |
| Red-team scans are unavailable in the project region | Use the validated Sweden Central universal project or another supported-region project |

## Pre-session smoke test

Run this as an instructor from a fresh environment:

1. Open `WORKSHOP-QUICKSTART.md`.
2. Create or open a Codespace.
3. Confirm `labs\notebooks\.env` exists.
4. Run the **Workshop: Check readiness** task.
5. Run `lab-01-setup.ipynb` validation cells.
6. Create a test agent with a unique instructor prefix.
7. Send one test prompt.
8. Confirm traces appear in Foundry or Application Insights.
9. Run one small evaluation or use pre-run evaluation output.
10. Run `lab-06-redteam.ipynb` and confirm a red-team run completes.
11. Confirm cleanup cells are not needed by participants.

## Day-of rescue plan

Keep these ready:

1. A known-good instructor environment projected on screen.
2. Pre-run screenshots or notebook outputs.
3. A list of group ids and assigned participants.
4. A reset procedure for mistakenly deleted agents or evaluations.
5. A short "watch only" path for participants who cannot authenticate in time.
