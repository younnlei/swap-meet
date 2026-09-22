from swap_meet.item import Item


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


    def get_by_id(self, id):
        """Return the item with the matching ID."""

        for item in self.inventory:
            if item.id == id:
                    return item

        return None
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.remove(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        other_vendor.add(my_item)
        return True