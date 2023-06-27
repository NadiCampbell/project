from flask import render_template, request, redirect
from flask import Blueprint
from models.city import City
from repositories import city_repository
from repositories import country_repository

cities_blueprint = Blueprint('cities', __name__)

@cities_blueprint.route('/cities')
def cities():
    cities = city_repository.select_all()
    return render_template('cities/index.html', cities = cities)


@cities_blueprint.route('/cities/<id>')
def show(id):
    city = city_repository.select(id)
    return render_template("/cities/show.html", city = city)

@cities_blueprint.route('/cities/new')
def new():
    countries = country_repository.select_all()
    return render_template('/cities/new.html', countries = countries)

@cities_blueprint.route('/cities/<id>/delete', methods=['POST'])
def delete(id):
    city = city_repository.select(id)
    city_repository.delete(id)
    return redirect(f"/countries/{city.country.id}")


@cities_blueprint.route('/cities', methods=['POST'])
def create():
    name = request.form['name']
    country = country_repository.select(request.form['country_id'])
    city = City(name, country)
    city_repository.save(city)
    return redirect(f"/countries/{country.id}")

