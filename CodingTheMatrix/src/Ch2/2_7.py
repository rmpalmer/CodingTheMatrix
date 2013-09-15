'''
Created on Sep 15, 2013

@author: rmp
'''

from downloads.vec import Vec

def zero_vec(D): return Vec(D,{})

def setitem(v,d,val): v.f[d] = val

def getitem(v,d):
    if d in v.f:
        return v.f[d]
    else:
        return 0
    
def scalar_mul(v, alpha):
    return Vec(v.D,{d:alpha*value for d,value in v.f.items()})

def add(u,v):
    return Vec(u.D, {d:getitem(u,d)+getitem(v,d) for d in u.D})

def neg(v):
    return Vec(v.D, {key:-value for key, value in v.f.items()})

if __name__ == '__main__':
    my_domain = {'a','b','c','d','e','f'}
    zv = zero_vec(my_domain)
    print(zv.f)
    setitem(zv,'c',3)
    print(getitem(zv,'c'))
    print(getitem(zv,'d'))
    setitem(zv,'d',4)
    print(getitem(zv,'d'))
    print(zv.f)
    scv = scalar_mul(zv, 1.5)
    print(getitem(scv, 'c'))
    ncv = neg(scv)
    