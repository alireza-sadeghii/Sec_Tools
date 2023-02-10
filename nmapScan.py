# @Author: Alireza
# CS50 Project
# Sec Tools : Nmap

# import python-nmap library
import nmap
mapper = nmap.PortScanner()

# scan the target ip
def port_scan(host):
    mapper.scan(host)
    return config_result()

# arrange output of target scan
def config_result():
    result = []
    for host in mapper.all_hosts():
        result.append("Host : " + host + "( " + mapper[host].hostname() + " ) ")
        result.append("Host State : " +  mapper[host].state())

    for protocol in mapper[host].all_protocols():
        result.append("-" * 10)
        result.append("Protocol : " + protocol)
        ports = mapper[host][protocol].keys()
        for port in ports:
            result.append("Port: " + str(port) + "\t   " + mapper[host][protocol][port]["state"] +
                          "\t   " + mapper[host][protocol][port]["name"])

    return result