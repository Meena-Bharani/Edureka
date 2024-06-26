# Verification and Encryption of Reference ID

# Module 2 –Introduction to Python for Apache Spark
# Case Study 2
# Domain –Telecom
# focus –Optimization
# Business challenge/requirement
# LifeTel Telecom is the latest entrant in the highly competitive Telecom market of Singapore.  It issues SIM to the verified users.
# Till now verification was manual through the photocopy of approved id card document. However,government has recently introduced Social ID called Reference ID
# which is mapped to fingerprint of user.LifeTel should now verify user against the fingerprint and Reference ID
# Key issues: Build a system where when user enters Reference ID it is encrypted, so that hackers cannot view the mapping of Reference ID and finger print
# Considerations: System should be secure
# Data volume-NA
# Additional information:-NA
# Business benefits: Company will be able to quickly issue SIM to user and expected gain in volume is approximately 10 times as the manual process of verification is replaced with secure automated system
# Approach to Solve: You have to use fundamentals of Python taught in module 2
# 1.Read the input from command line –Reference ID
# 2.Check for validity –it should be 12 digits and allows on number and alphabet
# 3.Encrypt the Reference ID and print it for reference
# Enhancements for code
# You can try these enhancements in code
# 1.Allow some special characters in ReferenceID
# 2.Give the option for decryption to user

# pip install cryptography

import re
from cryptography.fernet import Fernet
class telecom:
    global delimiter
    delimiter = '@'
    def __init__(self):
        try:
            self.ref_id = input('Enter user\'s reference Id: ')
            if len(self.ref_id) < 12:
                raise Exception('Reference ID must be 12 digit')
            if not bool(re.match(r'^[a-zA-Z0-9]*$', self.ref_id)):
                raise Exception('Allows only numbers and alphabets')
        except Exception as e:
            raise Exception('Error: ', e)
    @staticmethod
    def ancii_encryption(reference_id):
        encrypted_id = ''
        for i in reference_id:
            encrypted_id += str(ord(i)) + delimiter
        return encrypted_id
    @staticmethod
    def ancii_decryption(reference_id):
        lst = reference_id.split(delimiter)
        if len(lst)>12:
            # new_lst = str(' '.join(lst).split())
            decrypted_id = ''
            # print(new_lst)
            for i in lst:
                if i != '':
                    decrypted_id += str(chr(int(i)))
            return decrypted_id
        return ''

    @staticmethod
    def crypto_encryption(reference_id):
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encrypt_id = fernet.encrypt(reference_id.encode())
        # encrypt_id = fernet.encrypt(reference_id.encode())
        return encrypt_id

    @staticmethod
    def crypto_decryption(reference_id):
        key = Fernet.generate_key()
        fernet = Fernet(key)
        decrypt_id = fernet.decrypt(reference_id).decode()
        return decrypt_id

    # @staticmethod
    def verify_user_id(self):
        try:
            print('Reference ID : ', self.ref_id)
            enc = self.ancii_encryption(self.ref_id)
            dec = self.ancii_decryption(enc)
            print('Encrypted Reference ID : ', enc)
            print('decrypted Reference ID : ', dec)

            cenc = self.crypto_encryption(self.ref_id)
            # cdec = self.crypto_decryption(cenc)
            print('Encrypted Reference ID : ', cenc)
            # print('decrypted Reference ID : ', cdec)
        except Exception as e:
            raise Exception('Error: ',e)

t = telecom()
t.verify_user_id()


