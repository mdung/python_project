from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('FAQBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English language corpus data
trainer.train('chatterbot.corpus.english')

# Additional training with your custom data (if needed)
# trainer.train([
#     'What is your name?',
#     'My name is FAQBot.'
# ])

# Function to get a response from the chatbot
def get_response(user_input):
    return chatbot.get_response(user_input)

# Main interaction loop
while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        break

    response = get_response(user_input)
    print("FAQBot:", response)
