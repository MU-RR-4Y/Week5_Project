from db.run_sql import run_sql
from models.user import User
import repositories.destination_respository as destination_repo


def save(user):
    sql = '''INSERT INTO users (name, wish_list, visited_list)
          VALUES (%s, ARRAY[%s], ARRAY[%s])
          RETURNING id'''
    
    values = [user.name, user.wishlist, user.visited_list]
    result = run_sql(sql, values)
    user.id = result[0]['id']
    # for id in user.wishlist:
    #     sql = '''INSERT INTO users (wish_list)
    #             VALUES (%s)'''
    #     values = [id]
    #     run_sql(sql,values)

    return user



def select_all():
    users = []
    sql = '''SELECT * FROM users'''
    results = run_sql(sql)
    for result in results:
        wishlist =result['wish_list']
        visited_list = result['visited_list']
        user = User(result['name'],wishlist,visited_list, result['id'])
        users.append(user)
    return users


def delete_all():
    sql ='DELETE FROM users'
    run_sql(sql)