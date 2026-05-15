# Building Contoso Travel (Prompt Agent) Using Foundry SDK

> **Prepared workshop note:** If you are in an instructor-led workshop, start
> from `WORKSHOP-QUICKSTART.md` first. The instructor should already provide a
> `.env` file and a `WORKSHOP_GROUP_ID`. The notebooks use that group id to
> prefix shared Foundry resources.
> For the simplest participant flow, use `STUDENT-LAB-GUIDE.md`.

By now you should have completed the _infrastructure setup_ and _local dev container_ setup steps, and your VS Code environment should be connected to an existing Foundry project in your Azure subscription.

In these labs, you'll execute notebooks in order - walking you through the journey of building a Contoso Travel agent, grounding it in custom data and tools, then evaluating and tracing it - and running an AI Red Teaming scan to assess vulnerability to attack.

### 2.1 How To: Run a Notebook

The local VS Code dev container has pre-installed extensions and tools to support Jupyter notebooks. Take these actions to run any notebook:

1. Open the notebook (`.ipynb` file) in Visual Studio Code
1. Click **Select Kernel**, and pick the **Python 3.12** option.
1. Clear all outputs first, then **run each cell one at a time** (rather than "Run All")
1. Observe the results and understand each step before moving on.

**IMPORTANT**: Do NOT run the final cell of the notebook until you are done with the lab and have understood the code. Cleanup cells delete Foundry resources. In a prepared shared-project workshop, cleanup cells are blocked unless the instructor sets `WORKSHOP_ALLOW_CLEANUP=1`.

<br/>

### 2.2 Lab Notebooks

| Notebook | Description |
|---|---|
| [lab-01-setup.ipynb](lab-01-setup.ipynb) | Validate your environment, authenticate to Microsoft Foundry, and confirm your model deployment is ready. |
| [lab-02-agent.ipynb](lab-02-agent.ipynb) | Create a basic Contoso Travel concierge agent with system instructions and test it with travel queries. |
| [lab-03a-tools.ipynb](lab-03a-tools.ipynb) | Give the agent tools (functions) to look up flights, hotels, and car rentals from CSV data. |
| [lab-03b-workflow.ipynb](lab-03b-workflow.ipynb) | Orchestrate multiple specialized agents into a multi-agent workflow that collaborates on trip planning. |
| [lab-04-tracing.ipynb](lab-04-tracing.ipynb) | Instrument the agent with OpenTelemetry tracing and export telemetry to Application Insights. |
| [lab-05-evaluation.ipynb](lab-05-evaluation.ipynb) | Evaluate agent quality, safety, and agentic performance using built-in Foundry evaluators. |
| [lab-06-redteam.ipynb](lab-06-redteam.ipynb) | Run cloud-based adversarial red-team scans to find vulnerabilities before production deployment. |
| |

**Note**:
_The AI Red Teaming agent is region- and quota-dependent. The prepared universal workshop project uses a supported region for live red-team scans. If you point the notebooks at a different project whose region does not support red-team evaluations, the notebook will skip the live scan with a clear message._
