import os
import numpy as np

from sklearn.cluster import AffinityPropagation
from sklearn import cluster

from job_degradomeType import degradomeTypes
#this is for windows:
#
os.chdir("C:/Icas.Test/")
methodName = "affinity_propagation"


for length in ["71","121"]:
    for deg in degradomeTypes:
        #gaussian kernal
        g = np.loadtxt("cs_rna_distance/cs_rna_distance_matrix_" + length + "_" + deg + "_gaussian.txt",delimiter = " ")
        counts = ""
        for damping in [0.5,0.6,0.7,0.8,0.9]:
            method = AffinityPropagation(damping = damping, convergence_iter = 15, affinity="precomputed")
            method.fit(g)
            cluster_count = len(np.unique( method.labels_))
            counts = counts + "\t" + str(cluster_count)
            if(cluster_count==1):
                break
        print counts
print "Job Done!"
print "Job Done!"



from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
iris = load_iris()
X, y = iris.data, iris.target
X.shape

X_new = SelectKBest(chi2, k=2).fit_transform(X, y)
X_new.shape
