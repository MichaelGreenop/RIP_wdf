# -*- coding: utf-8 -*-
"""
Created on Thu May 20 18:47:02 2021

@author: customer
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

name = 'Flow_cellVRI_1 - CR - Nf - Bc.txt'


# Importing the dataset and determine the range analysed
def NumSpec(name):
    y = pd.read_csv(name,delimiter='\t')['Unnamed: 1']
    Y = len(y.unique())
    x = pd.read_csv(name,delimiter='\t')['#X']
    X = len(x.unique())
    return Y*X

def Dimensions2D(name):
    y = pd.read_csv(name,delimiter='\t')['Unnamed: 1']
    Y = len(y.unique())
    x = pd.read_csv(name,delimiter='\t')['#X']
    X = len(x.unique())
    print(Y)
    print(X)
    
def DimensionsReshape2D(name):
    y = pd.read_csv(name,delimiter='\t')['Unnamed: 1']
    Y = len(y.unique())
    x = pd.read_csv(name,delimiter='\t')['#X']
    X = len(x.unique())
    return(Y,X)

def lenSpec(name):
    l = pd.read_csv(name, delimiter='\t')['#Y']
    ln = len(l.unique())
    return ln

def FullNum(name):
    z = pd.read_csv(name, delimiter='\t')['#Y']
    Zl = len(z)
    return Zl

# Select the wavelength range 
def waves(name):
    w = pd.read_csv(name, delimiter='\t')['#Y']
    ln = int(len(w.unique()))
    length = int(len(w)/ln)
    W = np.array(w).reshape((length,ln))[0]
    return W

# Need too add the correct X*Y*Z to this part 
def DataMat2D(name):
    w = pd.read_csv(name, delimiter='\t')['#Y']
    data = pd.read_csv(name,delimiter='\t')['Unnamed: 3']
    X = int(len(w.unique()))
    Y = int(len(w)/X)
    df = np.array(data).reshape((Y,X))
    return df

# plot the sample spectrum 'y'
def plotSpec(x, y):
    spectra = DataMat2D(x)[y]
    plt.plot(waves(x), spectra)

# index values for set wavenumbers 
def rngSel(name,i,j):
    data = waves(name)
    result1 = np.where(data.astype(int) == i)
    result2 = np.where(data.astype(int) == j)
    return result1, result2

# Selecting the range from the data matrix
def rng_txt(name,i,j):
    data = DataMat2D(name)
    Rng = data[:,i:j]
    Mean = pd.DataFrame(Rng).T.mean()
    return Mean

def rng_csv(name,i,j):
    data = np.array(name)
    Rng = data[:,i:j]
    Mean = pd.DataFrame(Rng).T.mean()
    return Mean

# Determaning the number of z-steps (z-dimension)
def Znum(name):
    full = FullNum(name)
    XY = NumSpec(name)
    w = len(waves(name))
    Z = full/XY/w
    return Z  

# Rearanging the mean of the range into the 3D array
def Rng3D_txt(name, i, j):
    data = rng(name,i,j)
    y = pd.read_csv(name,delimiter='\t')['Unnamed: 1']
    Y = int(len(y.unique()))
    x = pd.read_csv(name,delimiter='\t')['#X']
    X = int(len(x.unique()))
    Z = int(Znum(name))
    df = np.array(data).reshape((Z,Y,X))
    return df

def Rng3D_csv(name, data, i, j):
    y = pd.read_csv(name,delimiter='\t')['Unnamed: 1']
    Y = int(len(y.unique()))
    x = pd.read_csv(name,delimiter='\t')['#X']
    X = int(len(x.unique()))
    Z = int(Znum(name))
    data = rng_csv(data,i,j)
    df = np.array(data).reshape((Z,Y,X))
    return df

# Plotting a slice 
def slicePlot(name, i, j, k):
    df = Rng3D(name, i, j)
    plt.imshow(df[k])
