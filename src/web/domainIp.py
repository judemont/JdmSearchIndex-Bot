import socket

def getIp(domain):
    IP = socket.gethostbyname(domain)
    return IP