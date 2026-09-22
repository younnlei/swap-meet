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
        return self.__class__.__name__