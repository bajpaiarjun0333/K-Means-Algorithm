#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 12:25:54 2018

@author: bajpaiarjun0333
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import pandas as pd

def generateSamples(m,n):
    X=np.zeros((m,n))
    #generate noise to shift the generated random number somewhere in the grid
    s=4
    #we design 3 clusters
    s1=np.array([0,0])
    s2=np.array([s,s])
    s3=np.array([0,s])
    s4=np.array([s,0])
    per_set=(int)(m/4)
    X[:per_set,:]=np.random.randn(per_set,n)+s1
    X[per_set:2*per_set,:]=np.random.randn(per_set,n)+s2
    X[2*per_set:3*per_set,:]=np.random.randn(per_set,n)+s3
    X[3*per_set:,:]=np.random.randn(per_set,n)+s4
    plt.axis("equal")
    plt.scatter(X[:,0],X[:,1])
    plt.xlabel("0th Dimension")
    plt.ylabel("1st Dimension")
    plt.title("Sample Plot")
    plt.show()
    return X
    

def findClusters(K,X,max_iter=20):
    #getting the shape of the data received
    m,n=X.shape
    
    #two basic steps are to assign cluster and then find clusters points
    #initially assign clusters to all zero
    clusters=np.zeros((K,n))
    clustBelong=np.ones((K,m))*-1
    #randomly assign clusters
    for k in range(K):
        c=np.random.choice(m)
        clusters[k,:]=X[c,:]
        dist=10000
        
    
    #random cluster initialization set
    #Now allocate each sample a cluster
    for i in range(max_iter):
        for j in range(m):
            final=j
            for k in range(K-1):
                dist2=np.linalg.norm(clusters[k]-X[j])
                if dist2<dist:
                    dist=dist2
                    final=k
                    print(final)
            clustBelong[final,j]=j
        #completed the assignment of cluster to each poing
        #now update the cluster points
        for k in range(K):
            mean=np.zeros((1,n))
            num=0
            for l in range(m):
                if clustBelong[l]>=0:
                    mean+=X[clustBelong[l]]
                    num=num+1
            mean=mean/num
            clusters[k,:]=mean
    return clusters

    
    
def plotClusters(X,clusters):
    plt.scatter(X[:,0],X[:,1])
    plt.scatter(clusters[:,0],clusters[:,1],color="red")
    plt.xlabel("0th dimension")
    plt.ylabel("1st dimension")
    plt.show()



def main():
    m=1000
    n=2
    X=generateSamples(m,n)
    print(X)
    #define the number of cluster to be found
    k=4
    clusters=findClusters(k,X)
    plotClusters(X,clusters)

if __name__=="__main__":
    main()
    