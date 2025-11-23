from typing import Type, Self 
from abc import ABC, abstractmethod
from operator import methodcaller

class FoodApp(ABC):
    def __init__(self):
        self.Food_List: {'VegBurger':VegProductFactory, 'VegPizza':VegProductFactory, 'Burger':NonVegProductFactory, 'Pizza':NonVegProductFactory}
        self.Order_List: list[str]=[]

    #a static method of a class that returns an object of that class' type. 
    #But unlike a constructor, the actual object it returns might be an instance of a subclass. 
    #!!! Unlike a constructor, an existing object might be reused, instead of a new object created.

    def MakeOrder(self, *Order): #An abstract interface method
        for P in Order:
            print(P)
            self.Order_List.append(P)
            
            
        

           

    def GetOrderDescription(self): #An abstract interface method

        for F in self.Order_List:
            F.GetDescription()

class Product(ABC):
    def Get_Price():
        pass
    def get_Discription():
        pass

class BurgerClass(Product):
    def __init__(self):
        self.Price = 0
        self.calories = 0
        self.description = ""
    
    def Get_Price(self):
        return self.Price
    def get_Discription(self):
        return self.description

class PizzaClass(Product):
    def __init__(self):
        self.Price = 0
        self.calories = 0
        self.description = ""
        self.size = ""

    def Get_Price(self):
        return self.Price
    def get_Discription(self):
        return self.description
    
class VegBurger(BurgerClass):
    def __init__(self):
        self.Price = 12
        self.calories = 800
        self.description = "A Burger with a Veg patty, Lettuce, Tomatos, Ketchup, Mustard, and Onions"

    def Get_Price(self):
        print(self.Price)
    def get_Discription(self):
        print(self.description)

class Burger(BurgerClass):
    def __init__(self):
        self.Price = 10
        self.calories = 1000
        self.description = "A Burger with a Meat patty, Onions, BQQ sause, Mushrooms, and Bacon"

    def Get_Price(self):
        print(self.Price)
    def get_Discription(self):
        print(self.description)

class VegPizza(PizzaClass):
    def __init__(self):
        self.Price = 11
        self.calories = 700
        self.description = "A pizza with Pepper's, Spinich, onions, and tomatos on top"
        self.size = "Small"

    def Get_Price(self):
        print(self.Price)
    def get_Discription(self):
        print(self.description)

class Pizza(PizzaClass):
    def __init__(self):
        self.Price = 11
        self.calories = 950
        self.description = "A Pizza with Pepperoni, Bacon, and Mushrooms"
        self.size = "Medium"

    def Get_Price(self):
        print(self.Price)
    def get_Discription(self):
        print(self.description)

availableProduct={'VegBurger':BurgerClass, 'VegPizza':PizzaClass}

class VegProductFactory(ProductFactory):

    def createBurger(self) -> BurgerClass:
        print("I am making the Burger...")
        return VegBurger().get_Discription()
    
    def createPizza(self) -> PizzaClass:
        print("I am making the Pizza...")
        return VegPizza().get_Discription()

    def get_Product(product):
        
        try:
            for k,v in availableProduct.items():
                if k in product:
                    if k == 'VegBurger':
                        #print("1")
                        return availableProduct[k]().createBurger()
                    elif  k == 'VegPizza':
                        #print("2")
                        return availableProduct[k]().createPizza()#!!! dif.implem. for Tables -> static
                                
            raise Exception('No VegFactory Found')
        except Exception as _e:
            print(_e)
        return None
    
availableProduct={'Burger':BurgerClass, 'Pizza':PizzaClass}

class NonVegProductFactory(ProductFactory):

    def createBurger(self) -> BurgerClass:
        print("I am making the Burger...")
        return Burger().get_Discription()
    
    def createPizza(self) -> PizzaClass:
        print("I am making the Pizza...")
        return Pizza().get_Discription()

    def get_Product(product):
        
        try:
            for k,v in availableProduct.items():
                if k in product:
                    if k=='Burger':
                        #print("1")
                        return availableProduct[k]().createBurger()
                    elif k=='Pizza':
                        #print("2")
                        return availableProduct[k]().createPizza()#!!! dif.implem. for Tables -> static
                                
            raise Exception('No Factory Found')
        except Exception as _e:
            print(_e)
        return None
    
availableProduct={'VegBurger':VegProductFactory, 'VegPizza':VegProductFactory, 'Burger':NonVegProductFactory, 'Pizza':NonVegProductFactory}

class ProductFactory(ABC):
    def __init__():
        super().__init__()
        
    @abstractmethod
    def createBurger(self) -> BurgerClass:
        pass
    
    def createPizza(self) -> PizzaClass:
        pass

    @staticmethod
    def get_Product(product):
        
        try:
            for k,v in availableProduct.items():
                if k in product:
                    if k == 'VegPizza':
                        #print("1")
                        return availableProduct[k].get_Product(product)
                    else:
                        #print("2")
                        return availableProduct[k].get_Product(product)#!!! dif.implem. for Tables -> static
                                
            raise Exception('No ProductFactory Found')
        except Exception as _e:
            print(_e)
        return None
    
Fa = FoodApp()
Fa.MakeOrder('VegPizza', 'Burger')