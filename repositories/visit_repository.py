from db.run_sql import run_sql
from models.visit import Visit
import repositories.destination_respository as destination_repo
import repositories.user_repository as user_repo

def save(visit):
    sql = '''INSERT INTO visits (user_id, destination_id, date, rating, comment) VALUES (%s, %s,%s,%s, %s) RETURNING id'''
    values = [visit.user.id, visit.destination.id, visit.date, visit.rating, visit.comment]
    result = run_sql(sql, values)
    visit.id = result[0]['id']
    return visit

def select_all():
    visits =[]
    sql = '''SELECT * FROM visits'''
    results = run_sql(sql)
    for result in results:
        user = user_repo.select(int(result['user_id']))
        destination =destination_repo.select(int(result['destination_id']))
        visit = Visit(user, destination , result['date'], result['rating'], result['comment'], result['id'])
        visits.append(visit)
    return visits 

