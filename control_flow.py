#Age eligibility checker child,adult,tenager
age=int(input("Enter your age:"))
if age<13:
    print("You are a child")
elif age>=13 and age<20:
    print("You are a teenager")
else:
    print("You are an adult")

#password validation
password=input("Enter your password:")
if len(password)<8:
    print("Password is too short")
elif len(password)>10:
    print("Password is too long")   
else:
    print("Password is valid")

#grade classification Excellent,Good,Average,Poor
marks=int(input("Enter your marks:"))
if marks>=90:
    print("Excellent")
elif marks>=80 and marks<90:
    print("Good")
elif marks>=60 and marks<80:
    print("Average")
else:
    print("Poor")

#multiplication table
number=int(input("Enter a number:"))
print("Multiplication table for", number)
for i in range(1,11):
    result=number*i
    print(number, "*", i, "=", result)


#atm widthrawal simulation
balance=1000
withdrawal_amount=int(input("Enter the amount to withdraw:"))
if withdrawal_amount>balance:
    print("Insufficient funds")
else:   
    balance-=withdrawal_amount
    print("Withdrawal successful. Your new balance is", balance)


#login system verify username and password
stored_username="admin"
stored_password="password123"
username=input("Enter your username:")
password=input("Enter your password:")
if username==stored_username and password==stored_password:
    print("Login successful")
else:    
    print("Invalid username or password")


#number guesser game
import random
number_to_guess=random.randint(1,100)
guess=int(input("Guess a number between 1 and 100:"))   
while guess!=number_to_guess:
    if guess< number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess=int(input("Guess a number between 1 and 100:"))

print("Congratulations! You guessed the number", number_to_guess)


