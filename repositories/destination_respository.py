from db.run_sql import run_sql
from models.destination import Destination
import repositories.country_repository as country_repo

def save(destination):
    sql = '''INSERT INTO destinations (name, country_id, information)
          VALUES (%s, %s, %s)
          RETURNING id'''
    values = [destination.name, destination.country.id,destination.information]
    result = run_sql(sql, values)
    destination.id = result[0]['id']
    return destination


def delete_all():
    sql = 'DELETE FROM destinations'
    run_sql(sql)

def select_all():
    destinations = []
    sql = '''SELECT * FROM destinations'''
    results = run_sql(sql)
    for result in results:
        country = country_repo.select(result['country_id'])
        destination = Destination(result['name'], country, result['information'], result['id'])
        destinations.append(destination)
    return destinations
    

def select(id):
    destination = None
    sql ='''SELECT * FROM destinations WHERE id = %s'''
    values = [id]
    results = run_sql(sql, values)
    if results is not None:
        result = results[0]
        country = country_repo.select(result['country_id'])
        destination = Destination(result['name'], country, result['information'],id)
    return destination

def delete(id):
    sql ='''DELETE FROM destinations WHERE id = %s'''
    values = [id]
    run_sql(sql, values)



