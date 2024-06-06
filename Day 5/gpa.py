science=int(input("Enter the marks of science:"))
maths=int(input("Enter the marks of maths:"))
health=int(input("Enter the marks of health:"))
DSA=int(input("Enter the marks of DSA:"))

if(science>100 or maths>100 or health>100 or DSA>100):
    print("Invalid")
    
else:
    total=science+maths+health+DSA
    gpa=(total/500)*4

    if gpa<4 and gpa>3.7:
        print("Gpa is A:",gpa)
        
    if gpa<3.7 and gpa>3.2:
        print("gpa is B:",gpa)
    if gpa<3.2 and gpa>2.9:
        print("gpa is C:",gpa)
    if gpa<2.9 and gpa>2.5:
        print("gpa is D:",gpa)
    if gpa<2.5 and gpa>1.9:
        print("gap is E:",gpa)