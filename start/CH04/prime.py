#!/usr/bin/env python3
# example workign with conditionals
#By Alex on 07/18/23

#set prime function
def is_prime(number):
    if number > 1:
        for i in range(2, int(number/2)+1):
            if (number % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

primec = input("What number would you like to check?\n")
primec = int(primec)
result = is_prime(primec)
if result == True:
    print(primec, "is prime.")
else:
    print(primec, "is not prime.")