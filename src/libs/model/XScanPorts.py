#!/Python36/python

import sys

import MySQLdb
# Config Path
sys.path.insert(0, "../")
# Import class MysqlConnection
from sqlclass import MysqlConnection

import MySQLdb

class XScanPorts (object):
    def __init__(self):
        self.TABLE = "x_scan_ports"

    def get_ports(self):
        sql = f"SELECT * FROM {self.TABLE} WHERE is_scan = 0"
        mysqlconn = MysqlConnection()
        conn = mysqlconn.connection()
        if conn.is_connected():
            cursor = conn.cursor(dictionary=True, buffered=True)
            cursor.execute(sql)
            db_consult = cursor.fetchall()
            cursor.close()
            return db_consult
        conn.close()

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


