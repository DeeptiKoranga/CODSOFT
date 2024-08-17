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
 
