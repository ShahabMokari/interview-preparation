import logging
import threading
import time

logging.basicConfig(
		level = logging.DEBUG,
		format ='[%(levelname)s] (%(threadName)-10s) % (message)s',
		)
def worker():
	print threading.currentThread().getName(), 'Starting'
	time.sleep(2)
	print threading.currentThread().getName(), 'Exiting'

def my_service():
	print threading.currentThread().getName(), 'Starting'
	time.sleep(3)
	print threading.currentThread().getName(), 'Existing'

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)

w.start()
w2.start()
t.start()

