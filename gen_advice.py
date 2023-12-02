import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_KEY"])

# Read the workout plan from the file
with open("workout_output.txt", "r") as f:
    workout_text = f.read()

# Create the conversation prompt
prompt = f"You are a personal trainer. You are helping a client with their weekly workout plan. Please provide advice for the exercises in each day: \n\n{workout_text}\n\n"

# Generate advice using the ChatCompletion API
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
)

# Extract the generated advice
advice = completion.choices[0].message.content

# Write the advice to a markdown file
with open("workout_advice.md", "w") as f:
    f.write(f"## Personal Trainer Advice\n\n{advice}")
