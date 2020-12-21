import threading
import time

x=8
y=0

def test():
    while True:
        print(x)

td=threading.Thread(target=test)

td.start()

time.sleep(2)

x=889

td.join()