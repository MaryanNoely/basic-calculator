from replit import clear
from art import logo

def add(n1,n2):
  return n1+n2

def substract(n1, n2):
  return n1-n2

def multiply(n1, n2):
  return n1*n2

def divide(n1,n2):
  if n2==0:
    print("You cannot devide by 0")
    return
  return n1/n2


print(logo)
end=False
option="no"


operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,  
}

while(end==False):
  if option=="no":
    fnum=float(input("What's your first number?: "))
  for op in operations:
    print(op)
  operator=input("Pick an operation: ")
  lnum=float(input("What's your second number?: "))
  function=operations[operator]
  result= function(fnum,lnum)
  if result == None:
    print("Wrong")
    end=True
  else: 
    print(f"{fnum} {operator} {lnum} = {result}")

  option=input("Type 'yes' to use the result or 'no' to start over: ").lower()
  if option == "yes":
    fnum=result
  else:
    clear()
