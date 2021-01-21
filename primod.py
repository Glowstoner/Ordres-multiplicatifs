#!/bin/python3

import matplotlib.pyplot as plt
import numpy as nump
import math

MAX = 10000

def f_pow(base, mod):
    for i in range(1, MAX+1):
        r = ((base**i)-1)/mod
        if r.is_integer():
            return int(i), int(r)

def f(base, mod):
    for i in range(1, MAX+1):
        r = base**i%mod
        if r == 1:
            return i
    return 0

def get_set(base, m):
    lx = []
    ly = []

    for i in range(1, m):
        lx.append(i)
        ly.append(f(base, i))
    return lx, ly

def get_set_fast(base, m):
    lx = []
    ly = []
    p  = []
    for i in range(1, m+1):
        for j in range(1, m+1):
            if (base**j)%i == 1:
                lx.append(i)
                ly.append(j)
                if j == i - 1:
                    p.append(i)
                break
        #print("*", i)
    return (p, (lx, ly))

def plot(n, m):
    fig, ax = plt.subplots()
    ax.set_title("g(a, m) = α {} premières bases".format(n))
    ax.set_ylabel("valeur de α = g(a, m)")
    ax.set_xlabel("valeur de m (modulo)")
    s = set()
    for i in range(0, n+1):
        p, l = get_set_fast(i, m)
        ax.plot(l[0], l[1])
        print("->", i)
        s.update(p)
    x = nump.linspace(0, m)
    y = x-1
    ax.plot(x, y)
    pl = list(s)
    pl.sort()
    print(pl)
    print(len(pl))
    plt.show()

def plot_one(n, m):
    fig, ax = plt.subplots()
    ax.set_title("g(a, m) = α avec une base a de {}".format(n))
    ax.set_ylabel("valeur de α = g(a, m)")
    ax.set_xlabel("valeur de m (modulo)")
    p, l = get_set_fast(n, m)
    ax.plot(l[0], l[1])
    x = nump.linspace(0, m)
    y = x-1
    #ax.plot(x, y)
    ls = list(p)
    ls.sort()
    print(ls)
    plt.show()

def frac_aprx(x, m):
    s = 0
    for i in range(1, m+1):
        s += (math.sin(2*i*math.pi*x))/i
    return 0.5-(s/math.pi)

def frac_basic(x):
    return x - math.floor(x)

def get_aprx(a, mod, m):
    f = lambda x: frac_aprx(math.log(mod*(x-frac_aprx(x, m)) + 1)/math.log(a), m)
    x = [0.1*k for k in range(1, 200000)]
    y = [f(k) for k in x]
    plt.plot(x, y)

def get_basic(a, mod):
    f = lambda x: frac_basic(math.log(mod*math.floor(x)+1)/math.log(a))
    x = [0.1*k for k in range(1, 200000)]
    y = [f(k) for k in x]
    plt.plot(x, y)
