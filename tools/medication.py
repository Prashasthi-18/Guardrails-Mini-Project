from langchain_core.tools import tool


@tool
def get_medication_info(medication: str) -> str:
    """
    Get general information about a medication.
    """

    medication_database = {
        "paracetamol": (
            "Paracetamol is commonly used to reduce fever and relieve mild to "
            "moderate pain. Follow the dosage prescribed by your doctor."
        ),
        "ibuprofen": (
            "Ibuprofen helps reduce pain, inflammation, and fever. "
            "Take it after food unless advised otherwise by your doctor."
        ),
        "cetirizine": (
            "Cetirizine is an antihistamine used to treat allergies such as "
            "sneezing, itching, and a runny nose."
        ),
        "amoxicillin": (
            "Amoxicillin is an antibiotic used to treat bacterial infections. "
            "Always complete the full course prescribed by your doctor."
        ),
    }

    medicine = medication.lower().strip()

    if medicine in medication_database:
        return medication_database[medicine]

    return (
        f"Sorry, I don't have information about '{medication}'. "
        "Please consult a doctor or pharmacist before taking any medication."
    )