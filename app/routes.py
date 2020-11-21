from app import app, db
from app.forms import PersonForm
from app.database_models import Person
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = PersonForm()
    if form.validate_on_submit():
        person = Person(last_name = form.last_name.data, first_name = form.first_name.data,
                        country = form.country.data, city = form.city.data, street = form.street.data,
                        number = form.number.data)
        db.session.add(person)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html', form = form)

@app.route('/peopledatabase')
def peopledatabase():
    people = Person.query.all()
    return render_template('peopledatabase.html', people = people)

@app.route('/map')
def map():
    return render_template('map.html')
