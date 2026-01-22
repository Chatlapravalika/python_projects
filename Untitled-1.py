print("🤖 Chatbot: Hello! I am a basic chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("🤖 Chatbot: Hello! How can I help you?")

    elif "how are you" in user_input:
        print("🤖 Chatbot: I'm fine! Thanks for asking 😊")

    elif "your name" in user_input:
        print("🤖 Chatbot: My name is SimpleBot.")

    elif "help" in user_input:
        print("🤖 Chatbot: I can answer simple questions like greetings, my name, and exit.")

    elif "thank" in user_input:
        print("🤖 Chatbot: You're welcome!")

    elif user_input == "bye":
        print("🤖 Chatbot: Goodbye! Have a nice day 👋")
        break

    else:
        print("🤖 Chatbot: Sorry, I didn't understand that.")
