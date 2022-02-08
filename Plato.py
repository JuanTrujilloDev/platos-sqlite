from queries import Connection
from Tipo import Tipo
from TiposComida import TipoComida

class Plato(Connection):

    '''
    Clase Plato (Mapeadora para operaciones con platos)

    Solo recibe la clase Connection que hara todas las queries y conexiones con sqlite.
    
    
    '''

    def __init__(self):
        
        super().__init__()

    def getAllPlatos(self):
        '''
        
        getAllPlatos:

        retorna todos los platos listados en la base de datos.
        
        '''

        return self.cursor().execute('SELECT * FROM Plato ORDER BY nombre').fetchall() 


       
    def getPlatoById(self):

        '''
        getPlatoById:

        Recibe por input el #id del plato.

        No retornara nada si el id es incorrecto

        Retorna el plato con el id correcto.
        
        '''

        platos = self.getAllPlatos()
        print("POR FAVOR SELECCIONA UN PLATO POR # DE PLATO: \n\n")
        for plato in platos:
            print("Plato #     | Nombre \n" + f"{plato[0]}             {plato[1]}")\
        
        while True:

            pk = input("Escribe el numero de id: ")
            try:
                pk = int(pk)

            except:
                print("\n\nERROR AL SELECCIONAR PLATO POR FAVOR ESCRIBE UN NUMERO \n\n")
            else:
                break

        plato =  self.cursor().execute(f'SELECT * FROM Plato WHERE id = "{pk}" ').fetchall()

        if plato:
            return plato
        else:
            print("\n No se encontro ningun plato con ese id")




    # Creacion de plato
    def createPlato(self):
        
        '''
        createPlato

        Funcion recibe multiples inputs con los atributos de Plato.

        Al final retorna la insercion del objeto en la DB.

        '''


        print("CREACION DE PLATO, POR FAVOR LLENA LOS SIGUIENTES DATOS:")

        nombre = input("\nNombre del plato: ")
        descripcion = input("\nDescripcion de como esta hecho: ")

        while True:
            precio = input("\nPrecio, recuerda que en miles de pesos no debe tener puntos")
            try:
                precio = int(precio)
            except:
                print("\nError al crear plato, se ingreso un valor erroneo en el precio.")
            else:
                break
        
        tipo = input("\nPara el tipo de plato por favor presiona:"
                     +"\n1. Uno para Entradas"
                     +"\n2. Dos para Platos Fuertes"
                     +"\n3. Tres para Postres"
                     +"\n4. Cuatro para Bebidas\n:")

        while tipo not in ["1","2","3","4"]:
            print("\nError al crear el tipo de plato, por favor vuelve a intentarlo.")
            tipo = input("\nPara el tipo de plato por favor presiona:"
                     +"\n1. Uno para Entradas"
                     +"\n2. Dos para Platos Fuertes"
                     +"\n3. Tres para Postres"
                     +"\n4. Cuatro para Bebidas\n:")
        
        tipo = int(tipo)

        tipos_comida = TipoComida()
        tipos_comida = tipos_comida.getAllTiposComida()
        listatipocomida = []
        for tipocomida in tipos_comida:
            print("\nPor favor selecciona para el tipo de plato: "
                 +f"\n{tipocomida[0]}. Para {tipocomida[1]}")
            listatipocomida.append(str(tipocomida[0]))

        tipocomida = input("\nSelecciona el id del tipo comida: ")

        while tipocomida not in listatipocomida:
            print("\nError, el TipoComida no se encuentra, intente nuevamente.")
            for tipocomida in tipos_comida:
                print("\nPor favor selecciona para el tipo de plato: "
                    +f"\n{tipocomida[0]}. Para {tipocomida[1]}")
            tipocomida = input("\nSelecciona el id del tipo comida: ")
        
        tipocomida = int(tipocomida)
        query = f'''INSERT INTO Plato(nombre, descripcion, precio, tipo, tipo_comida)
                   VALUES ("{nombre}", "{descripcion}", "{precio}", "{tipo}", "{tipocomida}")'''
        print(query)
        plato = self.cursor().execute(query)
        self.connect.commit()
        return plato


        
        

        
        
        

