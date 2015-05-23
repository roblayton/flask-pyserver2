from flask import Flask
from flask import Response, request
from flask.ext.cors import CORS
from flask.ext.pymongo import PyMongo
from bson.json_util import dumps
from bson.json_util import loads

app = Flask(__name__)
cors = CORS(app)
app.config['MONGO_HOST'] = 'mongodb://192.168.33.10'
app.config['MONGO_DBNAME'] = 'mydb'

# connect to the mongo db
mongo = PyMongo(app)

@app.route('/prototypes', methods=['GET', 'POST'])
def prototypes():
  if request.method == 'POST':
    mongo.db.mycollection.insert({'title': request.form['title'], 'content': request.form['content']})
    return Response('{}', status=200, mimetype='application/json')
  else:
    result = mongo.db.mycollection.find()
    data = dumps(result)
    response = Response(data, status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
  app.run()
