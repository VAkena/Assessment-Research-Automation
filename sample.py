import shutil
import urllib.request
from bs4 import BeautifulSoup
import requests
from urllib import request
from urllib.request import urlretrieve

# Load website from URL
source = requests.get(
    'https://handbook.uts.edu.au/directory/maj03445.html').text

# Create soup object and load parser
soup = BeautifulSoup(source, 'lxml')
# Create file using extension of choice
file = open('subjects.txt', 'w+')

# Select all subjects in the 'Completion Requirements' table
subject_names = soup.find_all('table')
# For every subject in the table, display the text attribute
for subject in subject_names:
    # Writes output to file
    print(subject.text, file=file)

file.close()

# Define  URL and output location
url = 'https://www.adobe.com/support/products/enterprise/knowledgecenter/media/c4611_sample_explain.pdf'
output_file = "./sample_file.pdf"

# Open URL and write to defined output file
with urllib.request.urlopen(url) as response, open(output_file, 'wb') as output:
    shutil.copyfileobj(response, output)
