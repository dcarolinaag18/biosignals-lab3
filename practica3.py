# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 09:25:48 2018

@author: Carolina
"""
import scipy.io as sio;
import matplotlib.pyplot as plt;
import numpy as np;
import math as mt


#libreria con rutinas de PDS
#import scipy.signal as signal;
#import matplotlib;

######3.2	Representación de señales
# Punto 1
Fo=40;
Tp=1/Fo;
Fs=1000;
T=1/Fs;
t=np.arange(0,Tp+T,T);
A=5;
x=A*np.sin(2*mt.pi*Fo*t);
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(t, x, marker='o')
ax.set(xlabel='Tiempo (s)', ylabel='Amplitud (V)');
plt.savefig('fig1.png')
plt.show()

#Punto 2
fo=Fo/Fs;
n=np.arange(0,len(t));
x1=A*np.sin(2*mt.pi*fo*n);
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(n, x1, marker='o')
ax.set(xlabel='Muestras', ylabel='Amplitud (V)');
plt.savefig('fig2.png')
plt.show()

#Punto 3
fig = plt.figure()
ax = fig.add_subplot(111)
ax.stem(n, x1, marker='o')
ax.set(xlabel='Muestras', ylabel='Amplitud (V)');
plt.savefig('fig3.png')
plt.show()

####3.3	Energía y potencia en el dominio del tiempo
# Energia
energia= sum(x**2)

# Pontencia
potencia=energia/(len(t)-1)

#rms
rms = np.sqrt(potencia)

#10 Ciclos
t10=np.arange(0,10*Tp+T,T);
x10 = A*np.sin(2*mt.pi*Fo*t10);
energia10 = sum(x10**2)
potencia10 = energia10/(len(t10)-1)
rms10 = np.sqrt(potencia)
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot(t10, x10, marker='o')

####3.4	Análisis de Fourier en tiempo discreto

#fft

X10 = np.fft.fft(x10);
X10ab = np.abs(X10);
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(X10ab)
ax.set(title='Módulos de la DFT');
plt.savefig('fig4.png')
plt.show()


N = len(X10);
F = np.arange(0,N)*Fs/N;
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(F,X10ab)
ax.set(xlabel='Frecuencia (Hz)');
plt.savefig('fig5.png')
plt.show()

Nmitad = mt.ceil(N/2);
Fmitad = np.arange(0,Nmitad)*Fs/N;
X10mitad = X10ab[0:Nmitad];
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(Fmitad,X10mitad)
ax.set(xlabel='Frecuencia (Hz)');
plt.savefig('fig6.png')
plt.show()


# Aplicación
Fo=60; # Frecuencia fundamental de la señal
Tp=1/Fo; # Periodo fundamental
Fs=9000; # Frecuencia de muestreo elegida
Ts=1/Fs; # Periodo de muestreo
t=np.arange(0,Tp+Ts,Ts); # Se crea el vector de tiempo, que toma un ciclo de la señal muestreada
x=np.sin(2*mt.pi*60*t)+np.sin(2*mt.pi*120*t)+np.sin(2*mt.pi*360*t); # Señal con tres componentes sinusoidales y frecuencia de muestreo de 9000Hz
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(t, x)
ax.set(xlabel='Tiempo (s)', ylabel='Amplitud (V)');
plt.savefig('fig7.png')
plt.show()

# Se toman 10 ciclos de la señal para calcular la transformada de Fourier
t10=np.arange(0,10*Tp+Ts,Ts) # vector de tiempo para 10 ciclos
x10=np.sin(2*mt.pi*60*t10)+np.sin(2*mt.pi*120*t10)+np.sin(2*mt.pi*360*t10); # señal muestreada con 10 ciclos
X10 = np.fft.fft(x10);
X10ab = np.abs(X10);
N = len(X10);
F10 = np.arange(0,N)*Fs/N;
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(F10,X10ab)
ax.set(xlabel='Frecuencia (Hz)');
plt.savefig('fig8.png')
plt.show()

Nmitad = mt.ceil(N/2);
Fmitad = np.arange(0,Nmitad)*Fs/N;
X10mitad = X10ab[0:Nmitad];
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(Fmitad,X10mitad)
ax.set(xlabel='Frecuencia (Hz)');
plt.savefig('fig9.png')
plt.show()

#ifft
X10i = np.fft.ifft(X10);
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(t10, X10i)
ax.set(xlabel='Tiempo (s)', ylabel='Amplitud (V)');
plt.savefig('fig10.png')
plt.show()

#Filtro
F1 = np.fft.fft(x10);
F2 = np.zeros((len(F1)));
F2[9:13] = F1[9:13];
#F2[17:21] = F1[17:21];
#F2[57:61] = F1[57:61];
xr = np.fft.ifft(F2);
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(t10, np.real(xr))
ax.set(xlabel='Tiempo (s)', ylabel='Amplitud (V)');
plt.savefig('fig11.png')
plt.show()

F2ab = np.abs(F2)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(F10,F2)
ax.set_xlim(0,120)
ax.set(xlabel='Frecuencia (Hz)',title='Espectro de frecuencia - 60 Hz');
plt.savefig('fig12.png')
plt.show()



