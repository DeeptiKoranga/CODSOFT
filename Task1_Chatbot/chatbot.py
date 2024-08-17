def chatbot_response(user_input):
    # Convert the input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Rule-based responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm here to help you!"
    elif "your name" in user_input:
        return "I'm a simple chatbot created for this task."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! If you have more questions, feel free to ask."
    elif "what time is it" in user_input:
        from datetime import datetime
        now = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}."
    elif "date" in user_input or "today" in user_input:
        from datetime import datetime
        today = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {today}."
    elif "joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "help" in user_input:
        return ("I can assist with the following commands:\n"
                "- 'hello' or 'hi': Greet the chatbot\n"
                "- 'how are you': Ask the chatbot how it is\n"
                "- 'your name': Inquire about the chatbot's name\n"
                "- 'bye' or 'goodbye': End the conversation\n"
                "- 'thank you' or 'thanks': Respond to thanks\n"
                "- 'what time is it': Get the current time\n"
                "- 'date' or 'today': Get today's date\n"
                "- 'joke': Hear a joke\n"
                "- 'help': Display this help message")
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

# Example chat loop
print("Welcome to the chatbot! Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
