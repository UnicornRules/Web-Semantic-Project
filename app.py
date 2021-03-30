from flask import Flask, jsonify
from flask_cors import CORS
import json
import rdf

#start app
print("starting app")
app = Flask(__name__)
CORS(app)
print("app started")

#load database
print("loading RDF database")
g=rdf.start()
print("database loaded")



@app.route('/fontaines', methods=['GET'])
def fontaines():
    return rdf.returnJson("fontaines",g)

@app.route('/piste', methods=['GET'])
def piste():
    return rdf.returnJson("piste",g)

@app.route('/activite', methods=['GET'])
def activite():
    return rdf.returnJson("activite",g)

@app.route('/parc1', methods=['GET'])
def parc1():
    return rdf.returnJson("parc1",g)

@app.route('/parc2', methods=['GET'])
def parc2():
    return rdf.returnJson("parc2",g)

@app.route('/parc3', methods=['GET'])
def parc3():
    return rdf.returnJson("parc3",g)

if __name__ == '__main__':
    app.run()
    