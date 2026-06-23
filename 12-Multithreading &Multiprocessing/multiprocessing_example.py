## PRocesses that run in parallel
### CPU-Bound Tasks-Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing).
## PArallel execution- Multiple cores of the CPU

import multiprocessing

import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'square: {i*i}')

def cube_number():
    for i in range(5):
        time.sleep(1.5)
        print(f'cube: {i*i*i}')

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_number)
    t = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    
    finished_time = time.time()-t
    print(finished_time)
    
    