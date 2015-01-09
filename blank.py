# -*- coding: utf-8 -*-
__author__ = 'wnduan'

# FILE_NAME = 'words.txt'
# def load_words(filename):
#     word_list = []
#     fin = open(filename,'r')
#     for line in fin:
#         word_list.append(line.strip().lower())
#     return word_list
#
# if __name__ == '__main__':
#     word_list = load_words(FILE_NAME)
#     for word in word_list:
#         if len(word) == 5:
#             print word

import random
w = []
v = []
for i in range(40):
    w.append(random.randint(1,9))
    v.append(random.randint(1,9))
print w
print v


