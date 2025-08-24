#You are given an integer A as input, and you need to determine whether it is a palindrome or not. A palindrome integer is one whose digits, when reversed, result in the same number

n=int(input("Enter the number: "))
b = n
rev  = 0
while(n>0):
    digit=n%10
    rev = rev * 10 + digit
    n//=10

if (b==rev):
   print("Yes it is pallindrome")
else:
   print("It is not ")


