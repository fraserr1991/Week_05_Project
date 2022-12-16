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
    return render_template("inventory/index.html", inventory = show_inventory)
