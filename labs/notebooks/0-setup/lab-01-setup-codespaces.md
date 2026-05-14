# Lab 01: Setup Development Environment

> **Instructor-led workshop:** Skip this lab if your instructor has already
> prepared Codespaces or a local dev container and provided `labs\notebooks\.env`.
> Start from `WORKSHOP-QUICKSTART.md` instead.

## 1. Launch GitHub Codespaces

1. [Fork the repository](https://github.com/Azure-Samples/microsoft-foundry-e2e-agent-observability-workshop/fork) to your own profile to get your sandbox.
1. Launch GitHub Codespace on your fork.
    - Click the blue Code button in your repo (in the browser)
    - Select the Codespaces tab
    - Click Create Codespace
1. A new browser tab opens with a VS Code environment
    - Wait till the IDE is completely loaded
    - Look for the terminal to become active
    - This can take quite a few minutes to complete
1. Congratulations - your dev environment is ready.

## 2. Run Setup-Env Script

_If you are in a multi-tenant situation, do this first_

```bash
# Set default tenant (used for login)
az login --tenant <TENANT_ID>

# Set default subscription
az account set --subscription <SUBSCRIPTION_NAME_OR_ID>

#Verify with
az account show
```

_Also check that the AI Toolkit and Azure extensions for VS Code are using the right tenants_.

1. Click Azure extension icon - look at Accounts & Tenants tab and ensure only 1 is checked.
1. Click the AITK extension icon - look at My Resources and ensure the default Foundry project is set.


1. In the VS Code terminal, run this command:

    ```bash
    ./labs/notebooks/setup-env.sh
    ```
1. It should prompt you to log into Azure as shown. Complete this step, then let the script run till complete.
    ![Run Env Script](assets/26-run-env-script.png)

1. You should see this success message - and a `.env` file with the right variables created should now be visible in the `labs/notebooks` folder.
    ![Dev Env Ready](assets/27-dev-env-ready.png)
1. Congratulations - your local env variables are set.

## 3. Choose Your Adventure

| Option | Description |
|:---|:---|
| [README.sdk.md](./../1-prompt-agents/README.sdk.md) | Traditional code-first path using the Microsoft Foundry SDKs and walking through code step-by-step|
| [README.skills.md](./../1-prompt-agents/README.skills.md)| Early preview coding agents path using the "observe" Foundry Skills to drive the _observe-optimize_ loop |

Once you've completed one path, you are welcome to return to this step and try the other. We suggest trying the Foundry Skills path first, to get an early intuition for how coding agents and skills can accelerate your development workflow in future.
