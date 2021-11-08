import mysql.connector

class MysqlConnection(object):
    def __init__(self):
         self.HOST = "192.168.0.103"
         self.USERNAME = "root"
         self.PASSWORD = "root"
         self.DATABASE = "xscanner"
    
    def connection(self):
        conn =  mysql.connector.connect(
            host=self.HOST,
            user=self.USERNAME,
            password=self.PASSWORD,
            database=self.DATABASE
        )    

        return conn       


if __name__=="__main__":
    print("--------------------------")
    mysqlconn = MysqlConnection()
    conn = mysqlconn.connection()
    conn.get_server_info();
    if conn.is_connected():
        print("Banco de dados conectado")
    
