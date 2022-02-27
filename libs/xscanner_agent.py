import os
import sys
import argparse

# Config Path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Get class AgentMethods
from agent_methods import AgentMethods

# Configuração de argumentos
argparse_init = argparse.ArgumentParser(description="")
argparse_init.add_argument("--type", metavar="  Define um tipo de scanner.", type=str)

argsdata = argparse_init.parse_args()


# Iniciando a classe AgentMethods.
agentMethods = AgentMethods()

# ...
if argsdata.type == "single_port":
    agentMethods.single_port_method()
    
# ... 
elif argsdata.type == "complex_port":
    agentMethods.complex_port_method()
