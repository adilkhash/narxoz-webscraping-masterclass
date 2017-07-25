import requests
from bs4 import BeautifulSoup


def get_paper_links(paper_tag):
    return paper_tag.h3.a.attrs['href']


url = 'https://scholar.google.com/scholar?hl=ru&q=computer+vision&btnG='

response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

paper_container = html.find_all('div', class_='gs_r')

links = [get_paper_links(paper_tag) for paper_tag in paper_container]

print(list(filter(lambda l: l.find('.pdf') != -1, links)))  # list only pdf
