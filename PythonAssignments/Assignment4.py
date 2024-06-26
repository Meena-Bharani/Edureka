# Module 4: Working with Modules and Handling Exceptions

# 1.A Robot moves in a Plane starting from the origin point (0,0). The robot can move UP, DOWN, LEFT, and RIGHT. The trace of Robot movement is as given following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# (The numbers after directions are steps)  Write a program to compute the current distance from the origin point after sequencing of movements.
# Hint:Use the math module.

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
# move_robot()

# 2.Data of XYZ company is stored in a sorted list. Write a program to search for specific data from that list.
# Hint:Use if/elif to deal with conditions.
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
# condition()

# 3.A weather forecasting organization wants to show whether it is day or night. Write a program to find whether is it dark outside or not based on the local system time.
# Hint:Use the time module.
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
# weather()

# 4.Write a program to find the distance between two locations when their latitude and longitudes are given.
# Hint:Use the math module.

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

# 5.Design a banking system software with options like cash withdrawal, cash credit,and change password.
# The software must display appropriate results based on user inputs.
# Hint:Use if else statements and functions.
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
# banking()

# 6.Write a prograthatch will find all numbers which are divisible by 7 but are not a multiple of 5, between 2,000 and 3,200(both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def divisible_7_not_multiple_5_2000_3200():
    lst =[]
    try:
        for i in range(2000,3501):
            if i%7==0 and i%5!=0:
                lst.append(str(i))
        print('Numbers obtained : ' ,','.join(lst))
    except Exception as e:
        raise Exception ('Error: ',e)

# 7.Write  a  prograthatch that can  compute  the  factorial of given  numbers.  Use recursion to find it.

def factorial(n):
    if n ==0 or n==1:
        return 1
    return n * factorial(n-1)

def findFactorial():
    n = int(input('Enter n value: '))
    f = factorial(n)
    print(f)
    return f
# 8.Write  a  program  that  calculates  and  prints  the value  according  to  the  given formula:Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30.D  is  the  variable  whose  values  should  be  input  to  your  program  in  a comma-separated sequence.
# Example Let  us  assume  the  following comma-separated input  sequence  is  given  to  the program:100,150,180 The output of the program should be:18,22,24
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

# 9.Write a program that takes 2 digits, X, Y as input and generates a 2-dimensional array. The element value in the ith row and jth column of the array should be i*j.
# Note:I =0,1,.., X-1; j=0,1,¡-Y-1.Example Suppose the following inputs are given to the program:3,5 Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

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

# 10.Write  a  program  that  accepts  a comma-separated sequence  of  words  as  input and  prints  the  words  in  a  comma-separated  sequence  after  sorting
# them alphabetically. Suppose the following input is supplied to the program: without,hello,bag,worldThen, the output should be:bag,hello,without,world

def sorting():
    tuples = input('Enter sequence of words: ')
    lst = list(tuples.split(','))
    lst.sort()
    print(','.join(lst))
    return ','.join(lst)

# 11.Write  a  program  that  accepts a sequence  of  lines  as  input  and  prints  the  lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:•Hello world•Practice makes perfect Then, the output should be:•HELLO WORLD•PRACTICE MAKES PERFECT

def make_upper():
    seq = input('Enter sequence of lines: ')
    print(seq.upper())
    return seq.upper()

# 12.Write  a  program  that  accepts  a  sequence  of whitespace-separated words  as input and prints the words after removing all duplicate words and sorting them
# alphanumerically. Suppose the following input is supplied to the program:hello world and practice makes perfect and hello world again Then,
# the output should be:again and hello makes perfect practice world

def remove_duplicate():
    inp = input('Enter whitespace-separated words: ')
    l = inp.split(' ')
    s = set(l)
    srt = sorted(s)
    print(' '.join(srt))
    return ' '.join(srt)

# 13.Write  a  program that accepts  a  sequence  of comma-separated 4-digit binary numbers as its input and then check whether they are divisible by 5 or not.
# The numbers  that  are  divisible  by  5  are  to  be  printed  in  a comma-separated sequence. Example 0100,0011,1010,1001 Then the output should be:1010

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


# 16.Case Study:
# Domain: Banking Marketing
# Focus: Optimization
# Business challenge/requirement: Bank of Portugal runs a marketing campaign to offer loans to clients.
# The loan is offered to only clients in selective professions. A list of successful campaigns (with client data) is given in the attached data set.
# You must come up with a program that reads the file and builds a set of unique profession lists.  Based on the given input professions of the client, the system tells whether the client is eligible to be approached for the marketing campaign.
#  Key issues: Tele Caller can only make x number of cold calls in a day. Hence to increase her effectiveness only eligible customers should be contacted.
#  Considerations :  The current system does not differentiate clients based on age and profession.
#  Data volume: 447 records in bank-data.csv
#  Additional information:-NA
#  Business benefits: The company can achieve between 15% to 20% higher conversion by targeting the right clients.
#  Approach to Solve: You must use the fundamentals of Python taught in Module 3.
#  1.Read file bank-data.csv
#  2.Build a set of unique jobs
#  3.Read the input from the command line –profession
#  4.Check if the profession is on the list
#  5.Print whether the client is eligible
# Enhancements for code: You can try these enhancements in code
# 1.Compute max and min age for loan eligibility based on data in csv file.
# 2.Store max and min age in the dictionary.
# 3.Make the professional check case insensitive.
# Currently program ends after the check. Take the input in the whileloop and end only if the user types "END" for profession

#  2.Name field contains full name –use a regular expression to separate title, first name, and last name
#  3.Store the data in Customer Class
#  4.Create Custom Exception –CustomerNotAllowedException
#  5.Pass a customer to function "create order" and throw CustomerNotAllowedException in case of black listed value is 1 Enhancements for code You can try these enhancements in code.
#  1.Change function createOrder to take product name and product code as input
#  2.Create Class OrderReturn object of type Order in case customer is eligible.

import csv
import os
class BankLoanOffer:
    def __init__(self,filename):
        try:
            # print('abspath: ',os.path.abspath(filename))
            # print('basename: ',os.path.basename(filename))
            # print('commonpath: ',os.path.commonpath(filename))
            # print('dirname: ',os.path.dirname(filename))
            # print('isfile: ',os.path.isfile(filename))
            # print('exists: ', os.path.exists(filename))
            # print('-----------')
            while True:
                jobs, age = [], []
                if os.path.isfile(filename) and os.path.exists(filename):
                    with open(filename,'r') as bank_data:
                        file = csv.DictReader(bank_data)
                        for data in file:
                            jobs = [i.lower() for i in list(set(data['job']))]
                            age = data['age']
                    if jobs and age:
                        prof = input('Enter profession to check the eligibility: ')
                        if prof.lower() == 'end':
                            return
                        if prof.lower() in jobs:
                            print(f'You are eligible since your profession is not in the list')
                        else:
                            print('You are not eligible since your profession is not in the list')
                        min_age = min(age)
                        max_age = max(age)
                        print(f'minimum age for loan eligibility is {min_age} and maximum age limit is {max_age}')
                        age_dict = {'min':min_age, 'max':max_age}
                        print(age_dict)
        except Exception as e:
            raise Exception('Error: ',e)

# Domain: E-Commerce
# Focus: Optimization
# Business challenge/requirement: GoodsKart—the largest e-commerce company in Indonesia, with revenue of $2B+ has acquired another e-commerce company FairDeal.  FairDeal has its own IT system to maintain the records of customers, sales, and so on. For ease of maintenance and cost savings, GoodsKartis integrating customer databases of both organizations hence customer data of FairDeal must be converted into GoodsKart customer data format.
# Key issues: GoodsKart customer data has more fields than in FairDeal customer data. Hence FairDeal data needs to be split and stored in GoodsKart Customer Object-Oriented Data Structure.
# Considerations: The system should convert the data at run time.
# Data volume-NA
# Additional information:-NA
# Business benefits: GoodsKart can eventually restructure the IT systems of FairDeal and reduce its cost by 20-30%
# Approach to Solve: You must use the fundamentals of Python taught in Module 3.
# 1.Read FairDealCustomerData.csv
# 2.Name field contains full name –use a regular expression to separate title, first name, and last name
# 3.Store the data in Customer Class
# 4.Create Custom Exception –CustomerNotAllowedException
# 5.Pass a customer to function "create order" and throw CustomerNotAllowedException in case of blacklisted value is 1
# Enhancements for codeYou can try these enhancements in code.
# 1.Change function createOrder to take productname and product code as input
# 2.Create Class Order
# Return object of type Order in case customer is eligible.

import csv
import os

class CustomerNotAllowedException(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return repr(self.value)
class Customer:
    # def __init__(self, owner, title, fname, lname, isblacklisted):
    #     self.owner = owner
    #     self.title = title
    #     self.fname = fname
    #     self.lname = lname
    #     self.isblacklisted = isblacklisted

    def __init__(self, owner, name, isblacklisted):
        self.owner = str(owner.strip())
        title,fname,*lname = name.strip().split(' ')
        self.title = str(title.strip())
        self.fname = str(fname.strip())
        self.lname = str(lname[0]) if len(lname)>0 else ''
        self.isblacklisted = int(isblacklisted)

    def __str__(self):
        return f'Owner : {self.owner} Customer: {self.title} {self.fname} {self.lname}  BlickListed: {self.isblacklisted}'

    # def __get__(self, instance, owner):
    #     print(instance.owner)
    #     return getattr(instance, self.fname)
class Order:
    def __init__(self, pname, pcode):
        self.pname = pname
        self.pcode = pcode

    def __str__(self):
        return f'Product name is {self.pname} and product code is {self.pcode}'

def createOrder(customer):
    try:
        if len(customer)>0:
            for i in customer:
                if int(i.isblacklisted) ==0:
                    raise CustomerNotAllowedException(f'Customer {i} is not allowed')
                else:
                    print(f'Customer {i} is allowed')
                    pname = input('Enter Product Name: ')
                    pcode = input('Enter Product Code: ')
                    ord = Order(pname,pcode)
                    print(ord)
                    return ord
    except CustomerNotAllowedException as e:
        print(e)
    except Exception as e:
        print('Error: ', e)
def readCSVFile(file_name):
    try:
        fpath = os.path.abspath(file_name)
        if os.path.exists(fpath):
            customers_from_excel = list(csv.reader(open(fpath)))
            customer_objects = [Customer(*cust) for cust in customers_from_excel]
            # print(len(customer_objects))
            # print(customer_objects)
            owner = input('Enter owner name to check for blacklisted: ')
            # name = input('Enter full name to check for blacklisted: ')
            customer_obj = [ cust for cust in customer_objects if str(cust.owner)==str(owner) ] #and ' '.join(cust.title+cust.fname+cust.lname) == str(name.strip()) ]
            if len(customer_obj) >0:
                createOrder(customer_obj)
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        fpath = os.path.abspath(file_name)
        print('Error: File not found in the path ',fpath)
    except Exception as e:
        print('Error: ',e)

# readCSVFile('FairDealCustomerData.csv')

if __name__== '__main__':
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

    # math_library_example()

    # bl = BankLoanOffer('bank-data.csv')
    readCSVFile('FairDealCustomerData.csv')