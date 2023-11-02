
import threading
from time import sleep

class first_thread(threading.Thread):
    def run(self):
        for i in range(10):
            print('1st thread', i)
            sleep(4)

class second_thread(threading.Thread):
    def run(self):
        for i in range(10):
            print('2nd thread', i)
            sleep(4)

class third_thread(threading.Thread):
    def run(self):
        for i in range(10):
            print('3rd thread', i)
            sleep(4)

class fourth_thread(threading.Thread):
    def run(self):
        for i in range(10):
            print('4th thread', i)
            sleep(4)


t1 = first_thread()
t2 = second_thread()
t3 = third_thread()
t4 = fourth_thread()


t1.start()
sleep(1)
t2.start()
sleep(1)
t3.start()
sleep(1)
t4.start()
