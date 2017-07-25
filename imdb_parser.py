import requests
from bs4 import BeautifulSoup


def get_movie_meta_data(film_div):
    title = film_div.h3.a.text
    rating = film_div.find('div', class_='ratings-imdb-rating').attrs['data-value']
    votes = film_div.find('span', attrs={'name': 'nv'}).attrs['data-value']
    return {'title': title, 'rating': rating, 'votes': votes}

if __name__ == '__main__':
    url = 'http://www.imdb.com/search/title?release_date=2016'
    response = requests.get(url)
    if response.status_code == 200:
        html = BeautifulSoup(response.text, 'html.parser')
        film_container = html.find_all('div', class_='lister-item mode-advanced')

        for film in film_container:
            print(get_movie_meta_data(film))
