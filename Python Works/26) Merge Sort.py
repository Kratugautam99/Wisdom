def merge_sort(arr,key=None,desc=False):
    if len(arr) <= 1:
       return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left,key,desc)
    merge_sort(right,key,desc)
    merge_two_sorted_lists(left,right,arr,key)
    if desc == True and len(arr)>1:
       arr = arr[::-1]  
       return arr
    
def merge_two_sorted_lists(a,b,arr,key=None,desc=False):
    if key: 
        lena = len(a)
        lenb = len(b)
        i=j=k=0
        while i < lena and j < lenb:
            if a[i][key] <= b[j][key]:
                arr[k] = a[i]
                i+=1
            else:
                arr[k] = b[j]
                j+=1
            k+=1
        while i < lena:
            arr[k] = a[i]
            i+=1
            k+=1
        while j < lenb:
            arr[k] = b[j]
            j+=1
            k+=1
    if not key:
        lena = len(a)
        lenb = len(b)
        i=j=k=0
        while i < lena and j < lenb:
            if a[i] <= b[j]:
                arr[k] = a[i]
                i+=1
            else:
                arr[k] = b[j]
                j+=1
            k+=1
        while i < lena:
            arr[k] = a[i]
            i+=1
            k+=1
        while j < lenb:
            arr[k] = b[j]
            j+=1
            k+=1
    if desc == True:
       arr = arr[::-1]  
       return arr
   

test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

for arr in test_cases:
    print(arr:=merge_sort(arr,desc=True))
    
print('\n')
elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
]
print(ele:=merge_sort(elements,'time_hours',True))