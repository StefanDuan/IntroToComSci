# -*- coding: utf-8 -*-
__author__ = 'wnduan'

# 数学中的排列组合问题在Python中有内置的运算模块itertools,可以import itertools，
# 然后其中的itertools.combinations(),itertools.combinations_with_replacement
# 还有itertools.permutations()三个函数可以用于计算组合，有重复的组合，以及排列问题。
# 但是作为学习，还是很希望能理解这些问题的算法。所以这里，以组合问题为例，来进行一个
# 讨论。

# 组合问题也就是从m个元素中，取出n个元素的问题表示为C(m,n)。首先，以一个简单的例子作为
# 切入点来写个函数。给定m=6个连续的整数（1,2,3,4,5,6），从中选出n=4个数组合。结果：
# 1,2,3,4
# 1,2,3,5
# 1,2,3,6
# ...
# 3,4,5,6
# 对于这样一个特定的问题，我们可以比较容易的实现：

def combNumberLoop4(m):
    """
    求解从m个整数中选出*4*个整数的组合问题。注意，只能解决m选4的问题。
    :param m: number of integer numbers，assume that m >= 4
    :return: a list of list, containing final results
    """
    res = [0,0,0,0]
    final_res = []
    for i in range(m-3):
        res[0] = i+1
        print i,res
        for j in range(i+1,m-2):
            res[1] = j+1
            print '\t',j,res
            for k in range(j+1,m-1):
                res[2] = k+1
                print '\t\t',k,res
                for l in range(k+1, m):
                    res[3] = l+1
                    final_res.append(res[:])
                    print '\t\t\t',l,res
    return final_res

# for e in combNumberLoop4(4):
#     print e

# 显然，上述算法并不具有普遍性，只能解决m选4的问题，对于n为其他数值的情形不适用。下一步，就是
# 要想办法找到一个更普遍的方法，对于给定的m，n可以得到相应的组合C(m,n)的结果。对于此问题，递归
# 是一个不错的方法，但是如何实现递归，主要有两个困难，就是递归参数的选取，还有递归中的循环如何实现。

def combNumberRecursive(m,n,container):
    """
    利用迭代来求解组合的问题
    :param m:
    :param n:
    :return:
    """
    if n > m or m==0:
        if n == 0:
            print container
        return
    else:
        container.append(m)
        combNumberRecursive(m-1,n-1,container)
        container.pop()
        combNumberRecursive(m-1,n,container)

combNumberRecursive(3,2,[])


# def combNumber(m, n, b, indent=''):
#     global totalNumberR
#     k = 1
#
#     for i in range(m, n-1, -1):
#         print indent, "Loop:", k
#         b[n-1] = i
#         if n-1>0:
#             print indent, "    Recursive with", i-1,n-1,b
#             combNumber(i-1,n-1,b,indent+'    ')
#         else:
#
#             print indent, '    ',b
#
#             totalNumberR += 1
#         k += 1
#
#
#     return totalNumberR
#
# group=[99,99,99,99,99]
# g2 = [99,99]
#
# totalNumberR = 0
#
# print "\nUsing Recursive: %d\n" % combNumber(4,2,group)





