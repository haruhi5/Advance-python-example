import logging
import multiprocessing
from multiprocessing import process
import socket
import time
import random

# Test function

def download(server,port):
    name = process.current_process().name
    logging.info(f'Process starts: name = {name}')

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address = (server,port)
    logging.info(f'Connecting to {server}/{port}')
    s.connect(address) # three way shacks
    logging.info(f'Sending to {server}/{port}')
    s.send(b'Hello')  # blocking, the unblocking way is better
    data = s.recv(1024)
    logging.info(f'Receiving data from {server}/{port}: {data} ')
    s.close()
    logging.info(f'Closing connection to {server}/{port}')


    logging.info(f'Process finishs: name = {name}')


def main():
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')

    download('voidrealms.com',80)
    # in localhost ports under 1024 are used by operating system

    logging.info(f'Finished {name}')

# global the setting in case of version and hardware issues
logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

if __name__ == '__main__':
    main()
