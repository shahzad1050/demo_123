print("if u want to turn on k_eletric press 1 or if u want to turn ups on press 2")

number = int(input( "enter the number") )
if number == 1 :
  print("k_eletric is on" )

elif number == 2:
  print ("ups is on ")

else: print("your have entered number wrong, only 1 and 2 is accepted")



# table with for loop

user_input =int (input("enter the table u want to print"))
for i in range(1,11):
   print(f"{user_input} x {i} = {user_input * i}") 


# Garde
user_name = input("enter your name")
user_marks = int (input("enter your marks"))
if user_marks >= 90:
  print("GARDE A")
elif user_marks >= 80:
   print("GARDE B")
elif user_marks >= 70:
  print("GARDE C")
elif user_marks >= 60:
   print(" GARDE D")
else: 
   print("you are fail")


#  dynamic fuction

def add(a,b):
        print(a + b)
add(7,5)        
 
def multiply(a,b):
        print(a * b)
multiply(7,5)     

def divide(a,b):
        print(a / b)
divide(7,5)    

def subtract(a,b):
        print(a - b)
subtract(7,5)    
