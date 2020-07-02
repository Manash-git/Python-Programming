
class Product():
    
    def __init__(self,name,price,weight,discount):
        self.name=name
        self.price=price
        self.weight=weight
        self.discount=discount
    
    def __repr__(self):
        return repr((self.name,self.price,self.weight,self.discount))
    
    def dis_price(self):
        return self.price - (self.price * self.discount)
    
    
product_list= [
    Product("Mango",50,10,.05),
    Product("Apple",40,8,.15),
    Product("Cherry",35,12,.01),
    Product("Orange",65,7,.20),
]

from operator import attrgetter,methodcaller,itemgetter

print(sorted(product_list,key=attrgetter('price')))
# print(sorted(product_list,key=attrgetter("price"), reverse=True))


print()
print(sorted(product_list, key= methodcaller("dis_price")))


inventory = [
    ("FCB", 5),
    ("RM", 2),
    ("MU", 9),
    ("ATM", 4),
    ("Liv", 2),
    ("Juve", 1)
]

print(sorted(inventory, key= itemgetter(1)))