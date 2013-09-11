'''
Created on Sep 10, 2013

@author: rmp
'''

def my_filter(L, num):
    return [x for x in L if (x%num) != 0]

def my_lists(L):
    return [list(range(1,x+1)) for x in L]

def my_function_composition(f,g):
    return {k:g[f[k]] for k in f.keys()}

def mySum(L):
    current = 0
    for x in L:
        current = current + x
    return current

def myProduct(L):
    current = 1
    for x in L:
        current = current * x
    return current

def myMin(L):
    current = ...
    for x in L:
        if (current == ...):
            current = x
        elif (x < current):
            current = x
    return current

def myConcat(L):
    current = ...
    for x in L:
        if (current == ...):
            current = x
        else:
            current = current + x
    return current

def myUnion(L):
    current = ...
    for x in L:
        if (current == ...):
            current = x
        else:
            current = current | x
    return current

if __name__ == '__main__':
    print('paragraph 1.7')
    print('1.7.1')
    mylist = [11,8,2,5]
    print (my_filter(mylist, 5))
    print('1.7.2')
    print(my_lists(mylist))
    print('1.7.3')
    myf = {'a':1, 'b':2, 'c':3, 'd':4}
    myg = {1:'alpha', 2:'beta', 3:'gamma', 4:'delta'}
    print(my_function_composition(myf,myg))
    print('1.7.4')
    print(mySum(mylist))
    print('1.7.5')
    print(myProduct(mylist))
    print('1.7.6')
    print(myMin(mylist))
    print('1.7.7')
    mystrings = ['foo','bar','hello','goodbye']
    print(myConcat(mystrings))
    print('1.7.8')
    mysets = [{1,5,6},{1,7,9},{11,5,7}]
    print(mysets)
    print(myUnion(mysets))