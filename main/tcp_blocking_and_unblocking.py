import logging
import multiprocessing
from multiprocessing import process
import socket
import select
import time
import random


# Test function

def socket_nonblocking(ip, port):
    name = process.current_process().name
    logging.info(f'Process starts: name = {name}')

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.info(f'Non Blocking: Creating socket {s}')
    address = (ip, port)
    logging.info(f'Non Blocking: Connecting...')
    ret = s.connect_ex(address)

    if ret != 0:
        logging.info('Non Blocking: Failed to connect!')
        return

    logging.info(f'Non Blocking: Connected successfully')
    s.setblocking(False)

    # setting for select
    inputs = [s]
    outputs = [s]
    while inputs:
        logging.info('Do something on the main thread')
        logging.info('Non Blocking: Waiting...')
        readable, writable, exceptional = select.select(inputs, outputs, inputs, 0.5)

        for s in writable:
            logging.info('Non Blocking: Sending...')
            data = s.send(b'Hello unblocking\r\n')
            logging.info(f'Non Blocking: Send data length: {data}')

            # notice it is ouptuts not writeable
            # only sending once for demon, or it is a attack!
            outputs.remove(s)

        for s in readable:  # something return from server

            logging.info('Non Blocking: Reading...')
            data = s.recv(1024)
            logging.info(f'Non Blocking: Read data length: {data}')
            # once readable means the server response, we can do the next step
            # here just close for demon
            logging.info('Do next step on the unblocking')
            logging.info('Non Blocking: Closeing...')
            s.close()
            inputs.remove(s)
            break

        for s in exceptional:
            logging.info('Non Blocking: Error')
            inputs.remove(s)
            outputs.remove(s)

    logging.info(f'Process finishs: name = {name}')


def main():
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')

    socket_nonblocking('voidrealms.com', 80)

    logging.info(f'Finished {name}')


# global the setting in case of version and hardware issues
logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

if __name__ == '__main__':
    main()
