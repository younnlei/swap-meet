from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id=None, condition=0, width=0, length=0):
        """ Wave 05: Represents a Decor object, which is a subclass of Item.
        Attributes: width, defaults to 0.
        length: defaults to 0.
        Method: get_category():returns the string "Decor".
        __str__(): returns a string
        """
        
        super().__init__(id, condition)
        self.width = width
        self.length = length
        
    def get_category(self):
        return "Decor"
    
    def __str__(self):
        message = super().__str__()
        width = self.width
        length = self.length
        return f"{message}It takes up a {width} by {length} sized space."