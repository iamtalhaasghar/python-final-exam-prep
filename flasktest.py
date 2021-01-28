from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/index')
def showHome():
    return render_template('index.html')

@app.route('/save', methods=['Post'])
def saveData():
    r = request.form.get('roll')
    n = request.form.get('name')
    import database
    database.insertData(r, n)
    return '<p>ok</p>'

@app.route('/show', methods=['Post'])
def showData():
    r = request.form.get('showRoll')
    import database
    name = database.searchStudent(r)
    return '<p>Your name is: %s</p>' % name

app.run(debug=True)
