import uuid

class Item:
    """
    Wave02: Represents an item with unique ID during a swap meet.
    attributes: id(int) and condition(float,default to 0).
    method: get_category(): returns a string with the class name.
    """
    def __init__(self,id=None, condition=0):
        if not id:
            self.id = uuid.uuid4().int
        else:
            self.id = id

        self.condition = condition

    def get_category(self):
        """ returns the name of the class instance as  self.__class__.__name__  """

        return "Item"
    
    def __str__(self):
        """ Wave03: returns string like an object of type Item with id ### """
        item_id = self.id
        item = self.get_category()

        return f"An object of type {item} with id {item_id}."
    
    def condition_description(self):
        """ 
        Wave05 : returns a description of an item's condition 
        Method: condition_description(): provides string describing the condition.
        """ 
        
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