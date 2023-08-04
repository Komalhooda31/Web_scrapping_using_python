import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
import html5lib
import re
import hashlib


files = pd.read_excel("Input.xlsx")
URLS = files['urls']


URL = 'https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/'
request = requests.get(URL)


def extract_save_content(URL):

    soup = BeautifulSoup(request.content, 'html5lib')
    paragraphs = soup.find_all('p',)
    headings = soup.find_all('h1')

    Output_file = create_from_url(URL)

    projects_folder = 'Projects'
    if not os.path.exists(projects_folder):
        os.mkdir(projects_folder)

# Writing content into the text file without tags
    with open(os.path.join(projects_folder,Output_file), 'w', encoding= 'utf-8') as file:
        for heading in headings:
            file.write(heading.get_text()+ '\n')
    
        for paragraph in paragraphs:
            file.write(paragraph.get_text()+ '\n')
    print(f'content from {URL}saved')


def create_from_url(URL):
    Output_file = URL.split('/')[-1]

    
    Output_file = re.sub(r'\W+', '', Output_file)

   
    if not Output_file:
        Output_file = f'article_{hashlib.md5(URL.encode()).hexdigest()}'
    
    return f'{Output_file}.txt'

url = URL.strip()  


# loop for all urls in the csv file.
for URL in URLS:
    URL = URL.strip()
    extract_save_content(URL)
    