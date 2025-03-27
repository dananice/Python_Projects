def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
        
# print(add(3,5,5,7))     

# *args you dont need a set number of inputs - called unlimited positional arguments 

def calculate(n,**kwargs):
    print(kwargs)
    # for key, value in kwargs.item():
    #     print(key)
    #     print(value)  
    
    # another way 
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)  
    
#   n =2 +3 =5  * 5 = 25
calculate(2,add=3, multiply=5) # kwargs is a dict 

class Car:
    
    def __init__(self, **kw):
    #    self.make = kw['make']
    #    self.model = kw['model']
        self.make = kw.get("make")   # benefit of get is if the key doesn't exist returns none instead of error
        self.model = kw.get("model") 
        self.color = kw.get('color')
        
       
my_car = Car(make="Nissan", model="GT-R")        
print(my_car.model)            
      