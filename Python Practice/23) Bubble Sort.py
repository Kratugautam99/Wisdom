def bubble_sort(ele, key):
    if key:
        size = len(ele)
        for i in range(size-1):
            swapped = False
            for j in range(size-1-i):
                if ele[j][key] > ele[j+1][key]:
                    tmp = ele[j]
                    ele[j] = ele[j+1]
                    ele[j+1] = tmp
                    swapped = True
            if not swapped:
                break
ele = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
bubble_sort(ele, 'transaction_amount')
print(ele)
    
