import requests

response = requests.get('http://narxoz.kz')

print('Request headers\n', response.request.headers)
print('Response headers\n', response.headers)
