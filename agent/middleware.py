from typing import Any
from langchain_core.messages import AIMessage

from langchain.agents.middleware import (
    AgentMiddleware,
    AgentState,
    hook_config,
    PIIMiddleware,
    HumanInTheLoopMiddleware
)
from langgraph.runtime import Runtime


class HealthcareSafetyFilter(AgentMiddleware):
    """
    Blocks harmful or non-medical requests before they reach the LLM.
    """

    BLOCKED_TOPICS = [
        "bomb",
        "weapon",
        "hack",
        "drugs",
        "suicide",
        "self-harm",
    ]

    @hook_config(can_jump_to=["end"])
    def before_agent(
        self,
        state: AgentState,
        runtime: Runtime,
    ) -> dict[str, Any] | None:

        # No messages yet
        if not state["messages"]:
            return None

        # Get the user's first message
        first_message = state["messages"][0]

        # Continue only if it's a human message
        if first_message.type != "human":
            return None

        user_input = first_message.content.lower()

        # Check for blocked words
        for word in self.BLOCKED_TOPICS:
            if word in user_input:
                return {
                    "messages": [
                        {
                            "role": "assistant",
                            "content": (
                                "❌ Sorry, I can only assist with healthcare-related "
                                "questions. If this is an emergency, please contact "
                                "your local emergency services."
                            ),
                        }
                    ],
                    "jump_to": "end",
                }

        # Everything is safe
        return None


class MedicalOutputValidator(AgentMiddleware):
    """
    Appends a medical disclaimer to every AI response.
    """

    DISCLAIMER = (
        "\n\n⚠️ Disclaimer: This is general health information and "
        "should not be considered professional medical advice. "
        "Please consult a qualified healthcare provider."
    )

    @hook_config(can_jump_to=["end"])
    def after_agent(
        self,
        state: AgentState,
        runtime: Runtime,
    ) -> dict | None:

        # No messages yet
        if not state["messages"]:
            return None

        # Get the latest message
        last_message = state["messages"][-1]

        # Make sure it's an AI response
        if not isinstance(last_message, AIMessage):
            return None

        # Avoid adding the disclaimer twice
        if "disclaimer" not in last_message.content.lower():
            last_message.content += self.DISCLAIMER

        return None