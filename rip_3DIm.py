

# You need to take the code from the VolumeRaman and VRI_of_range
# files in the Z. Python_modules file in the passport

# You can find the range select for different file kinds
# in the "common_functions" package in the RIP library this is in


"""

Functions within this module should include:
    - Shading to a peak
    - Shading to a range
    - Shading to a ratio or peaks or ranges

It should be possible to image the shaded VRI slices
either as individual slices or simultaniously.

"""
import numpy as np
import matplotlib.pyplot as plt
import common_functions_wdf as cf
import rip_rearrange_wdf as rr

class shade_peak3D:
    """Shades a 2D Raman image to the intensity of a peak"""

    def __init__(self, name, p, colour_map):
        # Initiating the variables 
        self.name = name # The file name
        self.p = p #The peak wavenumber
        self.colour_map = colour_map # The matplotlib colormap

        
    def plotP_3D(self):
        ldb = cf.two_variables(self.name, self.p).peak_txt()
        XYZ = rr.rearrange3D_stack(self.name).stack3D()
        img = np.array(ldb).reshape(XYZ) 
        plt.figure(figsize=(7,7))
        plt.imshow(img,cmap=self.colour_map)
        #plt.colorbar()
        plt.grid(False)
        plt.show()

        
        
"""    You want to be able to plot all the layers individually (one) and together (all)

    Below is the code for printing each slice individually,
    you need to add a variable to select a specific slice e.g. 1,2,3,...,n



    def plotP_3D_one(self):
        ldb = cf.two_variables(self.name, self.p).peak_txt()
        df = cf.one_variable(self.name).raw()
        y = df['Unnamed: 1']
        Y = int(len(y.unique()))
        x = pd.read_csv(self.name,delimiter='\t')['#X']
        X = int(len(x.unique()))
        full = cf.one_variable(self.name).FullNum()
        XY = cf.one_variable(self.name).NumSpec()
        w = len(cf.one_variable(self.name).waves())
        Z = full/XY/w
        img = np.array(ldb).reshape((int(Z),int(Y),int(X)))
        plt.figure(figsize=(7,7))
        plt.imshow(img,cmap=self.colour_map)
        #plt.colorbar()
        plt.grid(False)
        plt.show()
"""


class shade_range3D:
    """Shades a 3D Raman image (volumetric Raman image/VRI) to the intensity of an averaged selected range"""

    def __init__(self, name, p1, p2, colour_map):
        # Initiating the variables 
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.colour_map = colour_map
        
    def plotR_3D(self):
        ldb = cf.three_variables(self.name, self.p1, self.p2).rng_txt()
        XYZ = rr.rearrange3D_stack(self.name).stack3D()
        img = np.array(ldb).reshape(XYZ) 
        plt.figure(figsize=(3,15))
        plt.imshow(img,cmap=self.colour_map)
        #plt.colorbar()
        plt.grid(False)
        plt.show()


class shade_ratio_P3D:
    """Shades a 3D Raman image (volumetric Raman image/VRI) to the intensity of a ratio of two Raman peaks"""

    def __init__(self, name, p1, p2, colour_map):
        # Initiating the variables 
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.colour_map = colour_map
    
    def plotPR_3D(self): 
        ldb1 = cf.two_variables(self.name, self.p1).peak_txt() # Ponting out where changes have happened
        ldb2 = cf.two_variables(self.name, self.p2).peak_txt() # Ponting out where changes have happened
        
        XYZ = rr.rearrange3D_stack(self.name).stack3D()
        img = np.array(ldb1/ldb2).reshape(XYZ) 
        plt.figure(figsize=(3,15))
        plt.imshow(img,cmap=self.colour_map)
        #plt.colorbar()
        plt.grid(False)
        plt.show()


class shade_ratio_R3D:
    """Shades a 3D Raman image (volumetric Raman image/VRI) to the intensity 
    of a ratio of two averaged Raman spectral ranges."""

    def __init__(self, name, p1, p2, p3, p4, colour_map):
        # Initiating the variables 
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.colour_map = colour_map

    def plotRR_3D(self):
        ldb1 = cf.three_variables(self.name, self.p1, self.p2).rng_txt()
        ldb2 = cf.three_variables(self.name, self.p3, self.p4).rng_txt()
        
        XYZ = rr.rearrange3D_stack(self.name).stack3D()
        img = np.array(ldb1/ldb2).reshape(XYZ) 
        plt.figure(figsize=(3,15))
        plt.imshow(img,cmap=self.colour_map)
        #plt.colorbar()
        plt.grid(False)
        plt.show()
        
"""
The next steps will be to provide a method of exporting arrays, 
so they can be imaged independently by people who know matplotlib etc. 

Imaging slices individually is also a further step (see previous note)

"""