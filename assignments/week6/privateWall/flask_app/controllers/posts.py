from flask import render_template, session,flash,redirect, request
import re
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Message

@app.route('/post_message',methods=['POST'])
def post_message():
    if 'user_id' not in session:
        return redirect('/')

    data = {
        "sender_id":  request.form['sender_id'],
        "receiver_id" : request.form['receiver_id'],
        "content": request.form['content']
    }
    Message.save(data)
    return redirect('/dashboard')

@app.route('/destroy/message/<int:id>')
def destroy_message(id):
    data = {
        "id": id
    }
    Message.destroy(data)
    return redirect('/dashboard')

@app.route('/post/', methods=['post'])
def createPost():
    data = {
        'id': session['user_id']
        'content' : request.form['content']
    }
    Post.save(data)
    return redirect ('/wall/')

@app.route('/wall')
def showWall():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
    thePosts = getAllPosts()
        return render_template('wall.html', posts=thePosts)
