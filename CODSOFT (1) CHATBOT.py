# Simple Rule-Based Chatbot
# Author: JOHN MELVIN.M
# University: Mysore University School of Engineering

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I am a simple rule-based chatbot created by John."
    elif "how are you" in user_input:
        return "I'm just a program, but I'm doing fine. Thanks for asking!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I don't understand that yet."

# Main loop
print("Chatbot is running! Type 'bye' to exit.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! See you again.")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
