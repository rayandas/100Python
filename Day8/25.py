'''
Define a class, which have a class parameter and have a same instance parameter.
'''

class Car:
    name = "Car"
    def __init__(self,name=None):
        self.name = name 


bmw = Car("BMW")
print("%s name is %s"%(Car.name,bmw.name))

audi = Car()
audi.name = "Audi"
print("%s name is %s"%(Car.name,audi.name))

