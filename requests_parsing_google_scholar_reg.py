import re
import requests

response = requests.get('https://scholar.google.com/scholar?hl=ru&q=machine+learning&btnG=')
html_content = response.text
results = re.findall(r'<a href="((http|https)://(?P<url>.+?))"', html_content)

for link in results:
    print(link[0])
