from db.run_sql import run_sql

import repositories.inventory_repository as inventory_repository
import repositories.manufacturer_repository as manufacturer_repository

from models.inventory import Inventory
from models.manufacturer import Manufacturer

def save(inventory_item):
    sql = "INSERT INTO inventory_items (name, manufacturer_id, description, stock_quantity, buying_cost, selling_price) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [inventory_item.name, inventory_item.manufacturer.id, inventory_item.description, inventory_item.stock_quantity, inventory_item.buying_cost, inventory_item.selling_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    inventory_item.id = id
    return inventory_item

def select_all():
    inventory_items = []

    sql = "SELECT * FROM inventory_items"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        margin = inventory_repository.calculate_margin(row['buying_cost'], row['selling_price'])
        inventory_item = Inventory(row['name'], manufacturer, row['description'], int(row['stock_quantity']), int(row['buying_cost']), int(row['selling_price']), margin, row['id'])
        inventory_items.append(inventory_item)
    return inventory_items

def select(id):
    item = None
    sql = "SELECT * FROM inventory_items WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        item = Inventory(result['name'], manufacturer, result['description'], int(result['stock_quantity']), int(result['buying_cost']), int(result['selling_price']), result['id'] )
    return item

def update(inventory_item):
    sql = "UPDATE inventory_items SET (name, manufacturer_id, description, stock_quantity, buying_cost, selling_price) = (%s,%s,%s,%s,%s,%s) WHERE id = %s"
    values = [inventory_item.name, inventory_item.manufacturer.id, inventory_item.description, inventory_item.stock_quantity, inventory_item.buying_cost, inventory_item.selling_price, inventory_item.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM inventory_items WHERE id = %s"
    values = id
    run_sql(sql, values)

def calculate_margin(buying_cost, selling_price):
    margin = ("{0:.0%}".format(1-(buying_cost/selling_price)))
    return(margin)

    # tasks = []

    # sql = "SELECT * FROM tasks"
    # results = run_sql(sql)

    # for row in results:
    #     user = user_repository.select(row['user_id'])
    #     task = Task(row['description'], user, row['duration'], row['completed'], row['id'] )
    #     tasks.append(task)
    # return tasks

