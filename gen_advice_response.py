import json
import os
import requests

from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_KEY"])

github_token = os.environ["GITHUB_TOKEN"]

# The URL of the issue. You'd dynamically fetch this in your workflow
issue_url = os.environ["ISSUE_URL"]

# Get the issue details
response = requests.get(issue_url, headers={"Authorization": f"token {github_token}"})
issue_data = response.json()

# The body of the issue contains the workout details
workout_text = issue_data["body"]

# The new comment can be obtained from the GitHub event payload, or you could fetch it in a similar way as the issue
comment_text = os.environ["COMMENT_TEXT"]

# Build the full conversation prompt
prompt = f"""You are a personal trainer. You are helping a client with their weekly workout plan. For context, here is the plan:\n\n{workout_text}\n\nThe client also had the following question or comment:\n\n{comment_text}\n\nPlease continue the conversation with helpful and detailed advice for the client.\n\n"""

# Generate trainer advice using ChatCompletion
completion = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[{"role": "user", "content": prompt}],
)

# Extract the generated advice
advice = completion.choices[0].message.content

# Write the advice to a markdown file for the GitHub action comment
with open("comment_advice.md", "w") as f:
    f.write(f"## Personal Trainer Response\n\n{advice}")
