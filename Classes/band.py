class Band:
    
    def __init__(self,id,name,hometown) :
        self.id = id
        self.name = name
        self.hometown = hometown
        
    def __repr__(self) :
        return f"Band({self.id}:, {self.name}:, {self.hometown})"    