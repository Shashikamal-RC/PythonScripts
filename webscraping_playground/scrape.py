import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
subText = soup.select('.subtext')

links2 = soup2.select('.storylink')
subText2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subText + subText2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse = True)

def create_custom_hn(links, subText):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        votes = subText[idx].select('.score')
        if len(votes):
            point = int(votes[0].getText().replace(' points', ''))
            if point > 99:
                hn.append({'title': title, "link": href, "votes":point })
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))