import json
import os

import openai

# Load your OpenAI API key from an environment variable or secret management service
openai.api_key = os.environ["OPENAI_KEY"]

# Read in the workout plan from the file
with open("workout_output.txt", "r") as f:
    workout_text = f.read()

# Create the conversation payload
payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": f"You are a personal trainer. You are helping a client with their weekly workout plan. Please provide advice for the exercises in each day. Here is the plan:\n\n{workout_text}\n\n"}],
}

# Make the API call
response = openai.ChatCompletion.create(**payload)

# Extract and print the generated advice
advice = response['choices'][0]['message']['content']

# Write the advice to a markdown file
with open("workout_advice.md", "w") as f:
    f.write(f"## Personal Trainer Advice\n\n{advice}")
