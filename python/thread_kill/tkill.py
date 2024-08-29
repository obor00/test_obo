import threading
import ctypes
import time

class thread_with_exception(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self._continue = True

    def run(self):

        # target function of the thread class
        try:
            while self._continue:
                print('running ' + self.name)
                time.sleep(1)
        finally:
            print('ended')

    def get_id(self):

        # returns id of the respective thread
        #if hasattr(self, '_thread_id'):
        #    return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
        print ("thread id not found")

    def raise_exception(self):
        print("exception raised, thread id=" + str(self.get_id()))
        self._continue = False

print(threading._active.items())
t1 = thread_with_exception('Thread 1')
t1.start()
print(threading._active.items())
time.sleep(3)
t1.raise_exception()
t1.join()
print("end of join")
