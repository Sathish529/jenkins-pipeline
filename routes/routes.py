from config import app
from flask import jsonify,request
from models import people,Person

@app.route("/people")
def getPeople():
    listp=people.getPeople()
    result = [x.serialize() for x in listp]
    return jsonify(result)

@app.route("/people",methods=['POST'])
def addPeople():
    input=request.get_json()
    sno=input['sno']
    name=input['name']
    city=input['city']
    newitem=Person(sno,name,city)    
    people.add(newitem)
    return "Item added successfully"    
