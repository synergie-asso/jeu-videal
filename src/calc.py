from tkinter import *
from math import *


def plus(a, b):
    return 0


def moins(a, b):
    return 0


def times(a, b):
    return 0


def divide(a, b):
    return 0


# noinspection PyTrailingSemicolon
class Calc:
    function = {
        '+': plus,
        '-': moins,
        '/': divide,
        '*': times,
        ' ': times
    }

    def result(self):
        self.a = self.function[self.op](self.a, self.b)
        self.op = ' '
        self.b = 0
        self.z.set(str(self.a))

    def lambdaAddOperator(self, x):
        def addOperator(y):
            self.op = y
            self.z.set(str(self.a) + self.op)

        return addOperator(x)

    def lambdaAddNumber(self, x):
        def addNumber(y):
            if self.op == ' ':
                self.a = self.a * 10 + y
                self.z.set(str(self.a))
                print(self.a)
            else:
                self.b = self.b * 10 + y
                self.z.set(str(self.a) + self.op + str(self.b))
                print(self.b)

        return addNumber(x);

    def __init__(self):
        self.text = ""
        self.a = 0
        self.b = 0
        self.op = ' '

        win = Tk()
        win.title('Calc')

        grid = Frame(win)
        grid.grid(row=1, column=0)
        self.z = StringVar()
        entree = Entry(win, textvariable=self.z)
        entree.grid(row=0, column=0)
        self.z.set("0")

        Button(grid, text=' 9 ', command=lambda: self.lambdaAddNumber(9), height=2, width=4).grid(row=5, column=2)
        Button(grid, text=' 8 ', command=lambda: self.lambdaAddNumber(8), height=2, width=4).grid(row=5, column=1)
        Button(grid, text=' 7 ', command=lambda: self.lambdaAddNumber(7), height=2, width=4).grid(row=5, column=0)
        Button(grid, text=' 6 ', command=lambda: self.lambdaAddNumber(6), height=2, width=4).grid(row=4, column=2)
        Button(grid, text=' 5 ', command=lambda: self.lambdaAddNumber(5), height=2, width=4).grid(row=4, column=1)
        Button(grid, text=' 4 ', command=lambda: self.lambdaAddNumber(4), height=2, width=4).grid(row=4, column=0)
        Button(grid, text=' 3 ', command=lambda: self.lambdaAddNumber(3), height=2, width=4).grid(row=3, column=2)
        Button(grid, text=' 2 ', command=lambda: self.lambdaAddNumber(2), height=2, width=4).grid(row=3, column=1)
        Button(grid, text=' 1 ', command=lambda: self.lambdaAddNumber(1), height=2, width=4).grid(row=3, column=0)
        Button(grid, text=' 0 ', command=lambda: self.lambdaAddNumber(0), height=2, width=4).grid(row=6, column=1)

        Button(grid, text='+', command=lambda: self.lambdaAddOperator('+'), height=2, width=4).grid(row=3, column=5,
                                                                                                    padx=3, pady=3)
        Button(grid, text='-', command=lambda: self.lambdaAddOperator('-'), height=2, width=4).grid(row=3, column=6,
                                                                                                    padx=3, pady=3)
        Button(grid, text='*', command=lambda: self.lambdaAddOperator('*'), height=2, width=4).grid(row=4, column=6,
                                                                                                    padx=3, pady=3)
        Button(grid, text='/', command=lambda: self.lambdaAddOperator('/'), height=2, width=4).grid(row=4, column=5,
                                                                                                    padx=3, pady=3)

        Button(grid, text='=', command=self.result, height=3, width=4).grid(row=6, column=5, padx=5, pady=5)

        Button(win, text='Quit', command=win.destroy).grid(row=6, column=4)
        win.mainloop()


if __name__ == '__main__':
    Calc()
