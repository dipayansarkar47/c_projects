def sum(a,b): #sum
    print("The answer is: ",a+b)
def diff(a,b): #difference
    print("The answer is: ",a-b)
def product(a,b): #product
    print("The answer is: ",a*b)
def quotient(a,b): #quotient
    print("The answer is: ",a/b)


a,b = map(int,input("Enter numbers:").split())
c = input("Enter a operator: ")
if c == "+":
    sum(a,b)
elif c == "-":
    diff(a,b)
elif c == "*":
    product(a,b)
elif c == "/":
    quotient(a,b)
else:
    print("Invalid operator")






