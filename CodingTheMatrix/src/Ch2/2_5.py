'''
Created on Sep 14, 2013

@author: rmp
'''

def scalar_vector_mult(alpha, v):
    return [alpha*v[i] for i in range(len(v))]

if __name__ == '__main__':
    v = [2,4,6,8,9,7,5,3,1]
    print(scalar_vector_mult(3.4, v))