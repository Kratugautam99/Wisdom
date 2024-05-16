class BSTN:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None
        
    def addchild(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                return self.left.addchild(data)
            else:
                self.left = BSTN(data) 
        if data > self.data:
            if self.right:
                return self.right.addchild(data)
            else:
                self.right = BSTN(data)
                
    def search(self,val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements
        
    def calc_sum(self):
        sum = 0
        sum += self.data
        if self.left:
            sum += self.left.calc_sum()
        if self.right:
            sum += self.right.calc_sum()
        return sum
    
    def max_BST(self):
        if self.right:
            return self.right.max_BST()
        else:
            return self.data
        
    def min_BST(self):
        if self.left:
            return self.left.min_BST()
        else:
            return self.data
        
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            # minv = self.right.min_BST()
            # self.data = minv
            # self.right = self.right.delete(minv)
            maxv = self.left.max_BST()
            self.data = maxv
            self.left = self.left.delete(maxv)
        return self
    
        
    
def build_BST(elements):
    print('Building Tree with These Elements:',elements)
    root = BSTN(elements[0])
    for i in range(1,len(elements)):
        root.addchild(elements[i])
    return root

#The Input of the build_BST will be considered as pre_order_traversal of it according to code.
A = build_BST([15,12,7,14,27,20,23,88]).post_order_traversal()
print(A)  

    