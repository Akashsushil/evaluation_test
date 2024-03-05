palindrome=lambda s:s==s[::-1]
string=input("enter a string:")
if palindrome(string):
    print("The string is palindrome")
else:
    print("the string is not palindrome")