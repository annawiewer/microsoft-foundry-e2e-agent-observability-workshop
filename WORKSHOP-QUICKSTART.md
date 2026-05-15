# Workshop Quickstart

Use this page when an instructor has already prepared the Microsoft Foundry
project and the development environment for the class.

For this prepared workshop, **Lab 00: Setup Your Foundry Project is already
complete**. Participants should not create a Foundry project or Azure resources.

If you are doing the workshop on your own, start with
[Lab 00: Setup Your Foundry Project](./labs/notebooks/0-setup/lab-00-setup-project.md)
instead.

## Before you start

### What you need

This workshop uses a **local VS Code dev container**. Install or prepare these
before the workshop:

| Requirement | Why you need it |
| --- | --- |
| [Visual Studio Code](https://code.visualstudio.com/) | Opens the repository and notebooks |
| [Docker Desktop](https://www.docker.com/products/docker-desktop/) | Runs the dev container |
| [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) | Reopens the repository inside the container |
| [Git](https://git-scm.com/) | Clones the repository locally |
| Local clone of this repository | Contains the lab files |

You do **not** need to install Python packages manually. The dev container
includes the workshop tools and notebook environment.

Your instructor should give you:

| Item | Example |
| --- | --- |
| Group or seat id | `G01` |
| Foundry project endpoint | `https://foundry-ifm-ai-academy-hackathon.services.ai.azure.com/api/projects/hackathon-labs` |
| Model deployment name | `gpt-5.4` |
| Group id in `.env` | `WORKSHOP_GROUP_ID=G01` |
| Notebook sequence | Main SDK labs, plus optional labs if instructed |

After this page, use the [Student Lab Guide](./STUDENT-LAB-GUIDE.md) as your
main lab checklist.

This workshop uses one shared Foundry project for the class. To avoid breaking
other groups:

1. Do not run Lab 00 or create new Azure/Foundry infrastructure.
2. Always use your assigned group or seat id in names when a lab asks for a name.
3. Do not run cells or commands labeled `Cleanup` unless the instructor tells you.
4. Do not delete agents, evaluations, traces, deployments, or conversations in the Foundry portal.
5. If you see an error, stop and ask the instructor before retrying many times.

## Set up local VS Code

### 1. Install the required programs

Do this before the workshop starts:

1. Download and install [Visual Studio Code](https://code.visualstudio.com/).
2. Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
3. Start Docker Desktop and wait until it says it is running.
4. In VS Code, install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
5. Download and install [Git](https://git-scm.com/).

If Docker Desktop, Git, or VS Code asks you to restart your computer, restart
before continuing.

### 2. Clone the repository

Open PowerShell or another terminal and run:

```powershell
cd $HOME\Desktop
git clone https://github.com/annawiewer/microsoft-foundry-e2e-agent-observability-workshop.git
cd microsoft-foundry-e2e-agent-observability-workshop
code .
```

If your instructor gives you a different repository URL, use that URL in the
`git clone` command instead.

If `code .` does not open VS Code, open VS Code manually and select
**File > Open Folder...**, then choose the cloned repository folder.

### 3. Open the dev container

1. When VS Code opens, select **Reopen in Container**.
2. If you do not see the prompt, open the Command Palette and select **Dev Containers: Reopen in Container**.
3. Wait until setup finishes and the terminal is idle.
4. Confirm that `labs\notebooks\.env` exists. If it does not, ask the instructor for the prepared environment file.

## Run the readiness check

Before starting the labs:

1. In VS Code, open the Command Palette.
2. Select **Tasks: Run Task**.
3. Select **Workshop: Check readiness**.
4. Wait for the final line.

If the final line says `Workshop readiness: FAIL`, stop and ask the instructor
for help. If it says `PASS with warnings`, read the warnings before continuing.

## SDK notebook labs

The workshop uses Jupyter notebooks. You do not need to write code, but you will
run notebook cells one at a time.

Start here:

1. Open [Student Lab Guide](./STUDENT-LAB-GUIDE.md).
2. Follow the SDK notebook table.
3. Select the Python 3.12 kernel when VS Code asks.
4. Run one cell at a time.
5. Stop before any section named `Cleanup`.

Recommended order for a short instructor-led workshop:

| Order | Notebook | Purpose |
| --- | --- | --- |
| 1 | `lab-01-setup.ipynb` | Confirm the prepared project and model work |
| 2 | `lab-02-agent.ipynb` | Create and test a basic travel agent |
| 3 | `lab-03a-tools.ipynb` | Add travel data lookup tools |
| 4 | `lab-04-tracing.ipynb` | View traces and understand observability |
| 5 | `lab-05-evaluation.ipynb` | Evaluate quality and safety |

Use `lab-03b-workflow.ipynb` and `lab-06-redteam.ipynb` when the instructor
explicitly includes them. Red-team scans can take longer, so run them
instructor-led even though the prepared universal project supports them.

## What not to run

Do not run these during a prepared workshop unless instructed:

| File or section | Why |
| --- | --- |
| `labs\notebooks\0-setup\lab-00-setup-project.md` | Infrastructure is already prepared |
| `labs\notebooks\0-setup\lab-01-setup-local-dev-container.md` | Environment is already prepared |
| Notebook `Cleanup` sections | They delete shared Foundry resources |
| Portal delete actions | They can affect other groups |

## If something goes wrong

1. Copy the first red error message or take a screenshot.
2. Include your group id.
3. Tell the instructor which path and notebook you are using.
4. Do not share API keys or secrets in chat, screenshots, or issues.
