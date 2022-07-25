from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key="i dont understand what this does"

@app.route('/')
def dojo():
    return render_template("index.html")

@app.route('/process',methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')

# Method Not Allowed
# The method is not allowed for the requested URL.

@app.route('/result')
def success():
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True)