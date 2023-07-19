#!/usr/bin/env python3
# example working with Functions
#By Alex Lee 07/18/23

#input number
number = input("Please input a number:\n")
number = int(number)

divisor = input("Please input the divisor:\n")
divisor = int(divisor)

#check if it is divisble
def is_divisible(num, div):
    if num % div == 0:
        return True
    else:
        return False

if is_divisible(number, divisor) == True:
    print(number, "is divisable by", divisor)
else:
    print(number, "is not divisable by", divisor)
#if number % 2 == 0:
#    print(number, 'is even.')
#else:
#    print(number, 'is odd.')