class Beverage:
    def __init__(self, id_val, inventory):
        self.id_val = id_val
        self.inventory = inventory
        self.cost = 50

    
    def add_inventory(self, amount: int = 1):
        # Increase object inventory by 1 or specified value
        self.inventory = self.inventory + amount
        return self
    
    
    def remove_inventory(self):
        # Decrease object inventory by 1
        self.inventory = self.inventory - 1
        return self