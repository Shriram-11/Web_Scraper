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
        # print(soup)
        # Extract the topic (e.g., Problems on Trains)
        whole_topic = soup.find('div', class_='all-questions')
        # print(whole_topic)
        topic_title = whole_topic.find('h2')
        # print(topic_title.text)

        # Find all question blocks
        questions = whole_topic.find_all('p', class_='questionBody individual_question')
        for question in questions:
            print(question.text)
            print('---------------------------------')

        options_list = whole_topic.find_all('ol', class_='options-list')

        for options in options_list:
            for singular_option in options.find_all('li'):
                print(singular_option.text)
            print('---------------------------------')

        answer_cards = whole_topic.find_all('div', class_='card answer-card')
        for answer_card in answer_cards:
            answer = answer_card.find('div')
            if answer:
                print(answer.text.strip())
            print('---------------------------------')

        

if __name__ == "__main__":
    # Take the URL input from the user
    while True:
        try:
            url = input("Enter the URL of the aptitude questions page: ")
            run_url_scraper(url)
        except KeyboardInterrupt:
            print("\nExiting the program.")
            break