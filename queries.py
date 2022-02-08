import sqlite3


class Connection():

    def __init__(self):

        self.connect = sqlite3.connect('personas.db')

    
    def cursor(self):
        return self.connect.cursor()




 




    

