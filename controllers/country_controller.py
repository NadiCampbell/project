from flask import Flask, request, render_template, redirect
from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

from flask import Blueprint 

countries_blueprint = Blueprint('countries', __name__)

@countries_blueprint.route('/countries')
def countries():
    countries = country_repository.select_all()
    return render_template('/countries/index.html', countries = countries)


@countries_blueprint.route('/countries/<id>/edit')
def edit(id):
    country = country_repository.select(id)
    return render_template('/countries/edit.html', country = country)


@countries_blueprint.route('/countries/<id>')
def show(id):
    country = country_repository.select(id)
    return render_template("/countries/show.html", country = country)


@countries_blueprint.route('/countries/new')
def new():
    country = country_repository.select_all()
    return render_template('/countries/new.html', country = country)


# @countries_blueprint.route('/countries', methods=['POST'])
# def create():