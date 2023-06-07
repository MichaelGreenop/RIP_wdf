
"""This is a module used for the selection of different sections of the Raman
image, and also removing the background from the Raman image.

Both 2 and 3D slices"""

# You need to take the code from Kmean_Background in the Z. Python_modules
# file of the passport 

"""

In the previous version of this module, 
you use the functions to produce the k-means labels
and then substituted the clusters for the zero arrays.

In this version, you will provide a function to substitute the 
zero arrays and return the adapted data.

Potentially you will need to provide classes for when different 
ammounts of clusters relate to the background. You could have up to three 
and then let people addapt the code if they need more.

"""

# Step 1 - form the data with cf DataMat
# Step 2 - Produce the labels with the k-means 
# Step 3 - Concat the labels and the original dataset
# Step 4 - Convert all the background clusters to zero arrays



class background_labels:
    """Produces the labels that can then be 
        concatenated onto the main dataset"""
    
    def __init__(self, data, cluster_number):
        
        self.data = data
        self.cluster_number = cluster_number
    
    def Kmeans_labels(data, clusters):
        
        kmeans = KMeans(n_clusters=clusters, random_state=0).fit(data)
        labels = pd.DataFrame(kmeans.labels_)
        return labels
