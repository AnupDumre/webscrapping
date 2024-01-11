# Job Advertisement Scraper

# Importing necessary libraries for web scraping
from bs4 import BeautifulSoup
import requests
import time

# Prompting the user to input a skill they are not familiar with
print('Enter a skill that you are not familiar with: ')
unfamiliar_skill = input('>')

# Providing feedback to the user about the filtering process
print(f'Filtering out jobs requiring skill: {unfamiliar_skill}')

# Function to find and save the latest job advertisements
def find_jobs():
    # Fetching HTML content from the specified job search website
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=%22Data+Science%22&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    
    # Extracting job listings based on HTML structure
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    
    # Iterating through job listings and checking for the latest ones
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        
        # Filtering out jobs posted recently
        if 'few' in published_date:
            company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')
            cleaned_company_name = company_name.split('(')[0].strip()

            # Extracting required skills, more info link, and checking for unfamiliar skill
            skills = job.find('span', class_="srp-skills").text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                # Saving relevant job information in a text file
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {cleaned_company_name}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"More Info: {more_info}")
                print(f'File saved: {index}')

# Main execution block, continuously scraping for new job postings
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        # Providing feedback and waiting for a specified time before scraping again
        print(f"Waiting {time_wait} minute(s) before the next scrape...")
        time.sleep(time_wait * 60)
