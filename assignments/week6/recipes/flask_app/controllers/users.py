from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'user_id' not in session:
        return render_template('index.html')
    else:
        return redirect('/dashboard')

@app.route('/register/', methods=['post'])
def register():
    isValid = User.validate(request.form)
    if not isValid: # if isValid is False the redirect back to '/' with flash message
        return redirect('/')
    else:
        newUser = {
            'firstName': request.form['firstName'],
            'lastName': request.form['lastName'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
        id = User.save(newUser)
        if not id:
            flash("Something got messed up someplace")
            return redirect('/')
        else:
            session['user_id'] = id
            flash("You logged in")
            return redirect('/recipes/')

@app.route('/login/', methods=['post'])
def login():
    data = {
        'email': request.form['email']
    }
    user = User.getEmail(data)
    if not user:
        flash("That email is not in the database")
        redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Wrong password")
        return redirect('/')
    else:
        session['user_id'] = user.id
        flash("Welcome back!")
        return redirect('/recipes/')

# @app.route('/createUser/', methods=['post'])
# def createUser():
#     data = {
#         'firstName': request.form['firstName'],
#         'lastName': request.form['lastName'],
#         'email': request.form['email']
#     }
#     User.save(data)
#     return redirect('/recipes/')

@app.route('/logout/')
def logout():
    session.clear()
    flash("Later Skater")
    return redirect('/')