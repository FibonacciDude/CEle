import pandas as pd
import numpy as np
from collections import namedtuple
import math
nan = lambda s : isinstance(s, float) and math.isnan(s)

file = "gapjuncadjn2y.xlsx"
sheet = "N2Y_gap-junction_R2-4"

Neuron = namedtuple('Neuron', ['cls', 'func', 'id'])

def count(d):
    i = 0
    while nan(d[i]):
        i+=1
    p = d[i]
    d = d[i+1:]
    cnt = []
    i = 0
    for el in d:
        if nan(el):
            i+=1
        else:
            cnt.append((p, i+1))
            p = el
            i = 0
    cnt.append((p, i+1))
    return cnt

def get(i, d):
    s = 0
    for dd, cnt in d:
        s += cnt
        if i <= s:
            return dd


def read_dat(file):
    dat = np.array(pd.read_excel(file))[3:, :]
    head = count(dat[:, 0])
    funcs = count(dat[:, 1])
    print(head)
    print(count(dat[0]))
    neurons = {}
    for n, id_ in enumerate(dat[2, 3:-1]):
        cls, func = get(n, head), get(n, funcs)
        neurons[n] = Neuron(cls, func, id_)
    return neurons, dat[3:-1:, 3:-1]

neurons, arr = read_dat(file)
#print(neurons, arr.shape)
print(arr, arr.shape)
