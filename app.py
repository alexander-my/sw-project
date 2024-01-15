import requests
from flask import Flask, render_template
import clickhouse_driver
from clickhouse_driver import Client
import pandas as pd
from flask import render_template
from flask import jsonify


app = Flask(__name__)

# Функция для подключения к ClickHouse и выполнения запроса
def get_table_data(table_name):
    connection = clickhouse_driver.connect(host='clickhouse', database='starwars', user='default', password='')
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM {table_name}_table')
    data = cursor.fetchall()
    connection.close()  # Используйте close вместо disconnect
    return data

# Функция для общего шаблона страниц
def render_template_page(template_name, table_name):
    data = get_table_data(table_name)
    return render_template(template_name, data=data)

#Блок записи данных из истоника в clickhouse
def fetch_api_data():
    client = Client('clickhouse')
    ###########################################
    ###############Starships###################
    ###########################################
    url = 'https://swapi.dev/api/starships/'
    response = requests.get(url)
    if response.status_code == 200:
        starships_data = response.json().get('results', [])
        # Iterate through each starship data and insert it into the ClickHouse table
        for starship in starships_data:
            insert_query = '''
                INSERT INTO starwars.starships_table (
                    name, model, starship_class, manufacturer, cost_in_credits, length,
                    crew, passengers, max_atmosphering_speed, hyperdrive_rating, MGLT,
                    cargo_capacity, consumables, films, pilots, url, created, edited
                ) VALUES (
                    %(name)s, %(model)s, %(starship_class)s, %(manufacturer)s, %(cost_in_credits)s, %(length)s,
                    %(crew)s, %(passengers)s, %(max_atmosphering_speed)s, %(hyperdrive_rating)s, %(MGLT)s,
                    %(cargo_capacity)s, %(consumables)s, %(films)s, %(pilots)s, %(url)s, %(created)s, %(edited)s
                )
            '''
            client.execute(
                insert_query,
                {
                    'name': starship['name'],
                    'model': starship['model'],
                    'starship_class': starship['starship_class'],
                    'manufacturer': starship['manufacturer'],
                    'cost_in_credits': starship['cost_in_credits'],
                    'length': starship['length'],
                    'crew': starship['crew'],
                    'passengers': starship['passengers'],
                    'max_atmosphering_speed': starship['max_atmosphering_speed'],
                    'hyperdrive_rating': starship['hyperdrive_rating'],
                    'MGLT': starship['MGLT'],
                    'cargo_capacity': starship['cargo_capacity'],
                    'consumables': starship['consumables'],
                    'films': starship['films'],
                    'pilots': starship['pilots'],
                    'url': starship['url'],
                    'created': starship['created'],
                    'edited': starship['edited']
                }
            )
    ###########################################
    ###############People######################
    ###########################################
    url = 'https://swapi.dev/api/people/'
    response = requests.get(url)
    if response.status_code == 200:
        people_data = response.json().get('results', [])
        for person in people_data:
            insert_query = '''
                INSERT INTO starwars.people_table (
                    name, birth_year, eye_color, gender, hair_color, height, mass, skin_color, 
                    homeworld, films, species, starships, vehicles, url, created, edited
                ) VALUES (
                    %(name)s, %(birth_year)s, %(eye_color)s, %(gender)s, %(hair_color)s, %(height)s,
                    %(mass)s, %(skin_color)s, %(homeworld)s, %(films)s, %(species)s, %(starships)s,
                    %(vehicles)s, %(url)s, %(created)s, %(edited)s
                )
            '''
            client.execute(
                insert_query,
                {
                    'name': person['name'],
                    'birth_year': person['birth_year'],
                    'eye_color': person['eye_color'],
                    'gender': person['gender'],
                    'hair_color': person['hair_color'],
                    'height': person['height'],
                    'mass': person['mass'],
                    'skin_color': person['skin_color'],
                    'homeworld': person['homeworld'],
                    'films': person['films'],
                    'species': person['species'],
                    'starships': person['starships'],
                    'vehicles': person['vehicles'],
                    'url': person['url'],
                    'created': person['created'],
                    'edited': person['edited']
                }
            ) 
    ###########################################
    ###############Films#######################
    ###########################################
    url = 'https://swapi.dev/api/films/'
    response = requests.get(url)
    if response.status_code == 200:
        films_data = response.json().get('results', [])
        for film in films_data:
            insert_query = '''
                INSERT INTO starwars.films_table (
                    title, episode_id, opening_crawl, director, producer, release_date,
                    species, starships, vehicles, characters, planets, url, created, edited
                ) VALUES (
                    %(title)s, %(episode_id)s, %(opening_crawl)s, %(director)s, %(producer)s,
                    %(release_date)s, %(species)s, %(starships)s, %(vehicles)s, %(characters)s,
                    %(planets)s, %(url)s, %(created)s, %(edited)s
                )
            '''
            client.execute(
                insert_query,
                {
                    'title': film['title'],
                    'episode_id': film['episode_id'],
                    'opening_crawl': film['opening_crawl'],
                    'director': film['director'],
                    'producer': film['producer'],
                    'release_date': film['release_date'],
                    'species': film['species'],
                    'starships': film['starships'],
                    'vehicles': film['vehicles'],
                    'characters': film['characters'],
                    'planets': film['planets'],
                    'url': film['url'],
                    'created': film['created'],
                    'edited': film['edited']
                }
            )
    ###########################################
    ###############Vehicles####################
    ###########################################
    url = 'https://swapi.dev/api/vehicles/'
    response = requests.get(url)
    if response.status_code == 200:
        vehicles_data = response.json().get('results', [])
        insert_query = '''
            INSERT INTO starwars.vehicles_table (
                name, model, vehicle_class, manufacturer, length, cost_in_credits, crew,
                passengers, max_atmosphering_speed, cargo_capacity, consumables, films,
                pilots, url, created, edited
            ) VALUES (
                %(name)s, %(model)s, %(vehicle_class)s, %(manufacturer)s, %(length)s,
                %(cost_in_credits)s, %(crew)s, %(passengers)s, %(max_atmosphering_speed)s,
                %(cargo_capacity)s, %(consumables)s, %(films)s, %(pilots)s, %(url)s,
                %(created)s, %(edited)s
            )
        '''
        for vehicle in vehicles_data:
            client.execute(
                insert_query,
                {
                    'name': vehicle['name'],
                    'model': vehicle['model'],
                    'vehicle_class': vehicle['vehicle_class'],
                    'manufacturer': vehicle['manufacturer'],
                    'length': vehicle['length'],
                    'cost_in_credits': vehicle['cost_in_credits'],
                    'crew': vehicle['crew'],
                    'passengers': vehicle['passengers'],
                    'max_atmosphering_speed': vehicle['max_atmosphering_speed'],
                    'cargo_capacity': vehicle['cargo_capacity'],
                    'consumables': vehicle['consumables'],
                    'films': vehicle['films'],
                    'pilots': vehicle['pilots'],
                    'url': vehicle['url'],
                    'created': vehicle['created'],
                    'edited': vehicle['edited']
                }
            )
    ###########################################
    ###############Species####################
    ###########################################
    url = 'https://swapi.dev/api/species/'
    response = requests.get(url)
    if response.status_code == 200:
        species_data = response.json().get('results', [])
        insert_query = '''
            INSERT INTO starwars.species_table (
                name, classification, designation, average_height, average_lifespan,
                eye_colors, hair_colors, skin_colors, language, homeworld,
                people, films, url, created, edited
            ) VALUES (
                %(name)s, %(classification)s, %(designation)s, %(average_height)s,
                %(average_lifespan)s, %(eye_colors)s, %(hair_colors)s, %(skin_colors)s,
                %(language)s, %(homeworld)s, %(people)s, %(films)s, %(url)s,
                %(created)s, %(edited)s
            )
        '''

        for species in species_data:
            client.execute(
                insert_query,
                {
                    'name': species['name'],
                    'classification': species['classification'],
                    'designation': species['designation'],
                    'average_height': species['average_height'],
                    'average_lifespan': species['average_lifespan'],
                    'eye_colors': species['eye_colors'],
                    'hair_colors': species['hair_colors'],
                    'skin_colors': species['skin_colors'],
                    'language': species['language'],
                    'homeworld': species['homeworld'],
                    'people': species['people'],
                    'films': species['films'],
                    'url': species['url'],
                    'created': species['created'],
                    'edited': species['edited']
                }
            )
    ###########################################
    ###############Planets#####################
    ###########################################
    url = 'https://swapi.dev/api/planets/'
    response = requests.get(url)
    if response.status_code == 200:
        planets_data = response.json().get('results', [])
        insert_query = '''
            INSERT INTO starwars.planets_table (
                name, diameter, rotation_period, orbital_period, gravity, population,
                climate, terrain, surface_water, residents, films, url, created, edited
            ) VALUES (
                %(name)s, %(diameter)s, %(rotation_period)s, %(orbital_period)s,
                %(gravity)s, %(population)s, %(climate)s, %(terrain)s, %(surface_water)s,
                %(residents)s, %(films)s, %(url)s, %(created)s, %(edited)s
            )
        '''
        # Iterate through each planet data and insert it into the ClickHouse table
        for planet in planets_data:
            client.execute(
                insert_query,
                {
                    'name': planet['name'],
                    'diameter': planet['diameter'],
                    'rotation_period': planet['rotation_period'],
                    'orbital_period': planet['orbital_period'],
                    'gravity': planet['gravity'],
                    'population': planet['population'],
                    'climate': planet['climate'],
                    'terrain': planet['terrain'],
                    'surface_water': planet['surface_water'],
                    'residents': planet['residents'],
                    'films': planet['films'],
                    'url': planet['url'],
                    'created': planet['created'],
                    'edited': planet['edited']
                }
            )    
        return 0


#Маршруты
@app.route('/')
def index():
    return render_template('index.html')

# Добавление нового маршрута для получения данных из API и записи в ClickHouse
@app.route('/fetch_data')
def fetch_data():
    fetch_api_data()  
    return "All data fetched and saved to ClickHouse!"

# Добавление нового маршрута для получения данных из ClickHouse
@app.route('/get_data/<table_name>')
def get_data(table_name):
    data = get_table_data(table_name)
    return jsonify(data)

# Общий маршрут для отображения данных для всех страниц
@app.route('/show_data/<table_name>')
def show_data(table_name):
    return render_template('data_page.html', title=table_name.capitalize(), table=table_name)

if __name__ == '__main__':
    app.run(debug=True)
