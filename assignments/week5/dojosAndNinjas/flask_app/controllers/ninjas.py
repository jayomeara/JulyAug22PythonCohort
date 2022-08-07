from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import dojo, ninja
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html',dojos= dojo.Dojo.get_all())

@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')

# @app.route('/edit/ninja',methods=['POST'])
# def edit_ninja():
#     ninja.Ninja.save(request.form)
#     return redirect('/')

@app.route('/ninja/<int:id>/edit/')
def editNinja():
    pass

@app.route('/dojo/ninja/<int:ninja_id>/delete/')
def deleteNinja(ninja_id):
    data = {
        'id' : ninja_id
    }
    Ninja.delete(data)
    return redirect('/')