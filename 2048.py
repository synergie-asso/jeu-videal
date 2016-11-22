from random import randrange

from src.display3 import Display

size = 4


def fusion(carre1, carre2):
    return carre1 * 2


def isFusion(carre1, carre2):
    return carre1 == carre2


def win(tab):
    for i in range(len(tab)):
        if tab[i] == 64:
            return True
    return False


def check(grid, x, y, i, j):
    if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid) - 1:
        return False
    return grid[i][j] == grid[x][y]


def lose(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                return False
            else:
                if check(grid, i, j, i - 1, j) or check(grid, i, j, i + 1, j) or check(grid, i, j, i, j - 1) or check(
                        grid, i, j, i, j + 1):
                    return False
    return True


def newNumber():
    if randrange(4) == 0:
        return 4
    else:
        return 2


def main():
    grid = [[Square(0)] * size for _ in range(size)]
    liste = [Square(0)] * size * size
    d = Display(size)
    d.print_grid(grid)
    addNumber(grid)

    while (not lose(grid)):
        d.print_grid(grid)
        moved = False
        while not moved:
            dir = d.newDirection()
            if dir == 0:
                d.quit()
                return
            moved = moveNumber(grid, dir)
        addNumber(grid)
        for i in range(size):
            for j in range(size):
                liste[i + size * j] = grid[i][j]
        if (win(liste)):
            print("win")
    print("Lose")
    d.quit();


def moveNumber(grid, dir):
    hasmoved = False
    if dir % 2 == 0:
        for i in range(1 if dir > 0 else size - 2, size if dir > 0 else -1, dir // 2):
            for j in range(size):
                if grid[i][j] != 0:
                    k = i - dir // 2
                    move = True
                    while (k >= 0 if dir > 0 else k < size) and move:
                        if grid[k][j] != 0:
                            if grid[k][j].fusion or grid[i][j].fusion or not isFusion(grid[k][j].value,
                                                                                      grid[i][j].value):
                                if k + dir // 2 != i:
                                    hasmoved = True
                                    n = grid[i][j]
                                    grid[i][j] = Square(0)
                                    grid[k + dir // 2][j] = n
                            else:
                                hasmoved = True
                                grid[k][j] = Square(fusion(grid[i][j].value, grid[k][j].value));
                                grid[k][j].fusion = True
                                grid[i][j] = Square(0)
                            move = False
                        elif k == 0 or k == size - 1:
                            hasmoved = True
                            grid[k][j] = grid[i][j]
                            grid[i][j] = Square(0)
                            move = False
                        k -= dir // 2
    else:
        for j in range(1 if dir > 0 else size - 2, size if dir > 0 else -1, dir):
            for i in range(size):
                if grid[i][j] != 0:
                    k = j - dir
                    move = True
                    while (k >= 0 if dir > 0 else k < size) and move:
                        if grid[i][k] != 0:
                            if grid[i][k].fusion or grid[i][j].fusion or not isFusion(grid[i][k].value,
                                                                                      grid[i][j].value):
                                if k + dir != j:
                                    hasmoved = True
                                    n = grid[i][j]
                                    grid[i][j] = Square(0)
                                    grid[i][k + dir] = n
                            else:
                                hasmoved = True
                                grid[i][k] = Square(fusion(grid[i][j].value, grid[i][k].value));
                                grid[i][k].fusion = True
                                grid[i][j] = Square(0)
                            move = False
                        elif k == 0 or k == size - 1:
                            hasmoved = True
                            grid[i][k] = grid[i][j]
                            grid[i][j] = Square(0)
                            move = False
                        k -= dir
    for i in range(size):
        for j in range(size):
            grid[i][j].fusion = False
    return hasmoved


def addNumber(grid):
    count = 0;
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 0:
                count += 1
    number = randrange(count) + 1
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 0:
                number -= 1
                if number == 0:
                    grid[i][j] = Square(newNumber())


class Square:
    def __init__(self, v):
        self.value = v
        self.fusion = False;

    def __int__(self):
        return self.value

    def __add__(self, other):
        return self.value + other

    def __mul__(self, other):
        return self.value * other

    def __float__(self):
        return (float)(self.value)

    def ___le__(self, other):
        return self.value <= other

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return self.value != other

    def __gt__(self, other):
        return self.value > other

    def __ge__(self, other):
        return self.value >= other

    def __str__(self):
        return str(self.value)


if __name__ == "__main__":
    main()
