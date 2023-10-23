import json
import os
import requests

import openai

# Load your OpenAI API key and GitHub token from environment variables
openai.api_key = os.environ["OPENAI_KEY"]
github_token = os.environ["GITHUB_TOKEN"]

# The URL of the issue. You'd dynamically fetch this in your workflow
issue_url = os.environ["ISSUE_URL"]

# Get the issue details
response = requests.get(
    issue_url,
    headers={"Authorization": f"token {github_token}"}
)
issue_data = response.json()

# The body of the issue contains the workout details
workout_text = issue_data["body"]

# The new comment can be obtained from the GitHub event payload, or you could fetch it in a similar way as the issue
comment_text = os.environ["COMMENT_TEXT"]

# Create the conversation payload
payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": f"You are a personal trainer. You are helping a client with their weekly workout plan. For context, here is the plan:\n\n{workout_text}\n\n"},
        {"role": "user", "content": f"The client also had the following question or comment:\n\n{comment_text}\n\n"},
        {"role": "user", "content": f"Please continue the conversation with helpful and detailed advice for the client.\n\n"}
    ],
}

# Make the API call
response = openai.ChatCompletion.create(**payload)

# Extract the generated advice
advice = response['choices'][0]['message']['content']

# Write the advice to a markdown file to be used in the GitHub action to comment back
with open("comment_advice.md", "w") as f:
    f.write(f"## Personal Trainer Response\n\n{advice}")
