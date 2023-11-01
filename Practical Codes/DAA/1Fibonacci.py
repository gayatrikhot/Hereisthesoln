# Write a program to calculate Fibonacci numbers and find its step count

# Recursion code 1
# Function to calculate Fibonacci number using recursion
import time
rs= time.time()
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)



# Function to count the number of steps needed to calculate a Fibonacci number using recursion
def count_steps_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 1 + count_steps_recursive(n - 1) + count_steps_recursive(n - 2)


# Input the desired Fibonacci number 'n'
n = int(input("Enter the value of n: "))

# Calculate and print the Fibonacci number using recursion
fib_recursive = fibonacci_recursive(n)
print(f"Fibonacci number (Recursive) for n = {n}: {fib_recursive}")

# Calculate and print the number of steps needed using recursion
steps_recursive = count_steps_recursive(n)
print(f"Number of steps (Recursive) to calculate Fibonacci number for n = {n}: {steps_recursive}")
re=time.time()

'''
def generate_fibonacci_sequence(n):
    if n <= 0:
        return []
    
    fibonacci_sequence = []
    a, b = 0, 1
    
    while a <= n:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    return fibonacci_sequence

# Generate and print the list of Fibonacci numbers up to 'n'
fib_sequence = generate_fibonacci_sequence(n)
print(f"Fibonacci sequence up to {n}: {fib_sequence}")
'''


# Non-recursive code:
nrs=time.time()
first_num = int(input("Enter the first number of the fibonacci series... "))
second_num = int(input("Enter the second number of the fibonacci series... "))
num_of_terms = int(input("Enter the number of terms... "))
print("The numbers in fibonacci series are : ")
print(first_num)
print(second_num)
while(num_of_terms-1):
    
    third_num = first_num + second_num
    first_num=second_num
    second_num=third_num
    print(third_num)
    num_of_terms=num_of_terms-1

nre=time.time()


print("Time consume in recursive:",(re-rs),"ms", "Time Complexity: O(2^n)  Space Complexity:O(n)" )
print("Time consume in non-recursive:",(nre-nrs),"ms","Time Complexity: O(n), Space Complexity: O(1)")
    
    
