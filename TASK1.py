def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    return fact

num = int(input("Enter a number: "))
fact = factorial(num)

print(f'Factorial of {num} is: {fact}')

# Enter a number: 5
# Factorial of 5 is: 120