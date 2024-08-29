
import time
import concurrent.futures
import subprocess

def wait_on_b():
    ret=subprocess.run(['ls', '/sfdsf'], check=False)
    print('hello B')
    return ret

def wait_on_a():
    time.sleep(2)
    print('hello A')
    return 'A, sleep 2'

def wait_on_future():
    f = executor.submit(pow, 5, 2)
    # This will never complete because there is only one worker thread and
    # it is executing this function.
    print(f.result())

executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
b = executor.submit(wait_on_b)
a = executor.submit(wait_on_a)

executor.shutdown(wait=True)
print(b.result())
print(a.result())
