from flask import requests, Flask

URL = "https://api.groupme.com/v3/bots/post"
accessToken = "LWjIXZM4dl5CrDK8zzhZN4w7XUDTd2fcHhqfSLA8"
bot_id = "0762588ce49d56ec028df8dafe"
test_id = "0757dcd554eef85ed5096a34a5"
text = "Hope you all have a great day today!"
payload = {"bot_id" : test_id, "text" : text}

r = requests.post(URL, data=payload)

app = Flask(_name_)
@app.route('/', methods='[POST'])
def result():
	print(request.form['name'])
	return 'Received!'