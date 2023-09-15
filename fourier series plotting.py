#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:00:07 2022
@author: soudip
"""

import numpy as np
from math import pi
import matplotlib.pyplot as plt
from scipy.integrate import quad
function=input("enter the function")
pe=float(input("enter the period of the function"))
pe=pe/2
l=int(input("enter the l value"))
a=[]
b=[]
i=0
def s(x):
    hi=eval(function)
    return hi
#xlis=np.linspace(-pe,pe,num=1000)   # plotting for the constant function
#ylis=np.linspace(pe,pe,num=1000)
#plt.figure(num=0,dpi=120)
#plt.plot(xlis,ylis)
for i in range (0,l):
    def f(x):
     return (1/pe)*s(x)*(np.sin(i*x*pi/pe))
    def g(x):
     return (1/pe)*s(x)*(np.cos(i*x*pi/pe))
    m,u=quad(f,-pe,pe)
    n,h=quad(g,-pe,pe)
    a.append(m)
    b.append(n)
    i=i+1  
i=0 
#for i in range (1,l): # plotting for individual sin function
#    def h(x):
#     return a[i]*np.sin(i*x)
#    xlist=np.linspace(-pe,pe,num=1000)
#    ylist=h(xlist)
#    plt.figure(num=0,dpi=120)
#    plt.plot(xlist,ylist)
#i=0
#for i in range (1,l): # plotting for individual cos function
#    def o(x):
#     return     b[i]*np.cos(pi*i*x/pe)+b[0]/2
#    xlist=np.linspace(-pe,pe,num=1000)
#    ylist=o(xlist)
#    plt.figure(num=0,dpi=120)
#    plt.plot(xlist,ylist)
i=0
def su(x):
 summ=0
 for i in range (1,l):
    summ+=a[i]*np.sin(i*x*pi/pe)
 return summ   
def tu(x):
 summm=0
 for i in range (1,l):
    summm+=b[i]*np.cos(i*x*pi/pe)
 return summm   
def uio(x):
 return su(x)+ tu(x)+b[0]/2
xlist=np.linspace(-pe,pe,num=1000)
ylist=uio(xlist)
plt.figure(num=0,dpi=120)
plt.plot(xlist,ylist)
 
xli=np.linspace(-pe,pe,num=1000)
yli=s(xli)
plt.figure(num=0,dpi=120)
plt.plot(xli,yli)  