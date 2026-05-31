num1 = input("Enter your 1st number: ")
num2 = input("Enter your 2nd number: ")
decision = input("Enter the operation you want to perform (option: add, subtract, multiply, divide): ")

if decision == "add":
    result = int(num1) + int(num2)

elif decision == "subtract":
    result = int(num1) - int(num2)

elif decision == "multiply":
    result = int(num1) * int(num2)

elif decision == "divide":
    result = int(num1) / int(num2)

else:
    print("Invalid operation")


if decision in ["add", "subtract", "multiply", "divide"]:
    print("The result is: " + str(result))

