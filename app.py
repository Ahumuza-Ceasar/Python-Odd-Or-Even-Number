print('------------Program to Check an Odd Number Or Even Number------------')

try:
     num = int(input("Enter a number to check if Odd / Even: "))

     if num % 2 == 0:
       print(f'{num} is an Even number')

     elif num % 2 == 1:
        print(f'{num} is an Odd number')

except ValueError:
    print("Hey that's an invalid Entry")

