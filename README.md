# Automated Workout Planner and Personal Trainer

## Description
This repository contains a GitHub Actions workflow and associated Python scripts to automate the process of generating weekly workout plans. It uses OpenAI's GPT models to act as a "virtual personal trainer," offering advice and additional tips for the workouts generated. 

## Features

- **Automatic Issue Creation**: Every week, a new GitHub issue is created that contains a weekly workout plan.
- **Personal Trainer Advice**: A follow-up comment is added to the issue, offering professional advice on the workout plan, as if it came from a personal trainer.
- **Interactive Feedback**: Users can comment on the workout issue and receive additional advice and modifications to the workout plan.

## Usage

### Prerequisites
- Python 3.9+
- OpenAI API Key

### Setup

1. Clone this repo

2. Add your OpenAI API key to your GitHub repository secrets and name it `OPENAI_KEY`.

3. Enable GitHub Actions in your repository settings if you haven't.

4. Ensure that Actions has `write` access to your repository.

5. Customize the workouts.csv file to your liking.

### Workflow File Locations

- Main workout generation and issue creation: `.github/workflows/generate_workouts.yml`
- Personal trainer advice generation: `.github/workflows/advice_response.yml`

## How it Works

1. The `generate_workouts.yml` workflow runs weekly to create a new workout plan. It leverages a Python script to randomly select exercises and generate the workout plan.

2. The `advice_response.yml` workflow triggers when an issue with the label `workout-plan` is commented on by a non-actions user. It calls the OpenAI API to generate advice and comments on the issue.

## Limitations of Using Large Language Models for Workout Routines

While our system utilizes OpenAI's GPT models to generate workout plans and provide personal trainer advice, it's important to note that these large language models can sometimes produce unrealistic or inaccurate content. We advise users to review the generated workout routines for realism and consult with a professional trainer if necessary. This approach ensures that the workouts are not only innovative but also safe and tailored to your fitness level.

## Troubleshooting

- If the OpenAI call fails, check the API key and the rate limits for your account.
- If GitHub Actions fails, the error messages are usually very informative. Check the Actions tab for details.

## Contributions

Feel free to contribute to this project by opening issues or submitting pull requests.
