import requests
def get_info(url):
	result = requests.get(url)
	return result.json()
adress = "https://apidata.mos.ru/v1/datasets/2009/rows?api_key=d18da84ae7eaa38445ccba9730ac0055"
if __name__ == "__main__":
	data = get_info(adress)
	print (data)