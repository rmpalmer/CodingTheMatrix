'''
Created on Sep 14, 2013

@author: rmp
'''

from downloads.plotting import plot

def segment(pt1,pt2,n):
    return [(pt1[0] + (i/n)*(pt2[0]-pt1[0]),pt1[1]+(i/n)*(pt2[1]-pt1[1])) for i in range(n+1)]

if __name__ == '__main__':
    pt1 = [3.5,3]
    pt2 = [0.5, 1]
    seg = segment(pt1,pt2,10)
    print(seg)
    plot(seg,4)