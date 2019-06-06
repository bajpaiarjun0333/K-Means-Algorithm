#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 17:16:04 2018

@author: bajpaiarjun0333
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import pandas as pd

def generateSamples(m,n):
    X=np.zeros((m,n))
    #Generate noise to shift the generated random number somewhere in the grid
    s=4
    s1=np.array([0,0])
    s2=np.array([s,s])
    s3=np.array([0,s])
    s4=np.array([s,0])
    per_set=(int)(m/4)
    X[:per_set,:]=np.random.randn(per_set,n)+s1
    X[per_set:2*per_set,:]=np.random.randn(per_set,n)+s2
    X[2*per_set:3*per_set,:]=np.random.randn(per_set,n)+s3
    X[3*per_set:,:]=np.random.randn(per_set,n)+s4
    plt.scatter(X[:,0],X[:,1])
    plt.xlabel("0th Dimension")
    plt.ylabel("1st Dimension")
    plt.title("Sample Plot")
    plt.show()
    return X

def findClusters(X,max_iter=20):
    #Retriving the shape of the feature matrix
    m,n=X.shape
    k=4
    actualCluster=np.zeros((k,n))
    xCluster=np.zeros(m)
    #Random assign clusters
    for i in range(k):
        c=np.random.choice(m)
        actualCluster[i]=X[c]
    #Finished Assignment 
    #Now moving clusters to actual real position
    print(actualCluster)
    dist=1000
    for i in range(max_iter):
        for j in range(m):
            for k in range(k):
                dist2=np.linalg.norm(X[j]-actualCluster[k])
                if dist2<=dist:
                    dist=dist2
                    xCluster[j]=k
            dist=1000
            count=0
        sum=np.zeros((1,n))
        
        for j in range(k):
            for k in range(m):
                if xCluster[k]==j:
                    sum=sum+X[k]
                    count=count+1
            sum=sum/count
            count=0
            sum=np.zeros((1,n))
    return actualCluster

            
def plotFinal(X,k):
    plt.scatter(X[:,0],X[:,1])
    plt.scatter(k[:,0],k[:,1],color="red")
    plt.xlabel("0th Dimension")
    plt.ylabel("1st Dimension")
    plt.title("Sample Plot")
    plt.show()
    

def main():
    m=4000
    n=2
    X=generateSamples(m,n)
    k=findClusters(X)
    print("Final Cluster ",k)
    plotFinal(X,k)
    

    

if __name__=="__main__":
    main()
    