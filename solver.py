#!/usr/bin/env python
from __future__ import print_function
import numpy as np
import py222

hO = np.ones(2186, dtype=np.int) * 12
hP = np.ones(5040, dtype=np.int) * 12

moveStrs = {0: "U", 1: "U'", 2: "U2", 3: "R", 4: "R'", 5: "R2", 6: "F", 7: "F'", 8: "F2"}

# generate pruning table for the piece orientation states
def genOTable(s, d, lm=-1):
  index = py222.indexO(py222.getOP(s))
  if d < hO[index]:
    hO[index] = d
    for m in range(9):
      if int(m / 3) == int(lm / 3):
        continue
      genOTable(py222.doMove(s, m), d + 1, m)

# generate pruning table for the piece permutation states
def genPTable(s, d, lm=-1):
  index = py222.indexP(py222.getOP(s))
  if d < hP[index]:
    hP[index] = d
    for m in range(9):
      if int(m / 3) == int(lm / 3):
        continue
      genPTable(py222.doMove(s, m), d + 1, m)

# IDA* which prints all optimal solutions
def IDAStar(s, d, moves, lm=-1):
  if py222.isSolved(s):
    printMoves(moves)
    return True
  else:
    sOP = py222.getOP(s)
    if d > 0 and d >= hO[py222.indexO(sOP)] and d >= hP[py222.indexP(sOP)]:
      dOptimal = False
      for m in range(9):
        if int(m / 3) == int(lm / 3):
          continue
        newMoves = moves[:]; newMoves.append(m)
        solved = IDAStar(py222.doMove(s, m), d - 1, newMoves, m)
        if solved and not dOptimal:
          dOptimal = True
      if dOptimal:
        return True
  return False

# print a move sequence from an array of move indices
def printMoves(moves):
  moveStr = ""
  for m in moves:
    moveStr += moveStrs[m] + " "
  print(moveStr)

# solve a cube state
def solveCube(s):
  # print cube state
  py222.printCube(s)

  # FC-normalize stickers
  print("normalizing stickers...")
  s = py222.normFC(s)

  import time
  timer = time.time()
  # generate pruning tables
  print("generating pruning tables...")
  genOTable(py222.initState(), 0)
  genPTable(py222.initState(), 0)
  print(time.time() - timer)
  
  # run IDA*
  print("searching...")
  solved = False
  depth = 1
  while depth <= 11 and not solved:
    print("depth {}".format(depth))
    solved = IDAStar(s, depth, [])
    depth += 1

# can generate pruning tables ahead of time
# genOTable(py222.initState(), 0)
# genPTable(py222.initState(), 0)

if __name__ == "__main__":
  # input some scrambled state
  s = py222.doAlgStr(py222.initState(), "R U2 R2 F2 R' F2 R F R")
  # solve cube
  solveCube(s)

