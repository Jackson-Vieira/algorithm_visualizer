import pygame
import random

from sys import exit
from time import time

from settings import *
from algorithms import *

pygame.init()

class DrawSettings:
    def __init__(self, lst):
        self.screen = pygame.display.set_mode((LOBBY_DISPLAY_WIDTH, LOBBY_DISPLAY_HEIGTH))
        pygame.display.set_caption(NAME)
        self.algorithm = None
        self.sett_lst(lst)
    
    def sett_lst(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        self.unsorted = False

        self.block_width =  round((DISPLAY_WIDTH - SIDE_PADDING) / len(lst))
        self.block_height = round((DISPLAY_HEIGTH - TOP_PADDING) / (self.max_val - self.min_val))
        self.pos_x = SIDE_PADDING//2

    def drawList(self, index_colors = {}):
        self.screen.fill(BG_COLOR)

        for i, elm in enumerate(self.lst):
            x = self.pos_x + i * self.block_width
            y = DISPLAY_HEIGTH - (elm - self.min_val) * self.block_height

            color = BLOCK_COLORS[i%2]

            if i in index_colors:
                color = index_colors[i]
            
            pygame.draw.rect(self.screen, (color), (x, y, self.block_width, DISPLAY_WIDTH))

        pygame.display.update()


def update(draw_sett):
    draw_sett.screen.fill(BG_COLOR)
    draw_sett.drawList()

def generateList(n):
    lst = [i for i in range(n)]
    random.shuffle(lst)
    return lst

def drawText(draw_sett, algorithm, pos):
    font = pygame.font.get_default_font()
    font_obj = pygame.font.SysFont(font, 24)
    font_render = font_obj.render(f"{algorithm}", True, (255,255,255))
    draw_sett.screen.blit(font_render, pos)

def lobby(draw_sett):
    algorithms = ['1 - BubbleSort', '2 - SelectionSort', '3 - InsertionSort', '4 - MergeSort', 'ESC - Quit']
    buttons_pos = [(10, 20),(10, 50),(10, 80),(10, 110), (10, 140)]
    while True:
        draw_sett.screen.fill(BG_COLOR)
        x = 0
        for pos in buttons_pos:
            drawText(draw_sett, algorithms[x], pos)
            x += 1

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_1:
                    return 0
                if event.key == pygame.K_2:
                    return 1
                if event.key == pygame.K_3:
                    return 2
                if event.key == pygame.K_4:
                    return 3

        pygame.display.update()

def event():
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main()

def main():
    clock = pygame.time.Clock()
    algorithms = [bubbleSort, selectionSort, insertionSort, mergeSort]
    unsorted = True

    lst = generateList(NUMBER_OF_COLUMNS)
    draw_setts = DrawSettings(lst)
    index = lobby(draw_setts)
    algorithm = algorithms[index]
    alg_generator = algorithm(draw_setts)

    draw_setts.screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGTH))
    run = True

    inicio = time()
    while run:
        clock.tick(FPS)

        if unsorted:
            """Expecif case for mergeSort"""
            if algorithm == mergeSort:  
                    for merge in alg_generator:
                        for n in merge: 
                            event()
                    unsorted = False
                    end = time()
                    print("FINISH")
                    print(f"Time: {end-inicio:.2f} segundo(s)")
                    
            else:
                try:
                    next(alg_generator)

                except StopIteration:
                    unsorted = False
                    end = time()
                    print("FINISH")
                    print(f"Time: {end-inicio:.2f} segundo(s)")
                    
        else:
            update(draw_setts)
        
        event()
    
if __name__ == "__main__":
    main()