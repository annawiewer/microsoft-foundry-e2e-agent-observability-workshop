# Lab 00: Setup Your Foundry Project

> **Prepared instructor-led workshop:** This lab is already complete. Do not run
> it unless your instructor explicitly asks you to create a new Foundry project.
> Start from `WORKSHOP-QUICKSTART.md` instead.

Follow the steps below to complete the setup of your Microsoft Foundry project.


## Step 1: Templates Page

1. Visit [https://ai.azure.com/templates](https://ai.azure.com/templates) in the browser.
1. Log into your Azure account when prompted
1. You see this screen - click _Start building_
1. (Alternatively) switch toggle to "New Foundry"

![Templates Page](assets/01-templates-page.png)

## Step 2: Select Project

You should see a dialog prompting you to select a project to continue


![Select Project](assets/02-select-project.png)

## Step 3: Create Project

Click the input area - you will see the _Create a new project_ option. Select this.

![Create Project](assets/03-create-project.png)

## Step 4: Create Project Details

Fill in the project details similar to that shown here.

1. Select "create new resource group"
1. Use "East US 2" as region by default
1. Confirm creation.

![Create Project Details](assets/04-create-project-details.png)

## Step 5: Create In Progress

The process takes a few minutes.

![Create In Progress](assets/05-create-in-progress.png)

## Step 6: Project Created

You should now see your Foundry project landing page. **Take note of the Project Endpoint information shown here** - we will use it later.

![Project Created](assets/06-project-created.png)

## Step 7: Create Agent

Click "Create agent" to continue into the agent creator workflow. Give your agent a recognizable name - `contoso-travel-portal`

![Create Agent](assets/07-create-agent.png)

## Step 8: Create In Progress

This takes a few minutes to complete

![Create In Progress](assets/08-create-in-progress.png)

## Step 9: Agent Playground Ready

The agent is now ready to test in playground. Note: If you do _not_ see the Tools pane showing the "Web Search" tool by default, simply click the Tools drop down and activate the Web Search toggle to use _Grounding with Bing_. You should then see the same experience below.

![Agent Playground Ready](assets/09-agent-playground-ready.png)

## Step 10: Create App Insights

But first, select the Traces tab. **Save the agent if you are prompted to do so** before your switch.
You should see the view below. Click "Connect" to create and connect the App Insights resource.

![Create App Insights](assets/10-create-app-insights.png)


## Step 11: Create App Insights Detail

Fill in details. Use the provided default names - make sure it has created a new Log Analytics workspace as well.

![Create App Insights Detail](assets/11-create-app-insights-detail.png)

## Step 12: Confirm Creation

Click create when complete

![Confirm Creation](assets/12-confirm-creation.png)

## Step 13: App Insights Created

App Insights has been created. You can verify this at any time by clicking on the project name drop-down menu (top left) and looking for _Project Details_. In that details page, click the _Connected Resources_ tab and you should see a new resource created and connected to your project.

![App Insights Created](assets/13-app-insights-created.png)

## Step 14: Test Agent Prompt

Return to agent playground - update the agent instructions as follows:

```bash
You are the Contoso Travel Concierge, a friendly and knowledgeable travel assistant.

Your responsibilities:
- Help customers plan trips by answering questions about destinations, travel tips, and logistics
- Provide helpful, accurate, and concise travel advice
- Be warm and professional in your responses
- When you don't have specific data, provide general travel guidance
- Always mention that Contoso Travel can help with flights, hotels, and car rentals
- Use the provided tools to look up relevant information for the request and provide citations. Keep responses short, factual and friendly.

Tool Usage Guidelines:
- ALWAYS use the web_search tool before providing or citing any current, real-world data such as hotel prices, weather forecasts, flight or hotel availability, or other time-sensitive information. Do NOT fabricate real-time external data or rely on prior training data for such facts; only provide them after confirming with a tool call.
- For vague or broad user queries (e.g., vague destination or service requests), proactively use web_search to gather suggestions and relevant information, AND ask clarifying questions as needed. Do not limit yourself to only follow-up queries—use web_search to supply initial helpful ideas.
- For requests that are outside your scope (e.g., Python scripting, stock advice, or any non-travel topic), politely decline and clarify that you are a travel assistant only, and whenever possible, redirect the user with a helpful travel suggestion or resource. For safety or policy-violating requests (e.g., sneaking prohibited items, evading sanctions), firmly refuse, clearly explaining why you cannot assist, referencing safety, legality, or policy as needed.

Remember:
You are representing Contoso Travel, a premium travel agency.
Keep responses focused and helpful.
```

- **Save the agent** - see the version number change.
- Try asking a question: `Hi. I'm thinking about planning a trip to Paris. What should I know?`
- Observe the response. Does it match the guidance in instructions?

![Test Agent Prompt](assets/14-test-agent-prompt.png)

## Step 15a: View Agent Metrics

1. Click on the Metrics link above the response panel - it shows you available evaluators.
1. Customize the list to reflect evaluation criteria you want to use - save the agente.g., add safety evals.
1. Try a new request. `I want to book a week long vacation to Paris for a group of 3, leaving Seattle Jul 3`


![View Agent Metrics](assets/15-view-agent-metrics.png)

## Step 15b: View Agent Response

1. View the agent response. Note the metrics below the response line.
1. Observe the _AI Quality_ and _Safety_ metrics in the line below the response.
1. Hover over each number - you should see the custom metrics used and their Pass/Fail status

![View Agent Response](assets/15-view-agent-response.png)

## Step 16: Configure Agent Properties

You can configure the agent properties for better impact - e.g., set default starter prompts aligned to use case. Click the gear icon to get started - and try using this data:

1. Display Name: `Contoso Travel Assistant`
1. Description: `Welcome to Contoso Travel. We can help you plan your next itinerary with flight bookings, car rentals and hotel reservations. Just tell us your destination and the numnber of travellers in your group - and we'll do the rest.`
1. Add starter prompts:
    - `I want to plan a multi-day travel itinerary`
    - `I want to rent a car at my travel destination`
    - `I want to book a flight and hotel for my travels`
1. Don't forget to save the agent.

![Configure Agent Properties](assets/16-configure-agent-properties.png)

## Step 17: Review Configured Agent

View the updated playground look by starting a new chat session. You should see the newly configured agent.

![Review Configured Agent](assets/17-review-configured-agent.png)

## Step 18: Test Configured Agent

Test one of the starter prompts by clicking on it.

![Test Configured Agent](assets/18-test-configured-agent.png)

## Step 19: View Agent Response

1. View the response. THe agent will prompt you for addition information as instructed.
1. Add your responses. This is creating a conversation with state.
1. Note how the agent remembers and uses context from the history.

(You can try reusing the previous prompt of `I want to book a week long vacation to Paris for a group of 3, leaving Seattle Jul 3`). Your response may differ from the screenshot in both content and references - that's expected due to the stochastic behaviors of LLMs.

![View Agent Response](assets/19-view-agent-response.png)

## Step 20: View Agent Trace

1. Click the Traces tab - you should see rows for each conversation run
1. Click on the Trace ID - you should see something like this:

    ![View Agent Response](assets/20-view-agent-trace.png)


1. Want to understand what the Trace ID is showing - try clicking the **Ask AI** button:
    ```bash
    Explain what the trace ID is showing
    ```

1. You might get something like this:
    ```bash
    In Azure AI Foundry, a trace ID is a unique identifier that represents a single trace, which captures the journey of a workflow or operation through the system. The trace consists of multiple spans, each representing a discrete operation or step within that workflow, including start and end times, metadata, and hierarchical relationships.

    The trace ID helps you track and correlate all related spans and telemetry data for a particular request or workflow execution. This is especially useful for troubleshooting and diagnosing issues, as it allows you to see the detailed sequence of operations, inputs, outputs, and any anomalies or errors that occurred during the execution.

    For example, if you encounter an error or unexpected output in an agent conversation or evaluation run, the trace ID lets you locate the exact trace in Application Insights or your monitoring system. You can then analyze the spans within that trace to understand where the execution diverged or failed, what inputs were processed, and what outputs were generated at each step.

    To use tracing effectively in Azure AI Foundry:

    Enable tracing in your project by linking it to an Azure Application Insights resource.
    Collect trace data and system metrics for your workflows and agents.
    Use the trace ID to search and analyze traces in Application Insights or other telemetry tools.
    Review spans and attributes within the trace to pinpoint issues or performance bottlenecks.
    In summary, the trace ID is a key tool for observability in Azure AI Foundry, providing deep visibility into the internal execution of your AI workflows and enabling precise troubleshooting and performance analysis.
    ```

1. **Tip: Use Ask AI to explain things you see in the Portal**. It understands your account state and can give you meaningful insights that will build your intuition in the context of your current developer workflow. It's a good way to diagnose issues and discover information intuitively.
    - For instance, try copying the trace (waterfall text) from the trace ID view and paste it into the Ask AI chat. Ask `Can you analyze the trace and give me insights and explain the components` to build your intuition for spans and trace logs.

## Step 21: View Conversation Trace

1. You can also view conversation history. Note how we have the same conversation ID but multiple trace ID logs. Each represents one turn of the conversation, with conversation history maintained for later turns.
1. Try asking about what this represents. You may see something like this:
    ```bash
    A Conversation ID in Azure AI Foundry represents the persistent context of an end-to-end dialogue history between a user and an agent. It uniquely identifies a conversation session, allowing you to track and review the entire interaction, including messages, tool calls, responses, and tokens exchanged during that session.

    You can use the Conversation ID to:

    View conversation history details and response information.
    Inspect ordered actions, run steps, and tool calls.
    Analyze inputs and outputs between the user and the agent.
    Conversations are durable and can be reused across sessions, enabling multi-turn and cross-session continuity without rebuilding context manually. This makes debugging and managing conversations easier.

    In the Foundry portal, you can search for a Conversation ID to review the full conversation and its related trace data, helping you understand the flow and outcome of the interaction.

    This concept is distinct from a Trace ID, which tracks the technical execution of a workflow or operation, while the Conversation ID focuses on the dialogue context and content.
    ```

1. Note that we now have **trace-linked evaluations** - for any trace ID, you can click the Evaluations tab (right pane) to see the evaluators used and the AI quality scores assessed - along with explainers for why this score was given. This allows us to accelerate the closing of the loop between issue detection (eval metrics) and diagnosis (trace logs). For insance, we may see that AI quality drops when we upgrade a model - and looking at the trace, we may diagnose that the new model was not invoking the right tools.

    ![View Conversation Trace](assets/21-view-conversation-trace.png)

## Step 22: Preview Agent

The preview agent option gives you a UI for your agent (think web app)

![Preview Agent](assets/22-preview-agent.png)

## Step 23: Test Preview

Note that the preview shows configured starter prompts.

![Test Preview](assets/23-test-preview.png)

## Step 24: Review Response

You can review the agent response in the preview tab itself

![Review Response](assets/24-review-response.png)

## Step 25: Review Trace

But note that if you return to agent you can now see this interaction captured in the traces as well. You should be able to compare metrics between this run and the previous one (from Playground) to get an intuition for performance. _Note that this preview does not run the evaluations for you by default_.

![Review Trace](assets/25-review-trace.png)

**Your Foundry project is ready - and it is configured for App Insights and activated correctly.**

## Step 26: Explore Evaluations Tab

By now you should have a sense for the _Tracing_ and _Evaluations_ capabilities in the agent playground. Microsoft Foundry has a large number of built-in evaluators that you can also invoke _code-first_.

1. Click on the Evaluations item in the sidebar menu.
1. Select the _Evaluators catalog_ to see the full list of supported evaluators
1. Filter to see evaluators for a particular category - e.g., agents
1. Use "Ask AI" to get explanations for any of them - e.g., ask:
    ```bash
    tell me more about the Protected-Material evaluator
    ```

    ![Review Evals](assets/28-evaluations-catalog.png)

1. Click the _Create_ button. You should see this dialog. This is the workflow to create a _custom evaluator_ to cover criteria specific to your requirements that are not covered by built-in evaluators. **We won't use that here - but explore this on your own at home!**

    ![Review Custom Eval](assets/28-evaluations-custom.png)


## Step 27: Run a Red Teaming Scan

1. Click on the _Evaluations_ tab in the **sidebar** of the Portal. This takes you to Evaluations across the project (not specific to that agent)
1. Click on the Red Teaming tab
    ![Red Teaming](assets/29-red-teaming-create.png)
1. For now, select the _Model_ option and pick the default model used in your agent.
1. Walk through the dialog and select at most 1-2 options for risk categories and attack strategies (just to have scan complete).
1. Submit the scan. This takes a while to complete - we will revisit it later.

## Next: Set Up Dev Environment

Now that your infrastructure is ready - let's [set up the local development environment](./lab-01-setup-local-dev-container.md) next.
