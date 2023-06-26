from flask import render_template, request, redirect
from flask import Blueprint

from repositories import city_repository
from repositories import country_repository

cities_blueprint = Blueprint('cities', __name__)

@cities_blueprint.route('/cities')
def cities():
    cities = city_repository.select_all()
    return render_template('cities/index.html', cities = cities)
