from swap_meet.item import Item
class Clothing(Item):

    def __init__(self, id=None,condition=0, fabric="Unknown"):
        """ clothig class,sub class of Item 
        Attributes :fabric(str), default = "Unknown"
        Methods: get_category() returns "Clothing"; __str__() decribes fabric.
        """
        super().__init__(id, condition)
        self.fabric = fabric

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        message = super().__str__()
        fabric = self.fabric
        return f"{message}It is made from {fabric} fabric."



