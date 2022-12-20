from models.inventory import Inventory
from models.manufacturer import Manufacturer

import repositories.inventory_repository as inventory_repository
import repositories.manufacturer_repository as manufacturer_repository

manufacturer_1 = Manufacturer("Sage", 1981, True)
manufacturer_repository.save(manufacturer_1)
manufacturer_2 = Manufacturer("Rancilio", 1926, False)
manufacturer_repository.save(manufacturer_2)

manufacturer_3 = Manufacturer("Breville", 1932, False)
manufacturer_repository.save(manufacturer_3)
manufacturer_4 = Manufacturer("DeLonghi", 1902, True)
manufacturer_repository.save(manufacturer_4)
manufacturer_5 = Manufacturer("Motta", 1962, False)
manufacturer_repository.save(manufacturer_5)


inventory_item_1 = Inventory("Coffee Tamper", manufacturer_5, "Real wood 58.4mm competition coffee tamper", 20, 25, 35, "https://m.media-amazon.com/images/I/61C-kJ7b3ML._AC_SS450_.jpg")
inventory_repository.save(inventory_item_1)
inventory_item_2 = Inventory("The Oracle", manufacturer_1, "Bean to cup coffee machine with automatic milk frother", 2, 1000, 1500, "https://johnlewis.scene7.com/is/image/JohnLewis/233712798?$rsp-pdp-port-640-82$")
inventory_repository.save(inventory_item_2)
inventory_item_3 = Inventory("Silvia PRO", manufacturer_2, "Dual boiler coffee machine with milk frother", 5, 900, 1320, "https://www.coffeeitalia.co.uk/wp-content/uploads/2022/05/Rancilio-Silvia-Pro-X.jpg.webp")
inventory_repository.save(inventory_item_3)
inventory_item_4 = Inventory("Dual boiler", manufacturer_1, "Dual boiler coffee machine", 5, 900, 1150, "https://expertreviews.b-cdn.net/sites/expertreviews/files/7/33//the_dual_boiler_silver_steaming.jpg")
inventory_repository.save(inventory_item_4)
inventory_item_5 = Inventory("One Touch CoffeeHouse", manufacturer_3, "One touch coffee drinks", 0, 90, 159, "https://media.currys.biz/i/currysprod/10226012?$l-large$&fmt=auto")
inventory_repository.save(inventory_item_5)
inventory_item_6 =  Inventory("Magnifica", manufacturer_4, "Automatic Bean to Cup Coffee Machine", 20, 220, 280, "https://m.media-amazon.com/images/I/615reUL2OIL._AC_SX466_.jpg")
inventory_repository.save(inventory_item_6)
