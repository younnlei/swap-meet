from swap_meet.item import Item

class Electronics(Item):

    def __init__(self, id=None, condition=0, type="Unknown"):
        super().__init__(id, condition)
        self.type = type

    def get_category(self):
        return "Electronics"

    def __str__(self):
        message = super().__str__()
        type = self.type
        return f" {message}. This is a {type} device."
        
        
        
