# Thread basics
# Move a function to multple threads
# Wait for all threads to complete

import logging
from threading import Thread
import time
import random

# Function to perform

def longtask(name):
    maxs = 10
    logging.info(f'Task: {name} performing {str(maxs)} times')
    for x in range(maxs):
        logging.info(f'Task {name}: {x}')
        time.sleep(random.randrange(1,3))
    logging.info(f'Task {name}: complete')

def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S',level=logging.DEBUG)
    logging.info('Starting...')
    # longtask('main')
    threads = []
    for x in range(10):
        t = Thread(target=longtask, args=['thread-' + str(x)])
        threads.append(t)
        t.start()
    # main threads waits until all threads finished
    for ts in threads:
        ts.join()
    logging.info('Finished all threads')

if __name__ == '__main__':
    main()