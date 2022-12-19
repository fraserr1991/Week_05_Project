from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.inventory import Inventory
from models.manufacturer import Manufacturer
import repositories.inventory_repository as inventory_repository
import repositories.manufacturer_repository as manufacturer_repository

shop_blueprint = Blueprint("coffee equipment shop", __name__)

@shop_blueprint.route("/inventory")
def show_inventory():
    show_inventory = inventory_repository.select_all()
    show_manufacturers = manufacturer_repository.select_all()
    return render_template("inventory/index.html", inventory = show_inventory, manufacturers = show_manufacturers)

@shop_blueprint.route("/inventory/new_item", methods=['GET'])
def new_item():
    all_manufacturers = manufacturer_repository.select_all()
    return render_template("inventory/new_item.html", all_manufacturers = all_manufacturers)

@shop_blueprint.route("/inventory/new_item", methods=['POST'])
def add_item():
    item_name = request.form['item_name']
    manufacturer_id = request.form['manufacturer_id']
    description = request.form['description']
    quantity = request.form['quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    image = request.form['image']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    item = Inventory(item_name, manufacturer, description, quantity, buying_cost, selling_price, image)
    inventory_repository.save(item)
    return render_template("inventory/new_item.html")

@shop_blueprint.route("/manufacturer", methods=['GET'])
def show_manufacturer():
    all_manufacturers = manufacturer_repository.select_all() 
    return render_template("manufacturer/index.html", all_manufacturers = all_manufacturers)

@shop_blueprint.route("/manufacturer/new_manufacturer", methods=['GET'])
def new_manufacturer():
    all_manufacturers = manufacturer_repository.select_all() 
    return render_template("manufacturer/new_manufacturer.html", all_manufacturers = all_manufacturers)

@shop_blueprint.route("/manufacturer/new_manufacturer", methods=['POST'])
def add_manufacturer():
    name = request.form['name']
    established = request.form['established']
    manufacturer = Manufacturer(name, established)
    manufacturer_repository.save(manufacturer)
    return render_template("manufacturer/new_manufacturer.html")


# @tasks_blueprint.route("/tasks/<id>/edit", methods=['GET'])
# def edit_task(id):
#     task = task_repository.select(id)
#     users = user_repository.select_all()
#     return render_template('tasks/edit.html', task = task, all_users = users)

@shop_blueprint.route('/inventory/<index>', methods=['GET'])
def individual_item_info(index):
    selected_item = inventory_repository.select(index)
    return render_template('inventory/show.html/', item = selected_item)

@shop_blueprint.route("/inventory/<index>/edit_item/", methods=['GET'])
def get_edit_item(index):
    item = inventory_repository.select(index) 
    all_manufacturers = manufacturer_repository.select_all()
    return render_template("inventory/edit_item.html", item = item, all_manufacturers = all_manufacturers)

@shop_blueprint.route("/inventory/<id>", methods=['POST'])
def update_inventory(id):
    item_name = request.form['item_name']
    manufacturer_id = request.form['manufacturer_id']
    description = request.form['description']
    quantity = request.form['quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    image = request.form['image']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    margin = inventory_repository.calculate_markup(int(buying_cost), int(selling_price))
    item = Inventory(item_name, manufacturer, description, quantity, buying_cost, selling_price, image, margin, id)
    inventory_repository.update(item)
    return redirect('/inventory')

@shop_blueprint.route('/manufacturer/<index>', methods=['GET'])
def individual_manufacturer_info(index):
    selected_manufacturer = manufacturer_repository.select(index)
    return render_template('manufacturer/show.html/', manufacturer = selected_manufacturer)

@shop_blueprint.route("/manufacturer/<index>/edit_manufacturer/", methods=['GET'])
def get_edit_manufacturer(index):
    manufacturer = manufacturer_repository.select(index)
    return render_template("manufacturer/edit_manufacturer.html", manufacturer = manufacturer)

@shop_blueprint.route("/manufacturer/<id>", methods=['POST'])
def update_manufacturer(id):
    name = request.form['name']
    established = request.form['established']
    manufacturer = Manufacturer(name, established, id)
    manufacturer_repository.update(manufacturer)
    return redirect('/manufacturer')

@shop_blueprint.route('/inventory/<index>/delete/', methods=['POST'])
def delete_item(index):
    inventory_repository.delete(index)
    return redirect('/inventory')

@shop_blueprint.route('/manufacturer/<index>/delete/', methods=['POST'])
def delete_manufacturer(index):
    manufacturer_repository.delete(index)
    return redirect('/manufacturer')

# @tasks_blueprint.route("/tasks",  methods=['POST'])
# def create_task():
#     description = request.form['description']
#     user_id     = request.form['user_id']
#     duration    = request.form['duration']
#     completed   = request.form['completed']
#     user        = user_repository.select(user_id)
#     task        = Task(description, user, duration, completed)
#     task_repository.save(task)
#     return redirect('/tasks')