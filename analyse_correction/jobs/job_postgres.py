from infrastructures.database import connect_to_postgres, insert
from domain.types import StockPurchaseList

class Hydrate:
    
    def __init__(self, investments:StockPurchaseList ):
        self.conn =  connect_to_postgres()
        self.investments = investments
        
    def execute(self)->None:
        if self.conn is None:
            return

        insert(self.conn, self.investments)
        
        self.conn.close()
        
        return None
        