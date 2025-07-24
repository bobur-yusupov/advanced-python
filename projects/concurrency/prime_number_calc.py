import multiprocessing
import time

def is_prime(n) -> bool:
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 2:
            return False
    
    return True

def prime_number_list(n):
    prime_list = []

    for i in range(n + 1):
        if is_prime(i):
            prime_list.append(i)

    return prime_list

def calculate_prime_sum(n) -> int:
    prime_list = prime_number_list(n)
    result = 0

    for number in prime_list:
        result += number
    
    return result

def run_task(n):
    start_time = time.time()
    result = calculate_prime_sum(n)
    end_time = time.time()

    print(f"Task completed in {end_time - start_time:.4f} seconds with result: {result}")

if __name__ == "__main__":
    n = 1000000
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


"""
RESULT:

Task completed in 5.6842 seconds with result: 57379114500
Task completed in 5.6384 seconds with result: 57379114500
Sequential execution time: 11.3230 seconds

Task completed in 6.3811 seconds with result: 57379114500
Task completed in 6.4033 seconds with result: 57379114500
Multiprocessing execution time: 6.6177 seconds

"""