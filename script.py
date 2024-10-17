import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib3

# Suppress SSL warnings if you are disabling verification
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Take the URL input from the user
url = input("Enter the URL of the aptitude questions page: ")

# Make the request to the provided URL
response = requests.get(url, verify=False)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    questions = []
    options_list = []
    answers = []
    topics = []

    # Extract the topic (e.g., Problems on Trains)
    topic_element = soup.find('div', class_='h5 w-100 mb-3 p-0')
    topic = topic_element.text.strip() if topic_element else "Unknown"

    # Find all question blocks
    for question_block in soup.find_all('div', class_='bix-div-container'):
        # Extract the question
        question_element = question_block.find('div', class_='bix-td-qtxt')
        if question_element:
            question_text = question_element.text.strip()
        else:
            question_text = "Question not found"  # Handle missing questions

        # Extract the options
        options = []
        for option_block in question_block.find_all('div', class_='bix-td-option-val'):
            option_text = option_block.text.strip()
            options.append(option_text)

        # Extract the correct answer (letter) and match it to the actual option text
        answer_element = question_block.find('input', class_='jq-hdnakq')
        if answer_element:
            # The answer will be A, B, C, or D
            correct_option_letter = answer_element['value']
            # Match the letter to the corresponding option text
            option_mapping = {
                'A': options[0] if len(options) > 0 else '',
                'B': options[1] if len(options) > 1 else '',
                'C': options[2] if len(options) > 2 else '',
                'D': options[3] if len(options) > 3 else ''
            }
            correct_answer = option_mapping.get(
                correct_option_letter, "Answer not found")
        else:
            correct_answer = "Answer not found"  # Handle missing answers

        # Append data to lists
        topics.append(topic)
        questions.append(question_text)
        options_list.append(options)
        answers.append(correct_answer)

    # Create a DataFrame to store the scraped data
    data = {
        'Topic': topics,
        'Question': questions,
        'Option 1': [options[0] if len(options) > 0 else '' for options in options_list],
        'Option 2': [options[1] if len(options) > 1 else '' for options in options_list],
        'Option 3': [options[2] if len(options) > 2 else '' for options in options_list],
        'Option 4': [options[3] if len(options) > 3 else '' for options in options_list],
        'Answer': answers
    }

    df = pd.DataFrame(data)

    # Define the file path for the CSV
    csv_file = 'aptitude_questions_with_answers.csv'

    # Check if the file already exists
    if os.path.isfile(csv_file):
        # Append data to the existing CSV without writing the header
        df.to_csv(csv_file, mode='a', header=False, index=False)
    else:
        # Write a new CSV with the header
        df.to_csv(csv_file, mode='w', header=True, index=False)

    print("Data has been appended to aptitude_questions_with_answers.csv")

else:
    print(f"Failed to retrieve page, status code: {response.status_code}")
