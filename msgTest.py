from serverTest import msg_que_class

msgqueClass=msg_que_class()

msgQue=msgqueClass.get_msg_que()

while(True):
    if(not msgQue):
        print(msgQue.pop())
