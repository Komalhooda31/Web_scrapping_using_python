# Web_scrapping_using_python
Extracts content from a list of URLs stored in an Excel file, it extracts paragraphs (&lt;p>) and level 1 headings (&lt;h1>) from the web pages. The extracted content is then saved in separate text files inside a folder named "Projects".
It imports necessary libraries: pandas, os, requests, BeautifulSoup from bs4, html5lib, re, and hashlib.

The URLs are read from the "urls" column of the "Input.xlsx" Excel file using the pd.read_excel() function and stored in the URLS variable.

Two functions are defined:

extract_save_content(URL): This function fetches content from the specified URL, extracts paragraphs and level 1 headings, and saves them in a text file without HTML tags inside the "Projects" folder.
create_from_url(URL): This function generates a filename based on the URL, removing special characters and creating a unique filename based on the hash of the URL if necessary.
The script loops through each URL in the list of URLs and calls the extract_save_content() function for each URL. The content from each URL is saved as separate text files inside the "Projects" folder.
