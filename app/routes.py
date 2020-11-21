from app import app, db
from app.forms import PersonForm
from app.database_models import Person
from flask import render_template, redirect, url_for
import json
from app.route_algorithm import calculate_route

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
                        number = form.number.data, products = form.products.data)
        person.calculate_coords()
        if person.longitude and person.latitude:
            db.session.add(person)
            db.session.commit()
        else:
            print("Person " + person.last_name + " " + person.first_name + " does not have a valid address!")
        return redirect(url_for('index'))
    return render_template('register.html', form = form)

@app.route('/peopledatabase')
def peopledatabase():
    people = Person.query.all()
    return render_template('peopledatabase.html', people = people)

@app.route('/map')
def map():
    people_list = calculate_route()

    coords = []
    for person in people_list:
        coords.append({'lat':person.latitude, 'lng':person.longitude})

    return render_template('map.html', coords = json.dumps(coords))
