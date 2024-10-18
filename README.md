# Web_Scraper

# Documentation for Aptitude Questions Web Scraper

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [How to Use](#how-to-use)
4. [Dependencies](#dependencies)

---

## Project Overview

This project provides a Python script to scrape aptitude questions, their options, and correct answers from a webpage. The data is stored in a CSV file (`aptitude_questions_with_answers.csv`). The script ensures that all necessary fields are present before appending data to the CSV.

---

## Installation

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package manager)

### Setup

1. **Clone the repository**:
   Open a terminal or command prompt and run the following command to clone the project:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**:
   Create a virtual environment (optional but recommended) and install the required packages using the `requirements.txt` file:

   - Set up a virtual environment (optional):

     ```bash
     python -m venv .venv
     ```

   - Activate the virtual environment:

     - For Windows:
       ```bash
       .venv\Scripts\activate
       ```
     - For macOS/Linux:
       ```bash
       source .venv/bin/activate
       ```

   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

---

## How to Use

1. **Run the Script**:
   Execute the script by running `script.py`:

   ```bash
   python script.py
   ```

2. **Provide the URL**:
   You will be prompted to enter the URL of the aptitude questions webpage. Enter the full URL and press Enter.

   Example:

   ```
   Enter the URL of the aptitude questions page: https://www.indiabix.com/aptitude/time-and-distance/
   ```

3. **Check the Output**:
   The scraped data will be saved to `aptitude_questions_with_answers.csv`. If the file already exists, the data will be appended to it.

4. To close the code, press `Ctrl + C`.
---

## Dependencies

This project requires the following Python packages:

- `requests`: For making HTTP requests to retrieve the webpage.
- `beautifulsoup4`: For parsing HTML content.
- `pandas`: For storing and handling data in CSV format.
- `urllib3`: For managing HTTP requests and suppressing SSL warnings.

Install the dependencies by running:

```bash
pip install -r requirements.txt
```
