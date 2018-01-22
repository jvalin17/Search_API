import csv
from preprocess_chemicals_data import prepData
import sqlite3
class useDatabase :

    def ready(self, filename):
        prepData (filename)
        pass
    
    def __init__ (self):
        import csv 
        import sqlite3
        pass
        
    def createTable (self , table_name):
        con = sqlite3.connect(":memory:")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF  NOT EXISTS " +  table_name + "(Chemical_formula text, Band_gap real, Color text);")
        return cur,con
        
    def transferDataToTable (self,filename,cursor,con):
        
        with open(filename,'rb') as fin: 
            dr = csv.DictReader(fin) # comma is default delimiter
            to_db = [(i['Chemical_formula'], i['Band_gap'], i['Color'])for i in dr]

        cursor.executemany("INSERT INTO Chemicals (Chemical_formula, Band_gap, Color) VALUES (?, ?, ?);", to_db)
        con.commit()
        return cursor, con
        
    
    def executeQuery (self, cursor, con, query):
  
        #logging type of query
        print (type(query))

        try:
            cursor.execute(query)   
            data=cursor.fetchall()

            for row in data:
                #logging query results
                print (row)

            return data

        except:
            return None



    

