import os
import sys
# Config Path
sys.path.insert(0, "../")
# Import class MysqlConnection
from sqlclass import MysqlConnection

from uuid import uuid4

class XScanHistoryPort (object):
    def __init__(self):
        self.TABLE = "x_scan_history_ports"

    # Método de inserção de scanner para o historido de escaneamento das portas cadastras.;
    def set_history_host_scan(self, id_port, port, onoroff, host, temp_history, id_user, description=""):
        
        sql = f"INSERT INTO {self.TABLE} (id, id_port, port, onoroff, host, temp_history, created_at, id_user, description) VALUES (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP, %s, %s)"
        mysqlconn = MysqlConnection()
        conn = mysqlconn.connection()
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql, (str(uuid4()), id_port, port, onoroff, host, temp_history, id_user, description))
            conn.commit()
            cursor.close()
        conn.close()

    def get_date_history(self):
        sql = f"SELECT id, temp_history, created_at FROM {self.TABLE};"
        mysqlconn = MysqlConnection()
        conn = mysqlconn.connection()
        if conn.is_connected():
            cursor = conn.cursor(dictionary=True, buffered=True)
            cursor.execute(sql)
            db_consult = cursor.fetchall()
            cursor.close()            
            return db_consult
    
    def delete_history(self, id_hst):
        sql = f"DELETE FROM {self.TABLE} WHERE id=%s"
        mysqlconn = MysqlConnection()
        conn = mysqlconn.connection()
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql, (id_hst,))
            conn.commit()            
            cursor.close()
        conn.close()

    def delete_ports(self, id_pts):
        sql = f"DELETE FROM {self.TABLE} WHERE id=%s"
        mysqlconn = MysqlConnection()
        conn = mysqlconn.connection()
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql, (id_hst,))
            conn.commit()            
            cursor.close()
        conn.close()
        



if __name__=="__main__":
    xscanh = XScanHistoryPort()
