import py222
import numpy as np

n_features = 24
n_actions = 9

n_eps = 10000
n_steps = 1000

eps = 0.0
gamma = 1.0
alpha = 0.001

Q = np.random.randn(n_actions, n_features)

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
    Qs = np.dot(Q, s)
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
      Q[a] += alpha * (r - np.dot(Q[a], s)) * s
      break
    Q[a] += alpha * (r + gamma * np.dot(Q[ap], sp) - np.dot(Q[a], s)) * s
    s = sp
    a = ap
  s_avg += (1 / ep) * (step - s_avg)
  print("ep: {}, moves: {}, avg_moves: {}".format(ep, step, s_avg))
print(Q)
