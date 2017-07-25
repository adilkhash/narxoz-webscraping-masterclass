import requests
from bs4 import BeautifulSoup


def extract_proxies(tr_tag):
    ip = tr_tag.td.text
    port = tr_tag.td.next_sibling.text
    return ip, port


if __name__ == '__main__':
    url = 'https://free-proxy-list.net/anonymous-proxy.html'

    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')
    proxy_table = html.find('table', attrs={'id': 'proxylisttable'})
    table_rows = proxy_table.tbody.find_all('tr')

    proxies = [extract_proxies(tr_tag) for tr_tag in table_rows]

    print(proxies)
