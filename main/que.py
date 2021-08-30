import logging
import threading
from threading import Thread, Timer
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import time
import random


# Test function

def test_que(name, que):
    threadname = threading.current_thread().getName()
    logging.info(f'Thread starts: id = {threading.get_ident()} name = {threadname}')
    t = random.randrange(1, 5)
    time.sleep(t)

    logging.info(f'Thread ends: id = {threading.get_ident()} name = {threadname}')

    ret = 'Hello ' + name + 'your random number is ' + str(t)
    que.put(ret)


def queued():
    que = Queue()
    t = Thread(target=test_que, args=['Bryan', que])
    t.start()
    logging.info('Do something on the main thread')
    for i in range(1,10):
        print(i)
    t.join()
    ret = que.get()
    logging.info(f'Returned: {ret}')

def test_future(name):
    threadname = threading.current_thread().getName()
    logging.info(f'Thread starts: id = {threading.get_ident()} name = {threadname}')
    t = random.randrange(10, 60)
    time.sleep(t)

    logging.info(f'Thread ends: id = {threading.get_ident()} name = {threadname}')

    ret = 'Hello ' + name + 'your random number is ' + str(t)
    return ret

def pooled():
    worker = 20
    ret = []
    with ThreadPoolExecutor(max_workers=worker) as executor:
        for x in range(worker):
            future = executor.submit(test_future,'Bryan'+str(x))
            ret.append(future)
            # equal to join
            # the main thread is just creating the new thread
        logging.info('Do something on the main thread')
        for i in range(1,10):
            print(i)
    for r in ret:
        logging.info(f'Returned: {r.result()}')

def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Test Starting...')

    #queued()
    pooled()

    logging.info('Test Finished')


if __name__ == '__main__':
    main()
