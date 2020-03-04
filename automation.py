from bs4 import BeautifulSoup
import requests

# Get website
website = requests.get('https://www.studiobinder.com/blog/best-filmmaking-software-and-tools/#Story-Development')
soup = BeautifulSoup(website.content, 'html.parser')
content = soup.find('div', class_='thrv_wrapper thrv_text_element')
print(content)
