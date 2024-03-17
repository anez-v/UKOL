import abc
import math 

class Locality:
    def __init__(self, name, coefficient):
        self.name = name
        self.coefficient = coefficient

class Property(abc.ABC):
    def __init__(self, locality: Locality, area: int):
        self.locality = locality
        self.area = area
    
    @abc.abstractmethod
    def get_property_type(self):
        pass

    @abc.abstractmethod
    def calculate_tax(self):
        pass

    def __str__(self):
        property_type = self.get_property_type()
        return f"{property_type} o ploše {self.area} metrů čtverečních v lokalitě {self.locality.name} (koeficient {self.locality.coefficient}) je zdaněn {self.calculate_tax()} Kč."


class Estate (Property):
    def __init__(self, locality: Locality, estate_type: str, area: int):
        super ().__init__(locality, area)
        self.estate_type = estate_type
        

    def calculate_tax (self):
       types = {
           "land": 0.85,
           "building site": 9,
           "forrest": 0.35
       }
       estate_type_coef = types[self.estate_type]
       tax =  math.ceil (self.area * self.locality.coefficient * estate_type_coef)
       return tax

    def get_property_type(self):
        types = {
            "land": "Zemědělský pozemek",
            "building site": "Stavební pozemek",
            "forrest": "Les"
       }
        property_type = types[self.estate_type]
        return property_type

class Residence (Property):
    def __init__(self, locality: Locality, area: int, commercial: bool):
        super().__init__(locality, area)
        self.commercial = commercial
    def calculate_tax (self):
        tax = self.area * self.locality.coefficient * 15
        if self.commercial == True:
            tax = tax * 2
        return math.ceil (tax)
    
    def get_property_type(self):
        if self.commercial:
            property_type = "Kancelář"
        else:
            property_type = "Obytný prostor" 
        return property_type

#localities
vesnice = Locality ("Ves", 2)
mesto = Locality ("Město", 3)
manetin = Locality ("Manětín", 0.8)
brno = Locality ("Brno", 3)

#properties
les = Estate(vesnice, "forrest", 500)
byt = Residence(mesto, 60, False)
kancl = Residence(mesto, 60, True)
zemedelsky_pozemek = Estate (manetin, "land", 900)
dum = Residence(manetin, 120, False)
kancelar = Residence(brno, 90, True)

#test
print(les.calculate_tax()== 350)
print(byt.calculate_tax()== 2700)
print(kancl.calculate_tax()== 5400)
print(zemedelsky_pozemek.calculate_tax()== 612)
print(dum.calculate_tax()== 1440)
print(kancelar.calculate_tax()== 8100)

print(str(zemedelsky_pozemek))
print(str(dum))