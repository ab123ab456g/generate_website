from bs4 import BeautifulSoup
import requests
html_obj = requests.get('http://127.0.0.1:5000')
soup = BeautifulSoup(html_obj.text, 'html.parser')


if soup.h1.get_text() == 'home':
	print('Home Ok')