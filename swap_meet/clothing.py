from swap_meet.item import item
class Clothing(item):

    def __init__(self, id=None,condition=0, fabric="Unknown"):
        """ clothig class,sub class of Item 
        Attributes :fabric(str), default = "Unknown"
        Methods: get_category() returns "Clothing"; __str__() decribes fabric.
        """
        super().__init__(id, condition)
        self.fabric = fabric

    def get_category(self):
        return "Clothing"
