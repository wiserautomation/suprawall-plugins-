# Copyright 2026 SupraWall Contributors
# SPDX-License-Identifier: Apache-2.0

import os
import requests
from typing import Any, Dict, List, Optional
from langchain_core.callbacks import BaseCallbackHandler

class SupraWallCallbackHandler(BaseCallbackHandler):
    """
    Standard LangChain Callback Handler to enforce SupraWall security policies.
    
    This handler intercepts tool calls before execution and validates them
    against your defined policies in the SupraWall dashboard.
    """
    
    def __init__(
        self, 
        api_key: Optional[str] = None, 
        agent_id: str = "default_agent",
        api_url: Optional[str] = None
    ):
        """
        Initialize the SupraWall callback.
        
        Args:
            api_key: Your SupraWall API key (can also use SUPRAWALL_API_KEY env var).
            agent_id: A unique identifier for the agent being monitored.
            api_url: Optional override for the evaluation URL.
        """
        self.api_key = api_key or os.environ.get("SUPRAWALL_API_KEY")
        if not self.api_key:
            raise ValueError("SUPRAWALL_API_KEY is required either in __init__ or via environment variable.")
        
        self.agent_id = agent_id
        self.api_url = api_url or os.environ.get("SUPRAWALL_API_URL", "https://api.suprawall.io/v1/evaluate")

    def on_tool_start(
        self, 
        serialized: Dict[str, Any], 
        input_str: str, 
        **kwargs: Any
    ) -> Any:
        """
        Intercept tool calls and check for policy violations.
        """
        tool_name = serialized.get("name")
        
        # Payload for deterministic security evaluation
        payload = {
            "agentId": self.agent_id,
            "toolName": tool_name,
            "arguments": input_str,
            "metadata": {
                "framework": "langchain",
                "runId": str(kwargs.get("run_id", ""))
            }
        }
        
        try:
            res = requests.post(
                self.api_url, 
                json=payload, 
                headers={"Authorization": f"Bearer {self.api_key}"},
                timeout=2.0 # Fast-fail for low latency
            )
            
            if res.status_code == 200:
                decision_data = res.json()
                decision = decision_data.get("decision")
                
                if decision == "DENY":
                    reason = decision_data.get("reason", "Explicitly denied by policy.")
                    raise PermissionError(f"🛡️ SupraWall Blocked: {reason}")
                
                elif decision == "REQUIRE_APPROVAL":
                    approval_url = decision_data.get("approvalUrl", "https://app.supra-wall.com")
                    raise PermissionError(
                        f"🛡️ SupraWall: Action requires human approval. Visit: {approval_url}"
                    )
            else:
                # If the security layer is unreachable, we fail closed by default
                # to maintain the zero-trust principle.
                raise ConnectionError("🛡️ SupraWall Unreachable: Failing closed for security.")
                
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"🛡️ SupraWall Connection Error: {str(e)}")

class SupraWallToolkit:
    """Convenience class to inject SupraWall into LangChain agents."""
    def __init__(self, api_key: Optional[str] = None, agent_id: str = "default"):
        self.callback = SupraWallCallbackHandler(api_key=api_key, agent_id=agent_id)

    def get_callbacks(self):
        return [self.callback]
