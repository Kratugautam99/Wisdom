import time

def time_it(fx):
    def mfx(*args, **kwargs):
        start = time.perf_counter()
        result = fx(*args, **kwargs)
        end = time.perf_counter()
        print(f"{fx.__name__} ran in: {end - start} sec and resulted in {result}")
        return result
    return mfx

@time_it
def linear_search(listn,findn):
    idxs = []
    for idx, ele in enumerate((listn)):
        if ele == findn:
            idxs.append(idx)
    if idxs:
        return idxs
    return -1
@time_it
def binary_search(listn,findn):
    left_idx = 0
    right_idx = len(listn)-1
    mid_idx = -1
    idxs = []
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx)//2
        mid_no = listn[mid_idx]
        if mid_no == findn:
            idxs.append(mid_idx)
        if mid_no > findn:
            right_idx = mid_idx - 1
        else:
            left_idx = mid_idx + 1
    left_idx = 0
    right_idx = len(listn)-1
    mid_idx = -1
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx)//2
        mid_no = listn[mid_idx]
        if mid_no == findn:
            idxs.append(mid_idx)
        if mid_no < findn:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1
    idxs = set(idxs)
    idxs = list(idxs)
    if idxs:
        return idxs
    return -1
listn = [1,4,6,9,11,15,15,15,17,21,34,34,56]
findn = 15
idxs1 = linear_search(listn, findn)
idxs2 = binary_search(listn, findn)
listn = [i for i in range(45678980)]
findn = 3456729
idxs1 = linear_search(listn, findn)
idxs2 = binary_search(listn, findn)