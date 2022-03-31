from flask import Flask,jsonify,request

app = Flask(__name__)

studentDB=[
    {
        'rollno':'11',
        'name':'johan',
        'section':'A'
    },
{
        'rollno':'12',
        'name':'phil',
        'section':'B'
    }
]

@app.route("/",methods=['GET'])
def welcome():
    return 'welcome'

@app.route("/student/getstudents",methods=['GET'])
def getstudent():
    return jsonify({"stud":studentDB})

@app.route("/student/getstudent/<rollno>",methods=['GET'])
def getstudentdetails(rollno):
    student = [stud for stud in studentDB if(stud['rollno']==rollno)]
    print(student)
    return jsonify({"stud":student})

@app.route("/student/updatestudent/<rollno>", methods=['PUT'])
def updatestudentdetail(rollno):
    student = [stud for stud in studentDB if (stud['rollno'] == rollno)]

    if('rollno' in request.json) :
        print("Student available")
    if ('name' in request.json):
        student[0]['name'] = request.json['name']
    return jsonify({'stud':student[0]})

@app.route("/student/addstudent", methods=['POST'])
def addstudent():
    student = {
        'rollno':request.json['rollno'],
        'name': request.json['name'],
        'section': request.json['section']
    }
    studentDB.append(student)
    return jsonify({'stud':studentDB})

@app.route("/student/removestudent/<rollno>", methods=['DELETE'])
def removestudent(rollno):
    student = [stud for stud in studentDB if (stud['rollno'] == rollno)]

    if(len(student)>0):
        studentDB.remove(student[0])

    return jsonify({'stud':student})

app.run()