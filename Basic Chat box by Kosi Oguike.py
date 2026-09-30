# Basic Chatbot
# Simple rule based chatbot that replies to a few things

def get_reply(user_input):
    # clean the input a bit
    text = user_input.lower().strip()

    if text == "hello" or text == "hi" or text == "hey":
        return "Hi!"
    elif text == "how are you" or text == "how are you?":
        return "I'm fine, thanks!"
    elif text == "bye" or text == "goodbye" or text == "see you":
        return "Goodbye!"
    elif text == "what is your name" or text == "who are you":
        return "I'm just a simple chatbot."
    else:
        return "Sorry, I don't understand that. Try saying hello, how are you, or bye."

print("Simple Chatbot")
print("Type hello, how are you, or bye. Type quit to stop.\n")

# keep talking until user says quit
while True:
    user_msg = input("You: ")
    if user_msg.lower().strip() == "quit":
        print("Chatbot: Bye for now!")
        break

    reply = get_reply(user_msg)
    print("Chatbot: " + reply)