# Lab 01: Setup Local Development Environment

> **Instructor-led workshop:** Skip this lab if your instructor has already
> prepared a local dev container and provided `labs\notebooks\.env`.
> Start from `WORKSHOP-QUICKSTART.md` instead.

## 1. Install local tools

Install these before you start:

1. Download and install [Visual Studio Code](https://code.visualstudio.com/).
1. Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
1. Start Docker Desktop and wait until it says it is running.
1. In VS Code, install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
1. Download and install [Git](https://git-scm.com/).

If Docker Desktop, Git, or VS Code asks you to restart your computer, restart
before continuing.

You do not need to install Python packages manually. The dev container installs
the workshop tools and notebook environment.

## 2. Clone the repository

Open PowerShell or another terminal and run:

```powershell
cd $HOME\Desktop
git clone https://github.com/Azure-Samples/microsoft-foundry-e2e-agent-observability-workshop.git
cd microsoft-foundry-e2e-agent-observability-workshop
code .
```

If your instructor gives you a different repository URL, use that URL in the
`git clone` command instead.

If `code .` does not open VS Code, open VS Code manually and select
**File > Open Folder...**, then choose the cloned repository folder.

## 3. Open the repository in the dev container

1. Select **Reopen in Container** when VS Code prompts you.
1. If you do not see the prompt, open the Command Palette and select **Dev Containers: Reopen in Container**.
1. Wait until setup finishes and the terminal is idle.
1. Confirm that `labs\notebooks\.env` exists. If it does not, ask the instructor
   for the prepared environment file.

## 4. Run Setup-Env Script

_If you are in a multi-tenant situation, do this first_

```bash
# Set default tenant (used for login)
az login --tenant <TENANT_ID>

# Set default subscription
az account set --subscription <SUBSCRIPTION_NAME_OR_ID>

#Verify with
az account show
```

_Also check that the Azure extension for VS Code is using the right tenant_.

1. Click Azure extension icon - look at Accounts & Tenants tab and ensure only 1 is checked.


1. In the VS Code terminal, run this command:

    ```bash
    ./labs/notebooks/setup-env.sh
    ```
1. It should prompt you to log into Azure as shown. Complete this step, then let the script run till complete.
    ![Run Env Script](assets/26-run-env-script.png)

1. You should see this success message - and a `.env` file with the right variables created should now be visible in the `labs/notebooks` folder.
    ![Dev Env Ready](assets/27-dev-env-ready.png)
1. Congratulations - your local env variables are set.

## 5. Start the SDK notebook labs

Continue with [README.sdk.md](./../1-prompt-agents/README.sdk.md) to run the
Foundry SDK notebooks step by step.
