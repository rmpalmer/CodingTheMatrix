'''
Created on Sep 15, 2013

@author: rmp
'''

def list_dot(u,v):
    return sum([u[i]*v[i] for i in range(len(u))])

def dot_product_list(needle, haystack):
    s = len(needle)
    return [list_dot(needle, haystack[i:i+s]) for i in range(len(haystack)-s)]

if __name__ == '__main__':
    A = [1,2,3,4]
    B = [9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9]
    print (list_dot(A,B))
    x = dot_product_list(A, B)
    print(x)