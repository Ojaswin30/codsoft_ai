import random
import re


class SupportBot:

    def __init__(self, debug=False):
        """
        Initializes the bot with predefined responses and settings.
        """
        self.debug = debug  # Enable or disable debugging
        self.support_responses = {
            'ask_about_product': (r'\bproduct\b', self.ask_about_product),
            'technical_support': (r'\btechnical support\b', self.technical_support),
            'about_returns': (r'\breturn policy\b', self.about_returns),
            'general_query': (r'\bhelp\b', self.general_query)
        }
        self.negative_res = {"no", "nope", "nay", "not a chance", "sorry"}
        self.exit_commands = {"quit", "pause", "exit", "goodbye", "bye", "farewell"}

    def greet(self):
        """
        Greets the user and initializes the conversation.
        """
        self.name = input("Hello! Welcome to our customer support. What's your name?\n").strip()
        if self.debug:
            print(f"[DEBUG] Captured Name: {self.name}")
       
        self.chat()

    def make_exit(self, reply):
        """
        Checks if the user wants to exit the conversation.
        """
        if any(command in reply for command in self.exit_commands):
            print("Thanks for reaching out. Have a great day!")
            return True
        return False

    def chat(self):
        """
        Handles the main chat loop.
        """
        print("You can type your queries below. Type 'exit' or 'bye' to end the conversation.")
        while True:
            reply = input("Your query: ").lower().strip()
            if self.make_exit(reply):
                break
            print(self.match_reply(reply))

    def match_reply(self, reply):
        """
        Matches user input with predefined intents and returns an appropriate response.
        """
        for intent, (regex_pattern, handler) in self.support_responses.items():
            if re.search(regex_pattern, reply):
                if self.debug:
                    print(f"[DEBUG] Matched Intent: {intent}")
                return handler()
        return self.no_match_intent()

    def ask_about_product(self):
        responses = [
            "Our product is top-notch and has excellent reviews!",
            "You can find all product details on our website.",
            "We offer a wide variety of products for your needs. What are you looking for?"
        ]
        return random.choice(responses)

    def technical_support(self):
        responses = [
            "Please visit our technical support page for detailed assistance.",
            "You can also call our tech support helpline for immediate help.",
            "Our technical team is available 24/7 to help with your queries."
        ]
        return random.choice(responses)

    def about_returns(self):
        responses = [
            "We have a 30-day return policy.",
            "Please ensure the product is in its original condition when returning.",
            "For returns, visit our return policy page or contact customer service."
        ]
        return random.choice(responses)

    def general_query(self):
        responses = [
            "How can I assist you further?",
            "Is there anything else you'd like to know?",
            "Feel free to ask any questions about our services."
        ]
        return random.choice(responses)

    def no_match_intent(self):
        """
        Default response for unrecognized input.
        """
        responses = [
            "I'm sorry, I didn't quite understand that. Can you please rephrase?",
            "My apologies, could you provide more details?",
            "I'm not sure I understand. Could you clarify?"
        ]
        return random.choice(responses)


if __name__ == "__main__":
    bot = SupportBot(debug=False)
    bot.greet()




# oj
# Tell me about your product.
# I need technical support.
# What’s your return policy?
# I want to know about promotions.
# bye