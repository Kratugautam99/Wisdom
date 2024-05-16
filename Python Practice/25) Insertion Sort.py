# Less Optimal and Different Version
def insertion_sort_KG(ele):
    idx = 0
    while idx != len(ele):
        for i in range(0,idx):
            if ele[i] > ele[idx]:
                ele[i], ele[idx] = ele[idx], ele[i]
        idx += 1
    return ele

# More Optimal and Original version    
def insertion_sort_DP(ele):
    for i in range(1, len(ele)):
        anchor = ele[i]
        j = i - 1
        while j>=0 and anchor < ele[j]:
            ele[j+1] = ele[j]
            j = j - 1
        ele[j+1] = anchor
    return ele


# print(ele := insertion_sort_KG([15,37,25,27,28,30]))
# print(ele := insertion_sort_DP([15,37,25,27,28,30]))

def median_finder(ele):
    idx = 2
    arr = [float(ele[0])]
    while idx != len(ele)+1:
        sl = insertion_sort_DP(ele[:idx])
        if len(sl) % 2 == 0:
            m = sl[int(len(sl)/2)] + sl[int(len(sl)/2-1)]
            m = float(m/2)
        else:
            m = sl[int((len(sl)-1)/2)]
            m = float(m)
        arr.append(m)    
        idx += 1
    return arr

ele = median_finder([2,1,5,7,2,0,5])
for i in ele:
    print(i)