#You are given two integers A and B. You have to find the value of A^B. 
A=int(input("Enter the number A: "))
B=int(input("Enter the number B: "))
count=1
i=0
while(B>i):
    count*=A 
    i+=1
print(count)
# for i in range(B):
#     count*=A
# print(count)