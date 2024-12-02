#used to predict error codes
try:
    age = int(input("Age: "))
    print(age)
    income = 2000
    risk = income/age
except ZeroDivisionError:
    print("Age cannot be 0.")
except ValueError:
    print("Invalid Value")
