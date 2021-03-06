import numpy as np
from numpy import linalg as LA

import scipy as sc
from scipy.interpolate import interp1d
import scipy.integrate as integrate
import scipy.special as special

import random as rd

from sympy import besseli, besselk

#import matplotlib.pyplot as plt

import time 
start_time = time.time() 

#import matplotlib.pyplot as plt

#Size of steps on radial coordinate
def Delta_Mom(K,N):
    #return K/(N)
    return np.pi/2 /(N+1)
    #return 1./N

#Parametrization of the momentum in terms of tan(th)**r/sqrt(r)
def Tan_Mom(i,K,N,R):
    #return i*Delta_Mom(K,N)
    return K * np.tan( i * Delta_Mom(K,N) )**R/np.sqrt(R)
    #return K * ( i * Delta_Mom(K,N) )**R

#Jacobian of the lattice reconfig. to the tangent parametrization
def Jacobi(i,K,N,R):
    #return K**2 * Delta_Mom(K,N)# * R * ( i * Delta_Mom(K,N) )**(2*R-1)
    #return Delta_Mom(K,N)#Delta_Mom(N)*K**2*np.tan(np.pi/2*i/(N+1))**(2*R-1)/np.cos(np.pi/2*i/(N+1))**2
    return Delta_Mom(K,N)*K**2*np.tan(np.pi/2*i/(N+1))**(2*R-1)/np.cos(np.pi/2*i/(N+1))**2
    #return K**2 * Delta_Mom(K,N) * R * ( i * Delta_Mom(K,N) )**(2*R-1)

#Kinetic term of the m-layer system
def Kin_Term(k,Euv,K,N,M):
    return Euv*(k/K)**M

#Norm in the reciprocal lattice
def Norm_Mom(k1,k2,th):
    return k1**2 + k2**2 - 2*k1*k2*np.cos(th)

#Coulomb interaction
def Coulomb(k1,k2,th,Euv,K,G,A):
    num = Euv/K**2*G*np.exp( -A**2*Norm_Mom(k1,k2,th)/K**2 )
    return num

#Hopping/pairing terms
def Hopp_Pair(k1,k2,th,Euv,K,G,A,M,s):
    return -1/(4*np.pi)*( Coulomb(k1,k2,th,Euv,K,G,A) )*s*( s+np.cos(M*th) )

def SelfEnergy(k,Euv,K,N,M,G,A):
    Factor0 = 1/( 4*np.pi*A**2 )
    Factor1 = -K**2/( 2*A**4*k**2*np.pi )
    Factor2 = +K**2/( 2*A**4*k**2*np.pi ) * np.exp(-A**2*k**2/(2*K**2))
    return Euv*G*(Factor0+Factor1+Factor2)

#Angular momentum channels
def Four_Hopp_Pair(k1,k2,l,Euv,K,G,A,M,s):
    chopps = 10000
    suma = 0.
    x = np.pi/chopps*np.arange(0, chopps)
    y = Hopp_Pair(k1,k2,x,Euv,K,G,A,M,s)*np.cos(l*x)
    #suma = integrate.quad(y, x, even='last')
    suma = integrate.quad(lambda x: Hopp_Pair(k1,k2,x,Euv,K,G,A,M,s)*np.cos(l*x), 0, np.pi)[0]
    return suma

#Import the self-energy from file InteMm.txt
#SelfEnergyData = np.loadtxt(fname = "InteM1.txt")

Parameters = np.genfromtxt('ParametersABLN.txt') 

eCharge = Parameters[0]   #Coupling constant
eSpread = Parameters[1]   #Spreading constant
eAngMom = Parameters[2]   #Angular momentum channel
eRadMom = Parameters[3]   #Matrix size
eCutOff = Parameters[4]   #Number of UV cutoff intervals
ePowTan = Parameters[5]   #Number of UV cutoff intervals

#BloqueX = Parameters[4]
#BloqueY = Parameters[5]

file1 = open("HamVals.txt","w") 

GGG = eCharge           #Coupling constant
AAA = eSpread           #Spreading constant
LLL = eAngMom           #Angular momentum channel
NNN = int(eRadMom*10)   #Matrix size
RRR = ePowTan
SSS = int(eCutOff)      #Number of UV cutoff intervals

EUV = 1.                #UV cutoff energy
KKK = 1.                #UV cutoff momentum
MMM = 2                 #Number of layers

"""
PRINTING OF TERMS TO DO THE BENCH-MARK
print "Hopp"
print Hopp_Pair(Tan_Mom(1,RRR,KKK,NNN),Tan_Mom(2,RRR,KKK,NNN),np.pi/3,KKK,MMM,+1)
print "Four_Hopp"
print Four_Hopp_Pair(Tan_Mom(1,RRR,KKK,NNN),Tan_Mom(2,RRR,KKK,NNN),1,KKK,MMM,+1)
print "Pair"
print Hopp_Pair(Tan_Mom(1,RRR,KKK,NNN),Tan_Mom(2,RRR,KKK,NNN),np.pi/3,KKK,MMM,-1)
print "Four_Pair"
print Four_Hopp_Pair(Tan_Mom(1,RRR,KKK,NNN),Tan_Mom(2,RRR,KKK,NNN),1,KKK,MMM,-1)
print "Jacobi"
print Jacobi(1,RRR,KKK,NNN)
"""

#Radial coordinate slots
MomentumAxis   = np.zeros(2*NNN*SSS)
KineticAxis    = np.zeros(2*NNN*SSS)
SelfEnergyAxis = np.zeros(2*NNN*SSS)

for i in range(0, NNN*SSS):
    MomentumAxis[i] = (-1)**(RRR+1)*Tan_Mom(- NNN*SSS+i,KKK,NNN,RRR)
    KineticAxis[i]  = -Kin_Term(MomentumAxis[i],EUV,KKK,NNN,MMM)
    SelfEnergyAxis[i] = -SelfEnergy(MomentumAxis[i],EUV,KKK,NNN,MMM,GGG,AAA)
    print - NNN*SSS+i
for i in range(0, NNN*SSS):
    MomentumAxis[NNN*SSS+i] = +Tan_Mom(i+1,KKK,NNN,RRR)
    KineticAxis[NNN*SSS+i]  = +Kin_Term(MomentumAxis[NNN*SSS+i],EUV,KKK,NNN,MMM)
    SelfEnergyAxis[NNN*SSS+i] = SelfEnergy(MomentumAxis[NNN*SSS+i],EUV,KKK,NNN,MMM,GGG,AAA)
    print i+1

#print MomentumAxis
#print SelfEnergy

"""
PLOT OF TE SELF-ENERGY IN LOG MOMENTUM
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
line, = ax.plot(SelfEnergyData[:,0], SelfEnergyData[:,1], color='blue', lw=2,marker="*")
line, = ax.plot(MomentumAxis, SelfEnergy, color='red', marker="*")
plt.xlim(0.001, 10)

ax.set_xscale('log')

plt.show()
"""
#Bogoliubov Hamiltonian
HamiltonMatrix = np.zeros((2*NNN*SSS,2*NNN*SSS))
for i in range(0,NNN*SSS):
    mx = i+1
    for j in range(0,i+1):
        my = j+1
        if i==j:
            #Selection of the kinetic/self-energy terms on the diagonal
            Mom = Tan_Mom(mx,KKK,NNN,RRR)
            HamiltonMatrix[i+000][j+000] = Kin_Term(Mom,EUV,KKK,NNN,MMM) + SelfEnergy(Mom,EUV,KKK,NNN,MMM,GGG,AAA)
            HamiltonMatrix[i+NNN][j+NNN] = -HamiltonMatrix[i][j]
        else:
            #Off-diagonal terms
            #Definition of the momenta for the matrix element i,j
            Mom1 = Tan_Mom(mx,KKK,NNN,RRR)
            Mom2 = Tan_Mom(my,KKK,NNN,RRR)
            #Hopping terms 
            HamiltonMatrix[i+000][j+000] = Four_Hopp_Pair(Mom1,Mom2,LLL,EUV,KKK,GGG,AAA,MMM,+1)*np.sqrt( Jacobi(mx,KKK,NNN,RRR)*Jacobi(my,KKK,NNN,RRR) )
            HamiltonMatrix[j+000][i+000] = HamiltonMatrix[i][j]
            HamiltonMatrix[i+NNN*SSS][j+NNN*SSS] = -HamiltonMatrix[i][j]
            HamiltonMatrix[j+NNN*SSS][i+NNN*SSS] = -HamiltonMatrix[i][j]
            #Pairing terms
            HamiltonMatrix[i+000][j+NNN*SSS] = Four_Hopp_Pair(Mom1,Mom2,LLL,EUV,KKK,GGG,AAA,MMM,-1)*np.sqrt( Jacobi(mx,KKK,NNN,RRR)*Jacobi(my,KKK,NNN,RRR) )
            HamiltonMatrix[j+000][i+NNN*SSS] = +HamiltonMatrix[i+000][j+NNN*SSS]
            HamiltonMatrix[i+NNN*SSS][j+000] = -HamiltonMatrix[i+000][j+NNN*SSS]
            HamiltonMatrix[j+NNN*SSS][i+000] = -HamiltonMatrix[i+000][j+NNN*SSS]

#PRINTING OF THE FULL-HAMILTONIAN. Not recommended to activate for sizes NNN>4
#print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in HamiltonMatrix]))

np.savetxt('HamiltonCalculator0010.txt', HamiltonMatrix, fmt='%1.4e')   # use exponential notation

#DIAGONALIZATION OF THE HAMILTONIAN
HamiltonEigVals, HamiltonEigVecs = LA.eig( HamiltonMatrix )

#SORTING OF THE EIGENVALUES
idx = np.argsort(HamiltonEigVals)
HamiltonEigVals = HamiltonEigVals[idx]
HamiltonEigVecs = HamiltonEigVecs [:,idx]


#np.savetxt('MomentumAxis.txt', MomentumAxis, fmt='%1.4e')   # use exponential notation
#np.savetxt('KineticAxis.txt', KineticAxis, fmt='%1.4e')   # use exponential notation
#np.savetxt('SelfEnergyAxis.txt', SelfEnergyAxis, fmt='%1.4e')   # use exponential notation

#np.savetxt('ValsRe.txt', np.real(HamiltonEigVals), fmt='%1.4e')   # use exponential notation
#np.savetxt('ValsIm.txt', np.imag(HamiltonEigVals), fmt='%1.4e')   # use exponential notation
#np.savetxt('Vals.txt', HamiltonEigVals, fmt='%1.4e')   # use exponential notation
#np.savetxt('VecsHamiltonCalculator0010.txt', HamiltonEigVecs, fmt='%1.4e')   # use exponential notation

for m1 in range(0,2*NNN*SSS):
    file1.write("%s" % (MomentumAxis[m1])),
    file1.write("\t"),
    file1.write("%s" % (KineticAxis[m1]))
    file1.write("\t"),
    file1.write("%s" % (SelfEnergyAxis[m1]))
    file1.write("\t"),
    file1.write("%s" % (np.real(HamiltonEigVals[m1])))
    file1.write("\t"),
    file1.write("%s" % (np.imag(HamiltonEigVals[m1])))
    file1.write("\t"),
    file1.write("%s" % (HamiltonEigVals[m1]))
    file1.write('\n'),

file1.close() 

print "gK = ", GGG
print "aK = ", AAA
print "L = ", LLL
print "N = ", NNN

print "Fin"

#216
