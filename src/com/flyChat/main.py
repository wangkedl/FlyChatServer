# coding:utf-8
'''
Created on Jun 19, 2017

@author: wangke
'''
import json
from flask import Flask, request, Response, jsonify
from pymongo import MongoClient

app = Flask(__name__)
db = None

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


def getDbConn():
    client = MongoClient('123.57.164.21', 27017)
    db_auth = client.admin
    db_auth.authenticate("xxxx", "xxxx")
    global db 
    db = client.mongodb
    print '数据库连接正常！'


@app.route("/login/<name>/<password>", methods=['GET'])
def login(name, password):
    global db
    collection = db.user
    u2 = collection.find_one({'name':'wangke', 'password':'123'})
    print name
    print password
    # print request.args.get('abc')
    return jsonify({'tasks': tasks})

@app.route("/registerUser/<name>/<password>", methods=['GET'])
def registerUser(name, password):
    global db
    collection = db.user
    u2 = collection.find_one({'name':'wangke', 'password':'123'})
    print name
    print password
    print(u2)
    # print request.args.get('abc')
    return jsonify({'tasks': tasks})

if __name__ == "__main__":
    getDbConn()
    app.run(host='127.0.0.1', port=5003)
