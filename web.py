#A web Scraping program to get the names of universities of Bangladesh
import requests
from bs4 import BeautifulSoup

page = requests.get("https://en.wikipedia.org/wiki/List_of_universities_in_Bangladesh")
soup = BeautifulSoup(page.content, 'html.parser')
Table = soup.find('table',{'class':'wikitable sortable'})
TD = Table.findAll('td')
#Links = TD.find('a')

#Universities = []
#for Link in Links:
    #Universities.append(Link.get('title'))
    
#print(Links)
Un = []
for nam in TD:
    li = nam.find('a')
    if li == None:
        continue
    #print(li)
    if li.get('title') == "STEM fields":
        continue
    Un.append(li.get('title'))
print(Un)
