#Take an integer N as input and print the count of digits of that number.
n=int(input("Enter the number: "))
count=0
while(n>0):
    n=n//10
    count+=1
print(count)

