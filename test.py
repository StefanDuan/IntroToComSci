# - coding: utf-8 -

#def putchar(s):
#    index = len(s) - 1
#    while index >= 0:
#        print s[index]
#        index -= 1
#
#fruit = "abcdef"
#putchar(fruit)

##prefixes = "JKLMNOPQ"
##suffix_1 = "ack"
##suffix_2 = "uack"
##
##for letter in prefixes:
##    if letter in "OQ":
##        print letter + suffix_2
##    else:
##        print letter + suffix_1


# find the square root of perfect square
##x = 16
##ans = 0
##while ans*ans <= x:
##    ans += 1
##print ans

##fin = open('wordlist.txt', 'r')
##for line in fin:
##    word = line.strip()
##    if len(word)>20:
##        print word
##fin.close()

##def has_no_e(word):
##    return not('e' in word)

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

##fin = open('wordlist.txt', 'r')
##total = 0
##no_e = 0
##for line in fin:
##    word = line.strip()
##    total += 1
##    if has_no_e(word):
##        no_e += 1
##        print word, '  ',
##fin.close()
##print float(no_e)/float(total)

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

##fin = open('wordlist.txt', 'r')
##f_word = raw_input('Enter a string with forbidden letters:')
##no_forbidden = 0
##for line in fin:
##    word = line.strip()
##    if avoids(word, f_word):
##        no_forbidden += 1
##fin.close()
##print no_forbidden

def use_only(word, string):
    for letter in string:
        if letter in word:
            return True
    return False


