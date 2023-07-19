#!/usr/bin/env python3
# example workign with conditionals
#By Alex on 07/18/23

#set send_message function
def send_message(number):
    for i in range(number): 
        print("Yeah it is.")

#Is today a good day?
dayQ = input("Is today a good day? (y/n)")
if (dayQ == 'y'):
    send_message(3)
else:
    print("That's too bad.")