#3. Write a program to print all even numbers from 1 to N, where you have to take N as input from the user. 
num=int(input("Enter the number: "))
for i in range(1,num+1):
    if(i%2==0):
        print(i)

