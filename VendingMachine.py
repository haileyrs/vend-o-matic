from Beverage import Beverage

class VendingMachine:
    def __init__(self):
        self.inventory = {}
        self.balance = 0
        self.current_coins = 0

        # Uncomment to initialize with full inventory
        bev_1 = Beverage(1, 5)
        bev_2 = Beverage(2, 5)
        bev_3 = Beverage(3, 5)
        # bev_1 = Beverage(1, 0)
        # bev_2 = Beverage(2, 0)
        # bev_3 = Beverage(3, 0)
        self.inventory["1"] = bev_1
        self.inventory["2"] = bev_2
        self.inventory["3"] = bev_3


    def add_coin(self, amount):
        # Add coins one at a time to coin count
        self.current_coins = self.current_coins + amount
        return self.current_coins
    

    def remove_coins(self, empty_all: bool = False):
        # Remove coins from current coin count
        if empty_all:
            coins_to_return = self.current_coins
            self.current_coins = 0
            return coins_to_return
        
        if self.current_coins == 0:
            return self.current_coins
        else:
            self.current_coins = self.current_coins - 1
            return self.current_coins
    

    def get_all_inventory(self):
        # Fetch list of all inventory values
        counts = []
        for item in self.inventory.values():
            counts.append(item.inventory)
        return counts


    def get_inventory_by_id(self, item_id):
        # Fetch inventory for specific item by id
        item = self.inventory.get(item_id)
        return item.inventory


    def add_item_inventory(self, item_id):
        # Increase inventory for item if it is less than 5
        item = self.inventory.get(item_id)
        if item.inventory == 5:
            return
        else:
            item.add_inventory()
        return item


    def transact(self, item_id):
        # Perform transaction, updating inventory and returning all extra coins
        item = self.inventory.get(item_id)
        item.remove_inventory()
        response = {
            "quantity": 1,
            "coins_to_return": self.current_coins - 2,
            "inventory_remaining": item.inventory
        }
        self.remove_coins(True)
        self.balance = self.balance + 2
        return response
