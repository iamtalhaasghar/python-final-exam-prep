from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/index')
def myFunc():
    return render_template('index.html')

@app.route('/save', methods={"POST"})
def saveMessage():
    yourMessage = request.form.get("message")
    print(yourMessage)
    import database
    database.insertMessage(yourMessage)
    return "<p>Your message has been saved.</p>"

@app.route('/delete', methods={"POST"})
def deleteMessage():
    s = request.form.get("serial")
    print(s)
    import database
    database.deleteMessage(s)
    return "<p>Your message has been deleted.</p>"


@app.route('/update', methods={"POST"})
def updateMessage():
    s = request.form.get("serialToUpdate")
    nMsg = request.form.get("newMessage")
    print(s, nMsg)
    import database
    database.updateMessage(s, nMsg)
    return "<p>Your message has been updated.</p>"

@app.route('/show', methods={"POST"})
def showMessage():
    s = request.form.get("serialToShow")
    import database
    theMessage = database.showMessageOf(s)
    return "<h1>Your message is:</h1><h2> <br>%s</h2>" %(theMessage)


app.run(debug=True)
