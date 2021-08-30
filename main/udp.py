import logging
import multiprocessing
import sys
import threading
from multiprocessing import process
import socket
import time
import random

# Test function

def make_socket(ip='localhost', port=2021,boarding=False):
    name = process.current_process().name
    logging.info(f'Process starts: name = {name}')

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    address = (ip,port)
    if boarding == True:
        logging.info(f'{name}: start to send')
    else:
        s.bind(address)
        logging.info(f'{name}: start to bind socket {s} to {ip}/{port}')

    with s: # open and close
        while True:
            if boarding == True:
                logging.info(f'{name}: Sending...')
                data_send = b'Hello UDP'
                s.sendto(data_send,address)
                time.sleep(1)
            else:
                data_recv, addr = s.recvfrom(1024)
                logging.info(f'{name}: Receiving from {addr} = {data_recv}')
                time.sleep(1)

def main():
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')
    # ip = 'localhost'
    # port = 24050

    # broadcaster = make_socket(ip,port,boarding=True)
    # make it in process
    broadcaster = multiprocessing.Process(target=make_socket,kwargs={'boarding':True},daemon=True,name='Boardcaster')
    listener = multiprocessing.Process(target=make_socket, kwargs={'boarding': False},daemon=True,name='Listener')
    broadcaster.start()
    listener.start()

    logging.info('Do something on the main thread')
    timer = threading.Timer(25,sys.exit,[0])
    timer.start()

    logging.info(f'Finished {name}')

# global the setting in case of version and hardware issues
logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

if __name__ == '__main__':
    main()
