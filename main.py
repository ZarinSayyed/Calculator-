num1 = float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
operator=input("Enter the operation to be done on numbers: ")

if operator == "+":
  print (num1 + num2)
elif operator == "*":
  print(num1 * num2)
elif operator == "/":
  print(num1 / num2)
elif operator == " - ":
  print(num1 - num2)
else :
  print("Enter valid operator and try again")
