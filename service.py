import time
import os
import sys

# Config Path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Importando AgentMethods
from libs.agent_methods import AgentMethods


# Iniciando AgentMethods
agentMethods = AgentMethods()

# ...
while True:
    agentMethods.complex_port_method()
    agentMethods.single_port_method()
    time.sleep(5)