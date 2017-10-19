from bs4 import BeautifulSoup
from req import get_html
adress = 'https://yandex.ru/search/?lr=10735&clid=2240500&msid=1506722760.34372.22890.28703&text=python'

html = get_html(adress)

test = BeautifulSoup(html, "html.parser")

#print(test.prettify())
data = []	
for item in test.find_all('li',class_='serp-item'):
	block_title = item.find('a',class_= 'organic__url')
	#print (block_title.text)
	href = item.find('a',class_="path__item")
	data.append({
		"title":block_title.text,
		'link':href.get('href')
		})
	#print(href.get('href'))
print (data)