# a=50
# b=3

# print("The value of",a,"+",3,"is:",a+b)
# print("The value of",a,"-",3,"is:",a-b)
# print("The value of",a,"/",3,"is:",a/b)
# print("The value of",a,"*",3,"is:",a*b)

# Calculator making by Terminal

num1=float(input("Enter a First  number here:"))
num2=float(input("Enter a Second number here:"))


print("Press 1 for addition\npress 2 for subtraction\npress 3 for multiplication\npress 4 for division\npress 5 for modulo")

choice=int(input("Enter your choice from 1-5:"))

if choice ==1:
    print("The addition of given two number is",num1 +num2)
elif choice ==2:
    print("The Subtraction of given two number is",num1-num2)
    
elif choice ==3:
    print("The Multiplication of given two number is",num1*num2)
    
elif choice ==4:
    print("The Division of given two number is",num1/num2)
elif choice ==5:
    print("The Modulo of given two number is",num1%num2)
else:
    print("Invalid number")


