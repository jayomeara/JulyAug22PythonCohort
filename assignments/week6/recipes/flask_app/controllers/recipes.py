from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask import flash

# @app.route('/createRecipe/', methods=['post'])
# def createRecipe():
#     data = {
#         'name': request.form['name'],
#         'description': request.form['description'],
#         'instructions': request.form['instructions']
#         'dateCooked': request.form['dateCooked']
#         'under30': request.form['under30']
#     }
#     Recipe.save(data)
#     return redirect('/recipes/')

@app.route("/create")
def recipe_create_page():
    return render_template("create_recipe.html")