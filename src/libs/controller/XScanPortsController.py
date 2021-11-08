import sys
# Config Path
sys.path.insert(0, "../")

# import model ports table
from model import XScanPorts

# import controller History Port
from controller import XScanHistoryPortController

# Other libs
import socket
import nmap

class XScanPortsController (object):
    def __init__(self):
        self.message = ""
    
    # Metodo de consulta, busca regras de consulta na table de portas, para realizar o scanner.
    def get_ports(self):
        port = XScanPorts.XScanPorts();
        return port.get_ports()

    
    def set_is_scan(self, is_scan, idport):
        port = XScanPorts.XScanPorts()
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

    def test_advanced_ports(self):

        # Iniciando o history controller
        historyController = XScanHistoryPortController.XScanHistoryPortController()

        # Portas do DB
        dbports = self.get_ports();
        for dbport in dbports:
            if dbport["type_scan"] == "complex_ports":                

                # Criando scanner
                pscan = nmap.PortScanner()
                pscan.scan(dbport["host"], dbport["ports"], arguments="-T5 -A")

                # Filtrando os resultados... set_history_host_scan(self, id_port, port, onoroff, host, temp_history, id_user)
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
                                id_user=dbport['id_user'],host=dbport['host'], id_port=dbport['id'], onoroff=1, port=port, temp_history=dbport['temp_history'], description=template)
                            
                        else:
                            # Criando template description
                            template = f"""Port {port} is {state} service {name} version {version} - {product}"""
                            # Salvando o histórico do scan
                            historyController.set_history_host_scan(\
                                id_user=dbport['id_user'],host=dbport['host'], id_port=dbport['id'], onoroff=1, port=port, temp_history=dbport['temp_history'], description=template)

                # Concluindo a porta..
                self.set_is_scan(idport=dbport['id'], is_scan=1)
                            
