import os
import sys

# Config Path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Libs Controllers
from .controllers.XScanHistoryPortController import XScanHistoryPortController 
from .controllers.XScanPortsController import XScanPortsController


class AgentMethods (object):
    def __init__(self):
        pass
    
    def single_port_method(self):
        # Iniciando controller XScanPortsController
        portsController = XScanPortsController()
        
        # Iniciando controller XScanHistoryPortController
        historyController = XScanHistoryPortController()
        
        # Buscando todas as portas que ainda não foram escaneadas. 
        ports = portsController.get_ports(type_scan="single_port")

        # Percorrendo dicionário.
        for port in ports:
        
            # Checando se query porta já foi escaneada antes.
            if port['is_scan'] == 0:
                # Verificando de a porta está aberta ou fechada.
                if portsController.test_single_port(host=port['host'], port=port['ports']):
                    # Salvando o histórico de escaneamento que esteja a porta aberta.
                    historyController.set_history_host_scan(id_user=port['id_user'],host=port['host'], id_port=port['id'], onoroff=1, port=port['ports'], temp_history=port['temp_history'])
                    # Confirmando que foi escaneado.
                    portsController.set_is_scan(idport=port['id'], is_scan=1)
                else:
                    # Salvando o histórico de escaneamento que estejam com a porta fechada.
                    historyController.set_history_host_scan(id_user=port['id_user'], host=port['host'], id_port=port['id'], onoroff=0, port=port['ports'], temp_history=port['temp_history'])
                    # Confirmando que foi escaneado.
                    portsController.set_is_scan(idport=port['id'], is_scan=1)
                    
                    
    def complex_port_method(self):
        # test_advanced_ports
        portController = XScanPortsController()
        portController.test_advanced_ports()