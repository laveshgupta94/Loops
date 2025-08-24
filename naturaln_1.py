# Write a program to print all Natural numbers from N to 1, where you have to take N as input from the user. 

num=int(input("Enter the number: "))

# for i in range(num,0,-1):#for i in range(intial,end,step size)
#     print(i, end=' ')
i=num
while(num>=1):
    print(i)
    i-=1

    