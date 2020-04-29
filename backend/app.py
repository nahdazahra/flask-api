from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import requests
import simplejson
from datetime import date

today = date.today()
day = today.strftime("%d")
mon = today.strftime("%m")

app = Flask(__name__)
CORS(app)

@app.route('/date', methods=['GET'])
def home():
  url = "http://numbersapi.com/"+ mon +"/"+ day +"/date"
  r = requests.get(url).content
  return jsonify(r)

if __name__ == '__main__':
  app.run(debug=True,port=5000)