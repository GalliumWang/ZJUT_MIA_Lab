from multiprocessing.connection import Listener
import logging
import threading
import time

address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
listener = Listener(address, authkey=b'secret password')
conn = listener.accept()

msg_que=[]


#FIXME:archived
# class msg_que_class:
#     def __init__(self):
#         pass
#     def get_msg_que(self):
#         return msg_que

def listenerLaucher():
    global msg_que
    print('connection accepted from', listener.last_accepted)
    while True:
        msg = conn.recv()

        print("gap")
        if msg == 'close':
            conn.close()
            break
        msg_que.append(msg)
        #print(msg)
        listener.close()


x=threading.Thread(target=listenerLaucher)
x.start()

while(True):
    if(msg_que):
        print(msg_que.pop())



