#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
#Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.
num1 = int(float(input('Enter the first number: ')))
num2 = int(float(input('Enter the second number: ')))
if num1 < num2:
    print(f'The bigger number is {num2}')
elif num1 > num2:
    print(f'The bigger number is {num1}')
else:
    print(f'Equal')
