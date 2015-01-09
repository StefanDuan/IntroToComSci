__author__ = 'wnduan'

import string

def subStringMatchExact(target,key):
    index = 0
    res = ()
    while index != -1:
        index = string.find(target,key,index)
        if index != -1:
            res = res + (index,)
            index += 1
    return res

print subStringMatchExact("atgacatgcacaagtatgcat","atgc")
print "Starting Test..."
target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'
key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'
print subStringMatchExact(target1,key10)
print subStringMatchExact(target2,key10)
print subStringMatchExact(target1,key11)
print subStringMatchExact(target2,key11)
print subStringMatchExact(target1,key12)
print subStringMatchExact(target2,key12)
print subStringMatchExact(target1,key13)
print subStringMatchExact(target2,key13)
print "End of Test"