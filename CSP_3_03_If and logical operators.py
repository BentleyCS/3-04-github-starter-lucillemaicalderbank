from random import choice


#modify the below function such that it asks the user for 2 numbers as input.
#Then have it print out the larger number
def larger():
    num1=float(input("Enter number 1"))
    num2=float(input("Enter number 2"))

    if num1>num2:
        print(f"The larger number is {num1}")
    elif num2>num1:
        print(f"The larger number is {num2}")
    else:
        print("Number one and Number two are equal")
    pass
larger()
#Modify the below function such that it asks for the users score as an input.
#Then based on the score print out a letter grade.
# 90+ A
# 80+ B
# 70+ C
# 60+ D
# 59- F
def grade():
    pass
score=float(input("Enter your score"))
if score>=90:
    print("Your letter grade is an A")
elif score>=80:
    print("Your letter grade is a B")
elif score>=70:
    print("Your letter grade is a C")
elif score>=60:
    print("Your letter grade is a D")
else:
    print("Your letter grade is an F")
larger()
grade()
#Modify the below function such that it asks the user for a number then
#if the number is divisible by 3 print "fizz"
#if the number is divisible by 5 print "buzz"
#if both are the case then print "Fizzbuzz" instead of the prior two
#if niether are the case print the number.
def fizzBuzz():
    num=int(input("Enter a number"))

    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)
    pass
fizzBuzz()

#modify the below function such that it asks the user for an input number.
#if the number is even divide it by two.
#if the number is odd multiply it by 3 and add 1
#if n is 1 do nothing.
#then print the new number.
def collatz():
    n=int(input("Enter a number"))

    if n==1:
        print("No change")
    elif n%2==0:
        n=n//2
        print(f"new number is {n}")
    else:
        n=n*3+1
        print(f"New number is {n}")
    pass
collatz()

#The above two functions do not have function calls in the main file.
#Modify the below function such that when it is called it asks the user
# which of the two they would like to run and executes the corresponding function.
#If they answer with something than the expected results skip the questions.
def pickFunction():
    choice=input("What function to run? (fizzBuzz/collatz)").strip().lower()

    if choice=="fizzbuzz":
        fizzBuzz()
    elif choice=="collatz":
        collatz()
    else:
        print("Invalid")
    pass

pickFunction()


#Modify the below function such that it asks the user for a temperature.
#The format for tempearture should end in F For Fahrenheit and C for Celcius
#Then given the temperature if it is in Fahrenheit convert it to Celsius on vice versa
#Example 32F -> 0C  20C -> 68F
def convertTemperature():
    temp=input("Enter a temperature (End in F for Fahrenheit or C for Celcius)")
    if not temp[:-1].replace('.','',1).isdigit()or temp[-1] not in ['F','C']:
        print("Invalid format")
        return
    value=float(temp[:-1])
    unit=temp[-1]
    if unit=='F':
        celsius=(value-32)*5/9
        print(f"{value}F is equal to {celsius:.2f}C")
    elif unit=='C':
        fahrenheit=(value*9/5)+32
        print(f"{value}C is equal to {fahrenheit:.2f}F")
    pass
convertTemperature()