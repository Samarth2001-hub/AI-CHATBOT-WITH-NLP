import nltk
from nltk.chat.util import Chat, reflections

 
nltk.download('punkt')

 
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?"]
    ],
    [
        r"what is your name",
        ["I'm  Troy, a helpful AI built by xAI. What's your name?"]
    ],
    [
        r"how are you",
        ["I'm doing great, thanks for asking! How about you?"]
    ],
    [
        r"what can you do",
        ["I can answer questions, chat about almost anything, and even help with some tasks. What do you want to talk about?"]
    ],
    [
        r"bye|goodbye|exit",
        ["Goodbye! It was nice chatting with you."]
    ],
    [
        r"(.*)",   
        ["Sorry, I didn’t quite get that. Could you rephrase it?"]
    ]
]

 
chatbot = Chat(pairs, reflections)

 
def start_chat():
    print("Hi! I'm your chatbot. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

 
if __name__ == "__main__":
    start_chat()
