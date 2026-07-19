# Healthcare Guardrails Assistant

A simple AI-powered Healthcare Assistant built using **LangChain**, **LangGraph**, and **MistralAI** to demonstrate how **Guardrails** can make AI applications safer and more reliable.

This project showcases a multi-layer guardrail architecture, including input validation, PII protection, human approval, and output validation.

---

# Features

* Healthcare question answering
* Medication information
* Appointment booking
* Harmful request filtering
* PII (Email) redaction
* Human-in-the-Loop approval for appointment booking
* Automatic medical disclaimer
* Streamlit chat interface

---

# Project Structure

```
Healthcare-Guardrails-Agent/

│── app.py
│── requirements.txt
│── .env
│── README.md
│
├── agent/
│   ├── healthcare_agent.py
│   ├── middleware.py
│   ├── prompts.py
│   └── state.py
│
├── tools/
│   ├── symptoms.py
│   ├── medication.py
│   └── appointments.py
│
├── frontend/
│   └── streamlit_app.py
```

---

# Technologies Used

* Python
* LangChain
* LangGraph
* OpenAI GPT-4o Mini
* Streamlit
* Python Dotenv

---

# Guardrails Implemented

## 1. Healthcare Safety Filter

Blocks harmful or non-healthcare related requests before they reach the LLM.

Examples:

* Bomb making
* Weapons
* Hacking
* Drug synthesis
* Self-harm

---

## 2. PII Redaction

Automatically detects and redacts sensitive user information before sending it to the model.

Example:

```
Input:
My email is john@gmail.com
```

↓

```
My email is [REDACTED]
```

---

## 3. Human-in-the-Loop

Appointment booking requires manual approval before execution.

Flow:

```
User
   │
   ▼
Book Appointment
   │
   ▼
Pause
   │
Approve / Reject
   │
   ▼
Execute
```

---

## 4. Medical Output Validator

Automatically appends a medical disclaimer to every AI response.

Example:

```
Disclaimer:
This is general health information and should not be considered professional medical advice.
Please consult a qualified healthcare provider.
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project folder

```bash
cd Healthcare-Guardrails-Agent
```

Install the dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

```
OPENAI_API_KEY=your_openai_api_key
```

---

# Running the Project

### Terminal Version

```bash
python app.py
```

### Streamlit Version

```bash
streamlit run frontend/streamlit_app.py
```

---

# Available Tools

### Search Symptoms

Provides general information about common symptoms.

---

### Medication Information

Returns basic information about common medications.

---

### Book Appointment

Books a medical appointment after receiving human approval.

---

# Example Questions

```
What are the symptoms of fever?
```

```
Tell me about Paracetamol.
```

```
Book an appointment for John with Dr. Sharma on July 30.
```

---

# Learning Outcomes

This project demonstrates:

* LangChain Agents
* LangGraph
* AI Guardrails
* Middleware
* Tool Calling
* Prompt Engineering
* Human-in-the-Loop
* PII Protection
* AI Safety
* Healthcare AI Applications

---

# Future Improvements

* Connect to a real medical knowledge base
* Store appointments in a database
* User authentication
* Conversation memory
* Voice-based interaction
* LangSmith monitoring
* Persistent checkpoint storage
* Doctor availability checking

---

# Author

Developed as a beginner-friendly mini project to learn **AI Guardrails** using **LangChain** and **LangGraph**.
