import pygame
from pygame.locals import *
from math import log


class Display:
    def __init__(self, size):
        self.size = size
        pygame.init()
        self.window = pygame.display.set_mode((600, 600))
        red = (255, 0, 0)

        pygame.display.update()


    def waitEvent(self):
       for event in pygame.event.get():
           self.size = self.size
       while True :
           for event in pygame.event.get():
               if event.type == QUIT:
                   return 
               if event.type == KEYDOWN:
                   return      




    def quit(self):
        pygame.time.wait(1000)
        self.waitEvent()
        pygame.display.quit()
        pygame.quit()
        print("Exit Game")

    def newDirection(self):
        continuer = 1
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return 0
                if event.type == KEYDOWN and event.key == K_LEFT:
                    return 2
                if event.type == KEYDOWN and event.key == K_UP:
                    return 1
                if event.type == KEYDOWN and event.key == K_RIGHT:
                    return -2
                if event.type == KEYDOWN and event.key == K_DOWN:
                    return -1

    def print_grid(self, grid):
        pygame.draw.rect(self.window, (50, 50, 50), (50, 50, 500, 500));
        print();
        sizeSquare = 500 // self.size
        font = pygame.font.SysFont(None, 30)
        for j in range(self.size):
            for i in range(self.size):
                if grid[i][j] == 0:
                    pygame.draw.rect(self.window, (50, 50, 50), (
                    50 + sizeSquare * i + 1, 50 + sizeSquare * j + 1, sizeSquare - 2, sizeSquare - 2));
                else:
                    rect = pygame.draw.rect(self.window, (255,
                                                          255 - log(grid[i][j], 2) * 20, 20),
                                            (50 + sizeSquare * i + 1,
                                             50 + sizeSquare * j + 1,
                                             sizeSquare - 2, sizeSquare - 2))
                    number = font.render(str(grid[i][j]), 1, (10, 10, 10))
                    textpos = number.get_rect()
                    textpos.centerx = rect.centerx
                    textpos.centery = rect.centery
                    print(textpos)
                    self.window.blit(number, textpos)

    def print_score(self,score):
        pygame.draw.rect(self.window, (20, 20, 20), (440, 10, 200, 40));
        font = pygame.font.SysFont(None, 30)
        s = font.render("Score : "  + str(score), 1, (200, 200, 200))
        self.window.blit(s, (450, 20))
        pygame.display.update()


    def print_text(self, text):
        pygame.draw.rect(self.window, (0, 0, 0), (5, 20, 200, 40));
        font = pygame.font.SysFont(None, 30)
        s = font.render(text,  1, (200, 50, 50))
        self.window.blit(s, (10, 20))
        pygame.display.update()

