import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

from matplotlib.ticker import (MultipleLocator, NullFormatter,
                                   ScalarFormatter)

fiveSizes = [1./10,1./20,1./30,1./40,1./50]

fileL0 = np.genfromtxt('./fileL0.txt')

fileL0aK = fileL0[:,][:,5*0+0]
fileL0gK = fileL0[:,][:,5*0+1]
fileL0Im = fileL0[:,][:,5*0+2]

fileL2 = np.genfromtxt('./fileL2.txt')

fileL2aK = fileL2[:,][:,5*0+0]
fileL2gK = fileL2[:,][:,5*0+1]
fileL2Im = fileL2[:,][:,5*0+2]

fileL0log10 = np.genfromtxt('./fileL0log10.txt')

fileL0aKlog10 = fileL0log10[:,][:,5*0+0]
fileL0gKlog10 = fileL0log10[:,][:,5*0+1]
fileL0Imlog10 = fileL0log10[:,][:,5*0+2]

fileL2log10 = np.genfromtxt('./fileL2log10.txt')

fileL2aKlog10 = fileL2log10[:,][:,5*0+0]
fileL2gKlog10 = fileL2log10[:,][:,5*0+1]
fileL2Imlog10 = fileL2log10[:,][:,5*0+2]

########################################################################
########################################################################

#OPTIMAL curve_fit

def func(x,y,AK,GK):
    return AK**2/y**2 * np.exp(-GK*x**1)

def _gaussian(M, AK, GK):
    x, y = M
    arr = np.zeros(x.shape)
    arr = func(x,y,AK,GK)
    return arr

def log10func(x,y,AK,GK):
    return np.log10(AK**2/y**2 * np.exp(-GK*x**1))

CouplingSpreading0 = np.vstack((fileL0gK, fileL0aK))
CouplingSpreading2 = np.vstack((fileL2gK, fileL2aK))

poptL0, pcovL0 = curve_fit(_gaussian, CouplingSpreading0, fileL0Im)
poptL2, pcovL2 = curve_fit(_gaussian, CouplingSpreading2, fileL2Im)

print poptL0
print np.sqrt(np.diag(pcovL0))

#print poptL0+np.sqrt(np.diag(pcovL0))
#print poptL0-np.sqrt(np.diag(pcovL0))

print poptL2
print np.sqrt(np.diag(pcovL2))

#print poptL2+np.sqrt(np.diag(pcovL2))
#print poptL2-np.sqrt(np.diag(pcovL2))

#print (poptL2)/2.+(np.sqrt(np.diag(pcovL2)))/1.
#print (poptL2)/2.-(np.sqrt(np.diag(pcovL2)))/1.

axisL2gK = np.zeros(100)
axisL2aK = np.zeros(100)

from matplotlib import cm

plt.clf()
fig = plt.figure(figsize=plt.figaspect(1/2.))
fig.subplots_adjust(left=0.2,bottom=0.0,right=0.75,top=0.7,wspace=0.02,hspace=0.4)

axs = fig.add_subplot(1, 2, 1, projection='3d')
#axs.view_init(elev=6., azim=-134)
axs.view_init(azim=-131, elev=3.)

axs.set_xlim([0, 4-4/100.])
axs.set_ylim([0,10-10/100.])
axs.set_zlim(-10,+0.)

axs.set_xticks(np.arange(-0.0e+1,+4.01e+0, step=1.0e-0))
axs.set_yticks(np.arange(-0.0e+1,+10.01e+0, step=2.0e-0))
axs.set_zticks(np.arange(-10,0.1, step=1))

axs.plot(fileL0gKlog10, fileL0Imlog10, zdir='y', zs= 10, c='b', ls='None', marker='.', markersize=3)
axs.plot(fileL0aKlog10, fileL0Imlog10, zdir='x', zs=  4, c='b', ls='None', marker='.', markersize=3)
#axs.plot(fileL0gKlog10, fileL0aKlog10, zdir='z', zs=-10, c='b', ls='None', marker='.', markersize=3)

#axs.scatter(fileL0gKlog10, fileL0aKlog10, fileL0Imlog10, marker="o", c="b", s=5)

axisL0gK = np.arange(1.*np.rint(min(fileL0gKlog10))-0.2,1.*np.rint(max(fileL0gKlog10))+0.1,(1.*np.rint(max(fileL0gKlog10))-1.*np.rint(min(fileL0gKlog10)))/200.)
axisL0aK = np.arange(1.*np.rint(min(fileL0aKlog10))-0.2,1.*np.rint(max(fileL0aKlog10))+0.1,(1.*np.rint(max(fileL0aKlog10))-1.*np.rint(min(fileL0aKlog10)))/200.)

gridL0gK,gridL0aK = np.meshgrid(axisL0gK, axisL0aK) # grid of point
gridL0Im = log10func(gridL0gK, gridL0aK,*poptL0) # evaluation of the function on the grid

#axs.plot_surface(gridL0gK, gridL0aK, gridL0Im, rstride=8, cstride=8, alpha=0.6, cmap=cm.GnBu)
axs.plot_surface(gridL0gK, gridL0aK, gridL0Im, rstride=15, cstride=15, alpha=.5, cmap=cm.winter)
#cset = axs.contour(gridL0gK, gridL0aK, gridL0Im, zdir='z', offset=-10, cmap=cm.GnBu)
#cset = axs.contour(gridL0gK, gridL0aK, gridL0Im, zdir='x', offset=4, cmap=cm.rainbow_r, levels = [-0.15,0.05,0.45,1,2,2.225,2.5,2.85,3.33,4.01])grb
cset = axs.contour(gridL0gK, gridL0aK, gridL0Im, zdir='x', offset=4, cmap=cm.winter_r, levels = [-0.15,0.05,0.45,1,2,2.225,2.5,2.85,3.33,4.01])
#cset = axs.contour(gridL0gK, gridL0aK, gridL0Im, zdir='x', offset=4, cmap=cm.GnBu_r, levels = [-0.15,0.05,0.45,1,2,2.225,2.5,2.85,3.33,4.01])
#cset = axs.contour(gridL0gK, gridL0aK, gridL0Im, zdir='y', offset=10, cmap=cm.rainbow_r, levels = [1.03,2,3,5,7,9.91])
cset = axs.contour(gridL0gK, gridL0aK, gridL0Im, zdir='y', offset=10, cmap=cm.winter_r, levels = [1.03,2,3,5,7,9.91])
#cset = axs.contour(gridL0gK, gridL0aK, gridL0Im, zdir='y', offset=10, cmap=cm.GnBu_r, levels = [1.03,2,3,5,7,9.91])

#axs.scatter(fileL0gK, fileL0aK, np.log10(fileL0Im), marker="*", c='black', s=20,depthshade='True')

axs.set_xlabel('$1/g_{\\mathcal{K}}$')
axs.set_ylabel('$a_{\\mathcal{K}}$')
axs.set_zlabel('$\\log_{10}$Im[$E(k)(a_{\\mathcal{K}},g_{\\mathcal{K}})$]$/E_{\\mathrm{UV}}$')
axs.set_title("$\\ell = 0$" ,fontsize=14, fontname='Times New Roman', y=0.9)

axs = fig.add_subplot(1, 2, 2, projection='3d')
axs.view_init(azim=-131, elev=3.)
#axs.view_init(elev=11., azim=-125)
#axs.subplots_adjust(left=0.09,bottom=0.02,right=0.87,top=1.00,wspace=0.0,hspace=0.25)

axs.set_xticks([0,0.5,1,1.5,2])
axs.set_yticks([0,2,4,6,8,10])
axs.set_zticks(np.arange(-10,0.1, step=1))

axs.axes.set_xlim3d(left=0.01, right=1.99) 
axs.axes.set_ylim3d(bottom=0.01, top=9.99) 
axs.axes.set_zlim3d(bottom=-9.8, top=-0.2) 

#axs.set_xlim([0, 2])
#axs.axes.set_ylim3d(left=0.000001, right=9.9999999)#.set_ylim([0,10])
#axs.set_zlim([-10,0])

#axs.set_xticks(np.arange(-0.0e+1,+2.01e+0, step=0.5e-0))
#axs.set_yticks(np.arange(-0.0e+1,+10.01e+0, step=2.0e-0))
#axs.set_zticks(np.arange(-10,0.1, step=1))

#axs.plot_trisurf(fileL2gKlog10, fileL2aKlog10, fileL2Imlog10, cmap=plt.cm.Spectral)#, linewidth=0, antialiased=False)
#####################################################################################
#####################################################################################

axs = fig.add_subplot(1, 2, 2, projection='3d')
axs.view_init(azim=-131, elev=3.)
#axs.view_init(elev=11., azim=-125)
#axs.subplots_adjust(left=0.09,bottom=0.02,right=0.87,top=1.00,wspace=0.0,hspace=0.25)

axs.plot(fileL2gKlog10, fileL2Imlog10, zdir='y', zs= 10, c='r', ls='None', marker='.', markersize=3)
axs.plot(fileL2aKlog10, fileL2Imlog10, zdir='x', zs=  2, c='r', ls='None', marker='.', markersize=3)

axisL2gK = np.arange(1.*np.rint(min(fileL2gKlog10))-0.05,1.*np.rint(max(fileL2gKlog10))+0.025,(1.*np.rint(max(fileL2gKlog10))-1.*np.rint(min(fileL2gKlog10)))/200.)
axisL2aK = np.arange(1.*np.rint(min(fileL2aKlog10))-0.05,1.*np.rint(max(fileL2aKlog10))+0.025,(1.*np.rint(max(fileL2aKlog10))-1.*np.rint(min(fileL2aKlog10)))/200.)

gridL2gK,gridL2aK = np.meshgrid(axisL2gK, axisL2aK) # grid of point
gridL2Im = log10func(gridL2gK, gridL2aK,*poptL2) # evaluation of the function on the grid

axs.grid(True)
#fig.colorbar(surf2, shrink=0.5, aspect=5)

#axs.plot_trisurf(fileL2gKlog10, fileL2aKlog10, fileL2Imlog10, cmap=plt.cm.CMRmap)
#axs.scatter(fileL2gKlog10, fileL2aKlog10, fileL2Imlog10, marker="o", c="r", s=20)
#surf2 = axs.plot_surface(gridL2gK,gridL2aK, gridL2Im, rstride=1, cstride=1, cmap=cm.RdBu,linewidth=0, antialiased=False)
#axs.plot_surface(gridL2gK, gridL2aK, gridL2Im, rstride=8, cstride=8, alpha=0.6, cmap=cm.GnBu)
axs.plot_surface(gridL2gK, gridL2aK, gridL2Im, rstride=15, cstride=15, alpha=.5, cmap=cm.autumn)
#axs.plot_surface(gridL2gK, gridL2aK, gridL2Im, rstride=15, cstride=15, alpha=.7, cmap=cm.copper)
#cset = axs.contour(gridL2gK, gridL2aK, gridL2Im, zdir='z', offset=-10, cmap=cm.GnBu)
#cset = axs.contour(gridL2gK, gridL2aK, gridL2Im, zdir='x', offset=4, cmap=cm.rainbow_r, levels = [-0.15,0.05,0.45,1,2,2.225,2.5,2.85,3.33,4.01])grb
cset = axs.contour(gridL2gK, gridL2aK, gridL2Im, zdir='x', offset=2, cmap=cm.autumn_r, levels = [0.02,0.16,0.5,1,1.1,1.25,1.43,1.65,1.99])
#cset = axs.contour(gridL2gK, gridL2aK, gridL2Im, zdir='x', offset=4, cmap=cm.GnBu_r, levels = [-0.15,0.05,0.45,1,2,2.225,2.5,2.85,3.33,4.01])
#cset = axs.contour(gridL2gK, gridL2aK, gridL2Im, zdir='y', offset=10, cmap=cm.rainbow_r, levels = [1.03,2,3,5,7,9.91])
cset = axs.contour(gridL2gK, gridL2aK, gridL2Im, zdir='y', offset=10, cmap=cm.autumn_r, levels = [1.03,2,3,5,7,9.91])
#cset = axs.contour(gridL2gK, gridL2aK, gridL2Im, zdir='y', offset=10, cmap=cm.GnBu_r, levels = [1.03,2,3,5,7,9.91])

#axs.scatter(fileL2gK, fileL2aK, np.log10(fileL2Im), marker="*", c='black', s=20,depthshade='True')

axs.set_xlim([0,2-2/100.])
axs.set_ylim([0,10-10/100.])
axs.set_zlim(-10,+0.)

axs.set_xticks([0,0.5,1,1.5,2])
axs.set_yticks([0,2,4,6,8,10])
axs.set_zticks(np.arange(-10,0.1, step=1))

axs.axes.set_xlim3d(left=0.01, right=1.99) 
axs.axes.set_ylim3d(bottom=0.01, top=9.99) 
axs.axes.set_zlim3d(bottom=-9.8, top=-0.2) 

axs.set_xlabel('$1/g_{\\mathcal{K}}$')
axs.set_ylabel('$a_{\\mathcal{K}}$')
axs.set_zlabel('$\\log_{10}$Im[$E(k)(a_{\\mathcal{K}},g_{\\mathcal{K}})$]$/E_{\\mathrm{UV}}$')
axs.set_title("$\\ell = 2$" ,fontsize=14, fontname='Times New Roman', y=0.9)

plt.savefig('ZZZ-3D.pdf')
#plt.show()

######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################

######################################################################################################

######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################

def funcC0(a,A0,alpha):
    return (A0/a)**alpha

def funcG0(a,A0,alpha):
    return A0 + a * alpha

C0L0 = np.genfromtxt('./C0L0.txt')

C0L0aK = C0L0[:,][:,5*0+0]
C0L0C0 = C0L0[:,][:,5*0+1]
C0L0Er = C0L0[:,][:,5*0+2]

C0L2 = np.genfromtxt('./C0L2.txt')

C0L2aK = C0L2[:,][:,5*0+0]
C0L2C0 = C0L2[:,][:,5*0+1]
C0L2Er = C0L2[:,][:,5*0+2]

G0L0 = np.genfromtxt('./G0L0.txt')

G0L0aK = G0L0[:,][:,5*0+0]
G0L0G0 = G0L0[:,][:,5*0+1]
G0L0Er = G0L0[:,][:,5*0+2]

G0L2 = np.genfromtxt('./G0L2.txt')

G0L2aK = G0L2[:,][:,5*0+0]
G0L2G0 = G0L2[:,][:,5*0+1]
G0L2Er = G0L2[:,][:,5*0+2]

plt.clf()
fig, axs = plt.subplots(1, 2, figsize=(6, 3), sharey=False)
plt.subplots_adjust(left=0.25,bottom=0.20,right=0.8,top=0.7,wspace=0.35,hspace=0.5)

axs[0].errorbar(C0L0aK, C0L0C0, yerr=C0L0Er, c='b', ls='None', marker='None', markersize=3, capsize=2, capthick=.1)
axs[0].errorbar(C0L2aK, C0L2C0, yerr=C0L2Er, c='r', ls='None', marker='None', markersize=3, capsize=2, capthick=.1)

axisC0aK = np.arange(1.*np.rint(min(C0L2aK)),1.*np.rint(max(C0L2aK))+(1.*np.rint(max(C0L2aK))-1.*np.rint(min(C0L2aK)))/100.,(1.*np.rint(max(C0L2aK))-1.*np.rint(min(C0L2aK)))/100.)
axs[0].loglog(axisC0aK, funcC0(axisC0aK,0.528149,1.98966), c='b', ls='-', marker='None', markersize=3,linewidth=0.1)
axs[0].loglog(axisC0aK, funcC0(axisC0aK,0.508436,1.98052), c='r', ls='-', marker='None', markersize=3,linewidth=0.1)

axs[0].loglog(axisC0aK, funcC0(axisC0aK,0.528149-0.002915960,1.98966-0.00621368), c='b', ls='-', marker='None', markersize=3,linewidth=0.1)
axs[0].loglog(axisC0aK, funcC0(axisC0aK,0.508436-0.000499265,1.98052-0.00198037), c='r', ls='-', marker='None', markersize=3,linewidth=0.1)

axs[0].loglog(axisC0aK, funcC0(axisC0aK,0.528149+0.002915960,1.98966+0.00621368), c='b', ls='-', marker='None', markersize=3,linewidth=0.1)
axs[0].loglog(axisC0aK, funcC0(axisC0aK,0.508436+0.000499265,1.98052+0.00198037), c='r', ls='-', marker='None', markersize=3,linewidth=0.1)

axs[0].fill_between(axisC0aK, funcC0(axisC0aK,0.528149-0.002915960,1.98966-0.00621368),funcC0(axisC0aK,0.528149+0.002915960,1.98966+0.00621368), facecolor='blue', alpha=0.5)
axs[0].fill_between(axisC0aK, funcC0(axisC0aK,0.508436-0.000499265,1.98052-0.00198037),funcC0(axisC0aK,0.508436+0.000499265,1.98052+0.00198037), facecolor='red', alpha=0.5)

axs[0].plot(C0L0aK, C0L0C0, c=[0.0/1.5, 0.0/1.5, 1.0/1.5], ls='None', marker='.', markersize=1)
axs[0].plot(C0L2aK, C0L2C0, c=[1.0/1.5, 0.0/1.5, 0.0/1.5], ls='None', marker='.', markersize=1)

#axs[0].set_xlim([0,12.])
#axs[0].set_ylim([0,10-10/100.])
axs[0].grid(True)
axs[0].set_xscale("log")
axs[0].set_yscale("log")

axs[0].set_xlabel('$a_{\\mathcal{K}}$', fontsize=12, fontname='Times New Roman')
axs[0].set_xticks([1,2.,3.,4,5.,6,7.,8,9,10.])
axs[0].set_ylabel('$C_{0}(a_{\\mathcal{K}})$', fontsize=12, fontname='Times New Roman')
#axs[0].set_yticks([0,0.05,0.1,0.15,0.20,0.25,0.30])

###############################

axs[1].errorbar(G0L0aK, 100*(G0L0G0/1.-4), yerr=100*G0L0Er, c='b', ls='None', marker='.', markersize=5, capsize=3, capthick=.5,label='$\ell = 0$')
axs[1].errorbar(G0L2aK, 100*(G0L2G0/2.-4), yerr=100*G0L2Er, c='r', ls='None', marker='.', markersize=5, capsize=2, capthick=.5,label='$\ell = 2$')

axisG0aK = np.arange(1.*np.rint(min(G0L2aK)),1.*np.rint(max(G0L2aK))+(1.*np.rint(max(G0L2aK))-1.*np.rint(min(G0L2aK)))/100.,(1.*np.rint(max(G0L2aK))-1.*np.rint(min(G0L2aK)))/100.)
axs[1].plot(axisC0aK, 100*(funcG0(axisC0aK,4.01999/1.-4,0.00210989/1.)), c='b', ls='-', marker='None', markersize=3,linewidth=0.5)
axs[1].plot(axisC0aK, 100*(funcG0(axisC0aK,8.03441/2.-4,0.00778221/2.)), c='r', ls='-', marker='None', markersize=3,linewidth=0.5)

axs[1].plot(axisC0aK, 100*(funcG0(axisC0aK,(4.01999-0.00255665)/1.-4,(0.00210989-0.000644822)/1.)), c='b', ls='-', marker='None', markersize=3,linewidth=0.1)
axs[1].plot(axisC0aK, 100*(funcG0(axisC0aK,(8.03441-0.00154081)/2.-4,(0.00778221-0.000839023)/2.)), c='r', ls='-', marker='None', markersize=3,linewidth=0.1)

axs[1].plot(axisC0aK, 100*(funcG0(axisC0aK,(4.01999+0.00255665)/1.-4,(0.00210989+0.000644822)/1.)), c='b', ls='-', marker='None', markersize=3,linewidth=0.1)
axs[1].plot(axisC0aK, 100*(funcG0(axisC0aK,(8.03441+0.00154081)/2.-4,(0.00778221+0.000839023)/2.)), c='r', ls='-', marker='None', markersize=3,linewidth=0.1)

axs[1].fill_between(axisC0aK, 100*(funcG0(axisC0aK,(4.01999+0.00255665)/1.-4,(0.00210989+0.000644822)/1.)),100*(funcG0(axisC0aK,(4.01999-0.00255665)/1.-4,(0.00210989-0.000644822)/1.)), facecolor='blue', alpha=0.5)
axs[1].fill_between(axisC0aK, 100*(funcG0(axisC0aK,(8.03441-0.00154081)/2.-4,(0.00778221-0.000839023)/2.)),100*(funcG0(axisC0aK,(8.03441+0.00154081)/2.-4,(0.00778221+0.000839023)/2.)), facecolor='red', alpha=0.5)

axs[1].set_xlim([0,12.])
axs[1].set_xticks([0.,2.,4.,6.,8.,10.,12.])
#axs[1].set_ylim([0.00,0.08])
#axs[1].set_yticks([0,0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08])
axs[1].grid(True)

axs[1].set_xlabel('$a_{\\mathcal{K}}$', fontsize=12, fontname='Times New Roman')
axs[1].set_ylabel('$G_{0}(a_{\\mathcal{K}})-4$ (1E-2)', fontsize=12, fontname='Times New Roman')

#plt.clf()
#fig, axs = plt.subplots(1, 2, figsize=(6, 3),  projection='3d')
#plt.subplots_adjust(left=0.25,bottom=0.25,right=0.8,top=0.8,wspace=0.1,hspace=0.4)

axs[1].legend(bbox_to_anchor=(1.05, +0.63), loc=2, borderaxespad=0., ncol=1, labelspacing=1,handleheight=.05, columnspacing=.05, handletextpad=.05)

#plt.show()
fig.savefig('PlotC0G0.pdf')

######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################

######################################################################################################

######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################

