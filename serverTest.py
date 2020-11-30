from multiprocessing.connection import Listener

address = ('localhost', 6000)     # family is deduced to be 'AF_INET'
listener = Listener(address, authkey=b'secret password')
conn = listener.accept()



msg_que=[]


class msg_que_class:
    def __init__(self):
        pass
    def get_msg_que(self):
        return msg_que


print('connection accepted from', listener.last_accepted)

while True:
    msg = conn.recv()

    print("gap")
    if msg == 'close':
        conn.close()
        break
    msg_que.append(msg)

    print(msg)



listener.close()