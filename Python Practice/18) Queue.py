class Queue:
    def __init__(self):
        self.printer = []
    def Enqueue(self, val):
        self.printer.insert(0,val)
    def Dequeue(self):
        return print(self.printer.pop())
    def isempty(self):
        return len(self.printer) == 0
    def length(self):
        return len(self.printer)
 
# A = Queue()
# A.Enqueue(9)
# A.Enqueue(23)
# A.Enqueue(34)
# print(A.printer)
# A.Dequeue()   
# A.Dequeue()
# A.Dequeue()

from datetime import datetime
import threading
import time

class order:
    def __init__(self):
        self.printer = []
    def place(self):
        for i in range(5):
            o = input('\nEnter Name: ')
            p = input('Enter Order: ')
            q = datetime.now()
            t = q.strftime('%d-%m-%Y %H-%M-%S')
            val = dict()
            val['Name'] = o
            val['Order'] = p
            val['Date&Time'] = t
            self.printer.insert(0,val)
            time.sleep(2)
    def serve(self):
        print('\nNow Serving.....')
        while self.printer:
            time.sleep(4)
            print('\n',self.printer.pop(),sep='')

o = order()
t = time.time()

t1 = threading.Thread(target=o.place)
t1.start()
t1.join()
t2 = threading.Thread(target=o.serve)
t2.start()
t2.join()

print('\nTotal Time Taken (In Seconds):', time.time()-t)
print('Work Done')


