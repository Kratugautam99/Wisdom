class TreeNode:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
        self.both = f"{name}({designation})"
        self.children = []
        self.parent = None
    
    def getlvl(self):
        lvl =  0 
        p = self.parent
        while p:
            lvl +=1
            p = p.parent
        return lvl
    
    def depth(self, m=0):
        lvl = m
        max_depth = m
        for child in self.children:
            child_depth = child.depth(lvl + 1)
            max_depth = max(max_depth, child_depth)
        return max_depth

            
    def print_tree(self,val=None,n=0):
       if val == 'Designation':
           lvl = self.getlvl()
           prefix = ''
           if lvl == 0:
               spaces = ''
           else:
               prefix = '|--'
               spaces = '   ' * lvl
           print(spaces + prefix + self.designation)
           if self.children and n > 0:
              n -= 1
              for child in self.children:
                  child.print_tree(val,n)
       elif val == 'Name':
           lvl = self.getlvl()
           prefix = ''
           if lvl == 0:
               spaces = ''
           else:
               prefix = '|--'
               spaces = '   ' * lvl
           print(spaces + prefix + self.name)
           if self.children and n > 0:
              n -= 1
              for child in self.children:
                  child.print_tree(val,n)
       elif val == 'Both':
           lvl = self.getlvl()
           prefix = ''
           if lvl == 0:
               spaces = ''
           else:
               prefix = '|--'
               spaces = '   ' * lvl
           print(spaces + prefix + self.both)
           if self.children and n > 0:
               n -= 1
               for child in self.children:
                   child.print_tree(val,n)
                       
    def addchild(self,child):
        child.parent = self
        self.children.append(child)
 
def build_management_tree(n=100):
    lvl0 = TreeNode("Nilupul","CEO")
    lvl11 = TreeNode("Chinmay","CTO")
    lvl12 = TreeNode("Gels", "HR Head")
    lvl21 = TreeNode("Vishwa", "Infrastructure Head")
    lvl22 = TreeNode("Aamir", "Application Head")
    lvl23 = TreeNode("Peter", "Recruitment Manager")
    lvl24 = TreeNode("Waqas","Policy Manager")
    lvl31 = TreeNode("Dhaval", "Cloud Manager")
    lvl32 = TreeNode("Abhijit", "App Manager")
    lvl21.addchild(lvl31)
    lvl21.addchild(lvl32)
    lvl11.addchild(lvl21)
    lvl11.addchild(lvl22)
    lvl12.addchild(lvl23)
    lvl12.addchild(lvl24)
    lvl0.addchild(lvl11)
    lvl0.addchild(lvl12)
    if n == 100:
        n = lvl0.depth()
    print(n)
    print('\n')
    lvl0.print_tree('Both',n)
    print('\n')
    lvl0.print_tree('Designation',n)
    print('\n')
    lvl0.print_tree('Name',n)
build_management_tree()