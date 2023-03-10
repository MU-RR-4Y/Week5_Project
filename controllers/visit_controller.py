from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.visit import Visit
import repositories.user_repository as user_repo
import repositories.destination_respository as destination_repo
import repositories.visit_repository as visit_repo

visits_blueprint =Blueprint('visits', __name__)


#INDEX ('/') GET
@visits_blueprint.route('/visits')
def visit():
    visits = visit_repo.select_all()
    users = user_repo.select_all()
    destinations =destination_repo.select_all()
    return render_template('visits/index.html', visits = visits, destinations = destinations, users = users)





