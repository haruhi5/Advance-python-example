# Global Interpreter Lock
# automatically locks the multiple threads
# only one of them can reach the resource one time

import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random

# global resource estimation
counters = 0
counters_with_lock = 0


# Test function

def test(count):
    global counters, counters_with_lock
    s = random.randrange(1, 10)
    logging.info(f'Thread count-{count}: id = {threading.get_ident()} name = {threading.current_thread().getName()}')
    for x in range(count):
        logging.info(f'Count {threading.current_thread().getName()} += {count}')
        # inside the loop, it's a race condition
        counters += 1
        # locking
        lock = threading.Lock()
        lock.acquire()  # process the locking
        # # lock.acquire() # require twice from the same threads will cause the dead lock
        try:
            counters_with_lock += 1
        except:
            print('Error')
        finally:
            lock.release()
        # or use with lock, is also the same
        # with lock:
        #     logging.info(f'Lock for {threading.current_thread().getName()}')
        #     counters_with_lock += 1

    logging.info(f'Thread {count}: finished')


def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Test Starting...')

    workers = 2
    items = 4

    with ThreadPoolExecutor(max_workers=workers) as executor:
        for x in range(items):
            v = random.randrange(1, 10)
            executor.submit(test, v)
    print('counters: ', counters)
    print('counters with lock: ', counters_with_lock)
    logging.info('Test Finished')


if __name__ == '__main__':
    main()
