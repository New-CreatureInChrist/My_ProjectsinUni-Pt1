#Write a program that safely asks the user for two numbers and divides them, handling invalid input and division by zero.

#Algorithm :
#1. ask for input. type cast to integer.
#2. handle exception for invalid input
#3. handle exception for zero division
#4. end program

print("NUMBER DIVISOR First Edition")

try:
    num1 = int(input("Enter the number to be divided : "))
    num2 = int(input("Enter the divisor : "))

    print("Your quotient is: ",num1/num2)
except ZeroDivisionError:
    print("Zero cannot divide, please take note!")
except ValueError:
    print("Your inputted values have a problem... ")  
finally: 
    print("Program closes.")
