import time
import random
import requests
from bs4 import BeautifulSoup


def extract_paper_url(paper_tag):
    return paper_tag.h3.a.attrs['href']


def retrieve_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    papers_links = soup.find_all('div', attrs={'class': 'gs_r'})
    return papers_links


def get_url(query, max_page=10):
    links = []
    for page in range(0, max_page*10+10, 10):
        links.append('https://scholar.google.com/scholar?start='+str(page)+'&q='+query+'&hl=ru&as_sdt=0,5')
    return links


if __name__ == '__main__':
    ml_results = get_url('machine learning')
    all_papers = []
    for link in ml_results:
        print('Processing.. ', link)
        paper_tags = retrieve_url(ml_results[0])

        for paper in paper_tags:
            all_papers.append(extract_paper_url(paper))

        time.sleep(random.randint(3, 6))  # делаем паузу перед парсингом следующей страницы
