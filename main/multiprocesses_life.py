# Multiprocessing start and end - the whole life cycles.

import logging
import multiprocessing
from multiprocessing import process

import time
import random


# Test function

def test(msg, num):
    name = process.current_process().name
    logging.info(f'Process starts: name = {name}')
    for x in range(num):
        logging.info(f'{name} is working')
        time.sleep(1)

    logging.info(f'Process finishs: name = {name}')


def main():
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')
    logging.info('Test Starting...')

    num = random.randrange(5, 12)
    p = multiprocessing.Process(target=test, args=('Working', num), daemon=True, name='Worker')
    p.start()

    logging.info('Do something on the main thread')
    time.sleep(5)

    if p.is_alive():
        p.terminate()
        p.join()
        # has to join !!! or no returning exitcode
    # exitcode == 0, good
    # anything else is error, force shutdown the process
    logging.info(f'Exitcode: {p.exitcode}')

    logging.info(f'Stopping {name} as {__name__}')
    logging.info('Test Finished')


# global the setting in case of version and hardware issues
logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

if __name__ == '__main__':
    main()
