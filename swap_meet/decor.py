from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id=None, condition=0, width=0, length=0):
        super().__init__(id, condition)
        self.width = width
        self.length = length
        
    def get_category(self):
        return "Decor"
    
    def __str__(self):
        message = super().__str__()
        width = self.width
        length = self.length
        return f"{message} It takes up a {width} by {length} sized space."