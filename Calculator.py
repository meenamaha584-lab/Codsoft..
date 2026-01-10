a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        print("Divide by 0 is not allowed")
    else:
        return a/b
print("-----Simple calculator-----")
print("Enter your choice (1.(add)/2.(sub)/3.(mul)/4.(div)):")
choice=int(input())
if choice==1:
    print("1.Addition:",add(a,b))
elif choice==2:
    print("2.Subtraction:",subtract(a,b))
elif choice==3:
    print("3.Multiplication:",multiply(a,b))
elif choice==4:
    print("4.Division:",divide(a,b))
else:
    print("Invalid input")