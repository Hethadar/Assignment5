#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 10:44:35 2026

@author: ryantauber
"""
import numpy as np
import matplotlib.pyplot as plt
h=0.1
A=10
a=2
k=0.4
x=np.arange(0,20,.1)
values=len(x)
dxc=np.empty(values)
dxf=np.empty(values)
fx=np.empty(values)
dfx=np.empty(values)
#Electric field
def teal(x):
    return A*np.cos((np.pi*x)/a)*np.exp(-k*x)
for i in range(0,values):
    fx[i]=A*np.cos((np.pi*x[i])/a)*np.exp(-k*x[i])
#Analytic
def calers(x):
    return np.exp(-k*x)*((-(np.pi*A)/a)*np.sin((np.pi*x)/a)-(A*k)*np.cos((np.pi*x)/a))
for i in range(0,values):
    dfx[i]=np.exp(-k*x[i])*((-(np.pi*A)/a)*np.sin((np.pi*x[i])/a)-(A*k)*np.cos((np.pi*x[i])/a))
#Central diffrence
for i in range(0,values):
    dxc[i]=(teal(x[i]+h)-teal(x[i]-h))/(2*h)
#Forward diffrence
for i in range(0,values):
    dxf[i]=(teal(x[i]+h)-teal(x[i]))/h

#Errors h=0.1
err_for1=np.abs(dxf-dfx)
err_cen1=np.abs(dxc-dfx)

#Step 1
fig1=plt.figure()
ax=plt.axes()
ax.plot(x,fx,'-g')
plt.grid()
ax.set_xlabel('Position x(m)')
ax.set_ylabel('Electric field(V/m)')

#Step 2 C
fig2=plt.figure()
ax=plt.axes()
ax.plot(x,dxc,'-r',label="Central Diffrence")
ax.plot(x,dxf,'-b',label="Forward Diffrence")
ax.plot(x,dfx,'-y',label="Analytical")
plt.grid()
plt.legend()
ax.set_xlabel('Position x(m)')
ax.set_ylabel('dE/dx(V/m^2)')

#Step 2 D
fig3=plt.figure()
ax=plt.axes()
plt.semilogy(x,err_cen1,'-r',label="Central Error")
plt.semilogy(x,err_for1,'-b',label="Forward Error")
plt.grid()
plt.legend()
ax.set_xlabel('Position x(m)')
ax.set_ylabel('Absolute Error in dE/dx(V/m^2)')
"""
Central diffrencing method is more accurate as the error is smaller
"""
"""
Step E: forward diffrencing had it's error reduced by about a two times diffrence
center diffrencing had it's error reduced by about four times diffrence in error
these were found by comparing the two graphs generated with diffrent h values side by side
at the same position for each type of error
In terms of truncation error this means that forward diffrencing has a first order truncation error
while central diffrencing has a second order truncation error
"""

x0=1.0
dxs=10.0**-np.arange(1,16)
error_dx=np.abs((teal(x0+dxs)-teal(x0))/dxs -calers(x0))

#Step 2 E
fig4=plt.figure()
ax=plt.axes()
plt.loglog(dxs,error_dx,'-r', label="Forward diffrence error")
plt.grid()
plt.legend()
ax.set_xlabel('change in x(m)')
ax.set_ylabel('NUmerical-Analytical (V/m^2)')

"""
As dx gets very small the numerator goes closer to zero then the number of signfigant digits
Available for storage in the computer causing the diffence to be incorrect and the as dx gets smaller
that error gets amplified
"""


