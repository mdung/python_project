from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a ChatBot instance
chatbot = ChatBot('ProgrammingBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the programming-related corpus
trainer.train('chatterbot.corpus.english.computer_science')

# Train the chatbot on custom programming-related data
trainer.train([
    'What is Python?',
    'Python is a high-level programming language known for its simplicity and readability.',
    'How does a for loop work?',
    'A for loop is used to iterate over a sequence (such as a list, tuple, or string) in Python.',
    'What is object-oriented programming?',
    'Object-oriented programming (OOP) is a programming paradigm that uses objects and classes for organization and structure.',
    'How do I declare a variable in JavaScript?',
    'In JavaScript, you can declare a variable using the "var", "let", or "const" keyword.'
])

# Chat with the chatbot
print("Ask the chatbot programming-related questions. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    response = chatbot.get_response(user_input)
    print(f"Chatbot: {response}")
