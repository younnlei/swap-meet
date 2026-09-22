import uuid

class Item:
    """ Represents an item with unique ID during a swap meet
    attributes: id(int)
    method: get_category()
    """
    def __init__(self,id=None, condition=0):
        if not id:
            self.id = uuid.uuid4().int
        else:
            self.id = id

        self.condition = condition

    def get_category(self):
        """ returns the name of the class instance as  self.__class__.__name__      """
        return "Item"
    def __str__(self):
        """ returns string like an object of type Item with id ### """
        item_id = self.id
        item = self.get_category()
        return f" An object of type{item} with id {item_id}."
    def condition_description(self):
            
        if self.condition <= 1:
            return "Heavily Used"
        elif self.condition <= 2:
            return "Pretty Used"
        elif self.condition <= 3:
            return "Decent Condition"
        elif self.condition <= 4:
            return "Good Condition"
        else:
            return "Rarely Used"
        