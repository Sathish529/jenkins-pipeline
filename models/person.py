class Person:
    def __init__(self,sno,name,city):
        self.sno=sno
        self.name=name
        self.city=city
    
    def serialize(self):
        return {'sno':self.sno,'name':self.name,'city':self.city}

    def __repr__(self):
        return str(self.serialize())