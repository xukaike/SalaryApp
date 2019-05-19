#coding:utf-8
from _pydecimal import Decimal

from bson import ObjectId
from flask import Flask, jsonify, request, make_response,json
from flask_pymongo import PyMongo
from flask_cors import *
import numpy as np
import logging
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'webpro'
app.config["MONGO_URI"] = "mongodb://120.79.177.232:27017/webpro"
mongo = PyMongo(app)
CORS(app, supports_credentials=True)

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,ObjectId):
            return str(o)
        if isinstance(o,Decimal):
            return str(o)
        return json.JSONEncoder.default(self,o)
app.json_encoder = JSONEncoder

def addtoresult(result,u):
    for i in range(0,u.count()):
        result.append(u[i])
    return result

@app.route('/',methods=['GET'])
def index():
    u = mongo.db.recruit.find()
    r = np.random.randint(0, u.count(), size=10)
    result = []
    for i in r:
        result.append(u[int(i)])
    return jsonify(result)

@app.route('/query',methods=['POST'])
def query():
    if request.method=='POST':
        u = mongo.db.recruit.find(request.form)
        result = []
        for i in u:
            result.append(i)
        return jsonify(result)

@app.route('/queryuser',methods=['POST'])
def queryuser():
    if request.method=='POST':
        u  = mongo.db.user.find(request.form)
        if u.count()==0:
            return 'error'
        else:
            return jsonify(u[0])

@app.route('/search',methods=['POST'])
def search():
    if request.method=='POST':
        count = int(request.form['count'])
        turn = int(request.form['turn'])
        app.logger.error('requestkeyword:'+request.form['jobkeyword'])
        u = mongo.db.recruit.find({'jobkeyword':str.lower(request.form['jobkeyword'])})
        if u.count()==0:
            return 'error'
        else:
            result = []
            for i in range(0,count):
                result.append(u[int(turn*count)+i])
            return jsonify(result)

@app.route('/findbyword',methods=['POST'])
def findbyword():
    if request.method=='POST':
        count = int(request.form['count'])
        turn = int(request.form['turn'])
        keyword = request.form['keyword']
        result  = []
        sequence = ['job','education','companyfield','companyloc','workplace','welfare','jobdescription']
        u = mongo.db.recruit.find({'$or': [{sequence[0]:{'$regex':keyword,'$options':'i'}},{sequence[1]: {'$regex':keyword,'$options':'i'}},{sequence[2]: {'$regex':keyword,'$options':'i'}},{sequence[3]: {'$regex':keyword,'$options':'i'}},{sequence[4]: {'$regex':keyword,'$options':'i'}},{sequence[5]: {'$regex':keyword,'$options':'i'}},{sequence[6]: {'$regex':keyword,'$options':'i'}}]})
        if u.count()==0:
            return 'error'
        for i in range(0,count):
            result.append(u[count*turn+i])
        return jsonify(result)

@app.route('/detail',methods=['POST'])
def detail():
    if request.method=='POST':
        id = request.form['id']
        u = mongo.db.recruit.find_one({'_id':ObjectId(str(id))})
        return jsonify(u)

@app.route('/editpsw',methods=['POST'])
def editpsw():
    if request.method=='POST':
        id = request.form['id']
        newpasswd = request.form['passwd']
        oripasswd = request.form['original']
        confirm = request.form['confirm']
        users = mongo.db.user
        user = users.find_one({'_id':ObjectId(str(id))})
        if user['passwd']==oripasswd:
            if confirm==newpasswd:
                user['passwd'] = newpasswd
                users.save(user)
                return 'ok'
            else:
                return 'new password error'
        return 'original password error'