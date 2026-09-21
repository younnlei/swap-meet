class Vendor:
    """ mangaing a vendor's inventory of items.
    attributes: inventory(list), default empty list.
    method : add(item): adds an item to the inventory. 
    reove (item) from the inventory. """

    def __init__(self, inventory=None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory
    def add(self,item):
        self.inventory.append(item)
        return item
    def remove(self, item):

        if item in self.inventory: 
            self.inventory.remove(item)
            return item
        return False