#Write a program to find the sum of all Natural numbers from 1 to N, where you have to take N as input from user 

num=int(input("Enter the number: "))
add=0
for i in range(1,num+1):
    add+=i
print(add)  