import os
from dotenv import load_dotenv
import openai

# Load environment variables from the .env file
load_dotenv()

# Set up your OpenAI API credentials
openai.api_key = os.getenv("OPENAI_API_KEY")
ai_model = os.getenv("OPENAI_MODEL")

chat_messages = []

# Define the function for user input and model response
def chat_with_model(prompt):
    response = openai.ChatCompletion.create(
        model=ai_model,
        messages=prompt,
        temperature=0.7,
    )
    return response.choices[0].message.content

# Start the chat loop
print("Welcome to Chat with GPT!")
print("Type 'quit' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Chat ended.")
        break

    chat_messages.append({"role": "user", "content": user_input})

    # Send user input to the model and get the response
    model_response = chat_with_model(chat_messages)

    chat_messages.append({"role": "assistant", "content": model_response})

    print("GPT: " + model_response)
