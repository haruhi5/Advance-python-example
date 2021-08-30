# Example application: TCP Echo Server

import logging
import multiprocessing
from multiprocessing import process
import socket
import select
import time
import random


# Test function

def chat_server(ip, port):
    name = process.current_process().name
    logging.info(f'Process starts: name = {name}')

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.info(f'Creating socket: {server}')
    address = (ip, port)
    logging.info(f'Binding socket to server: {server}/{port}')
    server.bind(address)
    server.setblocking(False)
    server.listen(100)  # maximum 100 connections
    logging.info(f'Listening: {server}/{port}')

    # setting for select
    readers = [server]
    while True:
        logging.info('Waiting...')
        readable, writeable, exceptional = select.select(readers, [server], [server], 1)  # don't forget time period

        for s in readable:  # something return from server
            try:
                if s == server:
                    client, addr = s.accept()
                    # Wait for an incoming connection.  Return a new socket
                    # representing the connection, and the address of the client.
                    # For IP sockets, the address info is a pair (hostaddr, port).

                    # ! if not set unblocking, the program will block in accept step !

                    client.setblocking(False)
                    readers.append(client)
                    logging.info(f'Accepting connection: {client} - {addr}')
                else:
                    data = s.recv(1024)
                    if data:
                        logging.info(f'Reading data from {s}: {data}')
                    else:
                        s.close()
                        readers.remove(s)
                        logging.info(f'Close connection: {s}')

            except Exception as ex:
                logging.warning(f'Error: {ex.args}')

    logging.info(f'Process finishs: name = {name}')


def main():
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')
    ip = 'localhost'
    port = 31020

    chat_s = multiprocessing.Process(target=chat_server, args=(ip, port), daemon=True, name='Server')

    while True:
        command = input('Enter command: start or stop: ').strip()
        if command == 'start':
            logging.info(f'Server starting...')
            chat_s.start()
            command = ''
        if command == 'stop':
            logging.info(f'Server stopping...')
            chat_s.terminate()
            chat_s.join()
            chat_s.close()
            logging.info(f'Server Stopped')
            break
            #  if not close properly, the process will still running
            #  and next time will show the address is already used

    logging.info(f'Finished {name}')


# global the setting in case of version and hardware issues
logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

if __name__ == '__main__':
    main()
