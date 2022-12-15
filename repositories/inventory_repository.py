from db.run_sql import run_sql

import repositories.inventory_repository as inventory_repository
from models.inventory import Inventory

def save(inventory_item):
    sql = "INSERT INTO inventory_items (name, description, stock_quantity, buying_cost, selling_price) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [inventory_item.name, inventory_item.description, inventory_item.stock_quantity, inventory_item.buying_cost, inventory_item.selling_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    inventory_item.id = id
    return inventory_item

# def save(book):
#     sql = "INSERT INTO books (title, author_id) VALUES (%s, %s) RETURNING * "
#     values = [book.title, book.author.id]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     book.id = id
#     return book
