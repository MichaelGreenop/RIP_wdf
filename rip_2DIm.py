

# There might not have been much on the plotting of 2D Raman images
# As you can take the averages of the ranges from the common_function package and rearange
# with your own code

# You will potentially need to add this

"""

Functions within this module should include:
    - Shading to a peak
    - Shading to a range
    - Shading to a ratio or peaks or ranges

"""



import numpy as np
import matplotlib.pyplot as plt
import common_functions_wdf as cf
import rip_rearrange_wdf as rr


class shade_peak2D:
    """Shades a 2D Raman image to the intensity of a peak"""

    def __init__(self, name, p, colour_map):
        # Initiating the variables 
        self.name = name # The file name
        self.p = p #The peak wavenumber
        self.colour_map = colour_map # The matplotlib colormap

        
    def plotP_2D(self):
        ldb = cf.two_variables(self.name, self.p).peak_txt()
        XY = rr.rearrange2D(self.name).img()
        img = np.array(ldb).reshape(XY) 
        plt.figure(figsize=(3,15))
        plt.imshow(img,cmap=self.colour_map)
        #plt.colorbar()
        plt.grid(False)
        plt.show()



class shade_range2D:
    """Shades a 2D Raman image to the intensity of an averaged selected range"""

    def __init__(self, name, p1, p2, colour_map):
        # Initiating the variables 
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.colour_map = colour_map
        
    def plotR_2D(self):
        ldb = cf.three_variables(self.name, self.p1, self.p2).rng_txt()
        XY = rr.rearrange2D(self.name).img()
        img = np.array(ldb).reshape(XY)
        plt.figure(figsize=(3,15))
        plt.imshow(img,cmap=self.colour_map)
        #plt.colorbar()
        plt.grid(False)
        plt.show()


class shade_ratio_P2D:
    """Shades a 2D Raman image to the intensity of a ratio of two Raman peaks"""

    def __init__(self, name, p1, p2, colour_map):
        # Initiating the variables 
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.colour_map = colour_map
    
    def plotPR_2D(self): 
        ldb1 = cf.two_variables(self.name, self.p1).peak_txt()
        ldb2 = cf.two_variables(self.name, self.p2).peak_txt()
        XY = rr.rearrange2D(self.name).img()
        img = np.array(ldb1/ldb2).reshape(XY)
        plt.figure(figsize=(3,15))
        plt.imshow(img,cmap=self.colour_map)
        #plt.colorbar()
        plt.grid(False)
        plt.show()


class shade_ratio_R2D:
    """Shades a 2D Raman image to the intensity of a ratio of two averaged Raman spectral ranges."""

    def __init__(self, name, p1, p2, p3, p4, colour_map):
        # Initiating the variables 
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.colour_map = colour_map

    def plotRR_2D(self):
        ldb1 = cf.three_variables(self.name, self.p1, self.p2).rng_txt()
        ldb2 = cf.three_variables(self.name, self.p3, self.p4).rng_txt()
        
        XY = rr.rearrange2D(self.name).img()
        img = np.array(ldb1/ldb2).reshape(XY)
        plt.figure(figsize=(3,15))
        plt.imshow(img,cmap=self.colour_map)
        #plt.colorbar()
        plt.grid(False)
        plt.show()
        

"""
The next steps will be to provide a method of exporting arrays, 
so they can be imaged independently by people who know matplotlib etc. 

"""