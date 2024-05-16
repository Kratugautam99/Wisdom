# By Separate Chaining
class HashTable1:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False
        for idx,kv in enumerate(self.arr[h]):
            if kv[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx,kv in enumerate(self.arr[h]):
            if kv[0] == key:
                print('del',idx)
                del self.arr[h][idx]

#By Linear Probing
class HashTable2:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
    
    def get_hash(self,key):
        hash = 0
        for char in key:
            hash =+ ord(char)
        return hash % self.MAX
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_idx in prob_range:
            kv = self.arr[prob_idx]
            if kv is None:
                return
            if kv[0] == key:
                return kv[1]
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key,val)
        else:
            newh = self.find_slot(key,h)
            self.arr[newh] = (key,val)
            
    def get_prob_range(self,idx):
        return [*range(idx,len(self.arr))] + [*range(0,idx)]
 
    def find_slot(self,key,idx):
        prob_range = self.get_prob_range(idx)
        for prob_idx in prob_range:
            if self.arr[prob_idx] is None:
                return prob_idx
            if self.arr[prob_idx][0] == key:
                return prob_idx
        raise Exception('HashMap Full')
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_idx in prob_range:
            if self.arr[prob_idx] is None:
                return
            if self.arr[prob_idx][0] == key:
                self.arr[prob_idx] = None
        print(self.arr)
    
    
H = HashTable1()
I = HashTable2()
H['march 6'] = 66
H['march 17'] = 88
H['march 31'] = 99
H['march 1'] = 1
print(H.arr)
I['march 6'] = 66
I['march 17'] = 88
I['march 31'] = 99
I['march 1'] = 1
print(I.arr)

        
        