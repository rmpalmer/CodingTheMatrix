'''
Created on Sep 17, 2013

@author: rmp
'''
from downloads.vec import Vec, zero_vec

def list2vec(L):
    return Vec(set(range(len(L))), {i:L[i] for i in range(len(L))} )

def triangular_solver_n(rowlist,b):
    D = rowlist[0].D
    n = len(D)
    assert D == set(range(n))
    x = zero_vec(D)
    for i in reversed(range(n)):
        x[i] = (b[i] - rowlist[i] * x)/rowlist[i][i]
    return x

if __name__ == '__main__':
    rowlist = [list2vec([2,3,-4]),list2vec([0,1,2]),list2vec([0,0,5])]
    b = [10,3,15]
    x = triangular_solver_n(rowlist,b)
    print (x)