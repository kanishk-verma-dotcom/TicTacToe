# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 07:27:37 2020

@author: Kanishk
"""
import pygame
import numpy as np
pygame.init()
import math
import time
import sys
import random


def best_move(board):
    n = len(board)
    best_score = -math.inf
    move = (0, 0)
    for i in range(n):
        for j in range(n):
            if board[i][j] == "":
                board[i][j] = "x"
                score = minimax(board, 0, False, len(board))
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    move = (i, j)
    board[move[0]][move[1]] = "x"
    return board

scores = {
        "x" : 10,
        "o" : -10,
        "tie": 0
    }

def minimax(board, depth, is_max, n, alpha = -math.inf, beta = math.inf):
    winner = check_win(board)
    if winner:
        # print(depth)
        return scores[winner]
    if is_max:
        best_score = -math.inf
        for i in range(n):
            for j in range(n):
                if board[i][j] == "":
                    board[i][j] = "x"
                    score = minimax(board, depth+1, False, n, alpha, beta)+random.randint(-5, 5)
                    board[i][j] = ""
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta >= alpha:
                        pass
        return best_score
    else:
        best_score = math.inf
        for i in range(n):
            for j in range(n):
                if board[i][j] == "":
                    board[i][j] = "o"
                    score = minimax(board, depth+1, True,n, alpha, beta)+random.randint(-5, 5)
                    board[i][j] = ""
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if alpha >= beta:
                        pass
        return best_score

def check_win(board):
    n = len(board)
    first = board[0][0]
   
    diagonal = first != ""
    for i in range(n):
        if board[i][i] != first:
            diagonal = False
            break
    if diagonal:
        return first
    first = board[0][n-1]
    back_diag = first != ""
    for i in range(1, n+1):
        if board[i-1][n-i] != first:
            back_diag = False
            break
    if back_diag:
        return first

    for i in range(n):
        first = board[i][0]
        sideways = first != ""
        for j in range(n):
            if board[i][j] != first:
                sideways = False
        if sideways:
            return first

    for i in range(n):
        first = board[0][i]
        # print(first)
        sideways = first != ""
        for j in range(n):
            if board[j][i] != first:
                sideways = False
        if sideways:
            return first
    
    open_spots = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == "":
                open_spots += 1
    if open_spots == 0:
        return "tie"
    return None