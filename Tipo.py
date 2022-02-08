from queries import Connection

class Tipo(Connection):

    def __init__(self):
        super().__init__()
    
    def getAllTipos(self):
        return self.cursor().execute('SELECT * FROM Tipo ORDER BY id').fetchall()