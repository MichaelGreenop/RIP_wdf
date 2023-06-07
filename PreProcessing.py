# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:44:16 2021

@author: greenopm
"""

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve

def baseline_als(y):
    lam = 100
    p = 0.0001
    niter=10
    L = len(y)
    D = sparse.diags([1,-2,1],[0,-1,-2], shape=(L,L-2))
    w = np.ones(L)
    for i in range(niter):
        W = sparse.spdiags(w, 0, L, L)
        Z = W + lam * D.dot(D.transpose())
        z = spsolve(Z, w*y)
        w = p * (y > z) + (1-p) * (y < z)
    return z

def smoothTriangle(data, dropVals=False):
    degree = 3
    triangle=np.array(list(range(degree)) + [degree] + list(range(degree)[::-1])) + 1
    smoothed=[]

    for i in range(degree, len(data) - degree * 2):
        point=data[i:i + len(triangle)] * triangle
        smoothed.append(sum(point)/sum(triangle))
    if dropVals:
        return smoothed
    smoothed=[smoothed[0]]*int(degree + degree/2) + smoothed
    while len(smoothed) < len(data):
        smoothed.append(smoothed[-1])
    return smoothed

def EachRow(function, dimensions, data):
    new_df = np.apply_along_axis(function, dimensions, data)
    return new_df


