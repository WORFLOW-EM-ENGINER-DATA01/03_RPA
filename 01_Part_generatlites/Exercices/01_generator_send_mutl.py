

def gen_mult(m = 2) :

    while True:
        received = yield m
        
        if received is None :
            print("ici")
        m =  received * m 
        # print( received * m )
        

g = gen_mult() # instance du générateur itérateur 
# print( next(g) ) # 2
print( g.send(None) )

print("------")
for _ in range(10):
    print( g.send(3) ) 
    