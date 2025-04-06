# AI-CHATBOT-WITH-NLP

COMPANY : CODTECH IT SOLUTIONS

NAME : SAMARTH KUMAR SINGH

INTERN ID : CT04XBC

DOMAIN : PYTHON PROGRAMMING

DURATION : 4 WEEKS

MENTOR : NEELA SANTOSH

The code creates a basic chatbot that responds to user inputs based on predefined patterns and responses. It uses the nltk.chat.util.Chat utility from the NLTK (Natural Language Toolkit) library, which provides a simple framework for pattern-matching conversations. The chatbot runs in a loop, allowing continuous interaction until the user chooses to exit.
When you run the script, it prints a welcome message: "Hi! I'm your chatbot. Type 'exit' to end the chat."
You type a message (e.g., "hi"), and the input is converted to lowercase ("hi").
The Chat instance matches "hi" against the patterns in pairs:
It finds r"hi|hello|hey" and selects the response "Hello! How can I assist you today?"
The response is printed: "Chatbot: Hello! How can I assist you today?"
The loop continues, waiting for your next input.
If you type "exit," the loop breaks, and the program ends.
a) Rule-Based: It relies on predefined patterns, so it can’t handle complex queries or learn from interactions.
b) No Context: It doesn’t remember prior messages (unlike me, with my memory feature!).
c) Basic NLP: It uses simple regex matching rather than advanced techniques like intent recognition or entity extraction.
1) nltk: The Natural Language Toolkit is a widely-used Python library for NLP tasks. It provides tools for tokenization, stemming, tagging, parsing, and more. Here, it serves as the foundation for text processing.
2) Chat: A class within nltk.chat.util designed for creating rule-based chatbots. It takes a list of pattern-response pairs and uses regular expressions (regex) to match user inputs to predefined patterns. Internally, it tokenizes input using NLTK’s punkt tokenizer and applies regex matching.
3) reflections: A dictionary ({'i': 'you', 'me': 'you', 'my': 'your', ...}) that enables the chatbot to "reflect" user statements by swapping pronouns. For example, if a user says "I like to learn," the chatbot could respond "You like to learn?" This adds a layer of conversational dynamism, though it’s underutilized in this basic example.
 These imports provide the core functionality for pattern matching and response generation, abstracting away complex NLP tasks into a simple framework suitable for beginners.

The primary advantages of this code lie in its simplicity, accessibility, and customizability, making it an excellent choice for learning, quick prototyping, or small-scale, controlled interactions. It’s a practical starting point in the world of NLP and chatbot development, offering a balance of functionality and ease that more advanced systems sacrifice for power. If you’re looking to build something fast, understandable, and fully under your control, this code is a fantastic tool to have in your arsenal.

OUTPUT :

![Image](https://github.com/user-attachments/assets/a69f6819-934c-4ef5-b8e6-d7d0feb50e6d)
