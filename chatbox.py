print("🤖 ChatBot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if "hello" in user:
        print("🤖 ChatBot: Hi there!")
    elif "how are you" in user:
        print("🤖 ChatBot: I'm just code, but I'm doing great!")
    elif "bye" in user:
        print("🤖 ChatBot: Goodbye 👋")
        break
    else:
        print("🤖 ChatBot: I don't understand that.")