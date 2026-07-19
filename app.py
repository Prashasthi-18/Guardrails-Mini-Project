from langgraph.types import Command

from agent.healthcare_agent import healthcare_agent


config = {
    "configurable": {
        "thread_id": "healthcare_session_001"
    }
}


print("=" * 60)
print("🏥 Healthcare Guardrails Assistant")
print("Type 'exit' to quit.")
print("=" * 60)


while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("\nGoodbye! Stay healthy. 👋")
        break

    try:
        result = healthcare_agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            },
            config=config
        )

        print("\nAssistant:")
        print(result["messages"][-1].content)

    except Exception as e:

        if "__interrupt__" in str(e):

            print("\n⚠️ This action requires approval.")

            approval = input("Approve? (yes/no): ").strip().lower()

            if approval == "yes":

                result = healthcare_agent.invoke(
                    Command(
                        resume={
                            "decisions": [
                                {
                                    "type": "approve"
                                }
                            ]
                        }
                    ),
                    config=config
                )

                print("\nAssistant:")
                print(result["messages"][-1].content)

            else:

                result = healthcare_agent.invoke(
                    Command(
                        resume={
                            "decisions": [
                                {
                                    "type": "reject"
                                }
                            ]
                        }
                    ),
                    config=config
                )

                print("\nAppointment cancelled.")

        else:
            print(f"\nError: {e}")