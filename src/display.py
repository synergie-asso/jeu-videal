from math import log10, ceil;
import sys;


class Display() :
    def __init__(self, size):
        self.size = size;


    def quit(self) :
        print("Exit Game");


    def newDirection(self) :
        while True:
            char = sys.stdin.read(1);
            if (char == "z"):
                print("dir : 1");
                return 1;
            if (char == "q"):
                print("dir : 2");
                return 2;
            if (char == "s"):
                print("dir : -1");
                return -1;
            if (char == "d"):
                print("dir : -2");
                return -2;
            print ("Type 'z','q', 's' or 'd'");



    def print_grid (self, grid) :
        for j in range(self.size) :
            for i in range(self.size) :
                if grid[i][j] == 0 :
                    for k in range(5) :
                        print(" ", end="");
                else :
                    spaces = 5 - ceil(log10(grid[i][j]))
                    for k in range(spaces // 2) :
                        print(" ", end="");
                    print(grid[i][j], end="");
                    for k in range(spaces // 2 + spaces % 2) :
                        print(" ", end="");
                print("|", end="");
            print();
            for i in range(6 * self.size) :
                print("_", end="");
            print();
