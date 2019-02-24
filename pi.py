import math

def main():

    print("Welcome to Pi approximation!\n")

    n = int(input("Enter the number of terms to sum: "))

    approx = 0

    for i in range(1, n+1, 2):
        approx += 4 / i - 4 / (i+2)

    print("Approximate value of pi is: " + str(approx))

    print("Deviation from Pi is: " + str(math.pi - approx))

main()
