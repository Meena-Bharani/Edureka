
# Domain: E-Commerce
# Focus: Optimization
# Business challenge/requirement: GoodsKart—the largest e-commerce company in Indonesia, with revenue of $2B+ has acquired another e-commerce company FairDeal.
# FairDeal has its own IT system to maintain the records of customers, sales, and so on. For ease of maintenance and cost savings, GoodsKartis integrating customer
# databases of both organizations hence customer data of FairDeal must be converted into GoodsKart customer data format.
# Key issues: GoodsKart customer data has more fields than in FairDeal customer data. Hence FairDeal data needs to be split and stored in GoodsKart Customer
# Object-Oriented Data Structure.
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

readCSVFile('FairDealCustomerData.csv')