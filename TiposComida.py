from queries import Connection

class TipoComida(Connection):

    def __init__(self):
        super().__init__()

    # -------------------------- METODOS TIPOS COMIDA -----------------------------#

    def getAllTiposComida(self):
        return self.cursor().execute('SELECT * FROM TipoComida ORDER BY id').fetchall()


    # --------------------------- END METODOS TIPOS COMIDA -------------------------#