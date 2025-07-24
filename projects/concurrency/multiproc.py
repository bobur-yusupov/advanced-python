import multiprocessing
import time

"""
RESULT:

Task completed in 4.9360 seconds with result: 333333328333333350000000
Task completed in 7.2201 seconds with result: 333333328333333350000000
Sequential execution time: 12.1573 seconds

Task completed in 4.8349 seconds with result: 333333328333333350000000
Task completed in 4.9462 seconds with result: 333333328333333350000000
Multiprocessing execution time: 5.0915 seconds

"""

def cpu_bound_task(n):
    result = 0

    for i in range(n):
        result += i * i
    
    return result


def run_task(n):
    start_time = time.time()
    result = cpu_bound_task(n)
    end_time = time.time()

    print(f"Task completed in {end_time - start_time:.4f} seconds with result: {result}")


if __name__ == "__main__":
    n = 100000000

    start_time = time.time()
    run_task(n)
    run_task(n)
    end_time = time.time()
    print(f"Sequential execution time: {end_time - start_time:.4f} seconds\n")

    start_time = time.time()
    process1 = multiprocessing.Process(target=run_task, args=(n,))
    process2 = multiprocessing.Process(target=run_task, args=(n,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end_time = time.time()
    print(f"Multiprocessing execution time: {end_time - start_time:.4f} seconds")