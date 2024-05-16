def selection_sort(arr,key=None):
    if key:
        size = len(arr)
        for i in range(size-1):
            min_idx = i 
            for j in range(i+1,size):
                if arr[j][key] < arr[min_idx][key]:
                    min_idx = j
            if i != min_idx:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
    else:
        size = len(arr)
        for i in range(size-1):
            min_idx = i 
            for j in range(i+1,size):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            if i != min_idx:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]

Names = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]
selection_sort(Names,key='First Name')
print(Names)
selection_sort(Names,key='Last Name')
print(Names)

