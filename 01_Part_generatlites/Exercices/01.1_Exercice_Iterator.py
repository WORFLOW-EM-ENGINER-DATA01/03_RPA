import typing 

from typing import List

PRECISION = 10

class IterNumber:
    
    def __init__(self,coeff : float, numbers : List[int] ) -> None:
        self.coeff = coeff 
        self.numbers = numbers
        self.count = 0
    
    def __iter__(self):
        print(self.count)
        return self 
    
    def __next__(self):
        
        if self.count <  len( self.numbers ) :
            result = self.numbers[self.count] * self.coeff
            self.count += 1 

            return round( result , PRECISION )
        else:
            raise StopIteration
        
    def __len__(self): return len(self.numbers)
    
it = IterNumber(coeff=.01, numbers=[100, 456, 88])

for num in it:
    print(num)
    
# avec un while
it = IterNumber(coeff=.01, numbers=[100, 456, 88])

try:
    print("longueur de la liste" , len(it))
    while True:
        r = next(it)
        print(r)
except StopIteration:
    print("stop") 