def is_palindrome(num):
    if num == num[::-1]:
        return True
    else:
        return False

print("Enter a Number to check Palindrome: ")
num = input()

if is_palindrome(num):
    print(str(num) + " is Palindrome")
else:
    print(str(num) + " is Not Palindrome")
