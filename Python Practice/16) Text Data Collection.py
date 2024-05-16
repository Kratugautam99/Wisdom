import os
os.chdir('test Text')
print(os.getcwd())
with open('poem.txt','r') as p:
    po = p.read().replace(',','').replace('!','').replace(':','').replace(';','').replace('.','').lower().split('\n')
d = {}
for i in po:
    if i == '':
        po.remove(i)
    else:
        i = list(i.split(' '))
    for j in i:
        if j not in d:
            d[j] = 1
        else:
            d[j] += 1
print(po)
print(d)
