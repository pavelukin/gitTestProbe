from flask import Flask
from names_info import get_info
import requests


app = Flask(__name__)

@app.route("/")
def index():
	adress = 'https://apidata.mos.ru/v1/datasets/2009/rows?api_key=d18da84ae7eaa38445ccba9730ac0055'
	some_info = get_info(adress)
	name = "name"
	teso = ["Борис","gwergw"]
	i = 0
	while i <10 :
			buff += "<table><tr><th>%s</th></tr><tr>%s</tr></table>" %(teso,name)
			i +=1
	return buff
if __name__ == "__main__":
	app.run()

 