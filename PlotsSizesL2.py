import numpy as np
import matplotlib.pyplot as plt

fiveSizes = [1./10,1./20,1./30,1./40,1./50]

###############################################
###############################################
###############################################

datag000_25a001 = np.genfromtxt('./L2gK000_50.txt')

SystemSize = 1./10*datag000_25a001[:,][0+0*6:6+0*6,1]

EigenValImg000_25a001 = datag000_25a001[:,][0+0*6:6+0*6,2]
EigenValImg000_25a002 = datag000_25a001[:,][0+1*6:6+1*6,2]
EigenValImg000_25a003 = datag000_25a001[:,][0+2*6:6+2*6,2]
EigenValImg000_25a005 = datag000_25a001[:,][0+3*6:6+3*6,2]
EigenValImg000_25a007 = datag000_25a001[:,][0+4*6:6+4*6,2]
EigenValImg000_25a010 = datag000_25a001[:,][0+5*6:6+5*6,2]
print EigenValImg000_25a001
print EigenValImg000_25a010
datag000_30a001 = np.genfromtxt('./L2gK000_60.txt')

EigenValImg000_30a001 = datag000_30a001[:,][0+0*6:6+0*6,2]
EigenValImg000_30a002 = datag000_30a001[:,][0+1*6:6+1*6,2]
EigenValImg000_30a003 = datag000_30a001[:,][0+2*6:6+2*6,2]
EigenValImg000_30a005 = datag000_30a001[:,][0+3*6:6+3*6,2]
EigenValImg000_30a007 = datag000_30a001[:,][0+4*6:6+4*6,2]
EigenValImg000_30a010 = datag000_30a001[:,][0+5*6:6+5*6,2]

datag000_35a001 = np.genfromtxt('./L2gK000_70.txt')

EigenValImg000_35a001 = datag000_35a001[:,][0+0*6:6+0*6,2]
EigenValImg000_35a002 = datag000_35a001[:,][0+1*6:6+1*6,2]
EigenValImg000_35a003 = datag000_35a001[:,][0+2*6:6+2*6,2]
EigenValImg000_35a005 = datag000_35a001[:,][0+3*6:6+3*6,2]
EigenValImg000_35a007 = datag000_35a001[:,][0+4*6:6+4*6,2]
EigenValImg000_35a010 = datag000_35a001[:,][0+5*6:6+5*6,2]

datag000_40a001 = np.genfromtxt('./L2gK000_80.txt')

EigenValImg000_40a001 = datag000_40a001[:,][0+0*6:6+0*6,2]
EigenValImg000_40a002 = datag000_40a001[:,][0+1*6:6+1*6,2]
EigenValImg000_40a003 = datag000_40a001[:,][0+2*6:6+2*6,2]
EigenValImg000_40a005 = datag000_40a001[:,][0+3*6:6+3*6,2]
EigenValImg000_40a007 = datag000_40a001[:,][0+4*6:6+4*6,2]
EigenValImg000_40a010 = datag000_40a001[:,][0+5*6:6+5*6,2]

datag000_45a001 = np.genfromtxt('./L2gK000_90.txt')

EigenValImg000_45a001 = datag000_45a001[:,][0+0*6:6+0*6,2]
EigenValImg000_45a002 = datag000_45a001[:,][0+1*6:6+1*6,2]
EigenValImg000_45a003 = datag000_45a001[:,][0+2*6:6+2*6,2]
EigenValImg000_45a005 = datag000_45a001[:,][0+3*6:6+3*6,2]
EigenValImg000_45a007 = datag000_45a001[:,][0+4*6:6+4*6,2]
EigenValImg000_45a010 = datag000_45a001[:,][0+5*6:6+5*6,2]

datag000_50a001 = np.genfromtxt('./L2gK001_00.txt')

EigenValImg000_50a001 = datag000_50a001[:,][0+0*6:6+0*6,2]
EigenValImg000_50a002 = datag000_50a001[:,][0+1*6:6+1*6,2]
EigenValImg000_50a003 = datag000_50a001[:,][0+2*6:6+2*6,2]
EigenValImg000_50a005 = datag000_50a001[:,][0+3*6:6+3*6,2]
EigenValImg000_50a007 = datag000_50a001[:,][0+4*6:6+4*6,2]
EigenValImg000_50a010 = datag000_50a001[:,][0+5*6:6+5*6,2]

datag001_00a001 = np.genfromtxt('./L2gK002_00.txt')

EigenValImg001_00a001 = datag001_00a001[:,][0+0*6:6+0*6,2]
EigenValImg001_00a002 = datag001_00a001[:,][0+1*6:6+1*6,2]
EigenValImg001_00a003 = datag001_00a001[:,][0+2*6:6+2*6,2]
EigenValImg001_00a005 = datag001_00a001[:,][0+3*6:6+3*6,2]
EigenValImg001_00a007 = datag001_00a001[:,][0+4*6:6+4*6,2]
EigenValImg001_00a010 = datag001_00a001[:,][0+5*6:6+5*6,2]

datag002_00a001 = np.genfromtxt('./L2gK005_00.txt')

EigenValImg002_00a001 = datag002_00a001[:,][0+0*6:6+0*6,2]
EigenValImg002_00a002 = datag002_00a001[:,][0+1*6:6+1*6,2]
EigenValImg002_00a003 = datag002_00a001[:,][0+2*6:6+2*6,2]
EigenValImg002_00a005 = datag002_00a001[:,][0+3*6:6+3*6,2]
EigenValImg002_00a007 = datag002_00a001[:,][0+4*6:6+4*6,2]
EigenValImg002_00a010 = datag002_00a001[:,][0+5*6:6+5*6,2]

datag005_00a001 = np.genfromtxt('./L2gK010_00.txt')

EigenValImg005_00a001 = datag005_00a001[:,][0+0*6:6+0*6,2]
EigenValImg005_00a002 = datag005_00a001[:,][0+1*6:6+1*6,2]
EigenValImg005_00a003 = datag005_00a001[:,][0+2*6:6+2*6,2]
EigenValImg005_00a005 = datag005_00a001[:,][0+3*6:6+3*6,2]
EigenValImg005_00a007 = datag005_00a001[:,][0+4*6:6+4*6,2]
EigenValImg005_00a010 = datag005_00a001[:,][0+5*6:6+5*6,2]

#datag010_00a001 = np.genfromtxt('./L2gK010_00.txt')

#EigenValImg010_00a001 = datag010_00a001[:,][0+0*6:6+0*6,2]
#EigenValImg010_00a002 = datag010_00a001[:,][0+1*6:6+1*6,2]
#EigenValImg010_00a003 = datag010_00a001[:,][0+2*6:6+2*6,2]
#EigenValImg010_00a005 = datag010_00a001[:,][0+3*6:6+3*6,2]
#EigenValImg010_00a007 = datag010_00a001[:,][0+4*6:6+4*6,2]
#EigenValImg010_00a010 = datag010_00a001[:,][0+5*6:6+5*6,2]

###############################################
###############################################
###############################################

plt.clf()
fig, axs = plt.subplots(5, 2, figsize=(5, 10), sharex=False)
plt.subplots_adjust(left=0.20,bottom=0.05,right=0.90,top=0.9,wspace=0.4,hspace=0.2)

axs[0,0].semilogy(
              1000*SystemSize,EigenValImg000_25a001,c=[0.0, 1.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8],label='$a_{\\mathcal{K}}= 1$')
axs[0,0].plot(1000*SystemSize,EigenValImg000_25a002,c=[0.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8],label='$a_{\\mathcal{K}}= 2$')
axs[0,0].plot(1000*SystemSize,EigenValImg000_25a003,c=[0.5, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.5*0.8, 0.0*0.8, 1.0*0.8],label='$a_{\\mathcal{K}}= 3$')
axs[0,0].plot(1000*SystemSize,EigenValImg000_25a005,c=[1.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 1.0*0.8],label='$a_{\\mathcal{K}}= 5$')
axs[0,0].plot(1000*SystemSize,EigenValImg000_25a007,c=[1.0, 0.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8],label='$a_{\\mathcal{K}}= 7$')
axs[0,0].plot(1000*SystemSize,EigenValImg000_25a010,c=[1.0, 0.5, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8],label='$a_{\\mathcal{K}}=10$')
axs[0,0].grid(True)

axs[0,1].semilogy(
              1000*SystemSize,EigenValImg000_30a001,c=[0.0, 1.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[0,1].plot(1000*SystemSize,EigenValImg000_30a002,c=[0.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[0,1].plot(1000*SystemSize,EigenValImg000_30a003,c=[0.5, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.5*0.8, 0.0*0.8, 1.0*0.8])
axs[0,1].plot(1000*SystemSize,EigenValImg000_30a005,c=[1.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 1.0*0.8])
axs[0,1].plot(1000*SystemSize,EigenValImg000_30a007,c=[1.0, 0.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[0,1].plot(1000*SystemSize,EigenValImg000_30a010,c=[1.0, 0.5, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[0,1].grid(True)

axs[1,0].semilogy(
              1000*SystemSize,EigenValImg000_35a001,c=[0.0, 1.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[1,0].plot(1000*SystemSize,EigenValImg000_35a002,c=[0.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[1,0].plot(1000*SystemSize,EigenValImg000_35a003,c=[0.5, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.5*0.8, 0.0*0.8, 1.0*0.8])
axs[1,0].plot(1000*SystemSize,EigenValImg000_35a005,c=[1.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 1.0*0.8])
axs[1,0].plot(1000*SystemSize,EigenValImg000_35a007,c=[1.0, 0.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[1,0].plot(1000*SystemSize,EigenValImg000_35a010,c=[1.0, 0.5, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[1,0].grid(True)

axs[1,1].semilogy(
              1000*SystemSize,EigenValImg000_40a001,c=[0.0, 1.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[1,1].plot(1000*SystemSize,EigenValImg000_40a002,c=[0.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[1,1].plot(1000*SystemSize,EigenValImg000_40a003,c=[0.5, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.5*0.8, 0.0*0.8, 1.0*0.8])
axs[1,1].plot(1000*SystemSize,EigenValImg000_40a005,c=[1.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 1.0*0.8])
axs[1,1].plot(1000*SystemSize,EigenValImg000_40a007,c=[1.0, 0.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[1,1].plot(1000*SystemSize,EigenValImg000_40a010,c=[1.0, 0.5, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[1,1].grid(True)

axs[2,0].semilogy(
              1000*SystemSize,EigenValImg000_45a001,c=[0.0, 1.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[2,0].plot(1000*SystemSize,EigenValImg000_45a002,c=[0.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[2,0].plot(1000*SystemSize,EigenValImg000_45a003,c=[0.5, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.5*0.8, 0.0*0.8, 1.0*0.8])
axs[2,0].plot(1000*SystemSize,EigenValImg000_45a005,c=[1.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 1.0*0.8])
axs[2,0].plot(1000*SystemSize,EigenValImg000_45a007,c=[1.0, 0.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[2,0].plot(1000*SystemSize,EigenValImg000_45a010,c=[1.0, 0.5, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[2,0].grid(True)

axs[2,1].semilogy(
              1000*SystemSize,EigenValImg000_50a001,c=[0.0, 1.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[2,1].plot(1000*SystemSize,EigenValImg000_50a002,c=[0.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[2,1].plot(1000*SystemSize,EigenValImg000_50a003,c=[0.5, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.5*0.8, 0.0*0.8, 1.0*0.8])
axs[2,1].plot(1000*SystemSize,EigenValImg000_50a005,c=[1.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 1.0*0.8])
axs[2,1].plot(1000*SystemSize,EigenValImg000_50a007,c=[1.0, 0.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[2,1].plot(1000*SystemSize,EigenValImg000_50a010,c=[1.0, 0.5, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[2,1].grid(True)

axs[3,0].semilogy(
              1000*SystemSize,EigenValImg001_00a001,c=[0.0, 1.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[3,0].plot(1000*SystemSize,EigenValImg001_00a002,c=[0.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[3,0].plot(1000*SystemSize,EigenValImg001_00a003,c=[0.5, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.5*0.8, 0.0*0.8, 1.0*0.8])
axs[3,0].plot(1000*SystemSize,EigenValImg001_00a005,c=[1.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 1.0*0.8])
axs[3,0].plot(1000*SystemSize,EigenValImg001_00a007,c=[1.0, 0.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[3,0].plot(1000*SystemSize,EigenValImg001_00a010,c=[1.0, 0.5, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[3,0].grid(True)

axs[3,1].semilogy(
              1000*SystemSize,EigenValImg002_00a001,c=[0.0, 1.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[3,1].plot(1000*SystemSize,EigenValImg002_00a002,c=[0.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[3,1].plot(1000*SystemSize,EigenValImg002_00a003,c=[0.5, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.5*0.8, 0.0*0.8, 1.0*0.8])
axs[3,1].plot(1000*SystemSize,EigenValImg002_00a005,c=[1.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 1.0*0.8])
axs[3,1].plot(1000*SystemSize,EigenValImg002_00a007,c=[1.0, 0.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[3,1].plot(1000*SystemSize,EigenValImg002_00a010,c=[1.0, 0.5, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[3,1].grid(True)

axs[4,0].semilogy(
              1000*SystemSize,EigenValImg005_00a001,c=[0.0, 1.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[4,0].plot(1000*SystemSize,EigenValImg005_00a002,c=[0.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[4,0].plot(1000*SystemSize,EigenValImg005_00a003,c=[0.5, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.5*0.8, 0.0*0.8, 1.0*0.8])
axs[4,0].plot(1000*SystemSize,EigenValImg005_00a005,c=[1.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 1.0*0.8])
axs[4,0].plot(1000*SystemSize,EigenValImg005_00a007,c=[1.0, 0.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[4,0].plot(1000*SystemSize,EigenValImg005_00a010,c=[1.0, 0.5, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[4,0].grid(True)

axs[4,1].set_axis_off()
#axs[4,1].semilogy(
#              1000*SystemSize,EigenValImg010_00a001,c=[0.0, 1.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
#axs[4,1].plot(1000*SystemSize,EigenValImg010_00a002,c=[0.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
#axs[4,1].plot(1000*SystemSize,EigenValImg010_00a003,c=[0.5, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[0.5*0.8, 0.0*0.8, 1.0*0.8])
#axs[4,1].plot(1000*SystemSize,EigenValImg010_00a005,c=[1.0, 0.0, 1.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 1.0*0.8])
#axs[4,1].plot(1000*SystemSize,EigenValImg010_00a007,c=[1.0, 0.0, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
#axs[4,1].plot(1000*SystemSize,EigenValImg010_00a010,c=[1.0, 0.5, 0.0], marker='o',ls='None', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
#axs[4,1].grid(True)

axs[0,0].set_xlim(-0.0e+1,+12.1)
axs[0,0].set_xticks(np.arange(0.0e+1,+12.1, step=12./6))
axs[0,1].set_xlim(-0.0e+1,+12.1)
axs[0,1].set_xticks(np.arange(0.0e+1,+12.1, step=12./6))
axs[1,0].set_xlim(-0.0e+1,+12.1)
axs[1,0].set_xticks(np.arange(0.0e+1,+12.1, step=12./6))
axs[1,1].set_xlim(-0.0e+1,+12.1)
axs[1,1].set_xticks(np.arange(0.0e+1,+12.1, step=12./6))
axs[2,0].set_xlim(-0.0e+1,+12.1)
axs[2,0].set_xticks(np.arange(0.0e+1,+12.1, step=12./6))
axs[2,1].set_xlim(-0.0e+1,+12.1)
axs[2,1].set_xticks(np.arange(0.0e+1,+12.1, step=12./6))
axs[3,0].set_xlim(-0.0e+1,+12.1)
axs[3,0].set_xticks(np.arange(0.0e+1,+12.1, step=12./6))
axs[3,1].set_xlim(-0.0e+1,+12.1)
axs[3,1].set_xticks(np.arange(0.0e+1,+12.1, step=12./6))
axs[4,0].set_xlim(-0.0e+1,+12.1)
axs[4,0].set_xticks(np.arange(0.0e+1,+12.1, step=12./6))
axs[4,1].set_xlim(-0.0e+1,+12.1)
axs[4,1].set_xticks(np.arange(0.0e+1,+12.1, step=12./6))

# Turn off tick labels
axs[0,0].set_xticklabels([])
axs[0,1].set_xticklabels([])
axs[1,0].set_xticklabels([])
axs[1,1].set_xticklabels([])
axs[2,0].set_xticklabels([])
axs[2,1].set_xticklabels([])
axs[3,0].set_xticklabels([])

axs[3,1].set_xlim(-0.0e+1,+12.1)
axs[3,1].set_xticks(np.arange(0.0e+1,+12.1, step=12./6))
axs[4,0].set_xlim(-0.0e+1,+12.1)
axs[4,0].set_xticks(np.arange(0.0e+1,+12.1, step=12./6))


axs[3,1].set_xlim(-0.0e+1,+12.1)
axs[3,1].set_xticks(np.arange(0.0e+1,+12.1, step=12./6))
#axs[0,0].set_ylim(1e-0,+1e+3)
#axs[0,0].set_yticks(np.arange(-0.e-2,+3.1e-0, step=0.5e-0))

axs[0,0].legend(bbox_to_anchor=(-0.6, +1.4), loc=2, borderaxespad=0., ncol=6, labelspacing=.1,handleheight=.1, columnspacing=0.1, handletextpad=0.1)

axs[0,0].set_title("$g_{\\mathcal{K}}= 0.5$" ,fontsize=14, fontname='Times New Roman')
axs[0,1].set_title("$g_{\\mathcal{K}}= 0.6$" ,fontsize=14, fontname='Times New Roman')
axs[1,0].set_title("$g_{\\mathcal{K}}= 0.7$" ,fontsize=14, fontname='Times New Roman')
axs[1,1].set_title("$g_{\\mathcal{K}}= 0.8$" ,fontsize=14, fontname='Times New Roman')
axs[2,0].set_title("$g_{\\mathcal{K}}= 0.9$" ,fontsize=14, fontname='Times New Roman')
axs[2,1].set_title("$g_{\\mathcal{K}}= 1$" ,fontsize=14, fontname='Times New Roman')
axs[3,0].set_title("$g_{\\mathcal{K}}= 2$" ,fontsize=14, fontname='Times New Roman')
axs[3,1].set_title("$g_{\\mathcal{K}}= 5$" ,fontsize=14, fontname='Times New Roman')
axs[4,0].set_title("$g_{\\mathcal{K}}= 10$" ,fontsize=14, fontname='Times New Roman')
#axs[4,1].set_title("$g_{\\mathcal{K}}= 10$" ,fontsize=14, fontname='Times New Roman')

axs[0,0].set_ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}$', fontsize=12, fontname='Times New Roman')
axs[1,0].set_ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}$', fontsize=12, fontname='Times New Roman')
axs[2,0].set_ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}$', fontsize=12, fontname='Times New Roman')
axs[3,0].set_ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}$', fontsize=12, fontname='Times New Roman')
axs[4,0].set_ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}$', fontsize=12, fontname='Times New Roman')
axs[4,0].set_xlabel('$1/N\\times 10^{+3}$', fontsize=12, fontname='Times New Roman')
axs[3,1].set_xlabel('$1/N\\times 10^{+3}$', fontsize=12, fontname='Times New Roman')
#axs[4,1].set_xlabel('$1/N\\times 10^{+3}$', fontsize=12, fontname='Times New Roman')

#axs[0,0].text(-2.2, 2.0e-1, '(m)', fontsize=12)
#axs[0,1].text(-2.2, 2.0e-1, '(n)', fontsize=12)
#axs[1,0].text(-2.2, 2.0e-1, '(o)', fontsize=12)
#axs[1,1].text(-2.2, 2.0e-1, '(p)', fontsize=12)

#axs[0,0].text(-24, 2.5e1, "$k_{n} = \\mathcal{K}\\frac{\\tan^{2}\\left(\\frac{n\\pi/2}{N+1}\\right)}{\\sqrt{2}}$", fontsize=15)

#plt.show()
fig.savefig('PlotsSizesL2.pdf')
