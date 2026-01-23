def add(a,b):
    return a+b
def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

a = 6
b = 3

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation= int(input("enter from 1-4: "))

if operation==1:
    print("result: ", add(a,b))
elif operation==2:
    print("result: ", subtract(a,b))
elif operation==3:
    print("result: ", multiply(a,b))
elif operation==4:
    print("result: ", divide(a,b))
else:
    print("invalid choice")