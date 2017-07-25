# Py222

Py222 is a 2x2x2 Rubik's Cube representation written in Python. It has support for applying individual moves to the puzzle, as well as space-separated algorithm strings specified in [WCA notation](https://www.worldcubeassociation.org/regulations/#article-12-notation).

The move definitions are written for a sticker representation, but there are functions to normalize the state's stickers relative to a fixed DLB corner, convert it into a fixed-corner piece orientation and permutation (OP) representation, and hash the OP representation into unique indices. Also included is a sample IDA* solver (solver.py) which makes use of these functions.

# Dependencies

* numpy

# Usage

```python
  # get solved state
  s = initState()
  printCube(s)
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
  s = doAlgStr(s, "x y R U' R' U' F2 U' R U R' U F2")
  printCube(s)
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
  s = normFC(s)
  printCube(s)
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