# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 03:00:37 2020

@author: anils
"""

import pandas as pd
import numpy as np
import math
def linearregression(datapackage,valuey,valuex):
    YValues = pd.read_csv(datapackage)[valuey].values
    XValues = pd.read_csv(datapackage)[valuex].values
    YMatris = np.array(YValues)
    XMatris=np.array(XValues)
    YMatrisTranspose=YMatris.T
    YMatrisTransposexYMatris=np.dot(YMatrisTranspose,YMatris)
    OneMatris=np.ones((1,XMatris.size))
    XMatrisxOneMatris=np.vstack((OneMatris,XMatris))
    XMatrisxOneMatrisTranspose=XMatrisxOneMatris.T
    a123=np.dot(XMatrisxOneMatrisTranspose,XMatrisxOneMatris)
    XMatrisxOneMatrisTransposexXMatrisxOneMatrisTotalInverse=np.linalg.inv(a123)
    XMatrisxOneMatrisTransposexYMatris=np.dot(XMatrisxOneMatrisTranspose,YMatris)
    #a333=np.dot(XMatrisxOneMatrisTranspose,XMatrisxOneMatrisTransposexXMatrisxOneMatrisTotalInverse)
    #BETA=np.dot(YMatrisTranspose,a333)
    BETA=np.dot(XMatrisxOneMatrisTransposexXMatrisxOneMatrisTotalInverse,XMatrisxOneMatrisTransposexYMatris)
    
    B0=BETA[0]
    B1=BETA[1]
    
    Error=YMatris-B0
    ErrorTranspose=Error.T
    VarianceSq=np.dot(ErrorTranspose,Error)/(YMatris.size-1-1)
    VarianceSq=np.array(VarianceSq)
    VarianceBeta=np.dot(VarianceSq,XMatrisxOneMatrisTransposexXMatrisxOneMatrisTotalInverse)
    
    h=math.sqrt(VarianceBeta)/math.sqrt(XMatris.size)
    value=B1/h
    if value>= 1.96:
        print("reject")
    else:
        print("cannot reject")
    