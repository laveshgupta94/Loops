#Write a program to print all odd numbers from 1 to N, where you have to take N as input from user. 
num=int(input("Enter the number"))
for i in range(1,num):
    if(i%2!=0):
        print(i)

