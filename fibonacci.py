def main():
    n=int( input("give the value of n for the Fibonacci term"))
    nminus1=1
    nminus2=1
    if n<3:
        print(1)
    else:
        for i in range(3,n+1):
            result = nminus1 + nminus2
            nminus2 = nminus1
            nminus1 = result
        print (result)
main()
