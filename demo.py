'''string = 'She is so beautiful and she is a good singer.'
print(string.replace("is", "was" , 1))
##print(string.find('is', 1))        #---------to find the position
is_pos1 = string.find("is", 1)
is_pos2 = string.find("is", is_pos1+1)
print(is_pos2)

print(string.capitalize())
print(string.title())
print(string.startswith('she'))'''


#for i in string [-1::-1]:
    #print(str(i))

'''def reverse(s):
    str = ""
    for i in s:
        str = i+str
    return str
s='shraddha pratik'

print(reverse(s))'''
test = {10,20,30}
tests = {'a','b','c'},
for i in tests:
    print(i)

import sys
#a = {'ab' : 20}
a = [10,20]
print(a.__sizeof__())



digits = [0, 1, 5, 4]

for i in digits:
    print(i)
else:
    print("No items left.")


class product:

    def __init__(self,id,nm,price,qty):
        self.id=id
        self.name=nm
        self.price=price
        self.quantity=qty


    def __str__(self):
        return "id :{}, name :{}, qty :{}, price:{}".format(self.id,self.name,self.quantity,self.price)


    def __repr__(self):
        return str(self)


p1 = product(1,nm='abc',price=100,qty=2)  # 1st will be positional argument
print(p1)





