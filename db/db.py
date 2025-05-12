class DBFactory:
    def __init__(self):
        pass

    def create(self, dbtype: str , connection: str):
        if dbtype.lower() == 'postgres' or dbtype.lower() == 'postgresql':
            pass
        elif dbtype.lower() == 'mongo':
            pass
        elif dbtype.lower() == 'redis':
            pass
        else:
            pass

class DBManager:
    def __init__(self):
        self.factory = DBFactory()  


