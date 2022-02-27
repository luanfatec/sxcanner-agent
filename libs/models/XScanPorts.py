import os
import sys

# Config Path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import class MysqlConnection
from db.sqlclass import MysqlConnection


class XScanPorts (object):
    def __init__(self):
        self.TABLE = "x_scan_ports"

    def get_ports(self, type_scan):
        sql = f"""SELECT * FROM {self.TABLE} WHERE is_scan = 0 AND type_scan = "{type_scan}" """
        mysqlconn = MysqlConnection()
        conn = mysqlconn.connection()
        if conn.is_connected():
            cursor = conn.cursor(dictionary=True, buffered=True)
            cursor.execute(sql, (type_scan))
            db_consult = cursor.fetchall()
            cursor.close()
            conn.close()
            return db_consult

    def set_is_scan(self, is_scan, idport):
        sql = "UPDATE x_scan_ports SET is_scan=%s WHERE id = %s"
        mysqlconn = MysqlConnection()
        conn = mysqlconn.connection()
        if conn.is_connected():
            cursor = conn.cursor();
            cursor.execute(sql, (is_scan, idport))
            conn.commit()
            cursor.close()
        conn.close()


if __name__=="__main__":
    test = XScanPorts()
    print(test.get_ports())
    