from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI

from langgraph.checkpoint.memory import InMemorySaver

from agent.middleware import (
    HealthcareSafetyFilter,
    MedicalOutputValidator,
    PIIMiddleware,
    HumanInTheLoopMiddleware,
)

from tools.symptoms import search_symptoms
from tools.medication import get_medication_info
from tools.appointments import book_appointment


# Load environment variables
load_dotenv()


# Create the LLM
llm = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0,
)


# Create the Healthcare Agent
healthcare_agent = create_agent(
    model=llm,

    tools=[
        search_symptoms,
        get_medication_info,
        book_appointment,
    ],

    middleware=[

        # Guardrail 1
        HealthcareSafetyFilter(),

        # Guardrail 2
        PIIMiddleware(
            "email",
            strategy="redact",
            apply_to_input=True,
        ),

        # Guardrail 3
        HumanInTheLoopMiddleware(
            interrupt_on={
                "search_symptoms": False,
                "get_medication_info": False,
                "book_appointment": True,
            }
        ),

        # Guardrail 4
        MedicalOutputValidator(),
    ],

    checkpointer=InMemorySaver(),

    system_prompt=(
        "You are a helpful healthcare assistant. "
        "Answer only healthcare-related questions. "
        "Use the available tools whenever necessary. "
        "Never provide a medical diagnosis. "
        "Recommend consulting a qualified doctor for diagnosis."
    ),
)