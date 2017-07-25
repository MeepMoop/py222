# Py222

Py222 is a 2x2x2 Rubik's Cube representation written in Python. It has support for applying individual moves to the puzzle, as well as space-separated algorithm strings specified in [WCA notation](https://www.worldcubeassociation.org/regulations/#article-12-notation).

The move definitions are written for a sticker representation, but there are functions to normalize the state's stickers relative to a fixed DLB corner, convert it into a fixed-corner piece orientation and permutation (OP) representation, and hash the OP representation into unique indices. Also included is a sample IDA* solver (solver.py) which makes use of these functions. 

# Dependencies

* numpy

# Usage

```python
  import py222

  # get solved state
  s = py222.initState()
  py222.printCube(s)
```
```
      ┌──┬──┐
      │ 0│ 0│
      ├──┼──┤
      │ 0│ 0│
┌──┬──┼──┼──┼──┬──┬──┬──┐
│ 4│ 4│ 2│ 2│ 1│ 1│ 5│ 5│
├──┼──┼──┼──┼──┼──┼──┼──┤
│ 4│ 4│ 2│ 2│ 1│ 1│ 5│ 5│
└──┴──┼──┼──┼──┴──┴──┴──┘
      │ 3│ 3│
      ├──┼──┤
      │ 3│ 3│
      └──┴──┘
```
```python
  # do some moves
  s = py222.doAlgStr(s, "x y R U' R' U' F2 U' R U R' U F2")
  py222.printCube(s)
```
```
      ┌──┬──┐
      │ 2│ 2│
      ├──┼──┤
      │ 2│ 2│
┌──┬──┼──┼──┼──┬──┬──┬──┐
│ 0│ 3│ 1│ 4│ 3│ 0│ 4│ 1│
├──┼──┼──┼──┼──┼──┼──┼──┤
│ 3│ 3│ 1│ 1│ 0│ 0│ 4│ 4│
└──┴──┼──┼──┼──┴──┴──┴──┘
      │ 5│ 5│
      ├──┼──┤
      │ 5│ 5│
      └──┴──┘
```
```python
  # normalize stickers relative to DLB
  s = py222.normFC(s)
  py222.printCube(s)
```
```

      ┌──┬──┐
      │ 0│ 0│
      ├──┼──┤
      │ 0│ 0│
┌──┬──┼──┼──┼──┬──┬──┬──┐
│ 1│ 4│ 2│ 5│ 4│ 1│ 5│ 2│
├──┼──┼──┼──┼──┼──┼──┼──┤
│ 4│ 4│ 2│ 2│ 1│ 1│ 5│ 5│
└──┴──┼──┼──┼──┴──┴──┴──┘
      │ 3│ 3│
      ├──┼──┤
      │ 3│ 3│
      └──┴──┘
```

# Solver Usage

```python
import py222
import solver

# get solved state
s = py222.initState()

# apply some scramble
s = py222.doAlgStr(s, "R U2 R2 F2 R' F2 R F R")

# solve cube
solver.solveCube(s)
```
```
      ┌──┬──┐
      │ 2│ 3│
      ├──┼──┤
      │ 1│ 0│
┌──┬──┼──┼──┼──┬──┬──┬──┐
│ 1│ 3│ 5│ 4│ 2│ 2│ 4│ 3│
├──┼──┼──┼──┼──┼──┼──┼──┤
│ 4│ 2│ 0│ 0│ 4│ 1│ 0│ 5│
└──┴──┼──┼──┼──┴──┴──┴──┘
      │ 1│ 5│
      ├──┼──┤
      │ 3│ 5│
      └──┴──┘
normalizing stickers...
generating pruning tables...
searching...
depth 1
depth 2
depth 3
depth 4
depth 5
depth 6
depth 7
depth 8
F R2 F' R U2 R2 F' R 
F R2 F' R' F R2 U2 R' 
```
