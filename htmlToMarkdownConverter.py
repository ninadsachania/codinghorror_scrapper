# Author: Ninad Sachania

import bs4 as bs

sauce = ''

with open('urls.html', 'r') as f:
    for line in f:
        sauce = sauce + line

soup = bs.BeautifulSoup(sauce, 'lxml')


text = []
links = []

for a in soup.find_all('a'):
    text.append(a.text)
    links.append(a.get('href'))

dates = []

for span in soup.find_all('span'):
    dates.append(span.text)

if len(dates) != len(links):
    print('Error: Links and dates do not match')
    exit(-1)
else:
    for i, link in enumerate(links):
        with open('blogarchive.md', 'a') as f:
            f.write('[' + text[i] + '](' + links[i] + ') (' + dates[i].strip() + ')')
            f.write('\n\n')
