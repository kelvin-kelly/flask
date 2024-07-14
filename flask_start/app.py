

from flask import render_template, request, redirect, url_for  

from models import User  

from config import app, db  

  
  


@app.route('/home/')
def index():
    return render_template('index.html')

@app.route('/')
@app.route('/signup/', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        password = request.form.get('password')

        # Validate form data
        if not fname or not lname or not email or not password:
            return render_template('signup.html', error='Please fill in all fields')

        # Create a new User instance
        user = User(fname=fname, lname=lname, email=email, password=password)

        # Add the user to the database
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('signup.html')

  

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/logout/')
def logout():
    return render_template('logout.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    password = request.form['password']

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=8080)