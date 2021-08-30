# Intro to Multiprocessing
# Multiple processes running the same script
# This is VERY different than threading
# Each process has its own memory space and its own threads

import logging
import multiprocessing
from multiprocessing import process

import time
import random


# Test function

def test(num):
    name = process.current_process().name
    logging.info(f'Process starts: name = {name}')

    time.sleep(num * 2)

    logging.info(f'Process finishs: name = {name}')


def main():
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')
    logging.info('Test Starting...')
    processes = []
    for x in range(5):
        p = multiprocessing.Process(target=test, args=[x], daemon=True)
        processes.append(p)
        p.start()
    logging.info('Do something on the main thread')
    for i in range(12):
        print(i)
    logging.info(f'Finished {name}')
    for p in processes:
        p.join()

    logging.info('Test Finished')


# global the setting in case of version and hardware issues
logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

if __name__ == '__main__':
    main()
