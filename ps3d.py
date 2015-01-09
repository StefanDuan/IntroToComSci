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

def constrainedMatchPair(firstMatch,secondMatch,length):
    res = ()
    m = length
    for n in firstMatch:
        for k in secondMatch:
            if n+m+1 == k and (not n in res):
                res = res + (n,)
    return res

def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers

def subStringMatchExactlyOneSub(target,key):
    matchExact = subStringMatchExact(target,key)
    matchOneSub = subStringMatchOneSub(key,target)
    res = ()
    for n in matchOneSub:
        if n not in matchExact:
            res = res + (n,)
    return res

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

# print subStringMatchOneSub(key12,target1)
print subStringMatchExactlyOneSub(target2,key11)