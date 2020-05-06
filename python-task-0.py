#1. Accept two integer numbers from a user and return their product and if the product is greater than 1000, then return their sum
def prod_two(x,y):
    if x*y>1000:
        return (f"sum of both numbers: {x+y}")
    return (f"product of both numbers: {x*y}")
x=input("enter first number:\n")
y=input("enter second number:\n")
x=int(x)
y=int(y)
print(prod_two(x,y))  

#2.Accept n number from user and calculate the sum of all number between 1 and n including n
n=int(input("enter a number:\n"))
total=0
for i in range(1,n+1):
    total+=i
print(f"sum of 1 to {n}: {total}")


#3.Given a number count the total number of digits in a number
a=input("enter a number:\n")
print(f"total number of digits in {a} are {len(a)}")


#4.Accept string from a user and display only those characters which are present at an even index number.
def even_string(z):
    temp=""
    for i in range(0,len(z)):
        if i%2==0:
            temp+=z[i]
    return temp       

z=input("enter a string\n")
print(f"characters which are present at an even index number: {even_string(z)}")


#5.Write a python program to print all the prime number in a given interval and also check is a given input number is prime or not.
p=input("enter first number:\n")
q=input("enter second number:\n")
p=int(p)
q=int(q)
print(f"prime numbers between {p} and {q} are:\n")
for i in range(p,q+1):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            print(i)    
print("\n")

for i in range(2, p):
	if p % i  == 0:
		print(p,"is not prime number")
		break
else:
	print(p,"is a prime number")
for i in range(2, q):
	if q % i  == 0:
		print(q,"is not a prime number")
		break
else:
	print(q,"is a prime number")  


#6.Write a python program to print the Fibonacci series and also check if a given input number is Fibonacci number or not.
import math

def fibbo_seq(n):
   if n <= 1:
       return n
   else:
       return(fibbo_seq(n-1) + fibbo_seq(n-2))
n=input("enter a number:\n")
n=int(n)
print("\nFibonacci sequence:\n")
for i in range(n):
    print(fibbo_seq(i))

    
def checkPerfectSquare(n):
    sqrt = int(math.sqrt(n))
    if pow(sqrt, 2) == n:
        return True
    else:
        return False

def isFibonacciNumber(n):
    res1 = 5 * n * n + 4
    res2 = 5 * n * n - 4
    if checkPerfectSquare(res1) or checkPerfectSquare(res2):
        return True
    else:
        return False


if isFibonacciNumber(n):
    print ("\nYes,", n, "is a Fibonacci number")
else:
    print ("\nNo,", n, "is not a Fibonacci number")