#task1

import re

j="This#string%contains^special*characters&."

print(re.sub("[^a-zA-Z]"," ",j))

print(re.sub("[#%^*&.]"," ",j))

i=re.findall("^This", j)
if i:
  print("Yes")
else:
  print("No match")

#task 2

text=open("../Jupyter/read.txt", 'r')
x=text.read()

vowels=['a','e','i','o','u']

count_vowels=0

for i in x.lower():
    if i in vowels:
        count_vowels+=1

print(count_vowels)

words=[]
words_dict={}
print(x)
x = re.sub("[^a-zA-Z]"," ",x)
print(x)
for i in x.split():
    words.append(i)

    words_dict[i]=words.count(i)

print(words_dict)

#Abstarct class

from abc import ABC, abstractmethod


class Phone(ABC):
    @abstractmethod
    def process(self):
        pass


class Nokia(Phone):

    # overriding abstract method
    def process(self):
        print("If you use more I'll get heated")

R = Nokia()
R.process()

class Samsung(Phone):
    def process(self):
        print("I'll not get heated") # works when this is defined

    def works(self):
        print("its working")

S = Samsung()
S.process()
S.works()

#Inheritance

#method overloading #we can use *args

class addition:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None,d=None):

        s = 0

        if a != None and b != None and c != None and d != None:
            s = a + b + c
        elif a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a

        return s


s1 = addition(3, 4)
print(s1.sum(4, 7))

#we can use multipledispatch instead for many if/else and same function defining multiple times(drawback only latest one will be used)
from multipledispatch import dispatch

@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result);

@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result);

product(30,100)
product(2.5,5.0,10.0)

# method overriding

class Book:
    def show(self):
        print("Your in Book")

class Classmate(Book):
    def show(self):
        print("You are in classmate Book")

mybook = Classmate()
mybook.show()


