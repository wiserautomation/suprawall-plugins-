# 🛡️ langchain-suprawall

**Official SupraWall security and compliance integration for LangChain Python.**

SupraWall provides a deterministic security layer for AI agents, enabling enterprise-grade governance, human-in-the-loop approvals, and forensic audit logs. 

Built for teams that need to ship autonomous agents while staying compliant with the **EU AI Act (Articles 9, 12, & 14)** and SOC2/ISO27001 requirements.

---

## 🚦 Quick Start

Install via pip:

```bash
pip install langchain-suprawall
```

### With LangChain Agents (`create_react_agent`)

```python
from langchain_suprawall import SupraWallCallbackHandler
from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain import hub

llm = ChatOpenAI(model="gpt-4")
tools = [...] # Your tools
prompt = hub.pull("hwchase17/react")

# Initialize the security callback
suprawall = SupraWallCallbackHandler(
    api_key="your_suprawall_api_key",
    agent_id="payment-agent-01"
)

agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    callbacks=[suprawall] # Attach here
)
```

### With LangGraph

```python
from langgraph.prebuilt import create_react_agent
from langchain_suprawall import SupraWallCallbackHandler

suprawall = SupraWallCallbackHandler()

# Pass callbacks in the config during invocation
graph = create_react_agent(model, tools)
graph.invoke(
    {"messages": [("user", "delete my account")]},
    config={"callbacks": [suprawall]}
)
```

---

## 🏛️ EU AI Act Compliance

SupraWall is the first integration designed specifically to meet the high-risk AI requirements of the EU AI Act:

- **Article 9 (Risk Management)**: Identifies and mitigates risks through deterministic policy enforcement.
- **Article 12 (Logging)**: Automatically generates tamper-proof, time-stamped execution logs.
- **Article 14 (Human Oversight)**: Built-in hooks for "Human-in-the-Loop" (HITL) triggers on destructive actions.

---

## 🔒 Common Security Policies

Define policies in your SupraWall dashboard and they are automatically enforced via the callback:

### 1. Financial Guardrails (Refund Limits)
*Policy: "If tool `process_refund` is called with an amount > $500, block execution."*
SupraWall intercepts the tool start, evaluates the arguments, and raises a `PolicyViolation` exception if the check fails.

### 2. Destructive Action Approval
*Policy: "Require human approval for `delete_customer_record`."*
The callback will pause execution and wait for a signed approval from the SupraWall dashboard before letting the agent continue.

### 3. Prompt Injection Shield
SupraWall's runtime analysis detects adversarial intent (jailbreaks, DAN-style prompts) before they reach your sensitive tools.

---

## 📖 Documentation & Support

- **Full Documentation**: [docs.supra-wall.com](https://docs.supra-wall.com/integrations/langchain)
- **Dashboard**: [app.supra-wall.com](https://app.supra-wall.com)
- **Discord**: [Join our community](https://discord.gg/suprawall)

---

&copy; 2026 WiserAutomation. Licensed under the Apache License 2.0.
