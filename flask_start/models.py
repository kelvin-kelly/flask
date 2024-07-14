from config import db


class User(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, unique=False, primary_key=True)
    fname = db.Column(db.String(80), unique=False, nullable=False)
    lname = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    
    def __init__(self, fname, lname, email, password):
        self.fname = fname,
        self.lname = lname,
        self.email = email,
        self.password = password 
        
        
        


 
