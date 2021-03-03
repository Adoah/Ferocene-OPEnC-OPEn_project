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



DataFile1 = 'Data//OPEnC_Positive_volts.txt'   # This is Ea for OPEnC, n=1,2,3. it has a voltage range {0.2,1.2)    
DataFile2 = 'Data//OPEnC_Negative_volts.txt'   # This is Ea for OPEnC, n=1,2,3. it has a voltage range {-1.0,-0.2)  
data = pd.read_csv(DataFile1, delimiter = '\t',header=None)  
data1 = data[abs(data[0])>0] 
c=data1.dropna()
 


x_OPE1C,y_OPE1C=(c[0],c[1])  
x_OPE2C,y_OPE2C=(c[2],c[3]) 
x_OPE3C,y_OPE3C=(c[4],c[5])  

#plt.scatter(x_OPE1C,y_OPE1C)
#plt.scatter(x_OPE2C,y_OPE2C)
#plt.scatter(x_OPE3C,y_OPE3C)
#plt.show() 


ipar = {
   
    
        'E'   :	0.75,	
	'l'   :	1.2,	
	'cap' :	1.31e-19,	
	'W'   :	0.83,	
	'A'   :	0.25 
    }   


bnds = {
    'E'     : [0,1],
    'l'     : [0,1.5],
    'cap'   : [0,1],
    'W'     : [-1,1],
    'A'     : [-1,1] 
      } 
 
  
    



 

rawD={
          'X': c[0],
          'Y': c[1]    
          }
      
def fxn(V,E,l,cap,W,A):
    return models.nitzanmodel_fixedtemp_biasvoltage(V,E,l,cap,W,A)
    
Obj=Fitting(fxn,rawD)
Obj.Fit(bnds,ipar)
Obj.PrintFit()
    
plt.scatter(Obj.workD['X'],Obj.workD['Y'],color='black')  

plt.plot(Obj.modelD['X'],Obj.modelD['Y'],color='red')
plt.xlabel("voltage(V)") 
plt.ylabel("E_a")   
plt.title("Activation Energy for OPE1C")
plt.savefig("Ea_OPE1Cpng")    
#plt.legend() 
plt.show()
 
























































   
