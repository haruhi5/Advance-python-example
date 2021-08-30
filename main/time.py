import time
from threading import Timer


def display(msg):
    print(msg + '' + time.strftime('%H:%H:%S'))


def run_once():
    display('Run once:')
    t = Timer(5, display, ['Timeout:'])
    t.start()


run_once()
# notic this run immediatlly
# but it also only runs once
print('waiting...')
