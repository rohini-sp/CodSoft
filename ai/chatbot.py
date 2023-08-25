import random

# Dictionary of pattern and responses
pattern = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm just a bot, but I'm here to help!", "I'm doing well, thank you for asking!", "I don't have feelings, but I'm ready to assist you!"],
    "bye": ["Goodbye!", "Farewell!", "See you later!"],
    "default": ["I'm not sure what you mean. Can you please rephrase?", "I'm still learning, could you provide more details?", "I'm sorry, I don't have an answer for that."],
    "who created you": ["I was created by an enthusiastic learner Rohini!"],
    "what can you do" :["I can chat with you."],
    
}

# Function to generate a response
def generate_response(user_input):
    user_input = user_input.lower()
    
    for key in pattern:
        if key in user_input:
            return random.choice(pattern[key])
    
    return random.choice(pattern["default"])

# Main loop for the chatbot
print("Bot: Hi! I'm a simple chatbot. You can start a conversation or type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break
    
    response = generate_response(user_input)
    print("Bot:", response)
