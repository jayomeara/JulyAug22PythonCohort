from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key="i dont understand what this does"

@app.route('/')
def counter():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/delete')
def reset():
    session.clear()
    return redirect('/')

@app.route('/add')
def add():
    session['count'] += 2
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)