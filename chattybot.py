import random  # import random once at the top

class ChatBot:
    def __init__(self, name):
        """
        Initialize the chatbot with a name.
        Also sets up a dictionary of possible responses and memory for user's name.
        """
        self.name = name
        self.user_name = None  # stores the user's name if they introduce themselves
        self.responses = {
            'hi': ['Hello! 👋', 'Hi there! 🙂', 'Hey! 😄'],  # random greetings with emojis
            'bye': ['Goodbye! 👋', 'See you later! 🙂', 'Bye! 😎'],
            'help': ['I can respond to "hi" 👋, "bye" 👋, and "help" ❓']
        }

    def greet(self):
        """
        Print a greeting from the chatbot when the program starts.
        """
        print(f"Hello, I am {self.name}, your chatbot! 🤖")

    def respond(self, message):
        """
        Process the user's message and return an appropriate response.
        Features:
        - Remember user's name
        - Randomized responses
        """
        message = message.lower()  # convert message to lowercase for easier matching
        
        # Memory: store user's name if they introduce themselves
        if message.startswith("my name is "):
            self.user_name = message.replace("my name is ", "").title()
            return f"Nice to meet you, {self.user_name}! 😃"

        # Randomized replies for predefined messages
        if message in self.responses:
            # If user_name exists and message is 'hi', personalize greeting
            if message == 'hi' and self.user_name:
                return f"Hello {self.user_name}! " + random.choice(self.responses[message])
            return random.choice(self.responses[message])

        # Default response for unrecognized input
        return "I don't understand that command. 🤔"


# --- Main Program ---
bot = ChatBot("Chatty")
bot.greet()  # initial greeting

while True:
    # Dynamic input prompt: shows user's name if remembered
    prompt = f"{bot.user_name}: " if bot.user_name else "You: "
    user_input = input(prompt)
    
    # Exit condition
    if user_input.lower() == 'exit':
        print(f'{bot.name}: Goodbye! 👋')
        break
    
    # Get bot response and print
    reply = bot.respond(user_input)
    print(f"{bot.name}: {reply}")

    # Replay feature after "bye"
    if user_input.lower() == "bye":
        again = input("Do you want to chat again? (yes/no): ")
        if again.lower() != "yes":
            print(f"{bot.name}: Okay, see you next time! 😊")
            break