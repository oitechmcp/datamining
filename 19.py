import multiprocessing as mp

def process_part(arr):
    return sum(x * x for x in arr)

if __name__ == '__main__':
    data = list(range(1, 101))
    mid = len(data) // 2
    part1, part2 = data[:mid], data[mid:]
    
    with mp.Pool(2) as pool:
        res1, res2 = pool.map(process_part, [part1, part2])
        
    print("Part 1 Result:", res1)
    print("Part 2 Result:", res2)
