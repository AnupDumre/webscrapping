from bs4 import BeautifulSoup

# Read HTML content from a local file
with open("localSite.html", "r") as html_file:
    content = html_file.read()

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(content, "lxml")

# Uncomment the following line to print the prettified HTML content
# print(soup.prettify())

# Find all the course cards with the class "card"
course_cards = soup.find_all("div", class_="card")

# Iterate through each course card and extract relevant information
for course in course_cards:
    # Extract course name from the h5 tag within the card
    course_name = course.h5.text
    
    # Extract link title or paragraph from the p tag within the card
    link_title = course.p.text
    
    # Print formatted information about each course
    print(f"Course Name: {course_name}\nDescription: {link_title}\n{'-' * 30}\n")
