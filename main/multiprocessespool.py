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
        logging.info(f'{name} : {msg} = {num}')
        time.sleep(1)

    logging.info(f'Process finishs: name = {name}')
    return msg + ' is finished'


def proc_results(results):
    logging.info(f'Result: {results}')


def main():
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')
    logging.info('Test Starting...')

    maxs = 5
    pool = multiprocessing.Pool(maxs)
    result = []

    for x in range(maxs):
        msg = 'Item' + str(x)
        num = random.randrange(1, 5)
        r = pool.apply_async(func=test, args=(msg, num), callback=proc_results)
        # run at the same time? or just once create than directly run?
        result.append(r)

    logging.info('Do something on the main thread')
    for i in range(10):
        print(i)

    for r in result:
        r.wait()
    pool.close()
    pool.join()

    logging.info(f'Stopping {name} as {__name__}')
    logging.info('Test Finished')


# global the setting in case of version and hardware issues
logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

if __name__ == '__main__':
    main()
