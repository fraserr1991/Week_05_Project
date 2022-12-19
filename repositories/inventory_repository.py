from db.run_sql import run_sql

import repositories.inventory_repository as inventory_repository
import repositories.manufacturer_repository as manufacturer_repository

from models.inventory import Inventory
from models.manufacturer import Manufacturer

def save(inventory_item):
    sql = "INSERT INTO inventory_items (name, manufacturer_id, description, stock_quantity, buying_cost, selling_price, image) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [inventory_item.name, inventory_item.manufacturer.id, inventory_item.description, inventory_item.stock_quantity, inventory_item.buying_cost, inventory_item.selling_price, inventory_item.image]
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
        markup = inventory_repository.calculate_markup(row['buying_cost'], row['selling_price'])
        inventory_item = Inventory(row['name'], manufacturer, row['description'], int(row['stock_quantity']), int(row['buying_cost']), int(row['selling_price']), row['image'], markup, row['id'])
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
        markup = inventory_repository.calculate_markup(result['buying_cost'], result['selling_price'])
        item = Inventory(result['name'], manufacturer.name, result['description'], int(result['stock_quantity']), int(result['buying_cost']), int(result['selling_price']), result['image'], markup, result['id'] )
    return item

def update(inventory_item):
    sql = "UPDATE inventory_items SET (name, manufacturer_id, description, stock_quantity, buying_cost, selling_price, image) = (%s,%s,%s,%s,%s,%s, %s) WHERE id = %s"
    values = [inventory_item.name, inventory_item.manufacturer.id, inventory_item.description, inventory_item.stock_quantity, inventory_item.buying_cost, inventory_item.selling_price, inventory_item.image, inventory_item.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM inventory_items WHERE id = %s"
    values = id
    run_sql(sql, values)

def calculate_markup(buying_cost, selling_price):
    markup = ("{0:.0%}".format((selling_price-buying_cost)/buying_cost))
    return(markup)

# def show_by_manufacturer(manufacturer_id)
#     item = None
#     sql = "SELECT * FROM inventory_items WHERE manufacturer_id = %s"
#     values = [manufacturer_id]
#     results = run_sql(sql, values)

#     if results:
#         result = results[0]
#         manufacturer = manufacturer_repository.select(result['manufacturer_id'])
#         markup = inventory_repository.calculate_markup(result['buying_cost'], result['selling_price'])
#         item = Inventory(result['name'], manufacturer.name, result['description'], int(result['stock_quantity']), int(result['buying_cost']), int(result['selling_price']), markup, result['id'] )
#     return item

    # tasks = []

    # sql = "SELECT * FROM tasks"
    # results = run_sql(sql)

    # for row in results:
    #     user = user_repository.select(row['user_id'])
    #     task = Task(row['description'], user, row['duration'], row['completed'], row['id'] )
    #     tasks.append(task)
    # return tasks

