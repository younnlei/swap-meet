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
            """Wave 3: returns string like an object of type Item with id ###"""
            item_id = self.id
            item = self.get_category()
            return f"An object of type {item} with id {item_id}."
    
    def condition_description(self):
        """ Wave5 : returns a description of an item's condition """ 
        
        if 4 <= self.condition <= 5:
            return "Like New!"
        elif 3 <= self.condition < 4:
            return "Rarely Used!"
        elif 2 <= self.condition < 3:
            return "Decent Condition"
        elif 1 <= self.condition < 2:
            return "Pretty Used"
        else:
            return "Pretty Bad"