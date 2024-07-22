#For Both Duplication Allowed and Not Allowed
def shell_sort(raa):
    size = len(raa)
    gap = size//2
    while gap > 0:
        for i in range(gap,size):
            anchor = raa[i]
            j = i
            while j>=gap and raa[j-gap]>anchor:
                raa[j] = raa[j-gap]
                j-=gap
            raa[j] = anchor
        gap = gap//2
    return list(set(raa))
    
y = shell_sort(z:=[2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3])
print(f'Duplication Allowed: {z} \n\nDuplication Not Allowed: {y}')