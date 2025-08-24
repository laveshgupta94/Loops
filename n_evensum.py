#You are given an integer A, you need to find and return the sum of all the even numbers between 1 and A.
A=int(input("Enter the number: "))
add=0
for i in range(1,A+1):
    if(i%2==0):
        add+=i
print(add)
    
