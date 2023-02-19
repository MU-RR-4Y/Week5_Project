from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.visit import Visit
import repositories.user_repository as user_repo
import repositories.destination_respository as destination_repo

visits_blueprint =Blueprint('visits', __name__)


# INDEX ('/') GET
@visits_blueprint.route('/visit/id')
def visit():
    



# NEW ('/new') GET
# CREATE ('/') POST
# SHOW ('/id') GET
# EDIT ('/id/edit') GET
# UPDATE ('/id') POST
# DELETE ('/id/delete') POST
