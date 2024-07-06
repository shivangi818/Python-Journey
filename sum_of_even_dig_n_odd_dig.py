#Write a program to input an integer N and print the sum of all its even digits and all its odd digits separately.

#Digits mean numbers, not the places! If the given integer is "13245", the even digits are 2 and 4, and the odd digits are 1, 3, and 5.

def sum_of_digit(n):
    str_=str(n)
    
    sum_even=0
    sum_odd=0
    
    for char in str_:
        digit=int(char)
        
        if digit%2==0:
            sum_even+=digit
        else:
            sum_odd+=digit
    print(sum_even,sum_odd)
n=int(input())
sum_of_digit(n)         