#####  Perform Various I/O operations using Python Code
#### MEENAKSHI
import sys

# 1.What is the output of the following code?
nums =set([1,1,2,3,3,3,4,4])
print(len(nums))
# Hint:Set consists unique element.
# ans: nums = [1,2,3,4] => length is 4

# 2.What will be the output?
d ={"john":40, "peter":45}
print(list(d.keys()))
# Hint: d.keys() is the function which will show keys.
# ans: d.keys() => ['john','peter']


# 3.A website requires a user to input username and password to register. Write a program to check the validity of password given by user.
# Following are the criteria for checking password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Hint: In case of input data being supplied to the question, it should be assumed to be a console input.

import sys
import re
def verify_password(pwd):
    try:
        # pwd = input('Enter the password: ')
        if not re.search('[a-z]',pwd):
            raise Exception('At least 1 letter between [a-z]')
        if not re.search('[A-Z]', pwd):
            raise Exception('At least 1 letter between [A-Z]')
        if not re.search('[0-9]', pwd):
            raise Exception('At least 1 number between [0-9]')
        if not re.search('[$#@]', pwd):
            raise Exception('At least 1 character from [$#@]')
        if len(pwd) <6:
            raise Exception('Minimum length of transaction password: 6')
        if len(pwd) >12:
            raise Exception('Maximum length of transaction password: 12')
    except Exception as e:
        raise Exception('Error: ',e)

# 4.Write a for loop that prints all elements of a list and their position in the list.
# a = [4,7,3,2,5,9]
# Hint: Use Loop to iterate through list elements.

def print_elements():
    try:
        a = [4, 7, 3, 2, 5, 9]
        for i,j in enumerate(a):
            print(j,'=>',i)
    except Exception as e:
        raise Exception('Error : ',e)

# 5.Please   write   a   program   which   accepts  a   string   from console   and   print   the characters that have even indexes.
# Example: If the following string is given as input to the program:H1e2l3l4o5w6o7r8l9d
# Then, the output of the program should be:Helloworld
#
def print_even_index(string):
    print(''.join([ j for i,j in enumerate(string) if i%2==0]))

# 6.Please write a program which accepts a string from console and print it in reverse order.
# Example: If the following string is given as input to the program: rise to vote sir
# Then, the output of the program should be:ris etov ot esir

def reverse_string(s):
    try:
        r = ''
        result = []
        for i in s[::-1]:
            tmp = ''
            for j in i:
                tmp = j + tmp
            result.append(tmp)
        print('reverse string is : ',' '.join(result))
    except Exception as e:
        raise Exception('Error : ',e)

# 7.Please write a program which count and print the numbers of each character in a string input by console.
# Example: If the following string is given as input to the program:abcdefgabc
# Then, the output of the program should be:a,2  c,2 b,2 e,1 d,1 g,1 f,1

def occurance(s):
    try:
        d = {}
        for i in s:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        print('\n'.join(['%s,%s' % (k,v) for k,v in d.items()]))
    except Exception as e:
        raise Exception('Error : ',e)

# or

def occurance1(s):
    try:
        d = {}
        for i in s:
            d[i] = d.get(i,0)+1
        print(d)
        print('\n'.join(['%s,%s' % (k,v) for k,v in d.items()]))
    except Exception as e:
        raise Exception('Error : ',e)

# 8.With   two   given   lists   [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],
# write   a program to make a list whose elements are intersection of the above given lists.

def intersection():
    try:
        l1 = [1,3,6,78,35,55]
        l2 = [12,24,35,24,88,120,155]
        s = set(l1) & set(l2)
        print(list(s))
    except Exception as e:
        raise Exception('Error : ',e)

# 9.Witha given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
def odered_reverse():
    try:
        l = [12,24,35,24,88,120,155,88,120,155]
        s = list(set(l))
        s.sort()
        print(s)
    except Exception as e:
        raise Exception('Error : ',e)
#
# 10.By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
def remove_from_list():
    try:
        l = [12,24,35,24,88,120,155]
        ele = 24
        # print([i for i in l if 24!=i])
        l1 =[]
        for i in l:
            if i in l1:
                l1.remove(i)
            elif i not in l1:
                l1.append(i)
        print(l1)
    except Exception as e:
        raise Exception('Error : ',e)

# 11.By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
def remove_element():
    try:
        l = [12,24,35,70,88,120,155]
        while True:
            rm = input(f'Enter index of the element to be removed from {l} : ')
            if not rm:
                return
            rm = int(rm)
            if rm < len(l):   #if rm in l:
                l.pop(rm)
                print(l)
            else:
                return
    except Exception as e:
        raise Exception('Error : ',e)
# 12. By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

def divisible_by_5_and_7():
    try:
        l = [12,24,35,70,88,120,155]
        print('original: ',l)
        for i in l:
            if i%5==0 and i%7==0:
                l.remove(i)
        print('after removal: ',l)
    except Exception as e:
        raise Exception('Error : ', e)

# 13.Please  write  a  program  to  randomly  generate  a  list  with  5  numbers,  which  are divisible by 5 and 7 , between 1 and 1000 inclusive.

import random
def random_divisible_by_5_and_7():
    return random.sample([i for i in range(1,1001) if i%5==0 and i%7==0],5)

# 14.Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a given  n  input  by console (n>0).
# Example:If the following n is given as input to the program:5 Then, the output of the program should be:3.55

def compute_n_by_n_plus_1():
    n = int(input('enter n value: '))
    tot = 0
    for i in range(1, n+1):
        tot += i / (i+1)
    print(round(tot,2))

if __name__ =='__main__':
    # pwd = sys.argv[1]
    # verify_password(pwd)
    #############
    # print_elements()
    #############
    # s = sys.argv[1]
    # print_even_index(s)
    # print_even_index('H1e2l3l4o5w6o7r8l9d')
    #############
    # s = sys.argv[1:]
    # reverse_string(s)
    # reverse_string('rise to vote sir')
    #############
    # s = sys.argv[1]
    # occurance(s)
    # occurance('abcdefgabc')
    # occurance1('abcdefgabc')
    #############
    # intersection()
    #############
    # odered_reverse()
    #############
    # remove_from_list()
    #############
    # remove_element()
    #############
    # divisible_by_5_and_7()
    #############
    # print(random_divisible_by_5_and_7())
    #############
    compute_n_by_n_plus_1()