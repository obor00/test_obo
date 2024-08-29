from time import sleep, perf_counter
from threading import Thread


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, *, daemon=None):
        #Thread.__init__(self, None, target, name, args, kwargs, daemon)
        Thread.__init__(self, None, target, name, args, kwargs)
        self._return = None

    def run(self):
        try:
            if self._target:
                self._return = self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs

    def join(self,timeout=None):
        Thread.join(self,timeout)
        return self._return


def task(id, tmout):
    print(f'Starting the task {id}...tmout {tmout}')
    sleep(tmout)
    print('done')


start_time = perf_counter()

# create and start 3 threads
threads = []
for n in range(1, 4):
    t = ThreadWithReturnValue(target=task, args=(n,n))
    threads.append(t)
    t.run()

# wait for the threads to complete
for t in threads:
    v = t.join()
    print('ret value = ' + v)

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')

