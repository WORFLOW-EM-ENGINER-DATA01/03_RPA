import typing
import csv

# récupération du Modèle pour hydrater un futur fichier de données
from Model import Passenger 

class Counter:
    def __init__(self, count = 0):
        self.count = count
        
c = Counter()

# lecture d'un fichier 
def gen_titanic(file, age = 41, count = 0):
    with open(file, 'r') as csv_file:
        # le quotechar='|' pour qu'il ne retire pas les doubles guillemets (sinon il ajour des éléments dans la liste, voir les données)
        spamreader = csv.reader(csv_file, delimiter=',', quotechar='|')
        for row in spamreader:
            if ( row[1]  == '1' ) \
            and ( "female" in row ) \
            and ( row[6] != '' and float( row[6] ) < age ) :
                count += 1
                yield {"id" : row[0], "name" : row[3], "age" : float( row[6] ) }
    c.count = count
            
g = gen_titanic("./Data/titanic.csv")

def save(P : Passenger) -> None :
    pass

try:
    while True:
        res = next(g)
        res = { 'survived' : 1, 'sex' : 'F', **res }
        Passenger(**res)
        print( Passenger.__dict__ )
        print(res)
except StopIteration as e:
    # Objet Count pour compter lors des traitements sur les données avec le générateur
    print( f"Nombre de personne répondant aux critères : {c.count}") 