

"""
In this module there are functions to:

        1) Form a list with 1 as a topic of the image and 0 being the background
        2) Remove the background by converting all spectra to zeros 
        3) Turn the zero spectra (the background) transparent
        and 
        4) Layer the resulting images 

You will need to produce an image for each target (nucleus, cytoplasm, scaffold, etc.)

Some background may relate to more than one cluster.
Options to turn up to three clusters will be provided.
Anyone needing more can adapt the provided code.

"""

#from PIL import Image
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd 
#import VolumeRaman as VRI   


"""
The first three classes select clusters
of interest, either one, two, or three
in an image and convert them into the area 
of interest (ones) and the background (zeros)

"""


class select_one_cluster:
    
   
       
    
    """"""

 

    def __init__(self, data, number_of_clusters, cluster_number):
        
        self.data = data
        self.cluster_number = cluster_number
        self.number_of_clusters = number_of_clusters

    def transparent(self):
        test_list = []
        kmeans = KMeans(self.number_of_clusters, random_state=0).fit(self.data)
        labels = np.array(kmeans.labels_)
        for i in range(len(labels)):
            if labels[i] == self.cluster_number:
                test_list.append(1)
            else:
                test_list.append(0)
        final_list = pd.DataFrame(test_list)
        return final_list



class select_two_clusters:
    """"""
    
    def __init__(self, data, number_of_clusters, cluster_number1, cluster_number2):
        
        self.data = data
        self.cluster_number1 = cluster_number1
        self.cluster_number2 = cluster_number2
        self.number_of_clusters = number_of_clusters
    
    
    
    def transparent2(self):
        test_list2 = []
        kmeans = KMeans(self.number_of_clusters, random_state=0).fit(self.data)
        labels = np.array(kmeans.labels_)
        for i in range(len(labels)):
            if labels[i] == self.cluster_number1:
                test_list2.append(1)
            elif labels[i] == self.cluster_number2:
                test_list2.append(1)
            else:
                test_list2.append(0)
        final_list2 = pd.DataFrame(test_list2)
        return final_list2


class select_three_clusters:
    """"""
    
    def __init__(self, data, number_of_clusters, cluster_number1, cluster_number2, cluster_number3):
        
        self.data = data
        self.cluster_number1 = cluster_number1
        self.cluster_number2 = cluster_number2
        self.cluster_number3 = cluster_number3
        self.number_of_clusters = number_of_clusters
    
    
    
    def transparent3(self):
        test_list3 = []
        kmeans = KMeans(self.number_of_clusters, random_state=0).fit(self.data)
        labels = np.array(kmeans.labels_)
        for i in range(len(labels)):
            if labels[i] == self.cluster_number1:
                test_list3.append(1)
            elif labels[i] == self.cluster_number2:
                test_list3.append(1)
            elif labels[i] == self.cluster_number3:
                test_list3.append(1)
            else:
                test_list3.append(0)
        final_list3 = pd.DataFrame(test_list3)
        return final_list3



"""
The next set of classes make the 
background area (the zeros) trasparent

"""




class one_transparent_cluster:
    """"""
    
    def __init__(self, data, number_of_clusters, cluster_number):
        
        self.data = data
        self.cluster_number = cluster_number
        self.number_of_clusters = number_of_clusters
        
    def transparent_df(self):
        labels = select_one_cluster(self.data, self.number_of_clusters, self.cluster_number).transparent()
        labels = labels.rename(columns={0:'Labels'})
        DF = pd.DataFrame(self.data)
        df = pd.concat([labels,DF],axis=1).set_index('Labels')
        df.loc[0] = 0
        final_df = df.iloc[:,1:]
        return final_df


class two_transparent_clusters:
    """"""
    
    def __init__(self, data, number_of_clusters, cluster_number1, cluster_number2):
        
        self.data = data
        self.cluster_number1 = cluster_number1
        self.cluster_number2 = cluster_number2
        self.number_of_clusters = number_of_clusters
    
    def transparent_df2(self):
        labels = select_two_clusters(self.data, self.number_of_clusters, self.cluster_number1, self.cluster_number2).transparent2()
        labels = labels.rename(columns={0:'Labels'})
        DF = pd.DataFrame(self.data)
        df = pd.concat([labels,DF],axis=1).set_index('Labels')
        df.loc[0] = 0
        final_df2 = df.iloc[:,1:]
        return final_df2

class three_transparent_clusters:
    """"""
    
    def __init__(self, data, number_of_clusters, cluster_number1, cluster_number2, cluster_number3):
        
        self.data = data
        self.cluster_number1 = cluster_number1
        self.cluster_number2 = cluster_number2
        self.cluster_number3 = cluster_number3
        self.number_of_clusters = number_of_clusters
    
    def transparent_df3(self): # Cell body
        labels = select_three_clusters(self.data, self.number_of_clusters, self.cluster_number1, self.cluster_number2, self.cluster_number3).transparent3()
        labels = labels.rename(columns={0:'Labels'})
        DF = pd.DataFrame(self.data)
        df = pd.concat([labels,DF],axis=1).set_index('Labels')
        df.loc[0] = 0
        final_df = df.iloc[:,1:]
        return final_df





"""

class layer:

    
    def __init__(self, name1, name2):
        
        self.name1 = name1
        self.name2 = name2
        
    def layering(self):
        background = Image.open("VRI_1_cellbody(t).png")
        foreground = Image.open("VRI_1_nucleicacids(t).png")
        
        background.paste(foreground, (0, 0), foreground)
        background.save('VRI_1_cell(t).png')


"""