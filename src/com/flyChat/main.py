'''
Created on Jun 19, 2017

@author: wangke
'''
import json
from flask import Flask, request, Response, jsonify
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route("/login", methods=['GET'])
def login():
    print request.args.get('abc')
    return jsonify({'tasks': tasks})

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5003)
