#Write a program to find the factorial o#f a number.

#Factorial of n is:

#n! = n * (n-1) * (n-2) * (n-3)....* 1

#Output the factorial of 'n'. If it does not exist, output 'Error'

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
print(fact(n))