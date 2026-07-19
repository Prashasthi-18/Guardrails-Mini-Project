import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

import streamlit as st

from agent.healthcare_agent import healthcare_agent


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Healthcare AI Assistant",
    page_icon="🩺",
    layout="wide",
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown(
    """
    <style>

    .main {
        padding-top: 2rem;
    }

    .title {
        text-align:center;
        font-size:38px;
        font-weight:700;
        color:#1f4e79;
        margin-bottom:5px;
    }

    .subtitle{
        text-align:center;
        color:gray;
        margin-bottom:30px;
    }

    div[data-testid="stChatMessage"]{
        border-radius:12px;
        padding:12px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    "<div class='title'>Healthcare AI Assistant</div>",
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='subtitle'>Secure Healthcare Assistant with LangChain Guardrails</div>",
    unsafe_allow_html=True,
)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("Project Information")

    st.write("### Guardrails Enabled")

    st.success("Input Safety Filter")

    st.success("PII Redaction")

    st.success("Human Approval")

    st.success("Medical Disclaimer")

    st.divider()

    st.write("### Example Questions")

    st.info("What are the symptoms of diabetes?")

    st.info("Tell me about Paracetamol")

    st.info("Book an appointment with Dr. Sharma tomorrow")

# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# User Input
# -----------------------------
user_input = st.chat_input(
    "Type your healthcare question..."
)

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    config = {
        "configurable": {
            "thread_id": "streamlit_session"
        }
    }

    with st.spinner("Generating response..."):

        result = healthcare_agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": user_input,
                    }
                ]
            },
            config=config,
        )

    response = result["messages"][-1].content

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)