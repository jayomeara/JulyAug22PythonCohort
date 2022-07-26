from flask import Flask, render_template, session, redirect, request
# I forgot to import request, which was tripping me up.

app = Flask(__name__)

app.secret_key="i dont understand what this does"


@app.route('/')
def dojo():
    session['gold'] = 0
    session['activity'] = []
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process():
    session['gold'] += 50
    session['activity'].append(session['building'])
    return redirect('/result')
    # if session['building'] == 'farm':
    #     session['gold'] += 50
    #     return redirect('/result')
    # elif session['building'] == 'cave':
    #     session['gold'] += 25
    #     return redirect('/result')
    # elif session['building'] == 'house':
    #     session['gold'] += 100
    #     return redirect('/result')
    # else: return redirect('/result')

@app.route('/result')
def success():
    return render_template('results.html')

if __name__=="__main__":
    app.run(debug=True)