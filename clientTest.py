from multiprocessing.connection import Client

address = ('localhost', 6000)
conn = Client(address, authkey=b'secret password')

conn.send(['a', 2.5, "d"]) 
conn.send([1,2,34,4,5,6])

while(True):
    pass

#conn.send('close')
# conn.close()