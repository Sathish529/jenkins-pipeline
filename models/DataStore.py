from models.person import Person

class Store:
    def __init__(self):
        self.list=[]

    def add(self,newone):
        self.list.append(newone)
    
    def getPeople(self):
        return self.list
    
people=Store()
people.add(Person(1,'Ravi','Chennai'))
people.add(Person(2,'Rajan','Mumbai'))
people.add(Person(3,'Arjun','Mumbai'))
