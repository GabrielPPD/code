# SEC PROJECT By Gabriel Paul Pace
# Session 2025
# Area and Volume Calculator
# Password Script
tries =int(6)
print("What is your password?")
def password():
    tries =int(6)
    pass1 = input("Password:")
    for i in range(tries):
        # Making it so everytime the user tries it removes a try.
        tries -= 1
        pass2 = input("Please confirm Password:")
        print("You have", tries,"left")
        if pass1 == pass2:
            print("Welcome")
            break
password()
    # Entering the calculator software
property = int(0)
volume = int(0)
    # Creating the first menu
print("________________")
print("1...Start")
print("0...Leave")
print("________________")
choice = int(input("Start? :  "))
# Creating the loop for the calculator
# Creating the 2nd menu which allows the user to choose either 2d or 3d shapes.
while choice == 1:
    print("________________")
    print("1...2D Mode.")
    print("2...3D Mode.")
    print("0...Leave")
    print("________________")
    choice2 = int(input("Choose : "))
    # 3d Mode menu
    if choice2 == 0:
        print("Please, come again!")
        break
    while choice2 == 2:
        print("________________")
        print("1...Cube")
        print("2...Cuboid")
        print("3...Sphere")
        print("4...Cylinder")
        print("5...Total")
        print("0...Leave")
        print("________________")
        choice4 = int(input("Choose : "))
        if choice4 == 1:
            # Doing the coding for the cube calculations
            volL = int(input("What is the length : "))
            vol = volh**3
            print("The Volume of the cube is", vol1)
            # Adding the volume to the total volume.
            volume = volume + vol
        elif choice4 == 2:
            # Doing the coding for the cuboid calculations.
            VolL = int(input("What is the length : "))
            VolH = int(input("What is the height : "))
            VolW = int(input("What is the width : "))
            vol1 = VolH*VolL*VolW
            print("The Volume of the cuboid is", vol1)
            volume = volume + vol1
        elif choice4 == 3:
            # The sphere calculations
            Volr = float(input("What is the radius : "))
            pi = 3.142
            Vol2 = Volr**3*pi*1.3333
            print("The Volume of the sphere is", Vol2)
            volume = volume + Vol2
        elif choice4 == 4:
            # the calculations for the volume of a cylinder
            Volr2 = float(input("What is the radius : "))
            VolH3 = int(input("What is the height : "))
            pi = 3.142
            Vol3 = Volr2**2*pi*VolH3
            print("The volume of the cylinder is", Vol3)
            volume = volume + Vol3
        elif choice4 == 5:
            # replicating the property code by doing a volume print
            print("Final Volume is", volume)
        elif choice4 == 0:
            break
        else:
            print("Returning.")
                
    while choice2 == 1:
        print("________________")
        print("1...Triangle")
        print("2...Circle")
        print("3...Square")
        print("4...Total")
        print("0...Leave")
        print("________________")
        choice3 = int(input("What type of shape are you trying to find the area of? : "))
#Calculate area of triangle
        if choice3 ==1:
            base = float(input("What is the base? : "))
            height = float(input("What is the height? : "))
            area = base*height*0.5
            print("Area of triangle is : ",area)
            print()
#Calculating the total property
            property = area + property
            print("Total area of property : ",property)
#Calculate area of circle
        elif choice3 ==2:
            rad = float(input("What is the radius? : "))
            pi = 3.142
            area1 = rad**2*pi
            print("Area of circle is : ",area1)
            print()
            property = area1 + property
            print("Total area of property : ",property)
#Calculate area of square
        elif choice3 ==3:
            length = float(input("What is the length? : "))
            area2 = length**2
            print("Area of square is : ",area2)
            print()
            property = property + area2
            print("Total area of property : ",property)
#Creating the exit code
        elif choice3 ==4:
            print("Final property is : ", property)
            break
        elif choice3 ==0:
            break
#Removing the possibility of user choosing a different number
        else:
            print("Invalid number.")

    if (choice == 0) or (choice != 1):
        print("Bye bye.")
        break
            
    else:
        print("Returning.")
    
        