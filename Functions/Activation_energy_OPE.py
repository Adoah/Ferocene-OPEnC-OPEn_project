from math import *
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation  
from scipy.integrate import quad,dblquad
from scipy import integrate
import datetime 
import csv
from scipy.optimize import minimize
from scipy.optimize import differential_evolution 
import glob 
import random 
#from New_Class import Model 
import models    
from F4 import Fitting 

DataFile1 = 'Data//OPEn_Positive_volts.txt'   # This is Ea for OPEn, n=1,2,3. it has a voltage range {0.2,1.0)    
DataFile2 = 'Data//OPEn_Negative_volts.txt'   # This is Ea for OPEn, n=1,2,3. it has a voltage range {-1.0,-0.2)  
data = pd.read_csv(DataFile2, delimiter = '\t',header=None)  
data1 = data[abs(data[0])>0] 
c=data1.dropna()
 

x=c[0] # this column is the voltage 
y1,y2,y3=(c[1],c[2],c[3])  # These columns are Ea for OPE1,OPE2,OP3 respectively 

#plt.scatter(x,y2)
#plt.show() 

ipar = {
   
    
        'E'   :	0.75,	
	'l'   :	1.2,	
	'cap' :	1.31e-19,	
	'W'   :	0.83,	
	'A'   :	0.26 
	
	
	
    }   


bnds = {
    'E'     : [0,1],
    'l'     : [0,1],
    'cap'   : [0,1],
    'W'     : [0,1],
    'A'     : [0,1] 
      } 
 
 
cols=[2]  


for col in cols: 
    print(col) 
    rawD={
          'X': c[0],
          'Y': c[col] 
          }
      
    def fxn(V,E,l,cap,W,A):
        return models.nitzanmodel_fixedtemp_biasvoltage(V,E,l,cap,W,A)
    
    Obj=Fitting(fxn,rawD)
    Obj.Fit(bnds,ipar)
    Obj.PrintFit()
    
    plt.scatter(Obj.workD['X'],Obj.workD['Y'],color='black',label=col)  

    plt.plot(Obj.modelD['X'],Obj.modelD['Y'],color='red',label=col)
    plt.xlabel("voltage(V)") 
    plt.ylabel("E_a")   
    plt.title("Activation Energy for OPE2")
    plt.savefig("Ea_OPE2.png")    
plt.legend() 
plt.show()
  





























































   
