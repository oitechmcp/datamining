import time
import multiprocessing as mp

def sum_part(arr):
    return sum(arr)

if __name__ == '__main__':
    numbers = list(range(10_000_000))
    
    t0 = time.time()
    seq_sum = sum(numbers)
    seq_time = time.time() - t0
    
    mid = len(numbers) // 2
    t0 = time.time()
    with mp.Pool(2) as pool:
        par_sum = sum(pool.map(sum_part, [numbers[:mid], numbers[mid:]]))
    par_time = time.time() - t0
    
    print(f"Sequential Time: {seq_time:.4f}s")
    print(f"Parallel Time:   {par_time:.4f}s")
