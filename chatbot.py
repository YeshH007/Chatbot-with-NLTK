import nltk
from nltk.chat.util import Chat, reflections

def chatbot():
    pairs = [
        [
            r"my name is (.*)",
            ["Hello %1, How are you today ?",]
        ],
        [
            r"what is your name ?",
            ["I am a chatbot created by you.",]
        ],
        [
            r"how are you ?",
            ["I'm doing good. How about you?",]
        ],
        [
            r"sorry (.*)",
            ["It's alright", "No problem",]
        ],
        [
            r"quit",
            ["Bye! Take care.",]
        ],
    ]

    chat = Chat(pairs, reflections)
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        print(chat.respond(user_input))

chatbot()
