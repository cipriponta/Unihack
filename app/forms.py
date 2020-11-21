from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from app.database_models import Person

class PersonForm(FlaskForm):
    last_name = StringField('Last Name:', validators=[DataRequired()])
    first_name = StringField('First Name:', validators=[DataRequired()])
    country = StringField('Country:', validators=[DataRequired()])
    city = StringField('City:', validators=[DataRequired()])
    street = StringField('Street:', validators=[DataRequired()])
    number = StringField('Number:', validators=[DataRequired()])
    submit = SubmitField('Submit')