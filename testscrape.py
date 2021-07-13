import requests
import pandas as pd
import pyap
import re
from bs4 import BeautifulSoup

url = 'http://www.patricksgrille.com/contact-patricks-grille'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)
li = []
output = ''
lglnm = '''Patrick's Grille'''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head',
    'input',
    'script',
    # there may be more elements you don't want, such as "style", etc.
]

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)

# for t in text:
#    if t.parent.name not in blacklist:
#        li.append(str(t))
# df = pd.DataFrame(li, columns=['Data'])
# df = (df.loc[df['Data'] != '\n'])

# Legal Name
if output.find(lglnm) != -1:
    print(lglnm)
else:
    print('Legal name not found')

# Address
addresses = pyap.parse(output, country='US')
for address in addresses:
    print(address)
    print(address.as_dict())

# Phone
r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
results = r.findall(output)
phones = ""
for x in results:
    phones += str(x) + "\n"
print(phones)

# Email
r = re.compile(r'(\b[\w.]+@+[\w.]+.+[\w.]\b)')
results = r.findall(output)
emails = ""
for x in results:
    emails += str(x)
print(emails)

# df['Data'].to_csv(
#      "C:/Users/Fungui/PycharmProjects/Webscraper/experian_test/experian_test/patricksgrille.csv")
