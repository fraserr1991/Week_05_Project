from models.inventory import Inventory
from models.manufacturer import Manufacturer

import repositories.inventory_repository as inventory_repository
import repositories.manufacturer_repository as manufacturer_repository

manufacturer_1 = Manufacturer("Sage", 1981)
manufacturer_repository.save(manufacturer_1)
manufacturer_2 = Manufacturer("Rancilio", 1926)
manufacturer_repository.save(manufacturer_2)

inventory_item_1 = Inventory("The Oracle", manufacturer_1, "Bean to cup coffee machine with automatic milk frother", 5, 1000, 1500)
inventory_repository.save(inventory_item_1)
inventory_item_2 = Inventory("Silvia PRO", manufacturer_2, "Dual boiler coffee machine with milk frother", 5, 900, 1320)
inventory_repository.save(inventory_item_2)
inventory_item_3 = Inventory("Dual boiler", manufacturer_1, "Dual boiler coffee machine", 5, 900, 1150)
inventory_repository.save(inventory_item_3)


