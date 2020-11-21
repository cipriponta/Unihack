from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    last_name = db.Column(db.String(32), index = True)
    first_name = db.Column(db.String(32), index = True)
    country = db.Column(db.String(32), index = True)
    city = db.Column(db.String(32), index = True)
    street = db.Column(db.String(32), index = True)
    number = db.Column(db.String(32), index = True)

    def __repr__(self):
        return '<User {} {}>'.format(self.last_name, self.first_name)