import itertools

class IceCreameMachine:
    
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        
        finalList = []
        if len(self.ingredients) > 0 and len(self.toppings) > 0:
            for i, t in itertools.product(self.ingredients, self.toppings):
                MyList = []
                MyList.append(i)
                MyList.append(t)    
                finalList.append(MyList)                             
        
        return finalList


if __name__ == "__main__":
    machine = IceCreameMachine(["vainilla","chocolate"],["chocolate souce"])
    print("*********** Output **********")
    print(machine.scoops())