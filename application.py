from flask import Flask
from flask import render_template, request
import json
import requests
from datetime import date
app = Flask(__name__)

@app.route('/')
def choose_date():
	return render_template('choose_date.html')

api_key = "DEMO_KEY"

@app.route('/get_image')
def get_image():
	query_date = request.args.get("query_date")
	hi_res = request.args.get("hi_res")
	today_date = date.today().strftime("%Y-%m-%d")
	if query_date>today_date:
		return "404, date is in the future", 404
	else:
		reply = requests.get("https://api.nasa.gov/planetary/apod", {"date": query_date, "api_key":api_key})
		reply = json.loads(reply.content)
		url = ""
		if hi_res:
			url = reply['hdurl']
		else:
			url = reply['url']
		return render_template('view_image.html',image_link=url, caption = reply['title'], date=query_date)

if __name__ == '__main__':
    app.run(debug=True)
