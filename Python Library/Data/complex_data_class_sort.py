
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

# # Using normal function
# def prod_sort(n):
#     return n.price
    
# after_sort= sorted(product_list,key= prod_sort)
# print(after_sort)

# # # Using lamda function
print()
print(sorted(product_list,key= lambda x: x.price))

print()

# print(sorted(product_list, key= lambda y: y.dis_price()))

    
product_list_a= [
    Product("Mango",50,10,.05),
    Product("Apple",40,10,.15),
    Product("Apple",40,8,.15),
    Product("Cherry",35,12,.01),
    Product("Orange",65,7,.20),
]

# print(sorted(product_list, key= lambda x: x.price))

weigh_sort= sorted( product_list_a, key= lambda w: w.weight)

# print(weigh_sort)
print( sorted(weigh_sort, key= lambda p: p.price))