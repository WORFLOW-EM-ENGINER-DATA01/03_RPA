import random 

def alea(p = 1, q = 10) :
    c = p, q
    while True:
        r = random.randint(*c)
        factor = yield r
        
        if factor is not None : c = factor
       
g = alea() # instance du générateur itérateur 
g.send(None) 
print("-----------------")
for i in range(50):
    print(next(g), end =" ")
    if i >= 25:
        if i == 25 : print(end="\n \n")
        print( g.send((-10, 0)), end = " " ) 
        
print()
    