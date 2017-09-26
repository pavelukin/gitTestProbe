from flask import Flask

api_key = 'd18da84ae7eaa38445ccba9730ac0055'

app = Flask(__name__)

@app.route("/")
def index():
	return "проверка работоспособности"
if __name__ == "__main__":
	app.run()
