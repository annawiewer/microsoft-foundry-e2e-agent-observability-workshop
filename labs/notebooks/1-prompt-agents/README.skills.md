# Observe & Optimize Contoso Travel (Prompt Agent) Using Foundry Skills

The [microsoft-foundry skill](https://github.com/microsoft/GitHub-Copilot-for-Azure/blob/main/plugin/skills/microsoft-foundry/SKILL.md) provides a comprehensive guide that teaches the coding agents (like GitHub Copilot) how to manage the full lifecycle of Microsoft Foundry AI agents. It is part of the GitHub Copilot for Azure extension that is installed alongside the AI Toolkit extension in this devcontainer.

## 1. Understand sub-skills

The microsoft-foundry skill provides structured workflows or _sub-skills_ that cover key capabilities like deploying, evaluating, invoking, and troubleshooting AI agents hosted on Microsoft Foundry.

Here is the current subset of sub-skills available - note that these are in early preview and will have issues and breaking changes. **We will focus on the "observe" skill - your feedback here will be useful**.


| Workflow	| What it does |
|:---|:---|
| create	| Scaffold new agent projects (Python/C#, using frameworks like Microsoft Agent Framework or LangGraph) |
| deploy	| Containerize code, push to Azure Container Registry, create/start/stop agent deployments|
| invoke | Send messages to agents, run single or multi-turn conversations
| observe 🌟	| Evaluate agent quality via batch evals, optimize prompts, compare versions |
| trace	| Query traces in App Insights, analyze latency and failures |
| troubleshoot	| View container logs, diagnose deployment failures |
| eval-datasets	| Harvest production traces into evaluation datasets, track regressions
| models/deploy-model |	Deploy AI models with capacity discovery across regions |
| project/create | Provision new Azure AI Foundry projects |
| rbac	| Manage permissions and role assignments |
| quota	| Check and manage capacity/quotas |
| | |


## 2. Set Default Project in AI Toolkit

1. Click on the AI Toolkit icon in GitHub Codespaces (left).
1. Under the **My Resources** tab, click the option to "Set default" project - and set it to the Foundry project we created earlier.
1. You may be prompted to log into your Azure account if you have not already done so.

_Once this is done, you should be able to see your Microsoft Foundry assets - the models used, the agents created *with versions* etc._ right in VS Code without needing to go to the Microsoft Foundry portal.

## 3. Verify Foundry Skill is Installed

1. Use "Control + Shift + P" to access Command Palette for VS Code.
1. Search for "Chat: Configure Skill" - scroll to the bottom of the list that is shown.
1. Verify that `microsoft-foundry` is listed - you can click it to view the details of installed sub-skills.

If required:

1. Look for "AI Tookit: Install Foundry Skill" and select it to ensure the latest skill is installed.
1. You will see a confirmation like this - which leads to the same file that you will get in the previous configuration step.
    ```
    AI Toolkit: Foundry skill 'microsoft-foundry' installed to '~/.agents/skills/microsoft-foundry/'.
    ```

_Foundry Skills capabilities should now be available to coding agents_


## 4. (Optional) Explore Sub-Skills

Activating the sub-skill requires some knowledge of keywords that are recognized as "entry points" to specific workflows, when used in your coding agent conversations. Let's take a look at what this involves for `observe` for instance.

1. Open the Command Palette (Control + Shift + P)
1. Look for "Chat: Configure Skills"
1. Select the microsoft-foundry option - click it
1. You should see a `SKILL.md` file open in the editor
1. Click the _Preview_ icon for a markdown preview
1. Look for the "observe" tool in the table - and click the linked markdown file

<details>

<summary> <b> CLICK HERE TO EXPAND AND VIEW THE GUIDANCE </b> </summary>

The last step above should open a document with instructions for the coding agent to follow. It may look something like this:

![observe](./../0-setup/assets/30-observability-loop.png)


Scroll down further to see the "Entry Points" section. This gives you an idea for the kinds of keywords or prompts that are seen as indicator of user intent that map to the _observe_ skill.

![observe](./../0-setup/assets/31-entry-points.png)

Scroll down further and you see more guidance to coding agents on how they should proceed. In this case, the skill ensures that the coding agent will look at the repository state (including environment variables) to orient itself - and then kickoff the workflow with best practices for evaluations.

![observe](./../0-setup/assets/32-loop-overview.png)

</details>

## 5. Activate GitHub Copilot Chat

It's time to take the skill for a spin. You will need GitHub Copilot Chat for this purpose. You should have access to a free tier with relevant models to pick from. Note that using the skill may use up premium requests based on your model selection.

1. Click the GitHub Copilot Chat button - it should slide out a panel to the side.
1. You may be prompted to start MCP servers - take required actions to ensure that the _Foundry MCP_ server is active.
    - Open the Command Palette (Control + Shift + P)
    - Search for "MCP: List Servers"
    - Look for Foundry MCP - start the server if needed
1. You can also click the tools icon in Copilot Chat (below text entry window) to view and manage the currently active MCP servers and tools available to your coding agent.


## 6. Try the "observe" skill

Let's see if we can trigger the observe skill by prompting our coding agent with a relevant task.

Use this prompt in your copilot chat window:

```bash
Use the Microsoft Foundry observe skill for this prepared workshop.

Project endpoint: <endpoint>
Group id: <group-id>

Evaluate the Contoso Travel agent and help me understand the results.
Prefix every dataset, evaluation, run, and version you create with my group id.
Do not delete, replace, or clean up shared resources unless I explicitly ask.
```

Replace <endpoint> with the Endpoint link for your Foundry project. This explicit priming with endpoint and name of skill is just a way of giving it even clearer hints to trigger the specific skill. However, note that coding agent behavior can be non-deterministic - and the foundry-skills usage may require more trial-and-error at this time.

## 6. Capture & Share Feedback

Once you kick off the Observability loop, the agent will continue to prompt you with actions it can take to improve your agent implementation. _Follow your intuition and explore various options to see what happens_.

1. Capture the prompts you provide as you go. Keep track of what happens and any issues you encounter - and share it with us!
1. Try to build your intuition for what happens by using "Ask AI" in the Foundry portal to explain outcomes (project state) or asking Copilot Chat to provide additional context.

Here are some things I was able to try:

1. Getting an evaluation dataset created
1. Running a batch eval on my agent endpoint
1. Getting a custom evaluator created
1. Having prompt optimized and new agent versions created
1. Having two versions compared based on batch evals run


