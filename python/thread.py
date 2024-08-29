from time import sleep, perf_counter
from threading import Thread


def task(id, tmout):
    print(f'Starting the task {id}...tmout {tmout}')
    sleep(tmout)
    print('done')


start_time = perf_counter()

# create and start 3 threads
threads = []
for n in range(1, 4):
    t = Thread(target=task, args=(n,n))
    threads.append(t)
    t.start()

# wait for the threads to complete
for t in threads:
    t.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')

