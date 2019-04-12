# Author: Ninad Sachania
import bs4 as bs
import requests 
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
URL = 'https://blog.codinghorror.com'

FILENAME = 'urls.html'

source = requests.get(URL).text
soup = bs.BeautifulSoup(source, 'lxml')

f = open(FILENAME, 'a')
md = open('main.md', 'w')

for i in range(1, 286):
    source = requests.get(URL + '/page/' + str(i) +'/').text
    soup = bs.BeautifulSoup(source, 'lxml')

    dates = []
    for timedate in soup.find_all('time'):
        dates.append(timedate.text)

    links = []
    for h2 in soup.find_all('h2', class_='post-title'):
        string = h2.a.text 
        # print(string)
        href = URL + h2.a.get('href')
        # print(href)

        final_string = '<a href="' + href + '">' + str(string) + '</a>'
        links.append(final_string)

        # f.write(final_string)
        # f.write('<br>')
        # f.write('\n')

    if len(dates) != len(links):
        print("Something's wrong @ " + str(i))
        exit(-1)
    else:
        for i, date in enumerate(dates):
            f.write(links[i] + ' <span> ' + date + '</span>')
            f.write('\n')
            f.write('<br>')
            f.write('\n')

            print(links[i], date)

print('Done')
