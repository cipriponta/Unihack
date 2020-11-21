from app.database_models import Person
import requests
import pprint

# Example Query
# 'https://router.hereapi.com/v8/routes?transportMode=bicycle&origin=52.5308,13.3847&destination=52.5323,13.3789&return=summary'

API_KEY = 'c3z4mt2KrKtmEXWcCjNnnYlJ0vwVwLZFNPpaa1l9T3I'
API_PATH = '&apikey=' + API_KEY
BASE_URL = 'https://router.hereapi.com/v8/routes?transportMode'
TRANSPORT_MODE = '=car'

def bubblesort(sorting_list):
    for i in range(0, len(sorting_list) - 1):
        for j in range(i, len(sorting_list)):
            if sorting_list[i]['route_length'] > sorting_list[j]['route_length']:
                sorting_list[i],sorting_list[j] = sorting_list[j],sorting_list[i]

def calculate_route_bewtween_two_points(pointa, pointb):
    ROUTE_URL = "&origin={latpointa},{lngpointa}&destination={latpointb},{lngpointb}&return=summary".format(
        latpointa = pointa.latitude,
        lngpointa = pointa.longitude,
        latpointb = pointb.latitude,
        lngpointb = pointb.longitude
    )

    URL = BASE_URL + TRANSPORT_MODE + ROUTE_URL + API_PATH

    response = requests.get(URL)
    data = response.json()
    return data['routes'][0]['sections'][0]['summary']['length']


def calculate_route():
    people_list = Person.query.all()

    starting_point = Person(last_name = "Starting", first_name = "Point", country = "Romania",
                            city = "Arad", street = "Bulevardul Revolutiei", number = "75")

    starting_point.calculate_coords()

    final_list = []
    sorting_list = []
    final_list.append(starting_point)

    while people_list:
        sorting_list = []

        for person in people_list:
            sorting_list.append({'element':person, 'route_length': calculate_route_bewtween_two_points(starting_point, person)})

        bubblesort(sorting_list)


        starting_point = sorting_list[0]['element']
        people_list.remove(starting_point)
        final_list.append(starting_point)

    return final_list
