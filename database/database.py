from sqlalchemy import create_engine
import os

class Database:
    def __init__(self): 
        self.engine = create_engine(
            f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
            f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        )
    
    def get_engine(self): 
        """
        cria o método get engine e retorna uma engine para conexão do db
        """
        return self.engine 