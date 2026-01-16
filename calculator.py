def calculate(n1,op,n2):
    if op=="+":
        return(n1+n2)
    elif op=="-":
        return(n1-n2)
    elif op=="*":
        return(n1*n2)
    elif op=="/":
        return(n1/n2)
    else:
        return("Invalid operator")
print("welcome to calculator")
import logo
print(logo.logo)
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
while op not in ['+', '-', '*', '/']:
    print(" Invalid operator. Try again.")
    op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))
reult = calculate(num1,op,num2)

print(f"The result is: {reult}")
choice=input("whther you want to continue with the result or start a new calculation? YES or NO ").lower()
while True:
    if choice =="yes":
        op = input("Enter operator (+, -, *, /): ")
        while op not in ['+', '-', '*', '/']:
             print(" Invalid operator. Try again.")
             op = input("Enter operator (+, -, *, /): ")
        num3 = float(input("Enter next number: "))
        reult = calculate(reult,op,num3)
        print(f"The result is: {reult}")
        choice=input("whther you want to continue with the result or start a new calculation? YES or NO ").lower()
    else:
        print("Thank you for using the calculator.")
        break