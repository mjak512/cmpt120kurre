def getEquation():
    return input("Enter an equation separated by spaces: ").split()


def calculate(equation):
    i=0
    while len(equation)>1 and hasProdDiv(equation):
        print(equation)
        if equation[i]=="*" or equation[i]=="/":
            process(equation,i)
            i=0
        else:
            i=i+1
    i=0
    while len(equation)>1:
        if equation[i]=="+" or equation[i]=="-":
            process(equation,i)
            i=0
        else:
            i=i+1
    return float(equation[0])

def hasProdDiv(equation):
    eqstr="".join(equation)
    if "*" in eqstr or "/" in eqstr:
        return True
    return False

def process(equation, i):
    if equation[i]=="*":
        result=float(equation[i-1])*float(equation[i+1])
    elif equation[i]=="/":
        result=float(equation[i-1])/float(equation[i+1])
    elif equation[i]=="+":
        result=float(equation[i-1])+float(equation[i+1])
    elif equation[i]=="-":
        result=float(equation[i-1])-float(equation[i+1])
    del equation[i-1:i+2]
    equation.insert(i-1,str(result))

def main():
    equation=getEquation()
    result=calculate(equation)
    print("The result of the equation is", result)

main()
