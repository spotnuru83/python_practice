import mysql.connector
from mysql.connector import Error

class MySQLDB:
    def __init__(self):
        pass

    def connect(self, host_name , user_name, password,db_name):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(host=host_name, user=user_name, password = password,database = db_name)
            self.cursor = self.connection.cursor()
            print("Successfully connected to MySQL.")
        except Error as e:
            print(f"The error '{e}' occurred.")

    def close(self):
        if self.connection is not None:
            self.connection.close()

    def read_query(self, query,show=False):
        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            if show:
                for record in records:
                    print(record)
        except Error as e:
            print(f"Error while fetching data:  {e}")

    def create_table(self, query):
        try:
            self.cursor.execute(query)            
            print("Table is created successfully or already exists. ")
        except Error as e:
            print(f"Error while creating table :  {e}")        
        

    def insert_record(self,query,values):
        try:
            self.cursor.execute(query,values)      
            self.connection.commit()      
            print("row inserted successfully. ")
        except Error as e:
            print(f"Error while inserting data :  {e}") 