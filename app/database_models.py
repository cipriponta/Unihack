from app import db
import requests
import json
import pprint

# Example

# https://geocoder.ls.hereapi.com/search/6.2/geocode.json
# ?languages=en-US
# &maxresults=4
# &searchtext=Sunnyvale
# &apiKey={YOUR_API_KEY}

API_KEY = 'c3z4mt2KrKtmEXWcCjNnnYlJ0vwVwLZFNPpaa1l9T3I'
API_PATH = '&apikey='+API_KEY
BASE_URL = 'https://geocode.search.hereapi.com/v1/geocode'


class Person(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    last_name = db.Column(db.String(32), index = True)
    first_name = db.Column(db.String(32), index = True)
    country = db.Column(db.String(32), index = True)
    city = db.Column(db.String(32), index = True)
    street = db.Column(db.String(32), index = True)
    number = db.Column(db.String(32), index = True)
    products = db.Column(db.String(32), index = True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __repr__(self):
        return '<User {} {}>'.format(self.last_name, self.first_name)

    def calculate_coords(self):
        ADDRESS_URL = '?q={number}+{street}%2C+{city}%2C+{country}'.format(
            number = self.number,
            street = self.street,
            city = self.city,
            country = self.country
        )
        URL = BASE_URL + ADDRESS_URL + API_PATH

        response = requests.get(URL)
        try:
            if response.status_code in range(200, 299):
                data = response.json()
                coords = data['items'][0]['access']
                if coords:
                    self.latitude = coords[0]['lat']
                    self.longitude = coords[0]['lng']
        except:
            self.latitude = None
            self.longitude = None

