def fibonacci_generator(n):
        a, b = 0, 1
        for c in range(n):
            print(a, end=' ')
            a, b = b, a + b\

print("Enter the Number to generate Fibonacci Series: ")
n = int(input())
fibonacci_generator(n)
