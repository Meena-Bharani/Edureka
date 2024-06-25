class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        # self.email = '{}.{}@email.com'.format(self.first,self.last)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

    @fullname.getter
    def fullname(self):
        return '{} {}'.format(self.first,self.last)


e = Employee('Haran','Shivanan')
print(e.email)
print(e.fullname)

e.fullname='Jeyaraj Muthu'
x = e.fullname
print(x)