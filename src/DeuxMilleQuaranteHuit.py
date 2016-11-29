from random import randrange

from src.display import Display
from src.square import Square
from tools import win, lose, fusion, isFusion, scoreFusion


def new_number():
    return 4 if randrange(4) == 0 else 2


class DeuxMilleQuaranteHuit:
    def __init__(self, size=4):
        self.size = size
        self.score = 0
        self.grid = [[Square(0)] * size for _ in range(size)]
        tab = [Square(0)] * size * size
        self.d = Display(size)
        self.add_number()

        while not lose(self.grid):
            moved = False
            while not moved:
                self.d.print_grid(self.grid)
                self.d.print_score(self.score)
                self.dir = self.d.newDirection()
                if self.dir == 0:
                    self.d.quit()
                    return
                moved = self.move_number()
                self.add_number()
            for i in range(size):
                for j in range(size):
                    tab[i + size * j] = self.grid[i][j]
            if win(tab):
                print("win")
        print("Lose")
        self.d.quit()

    def add_number(self):
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    count += 1
        if not count:
            print("Lose")
            self.d.quit()
        number = randrange(count) + 1
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    number -= 1
                    if number == 0:
                        self.grid[i][j] = Square(new_number())

    def move_number(self):
        has_moved = False
        if self.dir % 2 == 0:
            for i in range(1 if self.dir > 0 else self.size - 2, self.size if self.dir > 0 else -1, self.dir // 2):
                for j in range(self.size):
                    if self.grid[i][j] != 0:
                        k = i - self.dir // 2
                        move = True
                        while (k >= 0 if self.dir > 0 else k < self.size) and move:
                            if self.grid[k][j] != 0:
                                if self.grid[k][j].fusion or self.grid[i][j].fusion or not isFusion(
                                        self.grid[k][j].value,
                                        self.grid[i][j].value):
                                    if k + self.dir // 2 != i:
                                        has_moved = True
                                        n = self.grid[i][j]
                                        self.grid[i][j] = Square(0)
                                        self.grid[k + self.dir // 2][j] = n
                                else:
                                    has_moved = True
                                    self.score = scoreFusion(self.grid[i][j].value, self.score)
                                    self.grid[k][j] = Square(fusion(self.grid[i][j].value, self.grid[k][j].value))
                                    self.grid[k][j].fusion = True
                                    self.grid[i][j] = Square(0)
                                move = False
                            elif k == 0 or k == self.size - 1:
                                has_moved = True
                                self.grid[k][j] = self.grid[i][j]
                                self.grid[i][j] = Square(0)
                                move = False
                            k -= self.dir // 2
        else:
            for j in range(1 if self.dir > 0 else self.size - 2, self.size if self.dir > 0 else -1, self.dir):
                for i in range(self.size):
                    if self.grid[i][j] != 0:
                        k = j - self.dir
                        move = True
                        while (k >= 0 if self.dir > 0 else k < self.size) and move:
                            if self.grid[i][k] != 0:
                                if self.grid[i][k].fusion or self.grid[i][j].fusion or not isFusion(
                                        self.grid[i][k].value,
                                        self.grid[i][j].value):
                                    if k + self.dir != j:
                                        has_moved = True
                                        n = self.grid[i][j]
                                        self.grid[i][j] = Square(0)
                                        self.grid[i][k + self.dir] = n
                                else:
                                    has_moved = True
                                    self.score = scoreFusion(self.grid[i][j].value, self.score)
                                    self.grid[i][k] = Square(fusion(self.grid[i][j].value, self.grid[i][k].value))
                                    self.grid[i][k].fusion = True
                                    self.grid[i][j] = Square(0)
                                move = False
                            elif k == 0 or k == self.size - 1:
                                has_moved = True
                                self.grid[i][k] = self.grid[i][j]
                                self.grid[i][j] = Square(0)
                                move = False
                            k -= self.dir
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j].fusion = False
        return has_moved
