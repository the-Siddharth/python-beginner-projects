def is_palindrome(num_string):
    if num_string == num_string[::-1]:
        return True
    else:
        return False

print("Enter a Number or a String to check Palindrome: ")
num_string = input()

if is_palindrome(num_string):
    print(str(num_string) + " is Palindrome")
else:
    print(str(num_string) + " is Not Palindrome")
