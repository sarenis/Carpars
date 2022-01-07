import requests
from bs4 import	BeautifulSoup as BS
from fake_useragent import UserAgent
ua = UserAgent()

state = input('Город :')

URL = f"https://auto.ria.com/uk/legkovie/state/{state}/?page="
HEADERS = {'user-agent':f'{ua.random}','accept':'*/*'}


def get_html(url, params=None):
	r = requests.get(url, headers=HEADERS,params=params)
	return r


def get_content(html):
	soup = BS(html, 'html.parser')
	items = soup.find_all('div', class_='item ticket-title')
	sss = []
	for item in items:
		sss.append({
    		"title" : item.find('span', class_='blue bold').get_text()
    		})
	for i in sss:
		print(i['title'])
	global page
	page +=1

def parse(page):
	html = get_html(URL+page)
	if html.status_code == 200:
		get_content(html.text)
	else:
		print('Error')
page = 1
while True:

	parse(f'{page}')
	page += 1






