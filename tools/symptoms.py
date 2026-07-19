from langchain_core.tools import tool

@tool
def search_symptoms(symptoms: str) -> str:
    """
    Search for information about medical symptoms.
    """

    symptom_database = {
        "fever": (
            "A fever may be caused by an infection. "
            "Stay hydrated, get adequate rest, and monitor your temperature."
        ),
        "headache": (
            "Headaches can result from stress, dehydration, lack of sleep, "
            "or illness. Drink plenty of water and rest."
        ),
        "cough": (
            "A cough may be caused by a cold, allergies, or an infection. "
            "If it persists for more than two weeks, consult a doctor."
        ),
        "diabetes": (
            "Common symptoms of Type 2 Diabetes include frequent urination, "
            "increased thirst, fatigue, blurred vision, and slow wound healing."
        ),
    }

    symptom = symptoms.lower().strip()

    if symptom in symptom_database:
        return symptom_database[symptom]

    return (
        f"Sorry, I don't have information about '{symptoms}'. "
        "Please consult a healthcare professional for medical advice."
    )