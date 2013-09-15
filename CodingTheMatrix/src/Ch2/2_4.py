'''
Created on Sep 14, 2013

@author: rmp
'''

def addn(v,w):
    return [x+y for (x,y) in zip(v,w)]

if __name__ == '__main__':
    v = [1,2,3,4]
    w = [5,7,8,11]
    print(addn(v,w))