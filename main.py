# Import Math for GCD
import math

# Keep running unless breaks out
while True:
    # Input loop
    validInput = False
    while validInput == False:
        try:
            print(" # # # Tell me where your line crosses the X and Y axis. Values must be integers. # # #")
            x = int(input("Where does your line cross the X-axis? "))
            y = int(input("Where does your line cross the Y-axis? "))
            if x == 0 and y == 0:
                print("Sorry, I need two points.")
            elif x == 0 and not y == 0:
                print("That is just the Y-axis i.e. x=0")
                print("Give me non-zero integers please :)")
            elif not x == 0 and y == 0:
                print("That is just the X-axis i.e. y=0")
                print("Give me non-zero integers please :)")
            else:
                print("Thank you. I will find the equation of the line.")
                validInput = True
        except:
            print("Sorry, that is not a number")

    # Find the coefficients
    A = x
    B = y
    C = x*y

    # Divide out the GCD
    GCD = math.gcd(A,B,C)
    A /= GCD
    B /= GCD
    C /= GCD

    # Lead with positive only
    if A < 0:
        A *= -1
        B *= -1
        C *= -1

    # Force integers
    A = int(A)
    B = int(B)
    C = int(C)

    # Clean the ouput and print it
    line = "line: "+str(B)+"x+"+str(A)+"y="+str(C)
    line = line.replace("+-","-")
    line = line.replace("line: 1x","line: x")
    line = line.replace("+1y","+y")
    line = line.replace("-1y", "-y")
    print(line)

    # Quit?
    q = input("Quit? y/n: ")
    if q == "y":
        break

# Quit
print("Goodbye")
quit()