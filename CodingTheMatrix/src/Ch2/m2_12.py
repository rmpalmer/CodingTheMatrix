'''
Created on Sep 24, 2013

@author: rmp
'''

from m2_9 import list_dot

def policy_compare(sen_a, sen_b, voting_dict):
    sim = list_dot(voting_dict[sen_a], voting_dict[sen_b])
    return sim

def most_similar(sen, voting_dict):
    candidate = ""
    best = 0
    for item in voting_dict.items():
        name = item[0]
        if (name == sen):
            continue
        votes = item[1]
        sim = policy_compare(sen, name, voting_dict)
        #print(name, sim)
        if ((candidate == "") or (sim > best)):
            candidate = name
            best = sim
    return candidate
        
def least_similar(sen,voting_dict):
    candidate = ""
    best = 100
    for item in voting_dict.items():
        name = item[0]
        if (name == sen):
            continue
        votes = item[1]
        sim = policy_compare(sen, name, voting_dict)
        #print(name, sim)
        if ((candidate == "") or (sim < best)):
            candidate = name
            best = sim
    return candidate

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
    print(most_similar('Dole',voting_dict))
    print(least_similar('Dole',voting_dict))