n1 = float(input("first number: "))
n2 = float(input("second number: "))
print("Choose operation: ")
print("+ Addition")
print("- Subtraction")
print("* Multiplication")
print("/ Division")

op = input("Enter operator: ")

if op == "+":
    print("result:",n1+n2 )
elif op == "-":
     print("result: ",n1-n2)
elif op == "*":
     print("result: ",n1*n2)
elif op == "/":
 if n2 != 0:
     print("result: ",n1/n2)
 else:
        print("Error")
else:
            print("invalid operator")
