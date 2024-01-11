# Job Scraper

This Python script scrapes the latest job advertisements from a specified website (in this case, TimesJobs) and filters out jobs that require a specific skill that the user is not familiar with.

## Prerequisites

Make sure you have the following libraries installed before running the script:

- BeautifulSoup (`pip install beautifulsoup4`)
- requests (`pip install requests`)

## Usage

1. Run the script in a Python environment.
2. Enter the skill that you are not familiar with when prompted.
3. The script will filter out jobs requiring the specified skill and save relevant information about each job in separate text files.

## Code Explanation

The script performs the following steps:

1. Imports necessary libraries: `BeautifulSoup`, `requests`, and `time`.
2. Prompts the user to input a skill they are not familiar with.
3. Retrieves the HTML content of the job search page from TimesJobs.
4. Parses the HTML using BeautifulSoup.
5. Finds and extracts job listings based on their HTML structure.
6. Iterates through the job listings and extracts relevant information such as company name, required skills, and more info link.
7. Checks if the unfamiliar skill is not present in the required skills for each job.
8. Saves information about each eligible job in separate text files within a 'posts' directory.
9. The script runs in an infinite loop, continuously scraping and checking for new job postings at regular intervals.

**Note:** Make sure to adjust the URL in the `requests.get` method if you want to scrape job listings from a different website.

Feel free to customize the script to suit your specific requirements.