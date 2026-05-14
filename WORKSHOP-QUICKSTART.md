# Workshop Quickstart

Use this page when an instructor has already prepared the Microsoft Foundry
project and the development environment for the class.

If you are doing the workshop on your own, start with the normal setup labs in
`labs\notebooks\0-setup` instead.

## Before you start

Your instructor should give you:

| Item | Example |
| --- | --- |
| Group or seat id | `G01` |
| Foundry project endpoint | `https://foundry-ifm-ai-academy-hackathon.services.ai.azure.com/api/projects/hackathon-labs` |
| Model deployment name | `gpt-5.4` |
| Group id in `.env` | `WORKSHOP_GROUP_ID=G01` |
| Which path to follow | Foundry Skills, SDK notebooks, or both |

After this page, use the [Student Lab Guide](./STUDENT-LAB-GUIDE.md) as your
main lab checklist.

This workshop uses one shared Foundry project for the class. To avoid breaking
other groups:

1. Always use your assigned group or seat id in names when a lab asks for a name.
2. Do not run cells or commands labeled `Cleanup` unless the instructor tells you.
3. Do not delete agents, evaluations, traces, deployments, or conversations in the Foundry portal.
4. If you see an error, stop and ask the instructor before retrying many times.

## Choose your environment

### Option 1: GitHub Codespaces

Use this if you are not sure which environment to choose.

1. Open the repository in GitHub.
2. Select **Code**.
3. Select **Codespaces**.
4. Start the Codespace prepared by your instructor, or create a new one if instructed.
5. Wait until setup finishes and the terminal is idle.
6. Confirm that `labs\notebooks\.env` exists. If it does not, ask the instructor for the prepared environment file.

### Option 2: Local VS Code dev container

Use this only if your instructor has asked you to work locally.

1. Install VS Code, Docker Desktop, and the Dev Containers extension before the workshop.
2. Open this repository in VS Code.
3. Select **Reopen in Container** when prompted.
4. Wait until setup finishes and the terminal is idle.
5. Confirm that `labs\notebooks\.env` exists. If it does not, ask the instructor for the prepared environment file.

## Run the readiness check

Before starting the labs:

1. In VS Code, open the Command Palette.
2. Select **Tasks: Run Task**.
3. Select **Workshop: Check readiness**.
4. Wait for the final line.

If the final line says `Workshop readiness: FAIL`, stop and ask the instructor
for help. If it says `PASS with warnings`, read the warnings before continuing.

## Path A: Foundry Skills

This path uses GitHub Copilot Chat and Foundry Skills to guide the
observe-optimize loop.

Start here:

1. Open [Student Lab Guide](./STUDENT-LAB-GUIDE.md).
2. Copy the Path A prompt and fill in your endpoint and group id.
3. Use your group id in any agent, evaluation, dataset, or version names.
4. When Copilot suggests deleting or replacing shared resources, ask the instructor first.

## Path B: Foundry SDK notebooks

This path uses Jupyter notebooks. You do not need to write code, but you will run
notebook cells one at a time.

Start here:

1. Open [Student Lab Guide](./STUDENT-LAB-GUIDE.md).
2. Follow the Path B notebook table.
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
| `labs\notebooks\0-setup\lab-01-setup-codespaces.md` | Environment is already prepared |
| Notebook `Cleanup` sections | They delete shared Foundry resources |
| Portal delete actions | They can affect other groups |

## If something goes wrong

1. Copy the first red error message or take a screenshot.
2. Include your group id.
3. Tell the instructor which path and notebook you are using.
4. Do not share API keys or secrets in chat, screenshots, or issues.
