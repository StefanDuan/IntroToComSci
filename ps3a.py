__author__ = 'wnduan'

import string

def countSubStringMatch(target,key):
    counter = 0
    index = 0
    while index != -1:
        index = string.find(target,key,index)
        if index != -1:
            counter += 1
            index += 1
    return counter

def countSubStringMatchRecursive(target,key):
    index = string.find(target,key)
    if index == -1:
        return 0
    else:
        return countSubStringMatchRecursive(target[index+1:],key) + 1

# target = "atgacatgcacaagtatgcatatgc"
# key = "atgc"
# print countSubStringMatch(target,key)
# print countSubStringMatchRecursive(target,key)
