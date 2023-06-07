
from renishawWiRE import WDFReader
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import common_functions_wdf as cf
import rip_rearrange_wdf as rr

class KMS_img2D:
    
    """"""
    
    def __init__(self, name, data, clusters):
        
        self.name = name
        self.data = data
        self.clusters = clusters
     
    def Kmeans_img(self):
        kmeans = KMeans(n_clusters=self.clusters, random_state=0).fit(self.data)
        df = np.array(kmeans.labels_)
        XY = rr.rearrange2D(self.name).img()
        img = np.array(df).reshape(XY)
        plt.figure()
        plt.imshow(img)
        plt.colorbar() 
        plt.grid(False)
        plt.show()
        
    def Kmeans_array(self):
        kmeans = KMeans(n_clusters=self.clusters, random_state=0).fit(self.data)
        df = np.array(kmeans.labels_)
        reader = WDFReader(self.name)
        spectra = reader.spectra
        shp = spectra.shape
        cluster_array = np.array(df).reshape((shp[0],shp[1]))
        return cluster_array
    
    def Kmeans_labels(self):
        kmeans = KMeans(n_clusters=self.clusters, random_state=0).fit(self.data)
        labels = pd.DataFrame(kmeans.labels_)
        return labels

       
        
        
class KMS_img3D:
    """"""
    
    def __init__(self, name, data, clusters):
        
        self.name = name
        self.data = data
        self.clusters = clusters
     
    def Kmeans_slices(self):
        kmeans = KMeans(n_clusters=self.clusters, random_state=0).fit(self.data)
        df = np.array(kmeans.labels_)
        XYZ = rr.rearrange3D_stack(self.name).stack3D()
        img = np.array(df).reshape(XYZ)
        plt.figure(figsize=(3,15))
        plt.imshow(img)
        #plt.colorbar()
        plt.grid(False)
        plt.show()


"""

The next steps will be:
                    1) To add PCA shading (and possibly ICA but not until later)
                    2) To add the capacity to export the arrays, so that someone 
                        who knows matplotlib can image it as they wish


"""

























