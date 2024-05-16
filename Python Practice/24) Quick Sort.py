# implementation of quick sort in python using hoare partition scheme
def partition_hps(ele,start,end):
    pivotidx = start
    pivot = ele[pivotidx]
    while start < end:
        while start < len(ele) and ele[start] <= pivot:
            start += 1
        while ele[end] > pivot:
            end -= 1 
        if start < end:
            ele[start], ele[end] = ele[end], ele[start]
    ele[pivotidx], ele[end] = ele[end], ele[pivotidx]
    return end

def quick_sort_hps(ele,start,end):
    if start < end:
        pi = partition_hps(ele, start, end)
        quick_sort_hps(ele, start, pi-1)
        quick_sort_hps(ele, pi+1, end)

# implementation of quick sort in python using lomuto partition scheme
def partition_lps(ele, start, end):
    pivot = ele[end]
    pidx = start
    for i in range(start, end):
        if ele[i] <= pivot:
            ele[i], ele[pidx] = ele[pidx], ele[i]
            pidx += 1
    ele[pidx], ele[end] = ele[end], ele[pidx]
    return pidx

def quick_sort_lps(ele, start, end):
    if start < end:
        pidx = partition_lps(ele, start, end)
        quick_sort_lps(ele, start, pidx - 1)
        quick_sort_lps(ele, pidx + 1, end)
    
            
tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [6], []
        ]

for elements in tests:
    quick_sort_lps(elements, 0, len(elements)-1)
    print(f'sorted array by lps: {elements}')        
print('\n')
for elements in tests:
    quick_sort_hps(elements, 0, len(elements)-1)
    print(f'sorted array by hps: {elements}')        