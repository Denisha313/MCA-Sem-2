#!/usr/bin/env python
# coding: utf-8

# In[1]:


#add two no.
a=1
b=2
print(a+b)


# In[4]:


num1=int(input("enter first number:"))
num2=int(input("enter second number"))
sum=num1+num2
print(sum)


# In[6]:


#maximum two no.
a=30
b=20
if a>b:
    print("a is big")
else:
    print("b is big")


# In[8]:


a=int(input("enter first number"))
b=int(input("enter second number"))
if a>b:
    print("a is big")
else:
    print("b is big")


# In[14]:


#factorial
def factorial(n):
	
	# single line to find factorial
	return 1 if (n==1 or n==0) else n * factorial(n - 1);

# Driver Code
num = 5;
print("Factorial of",num,"is",
factorial(num))



# In[16]:


#simple intrest
p=8
t=6
r=8
si=(p*t*r)/100
print("the simple interst is",si)


# In[17]:


#compond interest
# interest for given values.

def compound_interest(principle, rate, time):

	# Calculates compound interest
	Amount = principle * (pow((1 + rate / 100), time))
	CI = Amount - principle
	print("Compound interest is", CI)

# Driver Code
compound_interest(10000, 10.25, 5)



# In[19]:


#area of circle

def findArea(r):
   PI = 3.142
   return PI * (r*r);
print("Area is %.6f" % findArea(5));


# In[21]:


#prime no
start = 11
end = 25
for i in range(start, end+1):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)


# In[1]:


def Fibonacci(n):
    if n<0:
        print("Incorrect input")
   
    elif n==1:
        return 0
   
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
  

  
print(Fibonacci(9))


# In[5]:


c = 'r'

print("The ASCII value of '" + c + "' is", ord(c))


# In[2]:


def squaresum(n) :

	sm = 0
	for i in range(1, n+1) :
		sm = sm + (i * i)
	
	return sm


n = 4
print(squaresum(n))



# In[5]:


# Simple Python program to find sum of series
# with cubes of first n natural numbers


def sumOfSeries(n):
	sum = 0
	for i in range(1, n+1):
		sum +=i*i*i
		
	return sum
n = 5
print(sumOfSeries(n))



# 
# 
# 
# 
