from db.run_sql import run_sql
from models.country import Country
from models.city import City


def save(city):
    sql = "INSERT INTO cities (name, country_id) VALUES (%s, %s) RETURNING id"
    values = [city.name, city.country.id]
    results = run_sql(sql, values)
    city.id = results[0]['id']
    return city

def select_all():
    cities = []

    sql = "SELECT * FROM cities"
    results = run_sql(sql)
    for row in results:
        city = City(row['name'], row['country_id'], row['id'])
        cities.append(city)
    return cities

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results: 
        result = results[0]
        city = City(result['name'],result['country_id'], result['id'])
    return city


def update(city):
    sql = """UPDATE cities SET (name) = (%s) WHERE id = %s"""
    values = [city.name, city.country.id, city.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values= [id]
    run_sql(sql,values)


