from flask import Flask, render_template, jsonify, url_for
import requests, json

app = Flask(__name__)

@app.route('/')
def sample_page():
  return render_template('index.html')

@app.route('/trivia', methods=['GET'])
def trivia():
  req = requests.get('http://localhost:5000/date').content
  return render_template('trivia.html', req=req)

if __name__ == '__main__':
  app.run(debug=True,host="0.0.0.0",port=80)