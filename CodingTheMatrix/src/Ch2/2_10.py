'''
Created on Sep 17, 2013

@author: rmp
'''
from downloads.vec import Vec

def list2vec(L):
    return Vec(set(range(len(L))), {i:L[i] for i in range(len(L))} )

if __name__ == '__main__':
    mylist = ['alpha','beta','gamma','delta']
    myvec = list2vec(mylist)
    print (myvec.f)