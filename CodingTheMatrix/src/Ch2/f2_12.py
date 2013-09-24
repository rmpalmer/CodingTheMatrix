'''
Created on Sep 24, 2013

@author: rmp
'''

def create_voting_dict(strlist):
    d = {}
    for i in range(len(strlist)):
        record = strlist[i].split()
        name = record[0]
        votes = record[3:]
        d[name] = [int(x) for x in votes]
    return d

if __name__ == '__main__':
    f = open("voting_record_dump109.txt")
    mylist = list(f)
    voting_dict = create_voting_dict(mylist)
    print(voting_dict['Gregg'])