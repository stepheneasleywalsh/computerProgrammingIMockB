# Student Number 00000000

# Import math for GCD
import math

# Loop forever
while True:
    # Ask for the intercepts
    print(" # # # Tell me where your line crosses the X and Y axis. Values must be integers. # # # ")
    try:
        A = int(input("Where does your line cross the X-axis? "))
        B = int(input("Where does your line cross the Y-axis? "))
        # Check they are not zero
        if A == 0 and B == 0:
            print("Sorry, I need two points")
        elif not A == 0 and B == 0:
            print("That is just the X-axis i.e. y = 0")
            print("Give me non-zero integers please :)")
        elif A == 0 and not B == 0:
            print("That is just the Y-axis i.e. x = 0")
            print("Give me non-zero integers please :)")
        else:
            # FIND THE EQUATION OF THE LINE
            print("Thank you. I will find the equation of the line.")
            C = A*B

            # Divide out the GCD
            GCD = math.gcd(B,A,C)
            B /= GCD
            A /= GCD
            C /= GCD

            # Make sure A B C are ints
            B = int(B)
            A = int(A)
            C = int(C)

            # Make sure it starts with +
            if B < 0:
                B *= -1
                A *= -1
                C *= -1

            # Clean output of the line
            line = "line: "+str(B)+"x+"+str(A)+"y="+str(C)
            line = line.replace("+-","-")
            line = line.replace("+1y","+y").replace("-1y","-y")
            line = line.replace("line: 1x","line: x")
            print(line)

            # Quit?
            q = input("Quit? y/n ")
            if q == "y":
                break
    except:
        print("Sorry, that is not a number")

# QUIT
print("Goodbye")
quit()