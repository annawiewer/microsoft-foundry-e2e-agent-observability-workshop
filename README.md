# Observe, Optimize & Protect AI Agents in Microsoft Foundry

This is a hands-on workshop for learning how to build, observe, evaluate,
optimize, and protect AI agents with Microsoft Foundry. The labs use a fictional
travel assistant for **Contoso Travel**.

## Start here

| I am... | Start with | Why |
| --- | --- | --- |
| Joining a live workshop | [Workshop Quickstart](./WORKSHOP-QUICKSTART.md), then [Student Lab Guide](./STUDENT-LAB-GUIDE.md) | Environment check first, lab flow second |
| Facilitating the workshop | [Instructor Guide](./INSTRUCTOR-GUIDE.md) | Setup, guardrails, and day-of checklist |
| Working self-paced | [Infrastructure Setup](./labs/notebooks/0-setup/lab-00-setup-project.md), then [Local Dev Container Setup](./labs/notebooks/0-setup/lab-01-setup-local-dev-container.md) | Build your own Foundry project and environment |
| Looking for help | [Support](./SUPPORT.md) | How to file issues or ask for help |

If you are in an instructor-led workshop, **do not start with Lab 00**. The
Foundry project has already been prepared by your instructor. Your instructor
should provide the Foundry endpoint, model deployment, group id, and prepared
`.env` file.

## What participants need

This workshop uses a **local VS Code dev container**. Install these before the
workshop:

| Requirement | Why you need it |
| --- | --- |
| [Visual Studio Code](https://code.visualstudio.com/) | Opens the workshop repository and notebooks |
| [Docker Desktop](https://www.docker.com/products/docker-desktop/) | Runs the dev container |
| [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) | Reopens the repository inside the container |
| [Git](https://git-scm.com/) | Clones the repository locally |
| Workshop repository cloned locally | Gives VS Code access to the lab files |

You do **not** need to install Python packages manually. The dev container
installs the workshop tools and notebook environment.

You also need access to the prepared Microsoft Foundry project. Your instructor
should provide the project endpoint, model deployment name, assigned group id,
and the prepared `labs\notebooks\.env` file.

## Before the workshop

Complete this setup before the live session starts:

1. Download and install [Visual Studio Code](https://code.visualstudio.com/).
2. Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
3. Start Docker Desktop once and wait until it says it is running.
4. Install the VS Code [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
5. Download and install [Git](https://git-scm.com/).
6. Clone this repository:

   ```powershell
   cd $HOME\Desktop
   git clone https://github.com/Azure-Samples/microsoft-foundry-e2e-agent-observability-workshop.git
   cd microsoft-foundry-e2e-agent-observability-workshop
   code .
   ```

7. When VS Code opens, select **Reopen in Container**.

If `code .` does not open VS Code, open VS Code manually and select
**File > Open Folder...**, then choose the cloned repository folder.

## Participant flow

1. Open [Workshop Quickstart](./WORKSHOP-QUICKSTART.md).
2. Confirm the repository is open in the dev container.
3. Confirm you have your assigned group id.
4. Confirm `labs\notebooks\.env` exists.
5. Run the VS Code task **Workshop: Check readiness**.
6. Open [Student Lab Guide](./STUDENT-LAB-GUIDE.md).
7. Follow the SDK notebook lab sequence.

**Golden rules:** do not run Lab 00 in a prepared workshop, use your group id in
names, run notebook cells one at a time, do not run `Cleanup` sections, do not
delete shared Foundry resources, and stop when you see a red error.

## Main lab path

The workshop now uses one participant path: **SDK notebook labs**. You will run
Jupyter notebook cells step by step in VS Code and inspect the results in
Microsoft Foundry.

| Lab set | Start |
| --- | --- |
| Main SDK notebooks | [Student Lab Guide](./STUDENT-LAB-GUIDE.md#sdk-notebook-labs) |
| Full notebook list | [SDK notebook overview](./labs/notebooks/1-prompt-agents/README.sdk.md#22-lab-notebooks) |
| Optional advanced labs | Use only when the instructor includes them |

## What you will learn

By the end of the main path, you should understand how to:

1. Build a basic travel assistant agent.
2. Ground answers with tools and data.
3. Inspect agent execution with traces.
4. Evaluate quality, safety, and task performance.
5. Improve an agent based on observed results.
6. Protect shared workshop resources by using group-specific names.

## Repository map

| Location | Purpose |
| --- | --- |
| [WORKSHOP-QUICKSTART.md](./WORKSHOP-QUICKSTART.md) | Participant entry point for prepared workshops |
| [STUDENT-LAB-GUIDE.md](./STUDENT-LAB-GUIDE.md) | Main checklist for participants |
| [INSTRUCTOR-GUIDE.md](./INSTRUCTOR-GUIDE.md) | Setup and facilitation guidance |
| [labs/notebooks/0-setup](./labs/notebooks/0-setup) | Self-paced or instructor setup; participants skip Lab 00 in prepared workshops |
| [labs/notebooks/1-prompt-agents](./labs/notebooks/1-prompt-agents) | SDK notebook labs |
| [labs/data](./labs/data) | Sample travel data used by the notebooks |

## Optional background

Contoso Travel is a fictional travel agency. In the labs, you help build an AI
travel assistant that can answer travel questions, use inventory data, produce
traces, run evaluations, and support red-team checks.

Useful Microsoft Foundry references:

| Resource | What it covers |
| --- | --- |
| [Foundry Control Plane](https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview?view=foundry) | Governance and operational control for agents, models, and tools |
| [Observability](https://learn.microsoft.com/en-us/azure/foundry/concepts/observability?view=foundry) | Monitoring and troubleshooting AI agents |
| [Agent Tracing](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept?view=foundry) | OpenTelemetry traces for agent runs |
| [Evaluations](https://learn.microsoft.com/en-us/azure/foundry/concepts/built-in-evaluators?view=foundry) | Built-in and custom quality, safety, and performance evaluators |
| [Red Teaming](https://learn.microsoft.com/en-us/azure/foundry/concepts/ai-red-teaming-agent?view=foundry) | Adversarial testing for AI systems |

## Contributing and legal

Contributions are welcome. Most contributions require a
[Contributor License Agreement](https://cla.opensource.microsoft.com).

This project follows the
[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Use of Microsoft trademarks or logos must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
