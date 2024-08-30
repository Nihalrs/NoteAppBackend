from flask import jsonify, request, Flask
from database import *

app=Flask(__name__)

@app.route('/')
def start():
    return 'Welcome to NoteApp!!'

@app.route('/addNote',methods=['POST'])
def newnote():
    data=request.get_json()
    email=data['email']
    title=data['title']
    content=data['content']
    category=data['category']
    date=data['date']
    
    result=addnote(email,title,category,content,date)
    return jsonify({"result":result})

@app.route('/deleteNote',methods=['POST'])
def removenote():
    data=request.get_json()
    noteid=data['noteid']
    
    result=delnote(noteid)
    return jsonify({"result":result})

@app.route('/recoverNote',methods=['POST'])
def recoverNote():
    data=request.get_json()
    noteid=data['noteid']
    
    result=recovernote(noteid)
    return jsonify({"result":result})

@app.route('/permenantdeleteNote',methods=['POST'])
def permadelnote():
    data=request.get_json()
    noteid=data['noteid']
    
    result=permenantdelnote(noteid)
    return jsonify({"result":result})

@app.route('/displayNote')
def dispNote():
    data=request.get_json()
    email=data['email']
    
    result=displayNote(email)
    return jsonify(result)

@app.route('/displayDelNote')
def dispDelNote():
    data=request.get_json()
    email=data['email']
    
    result=displayDelNote(email)
    return jsonify(result)

if __name__=='__main__':
    app.run()