
from controller import XScanPortsController, XScanHistoryPortController

import argparse
import datetime

parse = argparse.ArgumentParser()
parse.add_argument("--type", metavar="      Define um tipo de scanner.", type=str)
arguments = parse.parse_args()


# Realizando o scanner de porta por porta de acordo com os que estiverem inativos(Não executados) no banco.
if arguments.type == "single_port":
    portController = XScanPortsController.XScanPortsController() # Iniciando o controlador XScanPortsController.
    historyController = XScanHistoryPortController.XScanHistoryPortController() # Iniciando o controlador XScanHistoryPortController.
    
    # Recuperando portas que não estejam executadas;
    ports = portController.get_ports()
    
    for port in ports:

        if port["type_scan"] == "single_port":

            # Checando se query porta já foi escaneada antes.
            if port['is_scan'] == 0:
                # Verificando de a porta está aberta ou fechada.
                if portController.test_single_port(host=port['host'], port=port['ports']):
                    # Salvando o histórico de escaneamento que esteja a porta aberta.
                    historyController.set_history_host_scan(id_user=port['id_user'],host=port['host'], id_port=port['id'], onoroff=1, port=port['ports'], temp_history=port['temp_history'])
                    # Confirmando que foi escaneado.
                    portController.set_is_scan(idport=port['id'], is_scan=1)
                else:
                    # Salvando o histórico de escaneamento que estejam com a porta fechada.
                    historyController.set_history_host_scan(id_user=port['id_user'], host=port['host'], id_port=port['id'], onoroff=0, port=port['ports'], temp_history=port['temp_history'])
                    # Confirmando que foi escaneado.
                    portController.set_is_scan(idport=port['id'], is_scan=1)

# ... 
elif arguments.type == "complex_ports":
    # test_advanced_ports
    portController = XScanPortsController.XScanPortsController()
    portController.test_advanced_ports()


# ...
elif arguments.type == "check_history_ports":
    # ...   

    history = XScanHistoryPortController.XScanHistoryPortController()
    for hist in history.get_date_history():
        tmp = datetime.datetime.timestamp(hist['created_at'])
        timestmp = datetime.datetime.fromtimestamp(tmp)

        day = timestmp.day
        month = timestmp.month
        year = timestmp.year

        sd = datetime.date(year, month, day)

        td = datetime.date.today()
        dy = abs((td - sd).days)

        if dy == hist["temp_history"]:
            history.delete_history(id_hst=hist['id'])
        else:
            pass

    # ... 
