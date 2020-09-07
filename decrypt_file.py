import gnupg
import json
import os
import sys

def decrypt(file):
    #Communicate with system keys
    gpg = gnupg.GPG(gnupghome=f'{os.getcwd()}/.gnupg')

    #Fetch encrypted file then decrypt
    with open(file, 'rb') as jfile:
        stream = str(gpg.decrypt_file(jfile))
        output = stream.split('\n')
        hosts = json.loads(''.join(output))
    return hosts
