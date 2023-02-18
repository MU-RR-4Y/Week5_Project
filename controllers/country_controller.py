from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repo
import repositories.destination_respository as destination_repo

countries_blueprrnt = Blueprint('countries', __name__)

# INDEX ('/') GET
@countries_blueprrnt.route('/countries')
def countries():
    destination_list = []
    destinations = destination_repo.select_all()
    countries = country_repo.select_all()
    for destination in destinations:
        for country in countries:
            if destination.country.id == country.id:
                destination_list.append(destination)
    return render_template('countries/index.html', countries = countries, destinations = destination_list )


# NEW ('/new') GET
# CREATE ('/') POST
# SHOW ('/id') GET
# EDIT ('/id/edit') GET
# UPDATE ('/id') POST
# DELETE ('/id/delete') POST
