from project.api.nfe import nfe_sql
from typing import List, Dict
import json

import mysql.connector

def connect_and_use_query(sql_query, insert=False) -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'nfes'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute(sql_query)
    if not insert:
        results = [{'access_key': access_key, 'total_value': total_value} for (access_key, total_value) in cursor]
    else:
        connection.commit()
        results = True
    cursor.close()
    connection.close()

    return results

def create_many(nfe_list):
    sql_query = nfe_sql.create(nfe_list), True
    return connect_and_use_query(sql_query)


def read_all():
    sql_query = nfe_sql.read_all
    return connect_and_use_query(sql_query)

def read_one(access_key):
    sql_query = nfe_sql.read_one(access_key)
    return connect_and_use_query(sql_query)[0]
