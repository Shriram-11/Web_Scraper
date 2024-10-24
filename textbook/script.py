import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib3

# Suppress SSL warnings if you are disabling verification
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def run_url_scraper(url):
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
        whole_topic = soup.find('div', class_='all-questions')
        topic_title = whole_topic.find('h2').text.strip() if whole_topic.find('h2') else "Unknown"

        # Find all question blocks
        questions = whole_topic.find_all('p', class_='questionBody individual_question')
        options_list = whole_topic.find_all('ol', class_='options-list')
        answer_cards = whole_topic.find_all('div', class_='card answer-card')

        data = []

        for i in range(len(questions)):
            question_text = questions[i].text.strip()
            options = [opt.text.strip() for opt in options_list[i].find_all('li')]
            answer = answer_cards[i].find('div').text.strip() if answer_cards[i].find('div') else "Unknown"

            if len(options) >= 4:
                data.append({
                    'Topic': topic_title,
                    'Question': question_text,
                    'Option 1': options[0],
                    'Option 2': options[1],
                    'Option 3': options[2],
                    'Option 4': options[3],
                    'Answer': answer
                })

        if data:
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
            print("No valid data to append.")
    else:
        print(f"Failed to retrieve page, status code: {response.status_code}")

if __name__ == "__main__":
    # Take the URL input from the user
    while True:
        try:
            url = input("Enter the URL of the aptitude questions page: ")
            run_url_scraper(url)
        except KeyboardInterrupt:
            print("\nExiting the program.")
            break