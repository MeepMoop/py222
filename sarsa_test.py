import py222
import numpy as np
from nnpy import nn

n_features = 24
n_hidden = 256
n_actions = 9

n_eps = 10000
n_steps = 100

eps = 1.0
gamma = 1.0
alpha = 0.0001
rho = 0.7

Q = nn(n_features)
Q.add_layer('tanh', n_hidden)
Q.add_layer('tanh', n_hidden)
Q.add_layer('linear', n_actions)

def initState():
  s = py222.initState()
  lm = -3
  for i in range(1):
    m = np.random.randint(n_actions)
    while int(m / 3) == int(lm / 3):
      m = np.random.randint(n_actions)
    s = py222.doMove(s, m)
    lm = m
  return s

def chooseAction(s):
  if np.random.random() > eps:
    Q.forward(s)
    Qs = Q.output()
    return np.argmax(Qs)
  else:
    return np.random.randint(n_actions)

s_avg = 0.0
for ep in range(1, n_eps + 1):
  s = initState()
  a = chooseAction(s)
  for step in range(1, n_steps + 1):
    r = -1
    sp = py222.doMove(s, a)
    ap = chooseAction(sp)
    if py222.isSolved(sp):
      Q.forward(s)
      Qs = Q.output()
      Qs[a] = r
      Q.backward_mom(Qs, alpha, rho)
      break
    Q.forward(sp)
    Qmax = np.max(Q.output())
    Q.forward(s)
    Qs = Q.output()
    #print(Qs)
    Qs[a] = r + gamma * Qmax
    Q.backward_mom(Qs, alpha, rho)
    s = sp
    a = ap
  s_avg += (1 / ep) * (step - s_avg)
  print("ep: {}, moves: {}, avg_moves: {}".format(ep, step, s_avg))
<<<<<<< HEAD:test.py
  eps *= 0.99
print(np.round(Q, 2))
=======
print(Q)
>>>>>>> a8f116d02b78bc941a9529c3d9298243a5ac9d34:sarsa_test.py
