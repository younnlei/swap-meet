from swap_meet.item import Item

class Electronics(Item):
    """ Wave 05: represents an Electronicd object,which is a subclass of Item.
    Attributes: type(str): Description of the electronics device. Defaults to "Unknown".
    Methods: get_category(), returns the string "Electronics".
    __str__(): returns a string
    """

    def __init__(self, id=None, condition=0, type="Unknown"):
        super().__init__(id, condition)
        self.type = type

    def get_category(self):
        return "Electronics"

    def __str__(self):
        message = super().__str__()
        type = self.type
        return f"{message}This is a {type} device."
        
        
        
