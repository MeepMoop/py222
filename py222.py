#!/usr/bin/env python
from __future__ import print_function
import numpy as np

'''
    ┌──┐
    │ 0│
 ┌──┼──┼──┬──┐
 │ 4│ 2│ 1│ 5│
 └──┼──┼──┴──┘
    │ 3│
    └──┘

       ┌──┬──┐
       │ 0│ 1│
       ├──┼──┤
       │ 2│ 3│
 ┌──┬──┼──┼──┼──┬──┬──┬──┐
 │16│17│ 8│ 9│ 4│ 5│20│21│
 ├──┼──┼──┼──┼──┼──┼──┼──┤
 │18│19│10│11│ 6│ 7│22│23│
 └──┴──┼──┼──┼──┴──┴──┴──┘
       │12│13│
       ├──┼──┤
       │14│15│
       └──┴──┘

'''

def getSolved():
  return np.array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5])

def doMove(s, move):
  # [  U, U', U2,  R, R', R2,  F, F', F2]
  if move == 0:
    return s[[  2,  0,  3,  1, 20, 21,  6,  7,  4,  5, 10, 11, 12, 13, 14, 15,  8,  9, 18, 19, 16, 17, 22, 23]]
  elif move == 1:
    return s[[  1,  3,  0,  2,  8,  9,  6,  7, 16, 17, 10, 11, 12, 13, 14, 15, 20, 21, 18, 19,  4,  5, 22, 23]]
  elif move == 2:
    return s[[  3,  2,  1,  0, 16, 17,  6,  7, 20, 21, 10, 11, 12, 13, 14, 15,  4,  5, 18, 19,  8,  9, 22, 23]]
  elif move == 3:
    return s[[  0,  9,  2, 11,  6,  4,  7,  5,  8, 13, 10, 15, 12, 22, 14, 20, 16, 17, 18, 19,  3, 21,  1, 23]]
  elif move == 4:
    return s[[  0, 22,  2, 20,  5,  7,  4,  6,  8,  1, 10,  3, 12,  9, 14, 11, 16, 17, 18, 19, 15, 21, 13, 23]]
  elif move == 5:
    return s[[  0, 13,  2, 15,  7,  6,  5,  4,  8, 22, 10, 20, 12,  1, 14,  3, 16, 17, 18, 19, 11, 21,  9, 23]]
  elif move == 6:
    return s[[  0,  1, 19, 17,  2,  5,  3,  7, 10,  8, 11,  9,  6,  4, 14, 15, 16, 12, 18, 13, 20, 21, 22, 23]]
  elif move == 7:
    return s[[  0,  1,  4,  6, 13,  5, 12,  7,  9, 11,  8, 10, 17, 19, 14, 15, 16,  3, 18,  2, 20, 21, 22, 23]]
  elif move == 8:
    return s[[  0,  1, 13, 12, 19,  5, 17,  7, 11, 10,  9,  8,  3,  2, 14, 15, 16,  6, 18,  4, 20, 21, 22, 23]]

def doAlgStr(s, alg):
  moveInd = {"U": 0, "U'": 1, "U2": 2, "R": 3, "R'": 4, "R2": 5, "F": 6, "F'": 7, "F2": 8}
  moves = alg.split(" ")
  for move in moves:
    s = doMove(s, moveInd[move])
  return s

def isSolved(state):
  return np.array_equal(state, [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5])

def printCube(state):
  print("       ┌──┬──┐")
  print("       │ {}│ {}│".format(state[0], state[1]))
  print("       ├──┼──┤")
  print("       │ {}│ {}│".format(state[2], state[3]))
  print(" ┌──┬──┼──┼──┼──┬──┬──┬──┐")
  print(" │ {}│ {}│ {}│ {}│ {}│ {}│ {}│ {}│".format(state[16], state[17], state[8], state[9], state[4], state[5], state[20], state[21]))
  print(" ├──┼──┼──┼──┼──┼──┼──┼──┤")
  print(" │ {}│ {}│ {}│ {}│ {}│ {}│ {}│ {}│".format(state[18], state[19], state[10], state[11], state[6], state[7], state[22], state[23]))
  print(" └──┴──┼──┼──┼──┴──┴──┴──┘")
  print("       │ {}│ {}│".format(state[12], state[13]))
  print("       ├──┼──┤")
  print("       │ {}│ {}│".format(state[14], state[15]))
  print("       └──┴──┘")

if __name__ == '__main__':
  Y = "R U' R' U' F2 U' R U R' U F2"
  printCube(doAlgStr(getSolved(), Y))
