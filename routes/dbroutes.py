from config import app,db
from flask import jsonify,request,abort
from models import people,DbPerson

@app.route("/dbpeople")
def getDbPeople():
    listp=DbPerson.query.all()
    result = [x.serialize() for x in listp]
    return jsonify(result)


@app.route("/dbpeople",methods=['POST'])
def processDepartments():
    try:
        input=request.get_json()
        sno=input['sno']
        name=input['name']
        city=input['city']
        db.session.add(DbPerson(sno,name,city))
        db.session.commit()
        return {"status": "success"}, 201
    except:
        abort({'status':"Internal server error"},500)

