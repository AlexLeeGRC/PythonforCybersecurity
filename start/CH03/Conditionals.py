#!/usr/bin/env python3
# example workign with conditionals
#By Alex on 07/11/23

#Is today a good day?
dayQ = input("Is today a good day? (y/n)")
if (dayQ == 'y'):
    for i in range(10):
        print("Yes it is.")
else:
    print("That's too bad.")