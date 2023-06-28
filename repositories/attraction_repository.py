from db.run_sql import run_sql
from models.country import Country
from models.city import City
from models.attraction import Attraction

import repositories.city_repository as city_repository


def save(attraction):
    sql = "INSERT INTO attractions (name, city_id, review) VALUES (%s, %s, %s) RETURNING id"
    values = [attraction.name, attraction.city.id, attraction.review]
    results = run_sql(sql, values)
    attraction.id = results[0]['id']
    return attraction

def select_all():
    attractions = []

    sql = "SELECT * FROM attractions"
    results = run_sql(sql)
    for result in results:
        city = city_repository.select(result['city_id'])
        attraction = Attraction(result['name'], city, result['review'], result['id'])
        attractions.append(attraction)
    return attractions


def select(id):
    attraction = None
    sql = "SELECT * FROM attractions WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)


    if results: 
        result = results[0]
        city = city_repository.select(result['city_id'])
        attraction = Attraction(result['name'], city, result['review'], result['id'])
    return attraction


def update(attraction):
    sql = """UPDATE attractions SET (name, city, review, id) = (%s, %s, %s) WHERE id = %s"""
    values = [attraction.name, attraction.city.id, attraction.review, attraction.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM attractions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM attractions WHERE id = %s"
    values= [id]
    run_sql(sql,values)


def attractions_for_city(city):
    attractions = []
    sql = "SELECT * FROM attractions WHERE city_id = %s"
    values = [city.id]
    results = run_sql(sql,values)
    for row in results:
        city = city_repository.select(row['city_id'])
        attraction = Attraction(row['name'], city, row['review'], row['id'])
        attractions.append(attraction)
    return attractions
    



