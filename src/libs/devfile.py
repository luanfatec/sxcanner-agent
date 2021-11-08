import nmap

ip = "192.168.0.103"
port = '22-80'

pscan = nmap.PortScanner()
pscan.scan(ip, port, arguments="-T5 -A")

# print([(host, pscan[host]["tcp"]) for host in pscan.all_hosts()])

for host, ports in [(host, pscan[host]["tcp"]) for host in pscan.all_hosts()]:   
    for port, state, name, version, allports \
        in [(port, ports[port]["state"], ports[port]["name"], ports[port]["version"], ports[port]) for port in ports]:        
        if "script" in allports.keys():           
            print(f"""
                ------
                Port {port} is {state} service {name} version {version}\n
                ------
                Header:
                {allports["script"]["http-title"]}\n{allports["script"]["http-server-header"]}
            """)
        else:
            print(f"""
                ------
                Port {port} is {state} service {name} version {version}
                ------
            """)
            
    