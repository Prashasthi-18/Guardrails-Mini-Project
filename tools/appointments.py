from langchain_core.tools import tool


@tool
def book_appointment(patient_name: str, doctor: str, date: str) -> str:
    """
    Book a medical appointment.
    """

    return (
        f"✅ Appointment booked successfully!\n\n"
        f"Patient Name : {patient_name}\n"
        f"Doctor       : Dr. {doctor}\n"
        f"Date         : {date}\n\n"
        f"Please arrive 15 minutes before your scheduled appointment."
    )