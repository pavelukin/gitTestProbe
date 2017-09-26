from flask import Flask
from names_info import get_info
import requests


app = Flask(__name__)

@app.route("/")
def index():
	adress = 'https://apidata.mos.ru/v1/datasets/2009/rows?api_key=d18da84ae7eaa38445ccba9730ac0055'
	some_info = get_info(adress)
	
	test = "<table>" +"\
	<tr>"+"\
	<th>Имя</th><th>Год</th><th>Месяц</th><th>Количество</th>"
	"</tr>"
	"</table>"
	
	for count in some_info:
		Year = count["Cells"]["Year"]
		Month = count["Cells"]["Month"]
		Number_Of_Persons = count["Cells"]["NumberOfPersons"]
		Name = count["Cells"]["Name"]
		test += "<tr><td>%s</td><td>%s</td><td>"  "%s</td><td>%s</td></tr>"%(Name,Year,Month,Number_Of_Persons)
	return test
if __name__ == "__main__":
	app.run()

 