def merge(L1, L2):
    """Merge to sorted lists into a sorted list"""
    i = 0
    j = 0
    res = []
    while i<len(L1) and j<len(L2):
        if L1[i] < L2[j]:
            res.append(L1[i])
            i += 1
        else:
            res.append(L2[j])
            j += 1
    if i >= len(L1):
        res.extend(L2[j:])
    else:
        res.extend(L1[i:])
    return res

L1 = [2]
L2 = [1]
print merge(L1,L2)



def creat(smallest, largest):
    intSet = []
    for i in range(smallest, largest+1):
        intSet.append(None)
    return intSet

def insert(intSet, e):
    intSet[e] = 1

def member(intSet, e):
    return intSet[e] == 1


def readFloat(requestMsg, errorMsg):
    while True:
        val = raw_input(requestMsg)
        try:
            val = float(val)
            return val
        except:
            print(errorMsg)

def readVal(valType, requestMsg, errorMsg):
    while True:
        val = raw_input(requestMsg)
        try:
            val = valType(val)
            return val
        except:
            print(errorMsg)

#print readVal(int, 'Enter int: ', 'Not an int.')
