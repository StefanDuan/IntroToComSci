def bsearch(s, e, first, last, calls=1):
    print first, last, calls
    if last - first < 2:
        return e == first or e == last
    mid = first + (last - first)/2
    if s[mid] == e:
        return True
    if s[mid] > e:
        return bsearch(s, e, first, mid-1, calls+1)
    else:
        return bsearch(s, e, mid+1, last, calls+1)

def search(s,e):
    print bsearch(s,e,0,len(s)-1)
    print 'Search complete'

def selSort(s):
    for i in range(len(s)-1):
        minIndex = i
        minVal = s[i]
        for j in range(i+1, len(s)):
            if s[j] < minVal:
                minVal = s[j]
                minIndex = j
        if minIndex != i:
            temp = s[i]
            s[i] = minVal
            s[minIndex] = temp
    return s

##def bubbleSort(L):
##    for j in range(len(s)):
##        for i in range(len(s)-1):
##            if L[i] > L[i+1]:
##                temp = L[i]
##                L[i] = L[i+1]
##                L[i+1] = temp
##        print L

def bubbleSort(L):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(s)-1):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
                swapped = True
        print L
