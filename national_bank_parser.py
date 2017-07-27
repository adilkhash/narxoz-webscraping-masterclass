import requests
from bs4 import BeautifulSoup


# парсим НацБанк
def retrieve_national_bank_url():
    response = requests.get('http://www.nationalbank.kz/?docid=672&switch=english')
    soup = BeautifulSoup(response.text, 'html.parser')
    files = soup.find('div', attrs={'id': 'accordion'})
    tables = files.find_all('table')
    return tables


def retrieve_links(table):
    links = []
    table_rows = table.find_all('tr')  # ищем все строки в таблице

    for table_row in table_rows:
        td = table_row.find_all('td', attrs={'class': 'gen2'})
        if td:
            links.append(td[-1].a.attrs['href'])

    return links

if __name__ == '__main__':
    tables = retrieve_national_bank_url()
    all_links = []
    for table in tables:
        all_links += retrieve_links(table)
