#1. Write a program that takes a positive integer N as input from the user and prints all natural numbers numbers from 1 to N, with each number followed by a space.
 
num=int(input("Enter the number "))
i=1
while(num>=i):
    print(i, end=" ")
    i=i+1  
# for i in range(1,num+1):
#     print(i,end=' ')
              