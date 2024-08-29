import concurrent.futures
import time

def slow_function(n):
    """
    A slow function that takes 'n' seconds to complete.
    """
    time.sleep(n)
    return n

# Create a ThreadPoolExecutor with max_workers = 2
executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)

# Submit two tasks to the executor and get future objects
future1 = executor.submit(slow_function, 2)
future2 = executor.submit(slow_function, 3)

# Do some other work while the slow functions are running in the background

# Wait for the first future to complete and get the result
result1 = future1.result()

# Wait for the second future to complete and get the result
result2 = future2.result()

# Print the results
print("Result 1: ", result1)
print("Result 2: ", result2)

