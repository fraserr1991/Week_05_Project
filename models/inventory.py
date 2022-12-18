class Inventory():

    def __init__(self, name, manufacturer, description, stock_quantity, buying_cost, selling_price, margin = None, id = None):
        self.name = name
        self.manufacturer = manufacturer
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.margin = margin
        self.id = id
        