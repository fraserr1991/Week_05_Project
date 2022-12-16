from db.run_sql import run_sql

from models.manufacturer import Manufacturer

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, established) VALUES (%s, %s) RETURNING *"
    values = [manufacturer.name, manufacturer.established]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return 
    
def select(manufacturer_id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [int(manufacturer_id)]
    full_results = run_sql(sql, values)

    result = full_results[0]

    if result is not None:
        manufacturer = Manufacturer(result['name'], result['established'], result['id'])

    return manufacturer

def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['name'], row['established'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers
    
def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = id
    run_sql(sql, values)