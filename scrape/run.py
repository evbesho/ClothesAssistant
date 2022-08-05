from crypt import methods
import json
from flask import request
from flask import Flask, render_template, redirect, url_for
import main

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('search.html')

@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/test', methods=['POST'])
def test():
    output = request.get_json()
    print(output)
    print(type(output))
    result = json.loads(output)
    print(result)
    print(type(result))
    return result

@app.route('/run', methods=['POST'])
def run():
    output = request.get_json()
    mid = json.loads(output)
    search = mid["param"]
    data = main.start(search)
    jsonReturn = json.dumps(data)
    return jsonReturn



if __name__ == "__main__":
    app.run(debug=True)

