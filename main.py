# Import Math, needed for GCD calculation
import math

while True:
    while True:
        # Ask for A and B
        print(" # # # Tell me where your line crosses the X and Y axis. Values must be integers. # # #")
        try:
            A = int(input("Where does your line cross the X-axis? "))
            B = int(input("Where does your line cross the Y-axis? "))
            # Check that they are not zero
            if A == 0 and not B == 0:
                print("That is just the Y-axis i.e. x=0")
                print("Give me non-zero integers please :)")
            elif not A == 0 and B == 0:
                print("That is just the X-axis i.e. y=0")
                print("Give me non-zero integers please :)")
            elif A == 0 and B == 0:
                print("Sorry, I need two points.")
            else:
                break
        except:
            print("Sorry, that is not a number")

    # Calculating the equation of the line
    C = A*B
    GCD = math.gcd(B,A,C)
    B /= GCD
    A /= GCD
    C /= GCD
    B = int(B)
    A = int(A)
    C = int(C)

    # Making sure it doesn't start with minus
    if B < 0:
        B *= -1
        A *= -1
        C *= -1

    # Clean output
    line = "line: "+str(B)+"x+"+str(A)+"y="+str(C)
    line = line.replace("+-","-")
    line = line.replace("+1y","+y").replace(" 1x"," x")
    line = line.replace("-1y","-y")
    print(line)

    # Quit?
    q = input("Quit? y/n ")
    if q == "y":
        break

#Quit
print("Goodbye")
quit()