# Take an integer A as input. You have to print the sum of all odd numbers in the range [1,A]. 
A=int(input("Enter the number: ")) 
add=0
for i in range(1,A+1):
    if(i%2!=0):
        add+=i
print(add)
