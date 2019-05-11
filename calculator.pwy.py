from tkinter import *


class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num) 
        if self.new_num:
         self.current = x=temp2
         self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
                    self.current = temp + temp2
                    self.display(self.current)

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
            else:
                self.total = float(text_box.get())

 def display(self, value):
     text_box.delete(0, END)
     text_box.insert(0, value)

 def do_sum(self):
     if self.op == "add":
         self.total += self.current
     if self.op == "subtract":
         self.total -= self.current
     if self.op == "multiply":
         self.total *= self.current
     if self.op == "divide":
         self.total /= self.current
         self.new_num = True
         self.op_pending = False
         self.display(self.total)

 def operation(self, op):
     self.current = float(self.current)
     if self.op_pending:
         self.do_sum()
         elif not self.eq:
             self.total = self.current
             self.new_num = True
             self.op_pending = True
             self.op = op
             self.eq = False

 def cancel(self):
         self.eq = False
     self.current = "0"
     self.display(0)
     self.new_num = True

 def all_cancel(self):
     self.cancel()
     self.total = 0

 def sign(self):
     self.eq = False
     self.current = -(float(text_box.get()))
     self.display(self.current)

 
sum1 = Calc()
gui = Tk()
calc = Frame(gui)
calc.grid()



gui.title("Calculator")
gui.configure(bg='orange')
text_box = Entry(calc, justify=RIGHT)
text_box.grid(row = 0, column = 0, columnspan = 3, pady = 5)
text_box.insert(0, "0")



numbers = "9876543210"
i = 0
bttn = []
for m in range(1,4):
    for j in range(3):
        bttn.append(Button(calc, text = numbers[i], font = 'red', fg='white', bg = 'light blue' ))
        bttn[i].grid(row = m, column = j, pady = 5)
        bttn[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
        i += 1

        bttn_0 = Button(calc, text = "0", fg='green', bg = 'yellow', font = 'bold' )
        bttn_0["command"] = lambda: sum1.num_press(0)
        bttn_0.grid(row = 4, column = 1, pady = 5)


        bttn_div = Button(calc, text = "/", fg='grey', bg = 'pink' )
        bttn_div["command"] = lambda: sum1.operation("divide")
        bttn_div.grid(row = 4, column = 3, pady = 5)

        bttn_mult = Button(calc, text = "*" ,fg='grey', bg = 'pink')
        bttn_mult["command"] = lambda: sum1.operation("multiply")
        bttn_mult.grid(row = 3, column = 3, pady = 5)

        minus = Button(calc, text = "-",fg='grey', bg = 'pink' )
        minus["command"] = lambda: sum1.operation("subtract")
        minus.grid(row = 2, column = 3, pady = 5)

        point = Button(calc, text = ".", fg='grey', bg = 'pink' )
        point["command"] = lambda: sum1.num_press(".")
        point.grid(row = 4, column = 0, pady = 5)

        add = Button(calc, text = "+", fg='grey', bg = 'pink' )
        add["command"] = lambda: sum1.operation("add")
        add.grid(row = 1, column = 3, pady = 5)


        equals = Button(calc, text = "=", fg='grey', bg = 'pink' )
        equals["command"] = sum1.calc_total
        equals.grid(row = 5, column = 3, pady = 5)



        gui.mainloop()

clear = Button(calc, text = "M+", fg='green', bg = 'orange' )
clear["command"] = sum1.cancel
clear.grid(row = 5, column = 2, pady = 1)

clear = Button(calc, text = "MR", fg='green', bg = 'orange' )
clear["command"] = sum1.cancel
clear.grid(row = 5, column = 0, pady = 5)

clear = Button(calc, text = "M-", fg='green', bg = 'orange' )
clear["command"] = sum1.cancel
clear.grid(row = 4, column = 2, pady = 1)

clear = Button(calc, text = "MC", fg='green', bg = 'orange' )
clear["command"] = sum1.all_cancel
clear.grid(row = 5, column = 1, pady = 5)

equals = Button(calc, text = "=", fg='green', bg = 'orange' )
equals["command"] = sum1.calc_total
equals.grid(row = 5, column = 3, pady = 5)

from graphics import *


def main():
 win = drawCalculator()
 getInput(win)


def drawCalculator():
 win = GraphWin("Calculator Project", 325, 440)
 win.setBackground("darkblue")
 win.setCoords(0, -3, 13, 19)

 Rectangle(Point(1, 18), Point(12, 16)).draw(win)
 
 for c in range(-2, 14, 3):
 for r in range(3, 13, 3):
 Rectangle(Point(r - 2, c + 2), Point(r, c)).draw(win)

 button = ["Clear", "Quit", "", "=", "+/-", "0", ".", "-", "7", "8", "9", "+",
 "4", "5", "6", "*", "1", "2", "3", "/", "M+", "M-", "MR", "MC"]

 i = 0

 for c in range(-1, 15, 3):
 for r in range(2, 12, 3):
 Text(Point(r, c), button[i]).draw(win)
 i = i + 1
 return win


def getInput(win):
 click = ""
 i = ""
 equation = []
 printedEquation = Text(Point(0, 0), "")
 printedEquation.undraw()

 mem = 0
 while (i != "="):
 equation.append(click)
 prints = "".join(equation)
 print(prints)
 printedEquation.undraw()
 printedEquation = Text(Point(6.5, 17), prints)
 printedEquation.draw(win)

 p = win.getMouse()
 x = p.getX()
 y = p.getY()

 whereClicked = Buttons(x, y, win, prints, mem, printedEquation, equation)
 click, equation, mem = whereClicked.Click()


class Buttons:
 def __init__(self, x, y, win, printed, currentMemory, printedEquation, equation):
 self.x = x
 self.y = y
 self.clicked = ""
 self.win = win
 self.printed = printed
 self.memory = currentMemory
 self.printedEquation = printedEquation
 self.equation = equation

 def Click(self):
 if self.y <= 15 and self.y >= 13:
 if self.x <= 3 and self.x >= 1:
 self.clicked = ""
 newMemory = int(self.printed)
 self.memory = (self.memory + newMemory)
 elif (self.x <= 6 and self.x >= 4):
 self.clicked = ""
 newMemory = int(self.printed)
 self.memory = (self.memory - newMemory)
 elif (self.x <= 9 and self.x >= 7):
 self.printed = ""
 self.equation = []
 self.clicked = str(self.memory)
 elif (self.x <= 12 and self.x >= 10):
 self.clicked = ""
 self.memory = 0
 if (self.y <= 12 and self.y >= 10):
 if (self.x <= 3 and self.x >= 1):
 self.clicked = "1"
 elif (self.x <= 6 and self.x >= 4):
 self.clicked = "2"
 elif (self.x <= 9 and self.x >= 7):
 self.clicked = "3"
 elif (self.x <= 12 and self.x >= 10):
 self.clicked = "/"
 elif (self.y <= 9 and self.y >= 7):
 if (self.x <= 3 and self.x >= 1):
 self.clicked = "4"
 elif (self.x <= 6 and self.x >= 4):
 self.clicked = "5"
 elif (self.x <= 9 and self.x >= 7):
 self.clicked = "6"
 elif (self.x <= 12 and self.x >= 10):
 self.clicked = "*"
 elif (self.y <= 6 and self.y >= 4):
 if (self.x <= 3 and self.x >= 1):
 self.clicked = "7"
 elif (self.x <= 6 and self.x >= 4):
 self.clicked = "8"
 elif (self.x <= 9 and self.x >= 7):
 self.clicked = "9"
 elif (self.x <= 12 and self.x >= 10):
 self.clicked = "+"
 elif (self.y <= 3 and self.y >= 1):
 if (self.x <= 3 and self.x >= 1):
 self.clicked = ""
 elif (self.x <= 6 and self.x >= 4):
 self.clicked = "0"
 elif (self.x <= 9 and self.x >= 7):
 self.clicked = "."
 elif (self.x <= 12 and self.x >= 10):
 self.clicked = "-"
 elif (self.y <= 0 and self.y >= -2):
 if (self.x <= 12 and self.x >= 10):
 PrintedDisplay = Display(self.printed)
 FinAnswer = Calculate(PrintedDisplay.getDisplayNum())
 FinAnswer.concat()
 FinAnswer.calc()

 self.printedEquation.undraw()
 finalAnswer = Text(Point(6.5, 17), FinAnswer.getFinAnswer())
 finalAnswer.draw(self.win)
 i = "="
 elif (self.x <= 3 and self.x >= 1):
 self.clicked = ""
 self.printed = ""
 self.equation = []
 elif (self.x <= 6 and self.x >= 4):
 self.win.close()

 p = self.win.getMouse()
 self.x = p.getX()
 self.y = p.getY()

 if ((self.y <= 0 and self.y >= -2) and (self.x <= 3 and self.x >= 1)):
 finalAnswer.undraw()
 getInput(self.win)
 if ((self.y <= 0 and self.y >= -2) and (self.x <= 6 and self.x >= 4)):
 self.win.close()
 return self.clicked, self.equation, self.memory



class Display:
 def __init__(self, displayNum):
 self.displayNum = displayNum

 def getDisplayNum(self):
 return self.displayNum

 def setDisplayNum(self, newNum):
 self.displayNum = newNum


class Calculate:
 def __init__(self, display):
 self.display = display
 self.finAnswer = 0
 self.endOperation = 0

 def getFinAnswer(self):
 return self.finAnswer

 def eq(self, finalNum, i, equation=[]):
 del equation[i - 1:i + 2]
 equation.insert(i - 1, finalNum)
 print(equation)
 self.display = equation

 def multiply(self, num1, num2):
 self.endOperation = num1 * num2

 def divide(self, num1, num2):
 self.endOperation = num1 / num2

 def add(self, num1, num2):
 self.endOperation = num1 + num2

 def subtract(self, num1, num2):
 self.endOperation = num1 - num2

 def concat(self):
 finEq = []
 i = 0
 number = ""

 for n in range(len(self.display)):
 if self.display[n] == "+" or self.display[n] == "-" or self.display[n] == "*" or self.display[n] == "/":

 number = self.display[n - i: n]
 newNumber = "".join(number)
 finEq.append(newNumber)
 finEq.append(self.display[n])
 i = 0
 number = ""
 elif len(self.display) == n + 1:
 number = self.display[n - i: n + 1]
 newNumber = "".join(number)
 finEq.append(newNumber)
 i = 0
 number = ""
 else:
 i = i + 1

 self.display = finEq

 def calc(self):

 while len(self.display) != 1:

 while ("*" in self.display) or ("/" in self.display):

 for i in range(1, len(self.display)):
 if (self.display[i] == "*") or (self.display[i] == "/"):
 if self.display[i] == "*":
 self.multiply(float(self.display[i - 1]), float(self.display[i + 1]))
 self.endOperation = str(self.endOperation)
 self.eq(self.endOperation, i, self.display)
 break

 elif self.display[i] == "/":
 self.divide(float(self.display[i - 1]), float(self.display[i + 1]))
 self.endOperation = str(self.endOperation)
 self.ins(self.endOperation, i, self.display)
 break
 break

 for i in range(1, len(self.display)):
 if (self.display[i] == "+") or (self.display[i] == "-"):

 if self.display[i] == "+":
 self.add(float(self.display[i - 1]), float(self.display[i + 1]))
 self.endOperation = str(self.endOperation)
 self.eq(self.endOperation, i, self.display)
 break
 elif self.display[i] == "-":
 self.subtract(float(self.display[i - 1]), float(self.display[i + 1]))
 self.endOperation = str(self.endOperation)
 self.eq(self.endOperation, i, self.display)
 break

 break

 self.finAnswer = self.display[0]
main()
