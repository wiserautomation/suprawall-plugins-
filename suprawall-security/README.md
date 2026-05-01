# SupraWall Security Plugin for Dify

SupraWall is a deterministic security layer for AI agents. This plugin allows you to integrate SupraWall's policy enforcement and prompt injection detection directly into your Dify workflows and agents.

## Features

- **Prompt Injection Detection**: Automatically scan incoming prompts for malicious injection attempts.
- **Output Policy Enforcement**: Ensure agent responses comply with your corporate guidelines and safety policies.
- **Action Blocking**: Stop non-compliant agent actions before they reach production.
- **Privacy First**: High-performance local checks and secure API communication.

## Configuration

To use this plugin, you will need a SupraWall API Key. You can obtain one by signing up at [supra-wall.com](https://supra-wall.com).

1. Install the plugin from the Dify Marketplace.
2. In your workflow or agent, add the SupraWall tools.
3. Configure the `API Key` in the tool settings.

## Tools

### SupraWall Scan
Analyzes the input prompt for injection risks. Returns a risk score and detailed findings.

### SupraWall Enforce
Validates the agent's proposed output or action against active security policies.

## Support

For documentation and support, visit [docs.supra-wall.com](https://docs.supra-wall.com) or join our community Discord.

---
© 2026 SupraWall Contributors. Licensed under Apache 2.0.
