# 🛡️ SupraWall Plugins Monorepo

The industry-first deterministic security layer for AI Agents. Protect your agentic workflows with Zero-Trust guardrails.

[SupraWall.dev](https://suprawall.dev) | [Docs](https://docs.suprawall.dev) | [Security Policy](https://suprawall.dev/security)

---

## 📦 What's Inside?

This monorepo contains the official plugins and framework integrations for the SupraWall ecosystem.

### 🤖 LLM Marketplace Plugins
- **[Dify Plugin](./suprawall-security)**: Deterministic policy enforcement and threat scanning (SQLi, Prompt Injection) for Dify Workflows.
- **[MCP Claude Plugin](./mcp-plugin)**: Official Model Context Protocol (MCP) server for Anthropic Claude Desktop and Claude-powered agents.

### 🧱 Framework Integrations
Direct security middleware for your favorite AI frameworks:
- **[AutoGen](./autogen)**: Protect Microsoft AutoGen agent societies.
- **[CrewAI](./crewai)**: Secure your CrewAI multi-agent systems.
- **[LangChain (Python)](./langchain-py)** & **[LangChain (TS)](./langchain-ts)**: Seamless security wrappers for LangChain chains and agents.
- **[LlamaIndex](./llama-index)**: Secure RAG and agentic data retrieval.
- **[Vercel AI SDK](./vercel-ai)**: Integrated guardrails for Vercel AI projects.
- **[OpenClaw](./openclaw)**: Native security for the OpenClaw agent runtime.

---

## 🚀 Getting Started

### Installation
Every plugin/integration can be installed independently. Navigate to the specific directory for detailed setup instructions.

### Dify Marketplace (Coming Soon)
We are currently in review for the official [Dify Marketplace](https://cloud.dify.ai/plugins). You can install manually using the `.difypkg` in the `suprawall-security` folder while we wait.

### Claude Desktop (MCP)
To use the MCP plugin with Claude Desktop, add the following to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "suprawall": {
      "command": "npx",
      "args": ["-y", "@suprawall/mcp-plugin"]
    }
  }
}
```

---

## 🔒 Security First

SupraWall is built on **Deterministic Security**. We don't guess if an action is dangerous; we enforce your specific business policies before the agent even attempts the call.

### Found a security issue?
Please report it via our [Security Policy](https://suprawall.dev/security) or email `security@suprawall.dev`. 

---

## 📄 License
This project is licensed under the [Apache License 2.0](./LICENSE).

&copy; 2026 WiserAutomation. Agency. All rights reserved.
