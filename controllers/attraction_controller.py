from flask import render_template, request, redirect
from flask import Blueprint
from models.city import City
from models.attraction import Attraction
from repositories import city_repository
from repositories import country_repository
from repositories import attraction_repository

attractions_blueprint = Blueprint('attractions', __name__)

@attractions_blueprint.route('/attractions')
def attractions():
    attractions = attraction_repository.select_all()
    return render_template('attractions/index.html', attractions = attractions)


@attractions_blueprint.route('/attractions/<id>')
def show(id):
    attraction = attraction_repository.select(id)
    return render_template("/attractions/show.html", attraction = attraction)

@attractions_blueprint.route('/attractions/new')
def new():
    cities = city_repository.select_all()
    return render_template('/attractions/new.html', cities = cities)

@attractions_blueprint.route('/attractions/<id>/delete', methods=['POST'])
def delete(id):
    attraction = attraction_repository.select(id)
    attraction_repository.delete(id)
    return redirect(f"/cities/{attraction.city.id}")


@attractions_blueprint.route('/attractions', methods=['POST'])
def create():
    name = request.form['name']
    city = city_repository.select(request.form['city_id'])
    attraction = Attraction(name, city)
    attraction_repository.save(attraction)
    return redirect(f"/cities/{city.id}")

