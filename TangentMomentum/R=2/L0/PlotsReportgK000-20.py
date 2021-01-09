import numpy as np
import matplotlib.pyplot as plt

fiveSizes = [1./10,1./20,1./30,1./40,1./50]
fiveSizesA = [1./400,1./500,1./600,1./700,1./800]

###############################################
###############################################
###############################################

data0010011010 = np.genfromtxt('./gK000-20/aK001/N040/HamVals.txt')

MomentumAx0010011010 = data0010011010[:,][:,5*0+0]
KineticEne0010011010 = data0010011010[:,][:,5*0+1]
SelfEnergy0010011010 = data0010011010[:,][:,5*0+2]
EigenValRe0010011010 = data0010011010[:,][:,5*0+3]
EigenValIm0010011010 = data0010011010[:,][:,5*0+4]

data0010011020 = np.genfromtxt('./gK000-20/aK001/N050/HamVals.txt')

MomentumAx0010011020 = data0010011020[:,][:,5*0+0]
KineticEne0010011020 = data0010011020[:,][:,5*0+1]
SelfEnergy0010011020 = data0010011020[:,][:,5*0+2]
EigenValRe0010011020 = data0010011020[:,][:,5*0+3]
EigenValIm0010011020 = data0010011020[:,][:,5*0+4]

data0010011030 = np.genfromtxt('./gK000-20/aK001/N060/HamVals.txt')

MomentumAx0010011030 = data0010011030[:,][:,5*0+0]
KineticEne0010011030 = data0010011030[:,][:,5*0+1]
SelfEnergy0010011030 = data0010011030[:,][:,5*0+2]
EigenValRe0010011030 = data0010011030[:,][:,5*0+3]
EigenValIm0010011030 = data0010011030[:,][:,5*0+4]

data0010011040 = np.genfromtxt('./gK000-20/aK001/N070/HamVals.txt')

MomentumAx0010011040 = data0010011040[:,][:,5*0+0]
KineticEne0010011040 = data0010011040[:,][:,5*0+1]
SelfEnergy0010011040 = data0010011040[:,][:,5*0+2]
EigenValRe0010011040 = data0010011040[:,][:,5*0+3]
EigenValIm0010011040 = data0010011040[:,][:,5*0+4]

data0010011050 = np.genfromtxt('./gK000-20/aK001/N080/HamVals.txt')

MomentumAx0010011050 = data0010011050[:,][:,5*0+0]
KineticEne0010011050 = data0010011050[:,][:,5*0+1]
SelfEnergy0010011050 = data0010011050[:,][:,5*0+2]
EigenValRe0010011050 = data0010011050[:,][:,5*0+3]
EigenValIm0010011050 = data0010011050[:,][:,5*0+4]

data0010021010 = np.genfromtxt('./gK000-20/aK002/N040/HamVals.txt')

MomentumAx0010021010 = data0010021010[:,][:,5*0+0]
KineticEne0010021010 = data0010021010[:,][:,5*0+1]
SelfEnergy0010021010 = data0010021010[:,][:,5*0+2]
EigenValRe0010021010 = data0010021010[:,][:,5*0+3]
EigenValIm0010021010 = data0010021010[:,][:,5*0+4]

data0010021020 = np.genfromtxt('./gK000-20/aK002/N050/HamVals.txt')

MomentumAx0010021020 = data0010021020[:,][:,5*0+0]
KineticEne0010021020 = data0010021020[:,][:,5*0+1]
SelfEnergy0010021020 = data0010021020[:,][:,5*0+2]
EigenValRe0010021020 = data0010021020[:,][:,5*0+3]
EigenValIm0010021020 = data0010021020[:,][:,5*0+4]

data0010021030 = np.genfromtxt('./gK000-20/aK002/N060/HamVals.txt')

MomentumAx0010021030 = data0010021030[:,][:,5*0+0]
KineticEne0010021030 = data0010021030[:,][:,5*0+1]
SelfEnergy0010021030 = data0010021030[:,][:,5*0+2]
EigenValRe0010021030 = data0010021030[:,][:,5*0+3]
EigenValIm0010021030 = data0010021030[:,][:,5*0+4]

data0010021040 = np.genfromtxt('./gK000-20/aK002/N070/HamVals.txt')

MomentumAx0010021040 = data0010021040[:,][:,5*0+0]
KineticEne0010021040 = data0010021040[:,][:,5*0+1]
SelfEnergy0010021040 = data0010021040[:,][:,5*0+2]
EigenValRe0010021040 = data0010021040[:,][:,5*0+3]
EigenValIm0010021040 = data0010021040[:,][:,5*0+4]

data0010021050 = np.genfromtxt('./gK000-20/aK002/N080/HamVals.txt')

MomentumAx0010021050 = data0010021050[:,][:,5*0+0]
KineticEne0010021050 = data0010021050[:,][:,5*0+1]
SelfEnergy0010021050 = data0010021050[:,][:,5*0+2]
EigenValRe0010021050 = data0010021050[:,][:,5*0+3]
EigenValIm0010021050 = data0010021050[:,][:,5*0+4]

data0010051010 = np.genfromtxt('./gK000-20/aK005/N040/HamVals.txt')

MomentumAx0010051010 = data0010051010[:,][:,5*0+0]
KineticEne0010051010 = data0010051010[:,][:,5*0+1]
SelfEnergy0010051010 = data0010051010[:,][:,5*0+2]
EigenValRe0010051010 = data0010051010[:,][:,5*0+3]
EigenValIm0010051010 = data0010051010[:,][:,5*0+4]

data0010051020 = np.genfromtxt('./gK000-20/aK005/N050/HamVals.txt')

MomentumAx0010051020 = data0010051020[:,][:,5*0+0]
KineticEne0010051020 = data0010051020[:,][:,5*0+1]
SelfEnergy0010051020 = data0010051020[:,][:,5*0+2]
EigenValRe0010051020 = data0010051020[:,][:,5*0+3]
EigenValIm0010051020 = data0010051020[:,][:,5*0+4]

data0010051030 = np.genfromtxt('./gK000-20/aK005/N060/HamVals.txt')

MomentumAx0010051030 = data0010051030[:,][:,5*0+0]
KineticEne0010051030 = data0010051030[:,][:,5*0+1]
SelfEnergy0010051030 = data0010051030[:,][:,5*0+2]
EigenValRe0010051030 = data0010051030[:,][:,5*0+3]
EigenValIm0010051030 = data0010051030[:,][:,5*0+4]

data0010051040 = np.genfromtxt('./gK000-20/aK005/N070/HamVals.txt')

MomentumAx0010051040 = data0010051040[:,][:,5*0+0]
KineticEne0010051040 = data0010051040[:,][:,5*0+1]
SelfEnergy0010051040 = data0010051040[:,][:,5*0+2]
EigenValRe0010051040 = data0010051040[:,][:,5*0+3]
EigenValIm0010051040 = data0010051040[:,][:,5*0+4]

data0010051050 = np.genfromtxt('./gK000-20/aK005/N080/HamVals.txt')

MomentumAx0010051050 = data0010051050[:,][:,5*0+0]
KineticEne0010051050 = data0010051050[:,][:,5*0+1]
SelfEnergy0010051050 = data0010051050[:,][:,5*0+2]
EigenValRe0010051050 = data0010051050[:,][:,5*0+3]
EigenValIm0010051050 = data0010051050[:,][:,5*0+4]

data0010101010 = np.genfromtxt('./gK000-20/aK010/N040/HamVals.txt')

MomentumAx0010101010 = data0010101010[:,][:,5*0+0]
KineticEne0010101010 = data0010101010[:,][:,5*0+1]
SelfEnergy0010101010 = data0010101010[:,][:,5*0+2]
EigenValRe0010101010 = data0010101010[:,][:,5*0+3]
EigenValIm0010101010 = data0010101010[:,][:,5*0+4]

data0010101020 = np.genfromtxt('./gK000-20/aK010/N050/HamVals.txt')

MomentumAx0010101020 = data0010101020[:,][:,5*0+0]
KineticEne0010101020 = data0010101020[:,][:,5*0+1]
SelfEnergy0010101020 = data0010101020[:,][:,5*0+2]
EigenValRe0010101020 = data0010101020[:,][:,5*0+3]
EigenValIm0010101020 = data0010101020[:,][:,5*0+4]

data0010101030 = np.genfromtxt('./gK000-20/aK010/N060/HamVals.txt')

MomentumAx0010101030 = data0010101030[:,][:,5*0+0]
KineticEne0010101030 = data0010101030[:,][:,5*0+1]
SelfEnergy0010101030 = data0010101030[:,][:,5*0+2]
EigenValRe0010101030 = data0010101030[:,][:,5*0+3]
EigenValIm0010101030 = data0010101030[:,][:,5*0+4]

data0010101040 = np.genfromtxt('./gK000-20/aK010/N070/HamVals.txt')

MomentumAx0010101040 = data0010101040[:,][:,5*0+0]
KineticEne0010101040 = data0010101040[:,][:,5*0+1]
SelfEnergy0010101040 = data0010101040[:,][:,5*0+2]
EigenValRe0010101040 = data0010101040[:,][:,5*0+3]
EigenValIm0010101040 = data0010101040[:,][:,5*0+4]

data0010101050 = np.genfromtxt('./gK000-20/aK010/N080/HamVals.txt')

MomentumAx0010101050 = data0010101050[:,][:,5*0+0]
KineticEne0010101050 = data0010101050[:,][:,5*0+1]
SelfEnergy0010101050 = data0010101050[:,][:,5*0+2]
EigenValRe0010101050 = data0010101050[:,][:,5*0+3]
EigenValIm0010101050 = data0010101050[:,][:,5*0+4]
"""
data0010201010 = np.genfromtxt('./gK000-20/aK020/N010/HamVals.txt')

MomentumAx0010201010 = data0010201010[:,][:,5*0+0]
KineticEne0010201010 = data0010201010[:,][:,5*0+1]
SelfEnergy0010201010 = data0010201010[:,][:,5*0+2]
EigenValRe0010201010 = data0010201010[:,][:,5*0+3]
EigenValIm0010201010 = data0010201010[:,][:,5*0+4]

data0010201020 = np.genfromtxt('./gK000-20/aK020/N020/HamVals.txt')

MomentumAx0010201020 = data0010201020[:,][:,5*0+0]
KineticEne0010201020 = data0010201020[:,][:,5*0+1]
SelfEnergy0010201020 = data0010201020[:,][:,5*0+2]
EigenValRe0010201020 = data0010201020[:,][:,5*0+3]
EigenValIm0010201020 = data0010201020[:,][:,5*0+4]

data0010201030 = np.genfromtxt('./gK000-20/aK020/N030/HamVals.txt')

MomentumAx0010201030 = data0010201030[:,][:,5*0+0]
KineticEne0010201030 = data0010201030[:,][:,5*0+1]
SelfEnergy0010201030 = data0010201030[:,][:,5*0+2]
EigenValRe0010201030 = data0010201030[:,][:,5*0+3]
EigenValIm0010201030 = data0010201030[:,][:,5*0+4]

data0010201040 = np.genfromtxt('./gK000-20/aK020/N040/HamVals.txt')

MomentumAx0010201040 = data0010201040[:,][:,5*0+0]
KineticEne0010201040 = data0010201040[:,][:,5*0+1]
SelfEnergy0010201040 = data0010201040[:,][:,5*0+2]
EigenValRe0010201040 = data0010201040[:,][:,5*0+3]
EigenValIm0010201040 = data0010201040[:,][:,5*0+4]

data0010201050 = np.genfromtxt('./gK000-20/aK020/N050/HamVals.txt')

MomentumAx0010201050 = data0010201050[:,][:,5*0+0]
KineticEne0010201050 = data0010201050[:,][:,5*0+1]
SelfEnergy0010201050 = data0010201050[:,][:,5*0+2]
EigenValRe0010201050 = data0010201050[:,][:,5*0+3]
EigenValIm0010201050 = data0010201050[:,][:,5*0+4]
"""

MaxEigenValIm0011010 = np.zeros((4))
MaxEigenValIm0011020 = np.zeros((4))
MaxEigenValIm0011030 = np.zeros((4))
MaxEigenValIm0011040 = np.zeros((4))
MaxEigenValIm0011050 = np.zeros((4))
MaxEigenValIm0011Inf = np.zeros((4))

MaxEigenValIm0011010[0] = np.max(EigenValIm0010011010)
MaxEigenValIm0011010[1] = np.max(EigenValIm0010021010)
MaxEigenValIm0011010[2] = np.max(EigenValIm0010051010)
MaxEigenValIm0011010[3] = np.max(EigenValIm0010101010)
#MaxEigenValIm0011010[4] = np.max(EigenValIm0010201010)

MaxEigenValIm0011020[0] = np.max(EigenValIm0010011020)
MaxEigenValIm0011020[1] = np.max(EigenValIm0010021020)
MaxEigenValIm0011020[2] = np.max(EigenValIm0010051020)
MaxEigenValIm0011020[3] = np.max(EigenValIm0010101020)
#MaxEigenValIm0011020[4] = np.max(EigenValIm0010201020)

MaxEigenValIm0011030[0] = np.max(EigenValIm0010011030)
MaxEigenValIm0011030[1] = np.max(EigenValIm0010021030)
MaxEigenValIm0011030[2] = np.max(EigenValIm0010051030)
MaxEigenValIm0011030[3] = np.max(EigenValIm0010101030)
#MaxEigenValIm0011030[4] = np.max(EigenValIm0010201030)

MaxEigenValIm0011040[0] = np.max(EigenValIm0010011040)
MaxEigenValIm0011040[1] = np.max(EigenValIm0010021040)
MaxEigenValIm0011040[2] = np.max(EigenValIm0010051040)
MaxEigenValIm0011040[3] = np.max(EigenValIm0010101040)
#MaxEigenValIm0011040[4] = np.max(EigenValIm0010201040)

MaxEigenValIm0011050[0] = np.max(EigenValIm0010011050)
MaxEigenValIm0011050[1] = np.max(EigenValIm0010021050)
MaxEigenValIm0011050[2] = np.max(EigenValIm0010051050)
MaxEigenValIm0011050[3] = np.max(EigenValIm0010101050)
#MaxEigenValIm0011050[4] = np.max(EigenValIm0010201050)

fiveSizesB = [1./700,1./800]

MaxEigenValIm0011Inf[0] = np.polyfit(fiveSizesA, [MaxEigenValIm0011010[0],MaxEigenValIm0011020[0],MaxEigenValIm0011030[0],MaxEigenValIm0011040[0],MaxEigenValIm0011050[0]], 1)[[1]]
MaxEigenValIm0011Inf[1] = np.polyfit(fiveSizesA, [MaxEigenValIm0011010[1],MaxEigenValIm0011020[1],MaxEigenValIm0011030[1],MaxEigenValIm0011040[1],MaxEigenValIm0011050[1]], 1)[[1]]
MaxEigenValIm0011Inf[2] = np.polyfit(fiveSizesA, [MaxEigenValIm0011010[2],MaxEigenValIm0011020[2],MaxEigenValIm0011030[2],MaxEigenValIm0011040[2],MaxEigenValIm0011050[2]], 1)[[1]]
MaxEigenValIm0011Inf[3] = np.polyfit(fiveSizesB, [MaxEigenValIm0011040[3],MaxEigenValIm0011050[3]], 1)[[1]]



plt.clf()
fig, axs = plt.subplots(2, 2, figsize=(6, 6), sharey=False)
plt.subplots_adjust(left=0.2,bottom=0.2,right=0.95,top=0.9,wspace=0.4,hspace=0.4)

print MomentumAx0010011010[400]
print MomentumAx0010011020[500]

axs[0,0].semilogy(MomentumAx0010011010[400],EigenValIm0010011010[400], marker='^',c=[1.0, 0.0, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[0,0].plot(MomentumAx0010011020[500],EigenValIm0010011020[500], marker='s',c=[1.0, 0.0, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[0,0].plot(MomentumAx0010011030[600],EigenValIm0010011030[600], marker='p',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[0,0].plot(MomentumAx0010011040[700],EigenValIm0010011040[700], marker='h',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[0,0].plot(MomentumAx0010011050[800],EigenValIm0010011050[800], marker='8',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[0,0].plot(                             [0],[MaxEigenValIm0011Inf[0]], marker='o',c=[1.0, 0.0, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 1$', markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])

axs[0,0].plot(MomentumAx0010011010[400],EigenValIm0010021010[400], marker='^',c=[1.0, 0.5, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[0,0].plot(MomentumAx0010011020[500],EigenValIm0010021020[500], marker='s',c=[1.0, 0.5, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[0,0].plot(MomentumAx0010011030[600],EigenValIm0010021030[600], marker='p',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[0,0].plot(MomentumAx0010011040[700],EigenValIm0010021040[700], marker='h',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[0,0].plot(MomentumAx0010011050[800],EigenValIm0010021050[800], marker='8',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[0,0].plot(                             [0],[MaxEigenValIm0011Inf[1]], marker='o',c=[1.0, 0.5, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 2$', markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])

axs[0,0].plot(MomentumAx0010011010[400],EigenValIm0010051010[400], marker='^',c=[0.0, 1.0, 0.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[0,0].plot(MomentumAx0010011020[500],EigenValIm0010051020[500], marker='s',c=[0.0, 1.0, 0.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[0,0].plot(MomentumAx0010011030[600],EigenValIm0010051030[600], marker='p',c=[0.0, 1.0, 0.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[0,0].plot(MomentumAx0010011040[700],EigenValIm0010051040[700], marker='h',c=[0.0, 1.0, 0.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[0,0].plot(MomentumAx0010011050[800],EigenValIm0010051050[800], marker='8',c=[0.0, 1.0, 0.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[0,0].plot(                             [0],[MaxEigenValIm0011Inf[2]], marker='o',c=[0.0, 1.0, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 5$', markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])

axs[0,0].plot(MomentumAx0010101010[400],EigenValIm0010101010[400], marker='^',c=[0.0, 0.0, 1.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[0,0].plot(MomentumAx0010101020[500],EigenValIm0010101020[500], marker='s',c=[0.0, 0.0, 1.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[0,0].plot(MomentumAx0010101030[600],EigenValIm0010101030[600], marker='p',c=[0.0, 0.0, 1.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[0,0].plot(MomentumAx0010101040[700],EigenValIm0010101040[700], marker='h',c=[0.0, 0.0, 1.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[0,0].plot(MomentumAx0010101050[800],EigenValIm0010101050[800], marker='8',c=[0.0, 0.0, 1.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[0,0].plot(                             [0],[MaxEigenValIm0011Inf[3]], marker='o',c=[0.0, 0.0, 1.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 10$',markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])

axs[0,0].grid(True)
#axs[0,0].set_xlim(-0.0e+1,+2.0e+1)
#axs[0,0].set_xticks(np.arange(-0.0e+1,+2.01e+1, step=4.e-0))
#axs[0,0].set_ylim(1e-0,+1e+3)
#axs[0,0].set_yticks(np.arange(-0.e-2,+3.1e-0, step=0.5e-0))

axs[0,0].legend(bbox_to_anchor=(0.3, +1.3), loc=2, borderaxespad=0., ncol=4, labelspacing=1,handleheight=1, columnspacing=0.1, handletextpad=0.1)
#plt.suptitle('$\\ell=0XXX, g_{\\mathcal{K}}=0.1$', fontsize=20, fontname='Times New Roman')
axs[0,0].set_xlabel('$k/\\mathcal{K}\\times 10^{+5}$', fontsize=12, fontname='Times New Roman')
axs[0,0].set_ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}\\times 10^{+5}$', fontsize=12, fontname='Times New Roman')

###############################################
###############################################
###############################################

data0010011010 = np.genfromtxt('./gK000-30/aK001/N010/HamVals.txt')

MomentumAx0010011010 = data0010011010[:,][:,5*0+0]
KineticEne0010011010 = data0010011010[:,][:,5*0+1]
SelfEnergy0010011010 = data0010011010[:,][:,5*0+2]
EigenValRe0010011010 = data0010011010[:,][:,5*0+3]
EigenValIm0010011010 = data0010011010[:,][:,5*0+4]

data0010011020 = np.genfromtxt('./gK000-30/aK001/N020/HamVals.txt')

MomentumAx0010011020 = data0010011020[:,][:,5*0+0]
KineticEne0010011020 = data0010011020[:,][:,5*0+1]
SelfEnergy0010011020 = data0010011020[:,][:,5*0+2]
EigenValRe0010011020 = data0010011020[:,][:,5*0+3]
EigenValIm0010011020 = data0010011020[:,][:,5*0+4]

data0010011030 = np.genfromtxt('./gK000-30/aK001/N030/HamVals.txt')

MomentumAx0010011030 = data0010011030[:,][:,5*0+0]
KineticEne0010011030 = data0010011030[:,][:,5*0+1]
SelfEnergy0010011030 = data0010011030[:,][:,5*0+2]
EigenValRe0010011030 = data0010011030[:,][:,5*0+3]
EigenValIm0010011030 = data0010011030[:,][:,5*0+4]

data0010011040 = np.genfromtxt('./gK000-30/aK001/N040/HamVals.txt')

MomentumAx0010011040 = data0010011040[:,][:,5*0+0]
KineticEne0010011040 = data0010011040[:,][:,5*0+1]
SelfEnergy0010011040 = data0010011040[:,][:,5*0+2]
EigenValRe0010011040 = data0010011040[:,][:,5*0+3]
EigenValIm0010011040 = data0010011040[:,][:,5*0+4]

data0010011050 = np.genfromtxt('./gK000-30/aK001/N050/HamVals.txt')

MomentumAx0010011050 = data0010011050[:,][:,5*0+0]
KineticEne0010011050 = data0010011050[:,][:,5*0+1]
SelfEnergy0010011050 = data0010011050[:,][:,5*0+2]
EigenValRe0010011050 = data0010011050[:,][:,5*0+3]
EigenValIm0010011050 = data0010011050[:,][:,5*0+4]

data0010021010 = np.genfromtxt('./gK000-30/aK002/N010/HamVals.txt')

MomentumAx0010021010 = data0010021010[:,][:,5*0+0]
KineticEne0010021010 = data0010021010[:,][:,5*0+1]
SelfEnergy0010021010 = data0010021010[:,][:,5*0+2]
EigenValRe0010021010 = data0010021010[:,][:,5*0+3]
EigenValIm0010021010 = data0010021010[:,][:,5*0+4]

data0010021020 = np.genfromtxt('./gK000-30/aK002/N020/HamVals.txt')

MomentumAx0010021020 = data0010021020[:,][:,5*0+0]
KineticEne0010021020 = data0010021020[:,][:,5*0+1]
SelfEnergy0010021020 = data0010021020[:,][:,5*0+2]
EigenValRe0010021020 = data0010021020[:,][:,5*0+3]
EigenValIm0010021020 = data0010021020[:,][:,5*0+4]

data0010021030 = np.genfromtxt('./gK000-30/aK002/N030/HamVals.txt')

MomentumAx0010021030 = data0010021030[:,][:,5*0+0]
KineticEne0010021030 = data0010021030[:,][:,5*0+1]
SelfEnergy0010021030 = data0010021030[:,][:,5*0+2]
EigenValRe0010021030 = data0010021030[:,][:,5*0+3]
EigenValIm0010021030 = data0010021030[:,][:,5*0+4]

data0010021040 = np.genfromtxt('./gK000-30/aK002/N040/HamVals.txt')

MomentumAx0010021040 = data0010021040[:,][:,5*0+0]
KineticEne0010021040 = data0010021040[:,][:,5*0+1]
SelfEnergy0010021040 = data0010021040[:,][:,5*0+2]
EigenValRe0010021040 = data0010021040[:,][:,5*0+3]
EigenValIm0010021040 = data0010021040[:,][:,5*0+4]

data0010021050 = np.genfromtxt('./gK000-30/aK002/N050/HamVals.txt')

MomentumAx0010021050 = data0010021050[:,][:,5*0+0]
KineticEne0010021050 = data0010021050[:,][:,5*0+1]
SelfEnergy0010021050 = data0010021050[:,][:,5*0+2]
EigenValRe0010021050 = data0010021050[:,][:,5*0+3]
EigenValIm0010021050 = data0010021050[:,][:,5*0+4]

data0010051010 = np.genfromtxt('./gK000-30/aK005/N010/HamVals.txt')

MomentumAx0010051010 = data0010051010[:,][:,5*0+0]
KineticEne0010051010 = data0010051010[:,][:,5*0+1]
SelfEnergy0010051010 = data0010051010[:,][:,5*0+2]
EigenValRe0010051010 = data0010051010[:,][:,5*0+3]
EigenValIm0010051010 = data0010051010[:,][:,5*0+4]

data0010051020 = np.genfromtxt('./gK000-30/aK005/N020/HamVals.txt')

MomentumAx0010051020 = data0010051020[:,][:,5*0+0]
KineticEne0010051020 = data0010051020[:,][:,5*0+1]
SelfEnergy0010051020 = data0010051020[:,][:,5*0+2]
EigenValRe0010051020 = data0010051020[:,][:,5*0+3]
EigenValIm0010051020 = data0010051020[:,][:,5*0+4]

data0010051030 = np.genfromtxt('./gK000-30/aK005/N030/HamVals.txt')

MomentumAx0010051030 = data0010051030[:,][:,5*0+0]
KineticEne0010051030 = data0010051030[:,][:,5*0+1]
SelfEnergy0010051030 = data0010051030[:,][:,5*0+2]
EigenValRe0010051030 = data0010051030[:,][:,5*0+3]
EigenValIm0010051030 = data0010051030[:,][:,5*0+4]

data0010051040 = np.genfromtxt('./gK000-30/aK005/N040/HamVals.txt')

MomentumAx0010051040 = data0010051040[:,][:,5*0+0]
KineticEne0010051040 = data0010051040[:,][:,5*0+1]
SelfEnergy0010051040 = data0010051040[:,][:,5*0+2]
EigenValRe0010051040 = data0010051040[:,][:,5*0+3]
EigenValIm0010051040 = data0010051040[:,][:,5*0+4]

data0010051050 = np.genfromtxt('./gK000-30/aK005/N050/HamVals.txt')

MomentumAx0010051050 = data0010051050[:,][:,5*0+0]
KineticEne0010051050 = data0010051050[:,][:,5*0+1]
SelfEnergy0010051050 = data0010051050[:,][:,5*0+2]
EigenValRe0010051050 = data0010051050[:,][:,5*0+3]
EigenValIm0010051050 = data0010051050[:,][:,5*0+4]

data0010101010 = np.genfromtxt('./gK000-30/aK010/N010/HamVals.txt')

MomentumAx0010101010 = data0010101010[:,][:,5*0+0]
KineticEne0010101010 = data0010101010[:,][:,5*0+1]
SelfEnergy0010101010 = data0010101010[:,][:,5*0+2]
EigenValRe0010101010 = data0010101010[:,][:,5*0+3]
EigenValIm0010101010 = data0010101010[:,][:,5*0+4]

data0010101020 = np.genfromtxt('./gK000-30/aK010/N020/HamVals.txt')

MomentumAx0010101020 = data0010101020[:,][:,5*0+0]
KineticEne0010101020 = data0010101020[:,][:,5*0+1]
SelfEnergy0010101020 = data0010101020[:,][:,5*0+2]
EigenValRe0010101020 = data0010101020[:,][:,5*0+3]
EigenValIm0010101020 = data0010101020[:,][:,5*0+4]

data0010101030 = np.genfromtxt('./gK000-30/aK010/N030/HamVals.txt')

MomentumAx0010101030 = data0010101030[:,][:,5*0+0]
KineticEne0010101030 = data0010101030[:,][:,5*0+1]
SelfEnergy0010101030 = data0010101030[:,][:,5*0+2]
EigenValRe0010101030 = data0010101030[:,][:,5*0+3]
EigenValIm0010101030 = data0010101030[:,][:,5*0+4]

data0010101040 = np.genfromtxt('./gK000-30/aK010/N040/HamVals.txt')

MomentumAx0010101040 = data0010101040[:,][:,5*0+0]
KineticEne0010101040 = data0010101040[:,][:,5*0+1]
SelfEnergy0010101040 = data0010101040[:,][:,5*0+2]
EigenValRe0010101040 = data0010101040[:,][:,5*0+3]
EigenValIm0010101040 = data0010101040[:,][:,5*0+4]

data0010101050 = np.genfromtxt('./gK000-30/aK010/N050/HamVals.txt')

MomentumAx0010101050 = data0010101050[:,][:,5*0+0]
KineticEne0010101050 = data0010101050[:,][:,5*0+1]
SelfEnergy0010101050 = data0010101050[:,][:,5*0+2]
EigenValRe0010101050 = data0010101050[:,][:,5*0+3]
EigenValIm0010101050 = data0010101050[:,][:,5*0+4]
"""
data0010201010 = np.genfromtxt('./gK000-30/aK020/N010/HamVals.txt')

MomentumAx0010201010 = data0010201010[:,][:,5*0+0]
KineticEne0010201010 = data0010201010[:,][:,5*0+1]
SelfEnergy0010201010 = data0010201010[:,][:,5*0+2]
EigenValRe0010201010 = data0010201010[:,][:,5*0+3]
EigenValIm0010201010 = data0010201010[:,][:,5*0+4]

data0010201020 = np.genfromtxt('./gK000-30/aK020/N020/HamVals.txt')

MomentumAx0010201020 = data0010201020[:,][:,5*0+0]
KineticEne0010201020 = data0010201020[:,][:,5*0+1]
SelfEnergy0010201020 = data0010201020[:,][:,5*0+2]
EigenValRe0010201020 = data0010201020[:,][:,5*0+3]
EigenValIm0010201020 = data0010201020[:,][:,5*0+4]

data0010201030 = np.genfromtxt('./gK000-30/aK020/N030/HamVals.txt')

MomentumAx0010201030 = data0010201030[:,][:,5*0+0]
KineticEne0010201030 = data0010201030[:,][:,5*0+1]
SelfEnergy0010201030 = data0010201030[:,][:,5*0+2]
EigenValRe0010201030 = data0010201030[:,][:,5*0+3]
EigenValIm0010201030 = data0010201030[:,][:,5*0+4]

data0010201040 = np.genfromtxt('./gK000-30/aK020/N040/HamVals.txt')

MomentumAx0010201040 = data0010201040[:,][:,5*0+0]
KineticEne0010201040 = data0010201040[:,][:,5*0+1]
SelfEnergy0010201040 = data0010201040[:,][:,5*0+2]
EigenValRe0010201040 = data0010201040[:,][:,5*0+3]
EigenValIm0010201040 = data0010201040[:,][:,5*0+4]

data0010201050 = np.genfromtxt('./gK000-30/aK020/N050/HamVals.txt')

MomentumAx0010201050 = data0010201050[:,][:,5*0+0]
KineticEne0010201050 = data0010201050[:,][:,5*0+1]
SelfEnergy0010201050 = data0010201050[:,][:,5*0+2]
EigenValRe0010201050 = data0010201050[:,][:,5*0+3]
EigenValIm0010201050 = data0010201050[:,][:,5*0+4]
"""

MaxEigenValIm0011010 = np.zeros((4))
MaxEigenValIm0011020 = np.zeros((4))
MaxEigenValIm0011030 = np.zeros((4))
MaxEigenValIm0011040 = np.zeros((4))
MaxEigenValIm0011050 = np.zeros((4))
MaxEigenValIm0011Inf = np.zeros((4))

MaxEigenValIm0011010[0] = np.max(EigenValIm0010011010)
MaxEigenValIm0011010[1] = np.max(EigenValIm0010021010)
MaxEigenValIm0011010[2] = np.max(EigenValIm0010051010)
MaxEigenValIm0011010[3] = np.max(EigenValIm0010101010)
#MaxEigenValIm0011010[4] = np.max(EigenValIm0010201010)

MaxEigenValIm0011020[0] = np.max(EigenValIm0010011020)
MaxEigenValIm0011020[1] = np.max(EigenValIm0010021020)
MaxEigenValIm0011020[2] = np.max(EigenValIm0010051020)
MaxEigenValIm0011020[3] = np.max(EigenValIm0010101020)
#MaxEigenValIm0011020[4] = np.max(EigenValIm0010201020)

MaxEigenValIm0011030[0] = np.max(EigenValIm0010011030)
MaxEigenValIm0011030[1] = np.max(EigenValIm0010021030)
MaxEigenValIm0011030[2] = np.max(EigenValIm0010051030)
MaxEigenValIm0011030[3] = np.max(EigenValIm0010101030)
#MaxEigenValIm0011030[4] = np.max(EigenValIm0010201030)

MaxEigenValIm0011040[0] = np.max(EigenValIm0010011040)
MaxEigenValIm0011040[1] = np.max(EigenValIm0010021040)
MaxEigenValIm0011040[2] = np.max(EigenValIm0010051040)
MaxEigenValIm0011040[3] = np.max(EigenValIm0010101040)
#MaxEigenValIm0011040[4] = np.max(EigenValIm0010201040)

MaxEigenValIm0011050[0] = np.max(EigenValIm0010011050)
MaxEigenValIm0011050[1] = np.max(EigenValIm0010021050)
MaxEigenValIm0011050[2] = np.max(EigenValIm0010051050)
MaxEigenValIm0011050[3] = np.max(EigenValIm0010101050)
#MaxEigenValIm0011050[4] = np.max(EigenValIm0010201050)

MaxEigenValIm0011Inf[0] = np.polyfit(fiveSizes, [MaxEigenValIm0011010[0],MaxEigenValIm0011020[0],MaxEigenValIm0011030[0],MaxEigenValIm0011040[0],MaxEigenValIm0011050[0]], 1)[[1]]
MaxEigenValIm0011Inf[1] = np.polyfit(fiveSizes, [MaxEigenValIm0011010[1],MaxEigenValIm0011020[1],MaxEigenValIm0011030[1],MaxEigenValIm0011040[1],MaxEigenValIm0011050[1]], 1)[[1]]
MaxEigenValIm0011Inf[2] = np.polyfit(fiveSizes, [MaxEigenValIm0011010[2],MaxEigenValIm0011020[2],MaxEigenValIm0011030[2],MaxEigenValIm0011040[2],MaxEigenValIm0011050[2]], 1)[[1]]
MaxEigenValIm0011Inf[3] = np.polyfit(fiveSizes, [MaxEigenValIm0011010[3],MaxEigenValIm0011020[3],MaxEigenValIm0011030[3],MaxEigenValIm0011040[3],MaxEigenValIm0011050[3]], 1)[[1]]



axs[0,1].semilogy(MomentumAx0010011010[100],EigenValIm0010011010[100], marker='^',c=[1.0, 0.0, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[0,1].plot(MomentumAx0010011020[200],EigenValIm0010011020[200], marker='s',c=[1.0, 0.0, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[0,1].plot(MomentumAx0010011030[300],EigenValIm0010011030[300], marker='p',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[0,1].plot(MomentumAx0010011040[400],EigenValIm0010011040[400], marker='h',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[0,1].plot(MomentumAx0010011050[500],EigenValIm0010011050[500], marker='8',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[0,1].plot(                             [0],[MaxEigenValIm0011Inf[0]], marker='o',c=[1.0, 0.0, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 1$', markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])

axs[0,1].plot(MomentumAx0010011010[100],EigenValIm0010021010[100], marker='^',c=[1.0, 0.5, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[0,1].plot(MomentumAx0010011020[200],EigenValIm0010021020[200], marker='s',c=[1.0, 0.5, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[0,1].plot(MomentumAx0010011030[300],EigenValIm0010021030[300], marker='p',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[0,1].plot(MomentumAx0010011040[400],EigenValIm0010021040[400], marker='h',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[0,1].plot(MomentumAx0010011050[500],EigenValIm0010021050[500], marker='8',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[0,1].plot(                             [0],[MaxEigenValIm0011Inf[1]], marker='o',c=[1.0, 0.5, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 2$', markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])

axs[0,1].plot(MomentumAx0010011010[100],EigenValIm0010051010[100], marker='^',c=[0.0, 1.0, 0.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[0,1].plot(MomentumAx0010011020[200],EigenValIm0010051020[200], marker='s',c=[0.0, 1.0, 0.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[0,1].plot(MomentumAx0010011030[300],EigenValIm0010051030[300], marker='p',c=[0.0, 1.0, 0.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[0,1].plot(MomentumAx0010011040[400],EigenValIm0010051040[400], marker='h',c=[0.0, 1.0, 0.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[0,1].plot(MomentumAx0010011050[500],EigenValIm0010051050[500], marker='8',c=[0.0, 1.0, 0.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[0,1].plot(                             [0],[MaxEigenValIm0011Inf[2]], marker='o',c=[0.0, 1.0, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 5$', markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])

axs[0,1].plot(MomentumAx0010101010[100],EigenValIm0010101010[100], marker='^',c=[0.0, 0.0, 1.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[0,1].plot(MomentumAx0010101020[200],EigenValIm0010101020[200], marker='s',c=[0.0, 0.0, 1.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[0,1].plot(MomentumAx0010101030[300],EigenValIm0010101030[300], marker='p',c=[0.0, 0.0, 1.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[0,1].plot(MomentumAx0010101040[400],EigenValIm0010101040[400], marker='h',c=[0.0, 0.0, 1.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[0,1].plot(MomentumAx0010101050[500],EigenValIm0010101050[500], marker='8',c=[0.0, 0.0, 1.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[0,1].plot(                             [0],[MaxEigenValIm0011Inf[3]], marker='o',c=[0.0, 0.0, 1.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 10$',markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])

axs[0,1].grid(True)
#axs[0,1].set_xlim(-0.0e+1,+2.0e+1)
#axs[0,1].set_xticks(np.arange(-0.0e+1,+2.01e+1, step=4.e-0))
#axs[0,1].set_ylim(1e-0,+1e+3)
#axs[0,1].set_yticks(np.arange(-0.e-2,+3.1e-0, step=0.5e-0))

#axs[0,1].legend(bbox_to_anchor=(0.3, +1.3), loc=2, borderaxespad=0., ncol=4, labelspacing=1,handleheight=1, columnspacing=0.1, handletextpad=0.1)
#plt.suptitle('$\\ell=0XXX, g_{\\mathcal{K}}=0.1$', fontsize=20, fontname='Times New Roman')
axs[0,1].set_xlabel('$k/\\mathcal{K}\\times 10^{+5}$', fontsize=12, fontname='Times New Roman')
axs[0,1].set_ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}\\times 10^{+5}$', fontsize=12, fontname='Times New Roman')

###############################################
###############################################
###############################################

data0010011010 = np.genfromtxt('./gK000-40/aK001/N010/HamVals.txt')

MomentumAx0010011010 = data0010011010[:,][:,5*0+0]
KineticEne0010011010 = data0010011010[:,][:,5*0+1]
SelfEnergy0010011010 = data0010011010[:,][:,5*0+2]
EigenValRe0010011010 = data0010011010[:,][:,5*0+3]
EigenValIm0010011010 = data0010011010[:,][:,5*0+4]

data0010011020 = np.genfromtxt('./gK000-40/aK001/N020/HamVals.txt')

MomentumAx0010011020 = data0010011020[:,][:,5*0+0]
KineticEne0010011020 = data0010011020[:,][:,5*0+1]
SelfEnergy0010011020 = data0010011020[:,][:,5*0+2]
EigenValRe0010011020 = data0010011020[:,][:,5*0+3]
EigenValIm0010011020 = data0010011020[:,][:,5*0+4]

data0010011030 = np.genfromtxt('./gK000-40/aK001/N030/HamVals.txt')

MomentumAx0010011030 = data0010011030[:,][:,5*0+0]
KineticEne0010011030 = data0010011030[:,][:,5*0+1]
SelfEnergy0010011030 = data0010011030[:,][:,5*0+2]
EigenValRe0010011030 = data0010011030[:,][:,5*0+3]
EigenValIm0010011030 = data0010011030[:,][:,5*0+4]

data0010011040 = np.genfromtxt('./gK000-40/aK001/N040/HamVals.txt')

MomentumAx0010011040 = data0010011040[:,][:,5*0+0]
KineticEne0010011040 = data0010011040[:,][:,5*0+1]
SelfEnergy0010011040 = data0010011040[:,][:,5*0+2]
EigenValRe0010011040 = data0010011040[:,][:,5*0+3]
EigenValIm0010011040 = data0010011040[:,][:,5*0+4]

data0010011050 = np.genfromtxt('./gK000-40/aK001/N050/HamVals.txt')

MomentumAx0010011050 = data0010011050[:,][:,5*0+0]
KineticEne0010011050 = data0010011050[:,][:,5*0+1]
SelfEnergy0010011050 = data0010011050[:,][:,5*0+2]
EigenValRe0010011050 = data0010011050[:,][:,5*0+3]
EigenValIm0010011050 = data0010011050[:,][:,5*0+4]

data0010021010 = np.genfromtxt('./gK000-40/aK002/N010/HamVals.txt')

MomentumAx0010021010 = data0010021010[:,][:,5*0+0]
KineticEne0010021010 = data0010021010[:,][:,5*0+1]
SelfEnergy0010021010 = data0010021010[:,][:,5*0+2]
EigenValRe0010021010 = data0010021010[:,][:,5*0+3]
EigenValIm0010021010 = data0010021010[:,][:,5*0+4]

data0010021020 = np.genfromtxt('./gK000-40/aK002/N020/HamVals.txt')

MomentumAx0010021020 = data0010021020[:,][:,5*0+0]
KineticEne0010021020 = data0010021020[:,][:,5*0+1]
SelfEnergy0010021020 = data0010021020[:,][:,5*0+2]
EigenValRe0010021020 = data0010021020[:,][:,5*0+3]
EigenValIm0010021020 = data0010021020[:,][:,5*0+4]

data0010021030 = np.genfromtxt('./gK000-40/aK002/N030/HamVals.txt')

MomentumAx0010021030 = data0010021030[:,][:,5*0+0]
KineticEne0010021030 = data0010021030[:,][:,5*0+1]
SelfEnergy0010021030 = data0010021030[:,][:,5*0+2]
EigenValRe0010021030 = data0010021030[:,][:,5*0+3]
EigenValIm0010021030 = data0010021030[:,][:,5*0+4]

data0010021040 = np.genfromtxt('./gK000-40/aK002/N040/HamVals.txt')

MomentumAx0010021040 = data0010021040[:,][:,5*0+0]
KineticEne0010021040 = data0010021040[:,][:,5*0+1]
SelfEnergy0010021040 = data0010021040[:,][:,5*0+2]
EigenValRe0010021040 = data0010021040[:,][:,5*0+3]
EigenValIm0010021040 = data0010021040[:,][:,5*0+4]

data0010021050 = np.genfromtxt('./gK000-40/aK002/N050/HamVals.txt')

MomentumAx0010021050 = data0010021050[:,][:,5*0+0]
KineticEne0010021050 = data0010021050[:,][:,5*0+1]
SelfEnergy0010021050 = data0010021050[:,][:,5*0+2]
EigenValRe0010021050 = data0010021050[:,][:,5*0+3]
EigenValIm0010021050 = data0010021050[:,][:,5*0+4]

data0010051010 = np.genfromtxt('./gK000-40/aK005/N010/HamVals.txt')

MomentumAx0010051010 = data0010051010[:,][:,5*0+0]
KineticEne0010051010 = data0010051010[:,][:,5*0+1]
SelfEnergy0010051010 = data0010051010[:,][:,5*0+2]
EigenValRe0010051010 = data0010051010[:,][:,5*0+3]
EigenValIm0010051010 = data0010051010[:,][:,5*0+4]

data0010051020 = np.genfromtxt('./gK000-40/aK005/N020/HamVals.txt')

MomentumAx0010051020 = data0010051020[:,][:,5*0+0]
KineticEne0010051020 = data0010051020[:,][:,5*0+1]
SelfEnergy0010051020 = data0010051020[:,][:,5*0+2]
EigenValRe0010051020 = data0010051020[:,][:,5*0+3]
EigenValIm0010051020 = data0010051020[:,][:,5*0+4]

data0010051030 = np.genfromtxt('./gK000-40/aK005/N030/HamVals.txt')

MomentumAx0010051030 = data0010051030[:,][:,5*0+0]
KineticEne0010051030 = data0010051030[:,][:,5*0+1]
SelfEnergy0010051030 = data0010051030[:,][:,5*0+2]
EigenValRe0010051030 = data0010051030[:,][:,5*0+3]
EigenValIm0010051030 = data0010051030[:,][:,5*0+4]

data0010051040 = np.genfromtxt('./gK000-40/aK005/N040/HamVals.txt')

MomentumAx0010051040 = data0010051040[:,][:,5*0+0]
KineticEne0010051040 = data0010051040[:,][:,5*0+1]
SelfEnergy0010051040 = data0010051040[:,][:,5*0+2]
EigenValRe0010051040 = data0010051040[:,][:,5*0+3]
EigenValIm0010051040 = data0010051040[:,][:,5*0+4]

data0010051050 = np.genfromtxt('./gK000-40/aK005/N050/HamVals.txt')

MomentumAx0010051050 = data0010051050[:,][:,5*0+0]
KineticEne0010051050 = data0010051050[:,][:,5*0+1]
SelfEnergy0010051050 = data0010051050[:,][:,5*0+2]
EigenValRe0010051050 = data0010051050[:,][:,5*0+3]
EigenValIm0010051050 = data0010051050[:,][:,5*0+4]

data0010101010 = np.genfromtxt('./gK000-40/aK010/N010/HamVals.txt')

MomentumAx0010101010 = data0010101010[:,][:,5*0+0]
KineticEne0010101010 = data0010101010[:,][:,5*0+1]
SelfEnergy0010101010 = data0010101010[:,][:,5*0+2]
EigenValRe0010101010 = data0010101010[:,][:,5*0+3]
EigenValIm0010101010 = data0010101010[:,][:,5*0+4]

data0010101020 = np.genfromtxt('./gK000-40/aK010/N020/HamVals.txt')

MomentumAx0010101020 = data0010101020[:,][:,5*0+0]
KineticEne0010101020 = data0010101020[:,][:,5*0+1]
SelfEnergy0010101020 = data0010101020[:,][:,5*0+2]
EigenValRe0010101020 = data0010101020[:,][:,5*0+3]
EigenValIm0010101020 = data0010101020[:,][:,5*0+4]

data0010101030 = np.genfromtxt('./gK000-40/aK010/N030/HamVals.txt')

MomentumAx0010101030 = data0010101030[:,][:,5*0+0]
KineticEne0010101030 = data0010101030[:,][:,5*0+1]
SelfEnergy0010101030 = data0010101030[:,][:,5*0+2]
EigenValRe0010101030 = data0010101030[:,][:,5*0+3]
EigenValIm0010101030 = data0010101030[:,][:,5*0+4]

data0010101040 = np.genfromtxt('./gK000-40/aK010/N040/HamVals.txt')

MomentumAx0010101040 = data0010101040[:,][:,5*0+0]
KineticEne0010101040 = data0010101040[:,][:,5*0+1]
SelfEnergy0010101040 = data0010101040[:,][:,5*0+2]
EigenValRe0010101040 = data0010101040[:,][:,5*0+3]
EigenValIm0010101040 = data0010101040[:,][:,5*0+4]

data0010101050 = np.genfromtxt('./gK000-40/aK010/N050/HamVals.txt')

MomentumAx0010101050 = data0010101050[:,][:,5*0+0]
KineticEne0010101050 = data0010101050[:,][:,5*0+1]
SelfEnergy0010101050 = data0010101050[:,][:,5*0+2]
EigenValRe0010101050 = data0010101050[:,][:,5*0+3]
EigenValIm0010101050 = data0010101050[:,][:,5*0+4]
"""
data0010201010 = np.genfromtxt('./gK000-40/aK020/N010/HamVals.txt')

MomentumAx0010201010 = data0010201010[:,][:,5*0+0]
KineticEne0010201010 = data0010201010[:,][:,5*0+1]
SelfEnergy0010201010 = data0010201010[:,][:,5*0+2]
EigenValRe0010201010 = data0010201010[:,][:,5*0+3]
EigenValIm0010201010 = data0010201010[:,][:,5*0+4]

data0010201020 = np.genfromtxt('./gK000-40/aK020/N020/HamVals.txt')

MomentumAx0010201020 = data0010201020[:,][:,5*0+0]
KineticEne0010201020 = data0010201020[:,][:,5*0+1]
SelfEnergy0010201020 = data0010201020[:,][:,5*0+2]
EigenValRe0010201020 = data0010201020[:,][:,5*0+3]
EigenValIm0010201020 = data0010201020[:,][:,5*0+4]

data0010201030 = np.genfromtxt('./gK000-40/aK020/N030/HamVals.txt')

MomentumAx0010201030 = data0010201030[:,][:,5*0+0]
KineticEne0010201030 = data0010201030[:,][:,5*0+1]
SelfEnergy0010201030 = data0010201030[:,][:,5*0+2]
EigenValRe0010201030 = data0010201030[:,][:,5*0+3]
EigenValIm0010201030 = data0010201030[:,][:,5*0+4]

data0010201040 = np.genfromtxt('./gK000-40/aK020/N040/HamVals.txt')

MomentumAx0010201040 = data0010201040[:,][:,5*0+0]
KineticEne0010201040 = data0010201040[:,][:,5*0+1]
SelfEnergy0010201040 = data0010201040[:,][:,5*0+2]
EigenValRe0010201040 = data0010201040[:,][:,5*0+3]
EigenValIm0010201040 = data0010201040[:,][:,5*0+4]

data0010201050 = np.genfromtxt('./gK000-40/aK020/N050/HamVals.txt')

MomentumAx0010201050 = data0010201050[:,][:,5*0+0]
KineticEne0010201050 = data0010201050[:,][:,5*0+1]
SelfEnergy0010201050 = data0010201050[:,][:,5*0+2]
EigenValRe0010201050 = data0010201050[:,][:,5*0+3]
EigenValIm0010201050 = data0010201050[:,][:,5*0+4]
"""

MaxEigenValIm0011010 = np.zeros((4))
MaxEigenValIm0011020 = np.zeros((4))
MaxEigenValIm0011030 = np.zeros((4))
MaxEigenValIm0011040 = np.zeros((4))
MaxEigenValIm0011050 = np.zeros((4))
MaxEigenValIm0011Inf = np.zeros((4))

MaxEigenValIm0011010[0] = np.max(EigenValIm0010011010)
MaxEigenValIm0011010[1] = np.max(EigenValIm0010021010)
MaxEigenValIm0011010[2] = np.max(EigenValIm0010051010)
MaxEigenValIm0011010[3] = np.max(EigenValIm0010101010)
#MaxEigenValIm0011010[4] = np.max(EigenValIm0010201010)

MaxEigenValIm0011020[0] = np.max(EigenValIm0010011020)
MaxEigenValIm0011020[1] = np.max(EigenValIm0010021020)
MaxEigenValIm0011020[2] = np.max(EigenValIm0010051020)
MaxEigenValIm0011020[3] = np.max(EigenValIm0010101020)
#MaxEigenValIm0011020[4] = np.max(EigenValIm0010201020)

MaxEigenValIm0011030[0] = np.max(EigenValIm0010011030)
MaxEigenValIm0011030[1] = np.max(EigenValIm0010021030)
MaxEigenValIm0011030[2] = np.max(EigenValIm0010051030)
MaxEigenValIm0011030[3] = np.max(EigenValIm0010101030)
#MaxEigenValIm0011030[4] = np.max(EigenValIm0010201030)

MaxEigenValIm0011040[0] = np.max(EigenValIm0010011040)
MaxEigenValIm0011040[1] = np.max(EigenValIm0010021040)
MaxEigenValIm0011040[2] = np.max(EigenValIm0010051040)
MaxEigenValIm0011040[3] = np.max(EigenValIm0010101040)
#MaxEigenValIm0011040[4] = np.max(EigenValIm0010201040)

MaxEigenValIm0011050[0] = np.max(EigenValIm0010011050)
MaxEigenValIm0011050[1] = np.max(EigenValIm0010021050)
MaxEigenValIm0011050[2] = np.max(EigenValIm0010051050)
MaxEigenValIm0011050[3] = np.max(EigenValIm0010101050)
#MaxEigenValIm0011050[4] = np.max(EigenValIm0010201050)

MaxEigenValIm0011Inf[0] = np.polyfit(fiveSizes, [MaxEigenValIm0011010[0],MaxEigenValIm0011020[0],MaxEigenValIm0011030[0],MaxEigenValIm0011040[0],MaxEigenValIm0011050[0]], 1)[[1]]
MaxEigenValIm0011Inf[1] = np.polyfit(fiveSizes, [MaxEigenValIm0011010[1],MaxEigenValIm0011020[1],MaxEigenValIm0011030[1],MaxEigenValIm0011040[1],MaxEigenValIm0011050[1]], 1)[[1]]
MaxEigenValIm0011Inf[2] = np.polyfit(fiveSizes, [MaxEigenValIm0011010[2],MaxEigenValIm0011020[2],MaxEigenValIm0011030[2],MaxEigenValIm0011040[2],MaxEigenValIm0011050[2]], 1)[[1]]
MaxEigenValIm0011Inf[3] = np.polyfit(fiveSizes, [MaxEigenValIm0011010[3],MaxEigenValIm0011020[3],MaxEigenValIm0011030[3],MaxEigenValIm0011040[3],MaxEigenValIm0011050[3]], 1)[[1]]



axs[1,0].semilogy(MomentumAx0010011010[100],EigenValIm0010011010[100], marker='^',c=[1.0, 0.0, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[1,0].plot(MomentumAx0010011020[200],EigenValIm0010011020[200], marker='s',c=[1.0, 0.0, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[1,0].plot(MomentumAx0010011030[300],EigenValIm0010011030[300], marker='p',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[1,0].plot(MomentumAx0010011040[400],EigenValIm0010011040[400], marker='h',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[1,0].plot(MomentumAx0010011050[500],EigenValIm0010011050[500], marker='8',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[1,0].plot(                             [0],[MaxEigenValIm0011Inf[0]], marker='o',c=[1.0, 0.0, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 1$', markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])

axs[1,0].plot(MomentumAx0010011010[100],EigenValIm0010021010[100], marker='^',c=[1.0, 0.5, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[1,0].plot(MomentumAx0010011020[200],EigenValIm0010021020[200], marker='s',c=[1.0, 0.5, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[1,0].plot(MomentumAx0010011030[300],EigenValIm0010021030[300], marker='p',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[1,0].plot(MomentumAx0010011040[400],EigenValIm0010021040[400], marker='h',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[1,0].plot(MomentumAx0010011050[500],EigenValIm0010021050[500], marker='8',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[1,0].plot(                             [0],[MaxEigenValIm0011Inf[1]], marker='o',c=[1.0, 0.5, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 2$', markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])

axs[1,0].plot(MomentumAx0010011010[100],EigenValIm0010051010[100], marker='^',c=[0.0, 1.0, 0.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[1,0].plot(MomentumAx0010011020[200],EigenValIm0010051020[200], marker='s',c=[0.0, 1.0, 0.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[1,0].plot(MomentumAx0010011030[300],EigenValIm0010051030[300], marker='p',c=[0.0, 1.0, 0.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[1,0].plot(MomentumAx0010011040[400],EigenValIm0010051040[400], marker='h',c=[0.0, 1.0, 0.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[1,0].plot(MomentumAx0010011050[500],EigenValIm0010051050[500], marker='8',c=[0.0, 1.0, 0.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[1,0].plot(                             [0],[MaxEigenValIm0011Inf[2]], marker='o',c=[0.0, 1.0, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 5$', markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])

axs[1,0].plot(MomentumAx0010101010[100],EigenValIm0010101010[100], marker='^',c=[0.0, 0.0, 1.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[1,0].plot(MomentumAx0010101020[200],EigenValIm0010101020[200], marker='s',c=[0.0, 0.0, 1.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[1,0].plot(MomentumAx0010101030[300],EigenValIm0010101030[300], marker='p',c=[0.0, 0.0, 1.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[1,0].plot(MomentumAx0010101040[400],EigenValIm0010101040[400], marker='h',c=[0.0, 0.0, 1.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[1,0].plot(MomentumAx0010101050[500],EigenValIm0010101050[500], marker='8',c=[0.0, 0.0, 1.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[1,0].plot(                             [0],[MaxEigenValIm0011Inf[3]], marker='o',c=[0.0, 0.0, 1.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 10$',markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])

axs[1,0].grid(True)
#axs[1,0].set_xlim(-0.0e+1,+2.0e+1)
#axs[1,0].set_xticks(np.arange(-0.0e+1,+2.01e+1, step=4.e-0))
#axs[1,0].set_ylim(1e-0,+1e+3)
#axs[1,0].set_yticks(np.arange(-0.e-2,+3.1e-0, step=0.5e-0))

#axs[1,0].legend(bbox_to_anchor=(0.3, +1.3), loc=2, borderaxespad=0., ncol=4, labelspacing=1,handleheight=1, columnspacing=0.1, handletextpad=0.1)
#plt.suptitle('$\\ell=0XXX, g_{\\mathcal{K}}=0.1$', fontsize=20, fontname='Times New Roman')
axs[1,0].set_xlabel('$k/\\mathcal{K}\\times 10^{+5}$', fontsize=12, fontname='Times New Roman')
axs[1,0].set_ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}\\times 10^{+5}$', fontsize=12, fontname='Times New Roman')

###############################################
###############################################
###############################################

data0010011010 = np.genfromtxt('./gK000-50/aK001/N010/HamVals.txt')

MomentumAx0010011010 = data0010011010[:,][:,5*0+0]
KineticEne0010011010 = data0010011010[:,][:,5*0+1]
SelfEnergy0010011010 = data0010011010[:,][:,5*0+2]
EigenValRe0010011010 = data0010011010[:,][:,5*0+3]
EigenValIm0010011010 = data0010011010[:,][:,5*0+4]

data0010011020 = np.genfromtxt('./gK000-50/aK001/N020/HamVals.txt')

MomentumAx0010011020 = data0010011020[:,][:,5*0+0]
KineticEne0010011020 = data0010011020[:,][:,5*0+1]
SelfEnergy0010011020 = data0010011020[:,][:,5*0+2]
EigenValRe0010011020 = data0010011020[:,][:,5*0+3]
EigenValIm0010011020 = data0010011020[:,][:,5*0+4]

data0010011030 = np.genfromtxt('./gK000-50/aK001/N030/HamVals.txt')

MomentumAx0010011030 = data0010011030[:,][:,5*0+0]
KineticEne0010011030 = data0010011030[:,][:,5*0+1]
SelfEnergy0010011030 = data0010011030[:,][:,5*0+2]
EigenValRe0010011030 = data0010011030[:,][:,5*0+3]
EigenValIm0010011030 = data0010011030[:,][:,5*0+4]

data0010011040 = np.genfromtxt('./gK000-50/aK001/N040/HamVals.txt')

MomentumAx0010011040 = data0010011040[:,][:,5*0+0]
KineticEne0010011040 = data0010011040[:,][:,5*0+1]
SelfEnergy0010011040 = data0010011040[:,][:,5*0+2]
EigenValRe0010011040 = data0010011040[:,][:,5*0+3]
EigenValIm0010011040 = data0010011040[:,][:,5*0+4]

data0010011050 = np.genfromtxt('./gK000-50/aK001/N050/HamVals.txt')

MomentumAx0010011050 = data0010011050[:,][:,5*0+0]
KineticEne0010011050 = data0010011050[:,][:,5*0+1]
SelfEnergy0010011050 = data0010011050[:,][:,5*0+2]
EigenValRe0010011050 = data0010011050[:,][:,5*0+3]
EigenValIm0010011050 = data0010011050[:,][:,5*0+4]

data0010021010 = np.genfromtxt('./gK000-50/aK002/N010/HamVals.txt')

MomentumAx0010021010 = data0010021010[:,][:,5*0+0]
KineticEne0010021010 = data0010021010[:,][:,5*0+1]
SelfEnergy0010021010 = data0010021010[:,][:,5*0+2]
EigenValRe0010021010 = data0010021010[:,][:,5*0+3]
EigenValIm0010021010 = data0010021010[:,][:,5*0+4]

data0010021020 = np.genfromtxt('./gK000-50/aK002/N020/HamVals.txt')

MomentumAx0010021020 = data0010021020[:,][:,5*0+0]
KineticEne0010021020 = data0010021020[:,][:,5*0+1]
SelfEnergy0010021020 = data0010021020[:,][:,5*0+2]
EigenValRe0010021020 = data0010021020[:,][:,5*0+3]
EigenValIm0010021020 = data0010021020[:,][:,5*0+4]

data0010021030 = np.genfromtxt('./gK000-50/aK002/N030/HamVals.txt')

MomentumAx0010021030 = data0010021030[:,][:,5*0+0]
KineticEne0010021030 = data0010021030[:,][:,5*0+1]
SelfEnergy0010021030 = data0010021030[:,][:,5*0+2]
EigenValRe0010021030 = data0010021030[:,][:,5*0+3]
EigenValIm0010021030 = data0010021030[:,][:,5*0+4]

data0010021040 = np.genfromtxt('./gK000-50/aK002/N040/HamVals.txt')

MomentumAx0010021040 = data0010021040[:,][:,5*0+0]
KineticEne0010021040 = data0010021040[:,][:,5*0+1]
SelfEnergy0010021040 = data0010021040[:,][:,5*0+2]
EigenValRe0010021040 = data0010021040[:,][:,5*0+3]
EigenValIm0010021040 = data0010021040[:,][:,5*0+4]

data0010021050 = np.genfromtxt('./gK000-50/aK002/N050/HamVals.txt')

MomentumAx0010021050 = data0010021050[:,][:,5*0+0]
KineticEne0010021050 = data0010021050[:,][:,5*0+1]
SelfEnergy0010021050 = data0010021050[:,][:,5*0+2]
EigenValRe0010021050 = data0010021050[:,][:,5*0+3]
EigenValIm0010021050 = data0010021050[:,][:,5*0+4]

data0010051010 = np.genfromtxt('./gK000-50/aK005/N010/HamVals.txt')

MomentumAx0010051010 = data0010051010[:,][:,5*0+0]
KineticEne0010051010 = data0010051010[:,][:,5*0+1]
SelfEnergy0010051010 = data0010051010[:,][:,5*0+2]
EigenValRe0010051010 = data0010051010[:,][:,5*0+3]
EigenValIm0010051010 = data0010051010[:,][:,5*0+4]

data0010051020 = np.genfromtxt('./gK000-50/aK005/N020/HamVals.txt')

MomentumAx0010051020 = data0010051020[:,][:,5*0+0]
KineticEne0010051020 = data0010051020[:,][:,5*0+1]
SelfEnergy0010051020 = data0010051020[:,][:,5*0+2]
EigenValRe0010051020 = data0010051020[:,][:,5*0+3]
EigenValIm0010051020 = data0010051020[:,][:,5*0+4]

data0010051030 = np.genfromtxt('./gK000-50/aK005/N030/HamVals.txt')

MomentumAx0010051030 = data0010051030[:,][:,5*0+0]
KineticEne0010051030 = data0010051030[:,][:,5*0+1]
SelfEnergy0010051030 = data0010051030[:,][:,5*0+2]
EigenValRe0010051030 = data0010051030[:,][:,5*0+3]
EigenValIm0010051030 = data0010051030[:,][:,5*0+4]

data0010051040 = np.genfromtxt('./gK000-50/aK005/N040/HamVals.txt')

MomentumAx0010051040 = data0010051040[:,][:,5*0+0]
KineticEne0010051040 = data0010051040[:,][:,5*0+1]
SelfEnergy0010051040 = data0010051040[:,][:,5*0+2]
EigenValRe0010051040 = data0010051040[:,][:,5*0+3]
EigenValIm0010051040 = data0010051040[:,][:,5*0+4]

data0010051050 = np.genfromtxt('./gK000-50/aK005/N050/HamVals.txt')

MomentumAx0010051050 = data0010051050[:,][:,5*0+0]
KineticEne0010051050 = data0010051050[:,][:,5*0+1]
SelfEnergy0010051050 = data0010051050[:,][:,5*0+2]
EigenValRe0010051050 = data0010051050[:,][:,5*0+3]
EigenValIm0010051050 = data0010051050[:,][:,5*0+4]

data0010101010 = np.genfromtxt('./gK000-50/aK010/N010/HamVals.txt')

MomentumAx0010101010 = data0010101010[:,][:,5*0+0]
KineticEne0010101010 = data0010101010[:,][:,5*0+1]
SelfEnergy0010101010 = data0010101010[:,][:,5*0+2]
EigenValRe0010101010 = data0010101010[:,][:,5*0+3]
EigenValIm0010101010 = data0010101010[:,][:,5*0+4]

data0010101020 = np.genfromtxt('./gK000-50/aK010/N020/HamVals.txt')

MomentumAx0010101020 = data0010101020[:,][:,5*0+0]
KineticEne0010101020 = data0010101020[:,][:,5*0+1]
SelfEnergy0010101020 = data0010101020[:,][:,5*0+2]
EigenValRe0010101020 = data0010101020[:,][:,5*0+3]
EigenValIm0010101020 = data0010101020[:,][:,5*0+4]

data0010101030 = np.genfromtxt('./gK000-50/aK010/N030/HamVals.txt')

MomentumAx0010101030 = data0010101030[:,][:,5*0+0]
KineticEne0010101030 = data0010101030[:,][:,5*0+1]
SelfEnergy0010101030 = data0010101030[:,][:,5*0+2]
EigenValRe0010101030 = data0010101030[:,][:,5*0+3]
EigenValIm0010101030 = data0010101030[:,][:,5*0+4]

data0010101040 = np.genfromtxt('./gK000-50/aK010/N040/HamVals.txt')

MomentumAx0010101040 = data0010101040[:,][:,5*0+0]
KineticEne0010101040 = data0010101040[:,][:,5*0+1]
SelfEnergy0010101040 = data0010101040[:,][:,5*0+2]
EigenValRe0010101040 = data0010101040[:,][:,5*0+3]
EigenValIm0010101040 = data0010101040[:,][:,5*0+4]

data0010101050 = np.genfromtxt('./gK000-50/aK010/N050/HamVals.txt')

MomentumAx0010101050 = data0010101050[:,][:,5*0+0]
KineticEne0010101050 = data0010101050[:,][:,5*0+1]
SelfEnergy0010101050 = data0010101050[:,][:,5*0+2]
EigenValRe0010101050 = data0010101050[:,][:,5*0+3]
EigenValIm0010101050 = data0010101050[:,][:,5*0+4]
"""
data0010201010 = np.genfromtxt('./gK000-50/aK020/N010/HamVals.txt')

MomentumAx0010201010 = data0010201010[:,][:,5*0+0]
KineticEne0010201010 = data0010201010[:,][:,5*0+1]
SelfEnergy0010201010 = data0010201010[:,][:,5*0+2]
EigenValRe0010201010 = data0010201010[:,][:,5*0+3]
EigenValIm0010201010 = data0010201010[:,][:,5*0+4]

data0010201020 = np.genfromtxt('./gK000-50/aK020/N020/HamVals.txt')

MomentumAx0010201020 = data0010201020[:,][:,5*0+0]
KineticEne0010201020 = data0010201020[:,][:,5*0+1]
SelfEnergy0010201020 = data0010201020[:,][:,5*0+2]
EigenValRe0010201020 = data0010201020[:,][:,5*0+3]
EigenValIm0010201020 = data0010201020[:,][:,5*0+4]

data0010201030 = np.genfromtxt('./gK000-50/aK020/N030/HamVals.txt')

MomentumAx0010201030 = data0010201030[:,][:,5*0+0]
KineticEne0010201030 = data0010201030[:,][:,5*0+1]
SelfEnergy0010201030 = data0010201030[:,][:,5*0+2]
EigenValRe0010201030 = data0010201030[:,][:,5*0+3]
EigenValIm0010201030 = data0010201030[:,][:,5*0+4]

data0010201040 = np.genfromtxt('./gK000-50/aK020/N040/HamVals.txt')

MomentumAx0010201040 = data0010201040[:,][:,5*0+0]
KineticEne0010201040 = data0010201040[:,][:,5*0+1]
SelfEnergy0010201040 = data0010201040[:,][:,5*0+2]
EigenValRe0010201040 = data0010201040[:,][:,5*0+3]
EigenValIm0010201040 = data0010201040[:,][:,5*0+4]

data0010201050 = np.genfromtxt('./gK000-50/aK020/N050/HamVals.txt')

MomentumAx0010201050 = data0010201050[:,][:,5*0+0]
KineticEne0010201050 = data0010201050[:,][:,5*0+1]
SelfEnergy0010201050 = data0010201050[:,][:,5*0+2]
EigenValRe0010201050 = data0010201050[:,][:,5*0+3]
EigenValIm0010201050 = data0010201050[:,][:,5*0+4]
"""

MaxEigenValIm0011010 = np.zeros((4))
MaxEigenValIm0011020 = np.zeros((4))
MaxEigenValIm0011030 = np.zeros((4))
MaxEigenValIm0011040 = np.zeros((4))
MaxEigenValIm0011050 = np.zeros((4))
MaxEigenValIm0011Inf = np.zeros((4))

MaxEigenValIm0011010[0] = np.max(EigenValIm0010011010)
MaxEigenValIm0011010[1] = np.max(EigenValIm0010021010)
MaxEigenValIm0011010[2] = np.max(EigenValIm0010051010)
MaxEigenValIm0011010[3] = np.max(EigenValIm0010101010)
#MaxEigenValIm0011010[4] = np.max(EigenValIm0010201010)

MaxEigenValIm0011020[0] = np.max(EigenValIm0010011020)
MaxEigenValIm0011020[1] = np.max(EigenValIm0010021020)
MaxEigenValIm0011020[2] = np.max(EigenValIm0010051020)
MaxEigenValIm0011020[3] = np.max(EigenValIm0010101020)
#MaxEigenValIm0011020[4] = np.max(EigenValIm0010201020)

MaxEigenValIm0011030[0] = np.max(EigenValIm0010011030)
MaxEigenValIm0011030[1] = np.max(EigenValIm0010021030)
MaxEigenValIm0011030[2] = np.max(EigenValIm0010051030)
MaxEigenValIm0011030[3] = np.max(EigenValIm0010101030)
#MaxEigenValIm0011030[4] = np.max(EigenValIm0010201030)

MaxEigenValIm0011040[0] = np.max(EigenValIm0010011040)
MaxEigenValIm0011040[1] = np.max(EigenValIm0010021040)
MaxEigenValIm0011040[2] = np.max(EigenValIm0010051040)
MaxEigenValIm0011040[3] = np.max(EigenValIm0010101040)
#MaxEigenValIm0011040[4] = np.max(EigenValIm0010201040)

MaxEigenValIm0011050[0] = np.max(EigenValIm0010011050)
MaxEigenValIm0011050[1] = np.max(EigenValIm0010021050)
MaxEigenValIm0011050[2] = np.max(EigenValIm0010051050)
MaxEigenValIm0011050[3] = np.max(EigenValIm0010101050)
#MaxEigenValIm0011050[4] = np.max(EigenValIm0010201050)

MaxEigenValIm0011Inf[0] = np.polyfit(fiveSizes, [MaxEigenValIm0011010[0],MaxEigenValIm0011020[0],MaxEigenValIm0011030[0],MaxEigenValIm0011040[0],MaxEigenValIm0011050[0]], 1)[[1]]
MaxEigenValIm0011Inf[1] = np.polyfit(fiveSizes, [MaxEigenValIm0011010[1],MaxEigenValIm0011020[1],MaxEigenValIm0011030[1],MaxEigenValIm0011040[1],MaxEigenValIm0011050[1]], 1)[[1]]
MaxEigenValIm0011Inf[2] = np.polyfit(fiveSizes, [MaxEigenValIm0011010[2],MaxEigenValIm0011020[2],MaxEigenValIm0011030[2],MaxEigenValIm0011040[2],MaxEigenValIm0011050[2]], 1)[[1]]
MaxEigenValIm0011Inf[3] = np.polyfit(fiveSizes, [MaxEigenValIm0011010[3],MaxEigenValIm0011020[3],MaxEigenValIm0011030[3],MaxEigenValIm0011040[3],MaxEigenValIm0011050[3]], 1)[[1]]



axs[1,1].semilogy(MomentumAx0010011010[100],EigenValIm0010011010[100], marker='^',c=[1.0, 0.0, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[1,1].plot(MomentumAx0010011020[200],EigenValIm0010011020[200], marker='s',c=[1.0, 0.0, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[1,1].plot(MomentumAx0010011030[300],EigenValIm0010011030[300], marker='p',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[1,1].plot(MomentumAx0010011040[400],EigenValIm0010011040[400], marker='h',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[1,1].plot(MomentumAx0010011050[500],EigenValIm0010011050[500], marker='8',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[1,1].plot(                             [0],[MaxEigenValIm0011Inf[0]], marker='o',c=[1.0, 0.0, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 1$', markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])

axs[1,1].plot(MomentumAx0010011010[100],EigenValIm0010021010[100], marker='^',c=[1.0, 0.5, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[1,1].plot(MomentumAx0010011020[200],EigenValIm0010021020[200], marker='s',c=[1.0, 0.5, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[1,1].plot(MomentumAx0010011030[300],EigenValIm0010021030[300], marker='p',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[1,1].plot(MomentumAx0010011040[400],EigenValIm0010021040[400], marker='h',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[1,1].plot(MomentumAx0010011050[500],EigenValIm0010021050[500], marker='8',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[1,1].plot(                             [0],[MaxEigenValIm0011Inf[1]], marker='o',c=[1.0, 0.5, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 2$', markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])

axs[1,1].plot(MomentumAx0010011010[100],EigenValIm0010051010[100], marker='^',c=[0.0, 1.0, 0.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[1,1].plot(MomentumAx0010011020[200],EigenValIm0010051020[200], marker='s',c=[0.0, 1.0, 0.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[1,1].plot(MomentumAx0010011030[300],EigenValIm0010051030[300], marker='p',c=[0.0, 1.0, 0.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[1,1].plot(MomentumAx0010011040[400],EigenValIm0010051040[400], marker='h',c=[0.0, 1.0, 0.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[1,1].plot(MomentumAx0010011050[500],EigenValIm0010051050[500], marker='8',c=[0.0, 1.0, 0.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[1,1].plot(                             [0],[MaxEigenValIm0011Inf[2]], marker='o',c=[0.0, 1.0, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 5$', markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])

axs[1,1].plot(MomentumAx0010101010[100],EigenValIm0010101010[100], marker='^',c=[0.0, 0.0, 1.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[1,1].plot(MomentumAx0010101020[200],EigenValIm0010101020[200], marker='s',c=[0.0, 0.0, 1.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[1,1].plot(MomentumAx0010101030[300],EigenValIm0010101030[300], marker='p',c=[0.0, 0.0, 1.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[1,1].plot(MomentumAx0010101040[400],EigenValIm0010101040[400], marker='h',c=[0.0, 0.0, 1.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[1,1].plot(MomentumAx0010101050[500],EigenValIm0010101050[500], marker='8',c=[0.0, 0.0, 1.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[1,1].plot(                             [0],[MaxEigenValIm0011Inf[3]], marker='o',c=[0.0, 0.0, 1.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 10$',markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])

axs[1,1].grid(True)
#axs[1,1].set_xlim(-0.0e+1,+2.0e+1)
#axs[1,1].set_xticks(np.arange(-0.0e+1,+2.01e+1, step=4.e-0))
#axs[1,1].set_ylim(1e-0,+1e+3)
#axs[1,1].set_yticks(np.arange(-0.e-2,+3.1e-0, step=0.5e-0))

#axs[1,1].legend(bbox_to_anchor=(0.3, +1.3), loc=2, borderaxespad=0., ncol=4, labelspacing=1,handleheight=1, columnspacing=0.1, handletextpad=0.1)
#plt.suptitle('$\\ell=0XXX, g_{\\mathcal{K}}=0.1$', fontsize=20, fontname='Times New Roman')
axs[1,1].set_xlabel('$k/\\mathcal{K}\\times 10^{+5}$', fontsize=12, fontname='Times New Roman')
axs[1,1].set_ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}\\times 10^{+5}$', fontsize=12, fontname='Times New Roman')


#plt.show()
fig.savefig('PlotsReportgK000-20.pdf')