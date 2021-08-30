import logging
import multiprocessing
import threading
from multiprocessing import process
import asyncio
import time
import random


# Test function

def display_m(msg):
    threadname = threading.current_thread().name
    processname = process.current_process().name
    logging.info(f'{processname}-{threadname}: {msg}')


async def work(name):
    display_m('Starting' + name)
    # Do something
    await asyncio.sleep(random.randint(1, 10))
    display_m('Ending' + name)


async def run_async(maxs):
    tasks = []
    for x in range(maxs):
        name = 'Item ' + str(x)
        tasks.append(asyncio.ensure_future(work(name)))
    await asyncio.gather(*tasks)


def main():
    mainname = process.current_process().name
    logging.info(f'Running {mainname} as {__name__}')
    logging.info('Test Starting...')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_async(50))
    loop.close()

    # logging.info('Do something on the main thread')
    # for i in range(10):
    #     print(i)

    logging.info(f'Stopping {mainname} as {__name__}')
    logging.info('Test Finished')


# global the setting in case of version and hardware issues
logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

if __name__ == '__main__':
    main()
