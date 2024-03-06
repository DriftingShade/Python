from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = 'WhO cAn *It Be NoW dOo DoO dOo395*'

@app.route('/')
def index():
    if 'rand_num' not in session:
        session['rand_num'] = 0
    session['rand_num'] = random.randint(1,100)
    print(session['rand_num'])
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    print("Random Number: ", session['rand_num'])
    return render_template('results.html', guess = int(request.form['guess']), number = int(session['rand_num']))

@app.route('/newgame', methods=['GET'])
def newgame():
	session.clear()

	return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)