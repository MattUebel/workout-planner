import pandas as pd
import random

def generate_weekly_workout(file_name):
    df = pd.read_csv(file_name)
    
    # Initialize Markdown-formatted output string
    md_output = "## Weekly Workout Plan\n\n"
    
    # Categorize exercises
    legs_exercises = df[df['body_part'] == 'Legs']
    push_exercises = df[df['body_part'] == 'Push Movements']
    pull_exercises = df[df['body_part'] == 'Pull Movements']
    core_exercises = df[df['body_part'] == 'Core']

    # Initialize workout week
    weekly_workout = {'Day 1 - Legs': [], 'Day 2 - Upper Body': [], 'Day 3 - Core': []}

    # Generate Leg day workouts
    specific_legs = random.sample(legs_exercises['exercise_name'].tolist(), 3)
    core_extra = random.sample(core_exercises['exercise_name'].tolist(), 3)
    weekly_workout['Day 1 - Legs'] = specific_legs + core_extra

    # Generate Upper Body day workouts (mixed Push and Pull)
    specific_push = random.sample(push_exercises['exercise_name'].tolist(), 2)
    specific_pull = random.sample(pull_exercises['exercise_name'].tolist(), 2)
    core_extra = random.sample(core_exercises['exercise_name'].tolist(), 2)
    weekly_workout['Day 2 - Upper Body'] = specific_push + specific_pull + core_extra

    # Generate Core day workouts
    specific_core = random.sample(core_exercises['exercise_name'].tolist(), 4)
    extra_legs = random.sample(legs_exercises['exercise_name'].tolist(), 1)
    extra_push = random.sample(push_exercises['exercise_name'].tolist(), 1)
    weekly_workout['Day 3 - Core'] = specific_core + [extra_legs[0], extra_push[0]]

    # Add the exercises to the Markdown-formatted output string
    for day, exercises in weekly_workout.items():
        md_output += f"### {day}\n\n"
        for exercise in exercises:
            md_output += f"- {exercise}\n"
        md_output += "\n"

    return md_output

# Read in the CSV and generate a weekly workout plan
weekly_plan = generate_weekly_workout('workouts.csv')

# Display the Markdown-formatted plan
print(weekly_plan)
