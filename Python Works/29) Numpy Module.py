import numpy as np
a = np.array([[1,2],[3,4],[5,6]], dtype=complex)
print(a.itemsize,a.dtype,a.ndim,a.shape,'\n',np.zeros((3,4)),'\n',np.linspace(1,5,9),'\n',a.reshape(2,3),'\n',a.ravel(),a.min(),a.max(),a.sum(),a.sum(axis=0),a.sum(axis=1),np.sqrt(a),np.std(a), a[1,1],a[0:2,1])
#you can also do cheap calc operations directly to list by numpy, a.dot(b)/np.dot(a,b) and np.cross(a,b) for dot and cross product respectively. 
for cell in np.nditer(a,order='F'):#or just a.flat/a.ravel()/a.flatten() for default of np.nditer(a,order='C'). Here,'C' is for rows and 'F' is for columns.
    print(cell)#for using more variety of np.nditer function you can search about flags.
print(b:=np.arange(6).reshape(3,2))
print(np.vstack((a,b)),'\n', np.hstack((a,b)))#v\hstack dtype will be of greater among a and b. learn v\h split it is just splitting instead of stacking nothing more.
print(c:= a>3,a[c])
a[c]=7
print(a)

