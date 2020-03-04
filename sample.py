from bs4 import BeautifulSoup
import requests

# Load Networking and Cybersecurity Major
source = requests.get('https://handbook.uts.edu.au/directory/maj03445.html').text
# Create soup object and load parser
soup = BeautifulSoup(source, 'lxml')

# Select all subjects in the 'Completion Requirements' table
subject_names = soup.find_all('table')
# For every subject in the table, display the text attribute
for subject in subject_names:
    print(subject.text)