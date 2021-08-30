import logging
import multiprocessing
from multiprocessing import process
import socket
import time
import random

# Test function

def server(ip,port):
    name = process.current_process().name
    logging.info(f'Process starts: name = {name}')

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address = (ip,port)
    logging.info(f'Binding {s}-socket to server: {port}')
    s.bind(address)

    logging.info(f'Listening only one request on {port}')
    s.listen(1)  # listening only one request
    logging.info(f'Accepting one request on {port}')
    conn,add = s.accept()
    logging.info(f'Accept connection {conn} from {add}')
    while True:
        data = conn.recv(1024)
        if len(data) == 0 or data == 'exit':
            conn.close()
            logging.info('Exiting')
            break
        # if not close than logging
        logging.info(f'Receiving data from {add}: {data} ')
    s.close()
    logging.info(f'Closing connection to {server}: {port}')


    logging.info(f'Process finishs: name = {name}')


def main():
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')

    server('localhost', port=2180)
    # in localhost ports under 1024 are used by operating system
    # for sys == win32, need to enable the telnet
    # it seems not safe? close it afterwards
    # in win32 I can receive the data once pressing the keyboard which is different from the video
    logging.info(f'Finished {name}')

# global the setting in case of version and hardware issues
logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

if __name__ == '__main__':
    main()
