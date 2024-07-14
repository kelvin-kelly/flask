from flask import Flask,render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/home/')
def index():
    return render_template('index.html')

@app.route('/')
@app.route('/signup/')
def signup():
    return render_template('signup.html')


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    password = request.form['password']

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=8080)