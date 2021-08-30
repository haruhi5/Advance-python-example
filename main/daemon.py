# daemon thread setting helps kill the thread after the main thread exits

import logging
import threading
from threading import Thread, Timer
from concurrent.futures import ThreadPoolExecutor
import time
import random


# Test function

def test():
    threadname = threading.current_thread().getName()
    logging.info(f'Thread starts: id = {threading.get_ident()} name = {threadname}')
    for x in range(60):
        logging.info('Working')
        time.sleep(1)

    logging.info(f'Thread ends: id = {threading.get_ident()} name = {threadname}')


def stop():
    logging.info('Exiting the Test')
    exit(0)


def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Test Starting...')

    timer = Timer(3, stop)
    timer.start()
    t = Thread(target=test, daemon=False)
    t.start()

    logging.info('Test Finished')


if __name__ == '__main__':
    main()
