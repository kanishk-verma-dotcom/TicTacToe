# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 07:26:43 2020

@author: Kanishk
"""
# Importing packages and other project dependencies
import pygame
import numpy as np
pygame.init()
import math
import time
import sys
import random
import time

from screenFunctions import rect, square, ellipse, circle, background, reset

from ticfunctions import best_move, minimax, check_win


SIZE = WIDTH, HEIGHT = 470, 470

def text_objects(text, font):
    white = (255,255,255)
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def text_objects1(text, font):
    black = (0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def main():
    padding = 10
    n = 3
    s = (WIDTH-padding*2)//n
    
    board = [["" for i in range(n)] for j in range(n)]

    turn = "x"

    x_image = pygame.image.load(r"C:\Users\Kanishk Verma\Desktop\TicTacToe\x.png")
    x_image = pygame.transform.scale(x_image, (s, s))
    o_image = pygame.image.load(r"C:\Users\Kanishk Verma\Desktop\TicTacToe\o.png")
    o_image = pygame.transform.scale(o_image, (s, s))

    loop = True
    gameover = False

    frame_count = 0
    human_played = False
    winner = False
    restarted = False
    
    running = True
    board = best_move(board)
    turn = "x" if turn == "o" else "o"
    # print(f"{turn}'s Turn")
    largeText = pygame.font.Font('freesansbold.ttf',30)
    
    screen = pygame.display.set_mode(SIZE) #Start the screen
    #alpha = 0
    TextSurf, TextRect = text_objects("Beat         Kanishk's TicTacToe AI Robot", largeText)
    TextRect.center = ((WIDTH/3),(HEIGHT/3))
    #TextSurf.fill((0, 0, 0, alpha), special_flags=pygame.BLEND_RGBA_MULT)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    TextSurf, TextRect = text_objects("Human you are O", largeText)
    TextRect.center = ((WIDTH/2),(HEIGHT/2))
    #TextSurf.fill((0, 0, 0, alpha), special_flags=pygame.BLEND_RGBA_MULT)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    
    
    while running:
        prev = frame_count
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
                if event.type == pygame.QUIT: #The user closed the window!
                    running = False #Stop running
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        board, loop, winner, restarted = reset(n)
                        
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    j = int(Mouse_x//s)
                    i = int(Mouse_y//s)
                    if i < n and j < n:
                        if board[i][j] == "":
                            board[i][j] = turn
                            turn = "x" if turn == "o" else "o"
                            # print(f"{turn}'s Turn")
                            human_played = True
                        winner = check_win(board)
                        # print(np.array(board))
                                

        if loop:
            rect(screen, (255, 255, 255), padding, padding, WIDTH-padding*2, HEIGHT-padding*2)
            
            # Logic goes here
            if not winner:
                winner = check_win(board)
            # print(winner)
            if winner:
                if winner == "tie":
                    print(winner.upper()+"!")
                    TextSurf, TextRect = text_objects1("It's a "+winner.upper()+'!', largeText)
                    #alpha = 0
                    #TextSurf.fill((255, 255, 255, alpha), special_flags=pygame.BLEND_RGBA_MULT)
                    TextRect.center = ((WIDTH/2),(HEIGHT/2))
                    screen.blit(TextSurf, TextRect)
                    
                    pygame.display.update()
                    time.sleep(2)
                else:
                    TextSurf, TextRect = text_objects1('AI is a WINNER!, you loose', largeText)
                    #TextSurf.fill((255, 255, 255, alpha), special_flags=pygame.BLEND_RGBA_MULT)
                    TextRect.center = ((WIDTH/2),(HEIGHT/2))
                    screen.blit(TextSurf, TextRect)
    
                    pygame.display.update()
                    time.sleep(2)
                    
                print("Press 'r' to restart")
                loop = False

            for i in range(n):
                for j in range(n):
                    item = board[i][j]
                    if item == "x":
                        screen.blit(x_image, (j*s+padding, i*s+padding))
                    elif item == "o":
                        screen.blit(o_image, (j*s+padding, i*s+padding))
                    square(screen, (0,0, 0), j*s+padding, i*s+padding, s, 3)


            pygame.display.update()

            if restarted:
                turn = "x"
                board = best_move(board)
                turn = "x" if turn == "o" else "o"
                restarted = False

            if human_played:
                time.sleep(.5)
                board = best_move(board)
                turn = "x" if turn == "o" else "o"
                # print(f"{turn}'s Turn")
                human_played = False
            frame_count += 1
    pygame.quit() #Close the window
    
    
if __name__ == "__main__":
    main()