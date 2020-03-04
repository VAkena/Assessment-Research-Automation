from bs4 import BeautifulSoup
import requests

# Load website from URL
source = requests.get(
    'https://handbook.uts.edu.au/directory/maj03445.html').text

# Create soup object and load parser
soup = BeautifulSoup(source, 'lxml')
# Create file using extension of choice
file = open('subjects.pdf', 'w+')

# Select all subjects in the 'Completion Requirements' table
subject_names = soup.find_all('table')
# For every subject in the table, display the text attribute
for subject in subject_names:
    # Writes output to file
    print(subject.text, file=file)

file.close()
