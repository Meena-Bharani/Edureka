# Module3–Functions, OOPs, Modulesin Python
# Case Study
# 11.A Robot moves in a Plane starting from the origin point (0,0). The robot can move toward UP, DOWN, LEFT, RIGHT. The trace of Robot movement is as given following:UP 5DOWN 3LEFT 3RIGHT 2The numbers after directions are steps.  Write a program to compute the distance current position after sequence of movements.Hint: Use math module.
def move_robot():
    try:
        pos = (0,0)
        lst = list(pos)
        while True:
            inp = str(input('Enter (position: UP-5, Down-7, Left-3, Right-2) (position,steps) : '))
            if not inp:
                break
            direction,steps = inp.split(',')
            d = int(direction)
            s = int(steps)
            if d == 5:
                lst[1] += s
            elif d==3:
                lst[0] -= s
            elif d==7:
                lst[1] -= s
            elif d==2:
                lst[0] += s
            else:
                pass
        print(lst)
    except Exception as e:
        raise Exception ('Error: ',e)

# 2.Data of XYZ company is stored in sorted list. Write a program for searching specific data from that list.Hint: Use if/elif to deal with conditions.
def condition():
    try:
        l = [1,2,3,4,5,6,7]
        l = sorted(l)
        data = 5
        if data in l:
            print(f'{data} found in the list')
            return True
        print(f'{data} not found in the list')
        return False
    except Exception as e:
        raise Exception('Error: ', e)

# 3.Weather forecasting organization wants to show is it day or night. So, write a program for such organization to findwhether is it dark outside or not.Hint: Use time module.
import time
def weather():
    try:
        tm = time.time()
        ltm = time.localtime(tm)
        print(f'Current time is {time.ctime(tm)}')
        if ltm.tm_hour >=6 and ltm.tm_hour <=17:
            print('It is day time')
            # return 'day'
        print('It is night time')
        # return 'night'
    except Exception as e:
        raise Exception('Error: ',e)

# 4.Write a program to find distancebetween two locations when their latitude and longitudes are given.Hint: Use math module.
# d = sqrt((x2-x1)**2 + (y2-y1)**2)
from math import sqrt, sin, cos , atan2, radians,acos, asin
def distance_ll():
    try:
        # 37.30287723453196, -121.97930713145826
        # Latitude1 = radians(37.30287723453196)
        # Longitude1 = radians(-121.97930713145826)
        #
        # # 37.3028740294792, -122.02343293256278
        # Latitude2 = radians(37.3028740294792)
        # Longitude2 = radians(-122.02343293256278)
        loc1 = str(input('Enter Latitude1,Longitude1:'))
        loc2 = str(input('Enter Latitude2,Longitude2:'))
        if not loc1 or not loc2:
            return
        print(loc1,loc2)
        Latitude1,Longitude1 = loc1.split(',')
        Latitude2,Longitude2 = loc2.split(',')
        Latitude1 = radians(float(Latitude1))
        Longitude1 = radians(float(Longitude1))
        Latitude2 = radians(float(Latitude2))
        Longitude2 = radians(float(Longitude2))
        Latitude = Latitude2 - Latitude1
        Longitude = Longitude2 - Longitude1

        R = 6371.0

        # formula  sqrt(sin ((l2-l1)/2)^2 + cos(lat2) * cos(lat1) * sin((lon2-lon1)/2)^2
        dist = pow(sin(Latitude/2),2) + cos(Latitude2) * cos(Latitude1) * pow(sin(Longitude/2),2)
        c = 2 * asin(sqrt(dist))
        # dist = sin(Latitude1) * sin(Latitude2) + cos(Latitude1) * cos(Latitude2) * cos(Longitude1 - Longitude2)
        # c = R * acos(dist)
        # c = 2 * atan2(sqrt(dist), sqrt(1-dist))
        distance = R * c
        print('Distance is ',distance)
        return distance
    except Exception as e:
        raise Exception('Error: ',e)

# distance_ll((37.30287723453196, -121.97930713145826), (37.3028740294792, -122.02343293256278))


# 5.Design a software for bank system. There should be options like cash withdraw, cash credit and change password. According to user input, the software should provide required output.Hint: Use if else statements and functions.
def banking():
    try:
        print('1. cash withdrawal')
        print('2. cash credit')
        print('3. change password')
        opt = int(input('choose an option '))
        if opt ==1:
            print('Cash withdrawal')
            return
        elif opt ==2:
            print('Cash credit')
            return
        elif opt ==3:
            print('change password')
            return
        return
    except Exception as e:
        raise Exception('Error: ',e)

# 6.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
#
def divisible_7_not_multiple_5_2000_3200():
    lst =[]
    try:
        for i in range(2000,3501):
            if i%7==0 and i%5!=0:
                lst.append(str(i))
        print('Numbers obtained : ' ,','.join(lst))
    except Exception as e:
        raise Exception ('Error: ',e)

# 7.Write a program which can compute the factorial of a given numbers. Use recursion to find it. Hint: Suppose the following input is supplied to the program:8Then, the output should be:40320
def factorial(n):
    if n ==0 or n==1:
        return 1
    return n * factorial(n-1)

def findFactorial():
    n = int(input('Enter n value: '))
    f = factorial(n)
    print(f)
    return f

# 8.Write a program that calculates and prints the value according to the given formula:Q = Square root of [(2 * C * D)/H]Following are the fixed values of C and H: C is 50. H is 30.D  is  the  variable  whose  values  should  be  input  to  your  program  in  a  comma-separated sequence. Example:Let  us  assume  the  following  comma  separated  input  sequence  is  given  to  the program:100,150,180The output of the program should be:18,22,24
from math import sqrt
def calculate():
    try:
        D = input('Enter multiple values in \',\' : ')
        C,H = 50, 30
        result = []
        if D:
            for i in D.split(','):
                print(i)
                formula = sqrt((2 * C * int(i)) / H)
                result.append(str(int(formula)))
            print('Output: ',','.join(result))
        return result
    except Exception as e:
        raise Exception('Error: ',e)

# 9.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.Note: i=0,1.., X-1; j=0,1,¡-Y-1.Example:Suppose the following inputs are given to the program:3,5Then, the output of the program should be:[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
def two_dimentional():
    m = int(input('Enter row value: '))
    n = int(input('Enter column value: '))
    dim =[]
    for i in range(m):
        col = []
        for j in range(n):
            col.append(int(input(f'Enter value for [{i},{j}] :')))
        dim.append(col)
    # for i in m:
    print(dim)
    return dim

# 10.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically. Suppose the following input is supplied to the program:without,hello,bag,worldThen, the output should be:bag,hello,without,world
def sorting():
    tuples = input('Enter sequence of words: ')
    lst = list(tuples.split(','))
    lst.sort()
    print(','.join(lst))
    return ','.join(lst)

# 11.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. Suppose the following input is supplied to the program:Hello worldPractice makes perfectThen, the output should be:HELLO WORLDPRACTICE MAKES PERFECT
def make_upper():
    seq = input('Enter sequence of lines: ')
    print(seq.upper())
    return seq.upper()

# 12.Write a program that accepts a sequence of whitespace separated words as input and   prints   the   words   after   removing   all   duplicate   words   and   sorting   them alphanumerically. Suppose the following input is supplied to the program:hello world and practice makes perfect and hello world againThen, the output should be:again and hello makes perfect practice world
def remove_duplicate():
    inp = input('Enter whitespace-separated words: ')
    l = inp.split(' ')
    s = set(l)
    srt = sorted(s)
    print(' '.join(srt))
    return ' '.join(srt)

# 13.Write  a  program  which  accepts  a  sequence  of  comma  separated  4  digit  binary numbers  as  its  input  and  then  check  whether  they  are  divisible  by  5  or  not.  The numbers that are divisible by 5 are to be printed in a comma separated sequence.
def binary_divisible_by_5():
    seq = input('Enter sequence  of comma-separated 4-digit binary numbers: ')
    divisible_by_5 = []
    binary_list = seq.split(',')
    for i in binary_list:
        i = int(i)
        ### convert binary to digit
        if i % 5 ==0:
            divisible_by_5.append(i)
    print(','.join(divisible_by_5))
    return ','.join(divisible_by_5)


# 14.Write a program that accepts a sentence and calculate the number of upper-case letters and lower-case letters. Suppose the following input is
# supplied to the program:Hello world! Then, the output should be:UPPER CASE 1 LOWER CASE 9

import re
class find_case:
    def __init__(self,sentence):
        self.upper = len(re.findall('[A-Z]',sentence))
        self.lower = len(re.findall('[a-z]',sentence))

    def __str__(self):
        return f'Upper case {self.upper} and Lower case {self.lower}'

# 15.Give an example of fsum and sum function of math library.

import math
def math_library_example():
    inp = list(map(int,input('Enter sequence of numbers to find sum: (ex: 1,2,3) :').strip().split(',')))
    print(math.fsum(inp))
    print(sum(inp))

if __name__ =='__main__':
    # move_robot()
    # condition()
    # weather()
    # distance_ll()
    # banking()
    # divisible_7_not_multiple_5_2000_3200()
    # findFactorial()
    # calculate()
    # two_dimentional()
    # sorting()
    # make_upper()
    # remove_duplicate()

    # sentence = input('Enter a sentence to count upper and lower cases: ')
    # f = find_case(sentence)
    # print(str(f))

    math_library_example()

