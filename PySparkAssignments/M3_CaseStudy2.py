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
