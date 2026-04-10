from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

print("Choose your AI mode")
print("Press 1 for Angry mode")
print("Press 2 for Funny mode")
print("Press 3 for Sad mode")
print("Press 4 for AI mode")

try:
    choice = int(input("Tell your choice: "))
except:
    print("Invalid input! Defaulting to Funny mode 😄")
    choice = 2

if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif choice == 2:
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif choice == 3:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."
elif choice == 4:
    mode = "You are a helpful and intelligent AI assistant. You respond clearly and helpfully."
else:
    print("Invalid choice! Defaulting to Funny mode 😄")
    mode = "You are a very funny AI agent. You respond with humor and jokes."

messages = [
    SystemMessage(content=mode)
]

print("----------------- Welcome! Type 0 to exit -----------------")

while True:
    prompt = input("You: ")

    if prompt == "0":
        print("Exiting... Goodbye 👋")
        break

    messages.append(HumanMessage(content=prompt))

    response = model.invoke(messages)

    messages.append(AIMessage(content=response.content))

    print("Bot:", response.content)

# Optional: print chat history
# print(messages)