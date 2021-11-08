import sys

# Config Path
sys.path.insert(0, "../")

# import model history table
from model import XScanHistoryPort

class XScanHistoryPortController(object):

    def __init__(self):
        self.message = ""

    # Método de inserção de scanner para o historido de escaneamento das portas cadastras.
    def set_history_host_scan(self, id_port, port, onoroff, host, temp_history, id_user, description=""):
        history = XScanHistoryPort.XScanHistoryPort()
        history.set_history_host_scan(id_port=id_port, port=port, onoroff=onoroff, host=host, temp_history=temp_history, id_user=id_user, description=description)
    
    def get_date_history(self):
        history = XScanHistoryPort.XScanHistoryPort()
        return history.get_date_history()

    def delete_history(self, id_hst):
        history = XScanHistoryPort.XScanHistoryPort()
        history.delete_history(id_hst=id_hst)

    def delete_ports(self, id_pts):
        history = XScanHistoryPort.XScanHistoryPort()
        history.delete_ports(id_pts=id_pts)



if __name__=="__main__":
    hcontroller = XScanHistoryPortController()