from db.run_sql import run_sql

from models.manufacturer import Manufacturer

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, established) VALUES (%s, %s) RETURNING *"
    values = [manufacturer.name, manufacturer.established]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer