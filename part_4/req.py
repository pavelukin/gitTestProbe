import requests

def get_html(url):
	try:
		result = requests.get(url)
		result.raise_for_status()
		return result.text
	except requests.exceptions.RequestException:
		return False
#html = get_html(adress)
#print(html)