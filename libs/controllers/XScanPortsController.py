import os
import sys

# Config Path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# import model ports table
from models.XScanPorts import XScanPorts

# import controller History Port
from controllers.XScanHistoryPortController import XScanHistoryPortController

# Other libs
import socket
import nmap
from multiprocessing import Pool


class XScanPortsController (object):
    def __init__(self):
        self.message = ""
    
    # Metodo de consulta, busca regras de consulta na table de portas, para realizar o scanner.
    def get_ports(self, type_scan):
        port = XScanPorts();
        return port.get_ports(type_scan=type_scan)

    
    def set_is_scan(self, is_scan, idport):
        port = XScanPorts()
        port.set_is_scan(idport=idport, is_scan=is_scan)


    # Metodo de teste, realiza o teste para verificar de a porta está aberta. 
    def test_single_port(self, host, port):        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(1)
        resp = client.connect_ex((host, int(port)))
        
        if resp == 0:
            return True
            client.close()
        else:
            return False
            client.close()
            
    def advanced_scan_aux(self, dbport, historyController):
        # Criando scanner
        pscan = nmap.PortScanner()
        pscan.scan(dbport["host"], dbport["ports"], "-T5 -A")  

        # Filtrando os resultados... 
        for host, ports in [(host, pscan[host]["tcp"]) for host in pscan.all_hosts()]:
            # ... 
            for port, state, name, version, product, allports \
                in [(pport, ports[pport]["state"], ports[pport]["name"], ports[pport]["version"], ports[pport]["product"], ports[pport]) for pport in ports]: 

                template = ""
                if "script" in allports.keys():
                    if "http-title" in allports.keys():
                        # Criando template description
                        template = f"""Port {port} is {state} service {name} version {version}\n-----\nHeader\n{allports["script"]["http-title"]}\n{allports["script"]["http-server-header"]}"""
                    else:                        
                        template = f"""Port {port} is {state} service {name} version {version}\n-----\n{allports["script"]}"""
                    # Salvando o histórico do scan
                    historyController.set_history_host_scan(\
                        id_user=dbport['id_user'],host=dbport['host'], id_port=dbport['id'],\
                        onoroff=1, port=port, temp_history=dbport['temp_history'], description=template)
                    
                else:
                    # Criando template description
                    template = f"""Port {port} is {state} service {name} version {version} - {product}"""
                    # Salvando o histórico do scan
                    historyController.set_history_host_scan(\
                        id_user=dbport['id_user'],host=dbport['host'], id_port=dbport['id'],\
                        onoroff=1, port=port, temp_history=dbport['temp_history'], description=template)

        # Concluindo a porta..
        self.set_is_scan(idport=dbport['id'], is_scan=1)

    def test_advanced_ports(self):

        # Iniciando o history controller
        historyController = XScanHistoryPortController()

        # Portas do DB
        dbports = self.get_ports(type_scan="complex_port");
        ps_pool = Pool(5)
        for dbport in dbports:
            ps_pool.apply_async(self.advanced_scan_aux, args=(dbport, historyController,))
        ps_pool.close()
        ps_pool.join()
                
                
                
if __name__=="__main__":
    xport = XScanPortsController()
    print(xport.get_ports())
    