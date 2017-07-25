import re

regex = re.compile(r'\d\d\d-\d\d\d-\d\d-\d\d')
result = regex.search('My telephone number is 701-577-15-57')

if result:
    print(result.group())


regex = re.compile(r'\d{3}-\d{3}-\d{2}-\d{2}')
result = regex.search('My telephone number is 701-577-15-57')

if result:
    print(result.group())
