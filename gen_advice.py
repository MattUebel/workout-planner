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
    "prompt": f"Hello my Personal Trainer! This is my workout plan for the week:\n{workout_text}\n\nCould you help with advice on the exercises for each day? Please respond with markdown formatted text",
    "max_tokens": 300
}

# Make the API call
response = openai.ChatCompletion.create(**payload)

# Extract and print the generated advice
advice = response.choices[0].text.strip()

# Write the advice to a markdown file
with open("workout_advice.md", "w") as f:
    f.write(f"## Personal Trainer Advice\n\n{advice}")
