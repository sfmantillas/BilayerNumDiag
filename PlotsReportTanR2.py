import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from matplotlib.ticker import (MultipleLocator, NullFormatter,
                                   ScalarFormatter)

fiveSizes = [1./10,1./20,1./30,1./40,1./50]

########################################################################
########################################################################
########################################################################

dataL0g000_250011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK001/N010/HamVals.txt')

MomentumAxL0g000_250011010 = dataL0g000_250011010[:,][:,5*0+0]
KineticEneL0g000_250011010 = dataL0g000_250011010[:,][:,5*0+1]
SelfEnergyL0g000_250011010 = dataL0g000_250011010[:,][:,5*0+2]
EigenValReL0g000_250011010 = dataL0g000_250011010[:,][:,5*0+3]
EigenValImL0g000_250011010 = dataL0g000_250011010[:,][:,5*0+4]

dataL0g000_250011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK001/N020/HamVals.txt')

MomentumAxL0g000_250011020 = dataL0g000_250011020[:,][:,5*0+0]
KineticEneL0g000_250011020 = dataL0g000_250011020[:,][:,5*0+1]
SelfEnergyL0g000_250011020 = dataL0g000_250011020[:,][:,5*0+2]
EigenValReL0g000_250011020 = dataL0g000_250011020[:,][:,5*0+3]
EigenValImL0g000_250011020 = dataL0g000_250011020[:,][:,5*0+4]

dataL0g000_250011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK001/N030/HamVals.txt')

MomentumAxL0g000_250011030 = dataL0g000_250011030[:,][:,5*0+0]
KineticEneL0g000_250011030 = dataL0g000_250011030[:,][:,5*0+1]
SelfEnergyL0g000_250011030 = dataL0g000_250011030[:,][:,5*0+2]
EigenValReL0g000_250011030 = dataL0g000_250011030[:,][:,5*0+3]
EigenValImL0g000_250011030 = dataL0g000_250011030[:,][:,5*0+4]

dataL0g000_250011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK001/N040/HamVals.txt')

MomentumAxL0g000_250011040 = dataL0g000_250011040[:,][:,5*0+0]
KineticEneL0g000_250011040 = dataL0g000_250011040[:,][:,5*0+1]
SelfEnergyL0g000_250011040 = dataL0g000_250011040[:,][:,5*0+2]
EigenValReL0g000_250011040 = dataL0g000_250011040[:,][:,5*0+3]
EigenValImL0g000_250011040 = dataL0g000_250011040[:,][:,5*0+4]

dataL0g000_250011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK001/N050/HamVals.txt')

MomentumAxL0g000_250011050 = dataL0g000_250011050[:,][:,5*0+0]
KineticEneL0g000_250011050 = dataL0g000_250011050[:,][:,5*0+1]
SelfEnergyL0g000_250011050 = dataL0g000_250011050[:,][:,5*0+2]
EigenValReL0g000_250011050 = dataL0g000_250011050[:,][:,5*0+3]
EigenValImL0g000_250011050 = dataL0g000_250011050[:,][:,5*0+4]

dataL0g000_250021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK002/N010/HamVals.txt')

MomentumAxL0g000_250021010 = dataL0g000_250021010[:,][:,5*0+0]
KineticEneL0g000_250021010 = dataL0g000_250021010[:,][:,5*0+1]
SelfEnergyL0g000_250021010 = dataL0g000_250021010[:,][:,5*0+2]
EigenValReL0g000_250021010 = dataL0g000_250021010[:,][:,5*0+3]
EigenValImL0g000_250021010 = dataL0g000_250021010[:,][:,5*0+4]

dataL0g000_250021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK002/N020/HamVals.txt')

MomentumAxL0g000_250021020 = dataL0g000_250021020[:,][:,5*0+0]
KineticEneL0g000_250021020 = dataL0g000_250021020[:,][:,5*0+1]
SelfEnergyL0g000_250021020 = dataL0g000_250021020[:,][:,5*0+2]
EigenValReL0g000_250021020 = dataL0g000_250021020[:,][:,5*0+3]
EigenValImL0g000_250021020 = dataL0g000_250021020[:,][:,5*0+4]

dataL0g000_250021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK002/N030/HamVals.txt')

MomentumAxL0g000_250021030 = dataL0g000_250021030[:,][:,5*0+0]
KineticEneL0g000_250021030 = dataL0g000_250021030[:,][:,5*0+1]
SelfEnergyL0g000_250021030 = dataL0g000_250021030[:,][:,5*0+2]
EigenValReL0g000_250021030 = dataL0g000_250021030[:,][:,5*0+3]
EigenValImL0g000_250021030 = dataL0g000_250021030[:,][:,5*0+4]

dataL0g000_250021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK002/N040/HamVals.txt')

MomentumAxL0g000_250021040 = dataL0g000_250021040[:,][:,5*0+0]
KineticEneL0g000_250021040 = dataL0g000_250021040[:,][:,5*0+1]
SelfEnergyL0g000_250021040 = dataL0g000_250021040[:,][:,5*0+2]
EigenValReL0g000_250021040 = dataL0g000_250021040[:,][:,5*0+3]
EigenValImL0g000_250021040 = dataL0g000_250021040[:,][:,5*0+4]

dataL0g000_250021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK002/N050/HamVals.txt')

MomentumAxL0g000_250021050 = dataL0g000_250021050[:,][:,5*0+0]
KineticEneL0g000_250021050 = dataL0g000_250021050[:,][:,5*0+1]
SelfEnergyL0g000_250021050 = dataL0g000_250021050[:,][:,5*0+2]
EigenValReL0g000_250021050 = dataL0g000_250021050[:,][:,5*0+3]
EigenValImL0g000_250021050 = dataL0g000_250021050[:,][:,5*0+4]

dataL0g000_250031010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK003/N010/HamVals.txt')

MomentumAxL0g000_250031010 = dataL0g000_250031010[:,][:,5*0+0]
KineticEneL0g000_250031010 = dataL0g000_250031010[:,][:,5*0+1]
SelfEnergyL0g000_250031010 = dataL0g000_250031010[:,][:,5*0+2]
EigenValReL0g000_250031010 = dataL0g000_250031010[:,][:,5*0+3]
EigenValImL0g000_250031010 = dataL0g000_250031010[:,][:,5*0+4]

dataL0g000_250031020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK003/N020/HamVals.txt')

MomentumAxL0g000_250031020 = dataL0g000_250031020[:,][:,5*0+0]
KineticEneL0g000_250031020 = dataL0g000_250031020[:,][:,5*0+1]
SelfEnergyL0g000_250031020 = dataL0g000_250031020[:,][:,5*0+2]
EigenValReL0g000_250031020 = dataL0g000_250031020[:,][:,5*0+3]
EigenValImL0g000_250031020 = dataL0g000_250031020[:,][:,5*0+4]

dataL0g000_250031030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK003/N030/HamVals.txt')

MomentumAxL0g000_250031030 = dataL0g000_250031030[:,][:,5*0+0]
KineticEneL0g000_250031030 = dataL0g000_250031030[:,][:,5*0+1]
SelfEnergyL0g000_250031030 = dataL0g000_250031030[:,][:,5*0+2]
EigenValReL0g000_250031030 = dataL0g000_250031030[:,][:,5*0+3]
EigenValImL0g000_250031030 = dataL0g000_250031030[:,][:,5*0+4]

dataL0g000_250031040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK003/N040/HamVals.txt')

MomentumAxL0g000_250031040 = dataL0g000_250031040[:,][:,5*0+0]
KineticEneL0g000_250031040 = dataL0g000_250031040[:,][:,5*0+1]
SelfEnergyL0g000_250031040 = dataL0g000_250031040[:,][:,5*0+2]
EigenValReL0g000_250031040 = dataL0g000_250031040[:,][:,5*0+3]
EigenValImL0g000_250031040 = dataL0g000_250031040[:,][:,5*0+4]

dataL0g000_250031050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK003/N050/HamVals.txt')

MomentumAxL0g000_250031050 = dataL0g000_250031050[:,][:,5*0+0]
KineticEneL0g000_250031050 = dataL0g000_250031050[:,][:,5*0+1]
SelfEnergyL0g000_250031050 = dataL0g000_250031050[:,][:,5*0+2]
EigenValReL0g000_250031050 = dataL0g000_250031050[:,][:,5*0+3]
EigenValImL0g000_250031050 = dataL0g000_250031050[:,][:,5*0+4]

dataL0g000_250051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK005/N010/HamVals.txt')

MomentumAxL0g000_250051010 = dataL0g000_250051010[:,][:,5*0+0]
KineticEneL0g000_250051010 = dataL0g000_250051010[:,][:,5*0+1]
SelfEnergyL0g000_250051010 = dataL0g000_250051010[:,][:,5*0+2]
EigenValReL0g000_250051010 = dataL0g000_250051010[:,][:,5*0+3]
EigenValImL0g000_250051010 = dataL0g000_250051010[:,][:,5*0+4]

dataL0g000_250051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK005/N020/HamVals.txt')

MomentumAxL0g000_250051020 = dataL0g000_250051020[:,][:,5*0+0]
KineticEneL0g000_250051020 = dataL0g000_250051020[:,][:,5*0+1]
SelfEnergyL0g000_250051020 = dataL0g000_250051020[:,][:,5*0+2]
EigenValReL0g000_250051020 = dataL0g000_250051020[:,][:,5*0+3]
EigenValImL0g000_250051020 = dataL0g000_250051020[:,][:,5*0+4]

dataL0g000_250051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK005/N030/HamVals.txt')

MomentumAxL0g000_250051030 = dataL0g000_250051030[:,][:,5*0+0]
KineticEneL0g000_250051030 = dataL0g000_250051030[:,][:,5*0+1]
SelfEnergyL0g000_250051030 = dataL0g000_250051030[:,][:,5*0+2]
EigenValReL0g000_250051030 = dataL0g000_250051030[:,][:,5*0+3]
EigenValImL0g000_250051030 = dataL0g000_250051030[:,][:,5*0+4]

dataL0g000_250051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK005/N040/HamVals.txt')

MomentumAxL0g000_250051040 = dataL0g000_250051040[:,][:,5*0+0]
KineticEneL0g000_250051040 = dataL0g000_250051040[:,][:,5*0+1]
SelfEnergyL0g000_250051040 = dataL0g000_250051040[:,][:,5*0+2]
EigenValReL0g000_250051040 = dataL0g000_250051040[:,][:,5*0+3]
EigenValImL0g000_250051040 = dataL0g000_250051040[:,][:,5*0+4]

dataL0g000_250051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK005/N050/HamVals.txt')

MomentumAxL0g000_250051050 = dataL0g000_250051050[:,][:,5*0+0]
KineticEneL0g000_250051050 = dataL0g000_250051050[:,][:,5*0+1]
SelfEnergyL0g000_250051050 = dataL0g000_250051050[:,][:,5*0+2]
EigenValReL0g000_250051050 = dataL0g000_250051050[:,][:,5*0+3]
EigenValImL0g000_250051050 = dataL0g000_250051050[:,][:,5*0+4]

dataL0g000_250071010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK007/N010/HamVals.txt')

MomentumAxL0g000_250071010 = dataL0g000_250071010[:,][:,5*0+0]
KineticEneL0g000_250071010 = dataL0g000_250071010[:,][:,5*0+1]
SelfEnergyL0g000_250071010 = dataL0g000_250071010[:,][:,5*0+2]
EigenValReL0g000_250071010 = dataL0g000_250071010[:,][:,5*0+3]
EigenValImL0g000_250071010 = dataL0g000_250071010[:,][:,5*0+4]

dataL0g000_250071020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK007/N020/HamVals.txt')

MomentumAxL0g000_250071020 = dataL0g000_250071020[:,][:,5*0+0]
KineticEneL0g000_250071020 = dataL0g000_250071020[:,][:,5*0+1]
SelfEnergyL0g000_250071020 = dataL0g000_250071020[:,][:,5*0+2]
EigenValReL0g000_250071020 = dataL0g000_250071020[:,][:,5*0+3]
EigenValImL0g000_250071020 = dataL0g000_250071020[:,][:,5*0+4]

dataL0g000_250071030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK007/N030/HamVals.txt')

MomentumAxL0g000_250071030 = dataL0g000_250071030[:,][:,5*0+0]
KineticEneL0g000_250071030 = dataL0g000_250071030[:,][:,5*0+1]
SelfEnergyL0g000_250071030 = dataL0g000_250071030[:,][:,5*0+2]
EigenValReL0g000_250071030 = dataL0g000_250071030[:,][:,5*0+3]
EigenValImL0g000_250071030 = dataL0g000_250071030[:,][:,5*0+4]

dataL0g000_250071040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK007/N040/HamVals.txt')

MomentumAxL0g000_250071040 = dataL0g000_250071040[:,][:,5*0+0]
KineticEneL0g000_250071040 = dataL0g000_250071040[:,][:,5*0+1]
SelfEnergyL0g000_250071040 = dataL0g000_250071040[:,][:,5*0+2]
EigenValReL0g000_250071040 = dataL0g000_250071040[:,][:,5*0+3]
EigenValImL0g000_250071040 = dataL0g000_250071040[:,][:,5*0+4]

dataL0g000_250071050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK007/N050/HamVals.txt')

MomentumAxL0g000_250071050 = dataL0g000_250071050[:,][:,5*0+0]
KineticEneL0g000_250071050 = dataL0g000_250071050[:,][:,5*0+1]
SelfEnergyL0g000_250071050 = dataL0g000_250071050[:,][:,5*0+2]
EigenValReL0g000_250071050 = dataL0g000_250071050[:,][:,5*0+3]
EigenValImL0g000_250071050 = dataL0g000_250071050[:,][:,5*0+4]

dataL0g000_250101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK010/N010/HamVals.txt')

MomentumAxL0g000_250101010 = dataL0g000_250101010[:,][:,5*0+0]
KineticEneL0g000_250101010 = dataL0g000_250101010[:,][:,5*0+1]
SelfEnergyL0g000_250101010 = dataL0g000_250101010[:,][:,5*0+2]
EigenValReL0g000_250101010 = dataL0g000_250101010[:,][:,5*0+3]
EigenValImL0g000_250101010 = dataL0g000_250101010[:,][:,5*0+4]

dataL0g000_250101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK010/N020/HamVals.txt')

MomentumAxL0g000_250101020 = dataL0g000_250101020[:,][:,5*0+0]
KineticEneL0g000_250101020 = dataL0g000_250101020[:,][:,5*0+1]
SelfEnergyL0g000_250101020 = dataL0g000_250101020[:,][:,5*0+2]
EigenValReL0g000_250101020 = dataL0g000_250101020[:,][:,5*0+3]
EigenValImL0g000_250101020 = dataL0g000_250101020[:,][:,5*0+4]

dataL0g000_250101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK010/N030/HamVals.txt')

MomentumAxL0g000_250101030 = dataL0g000_250101030[:,][:,5*0+0]
KineticEneL0g000_250101030 = dataL0g000_250101030[:,][:,5*0+1]
SelfEnergyL0g000_250101030 = dataL0g000_250101030[:,][:,5*0+2]
EigenValReL0g000_250101030 = dataL0g000_250101030[:,][:,5*0+3]
EigenValImL0g000_250101030 = dataL0g000_250101030[:,][:,5*0+4]

dataL0g000_250101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK010/N040/HamVals.txt')

MomentumAxL0g000_250101040 = dataL0g000_250101040[:,][:,5*0+0]
KineticEneL0g000_250101040 = dataL0g000_250101040[:,][:,5*0+1]
SelfEnergyL0g000_250101040 = dataL0g000_250101040[:,][:,5*0+2]
EigenValReL0g000_250101040 = dataL0g000_250101040[:,][:,5*0+3]
EigenValImL0g000_250101040 = dataL0g000_250101040[:,][:,5*0+4]

dataL0g000_250101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK010/N050/HamVals.txt')

MomentumAxL0g000_250101050 = dataL0g000_250101050[:,][:,5*0+0]
KineticEneL0g000_250101050 = dataL0g000_250101050[:,][:,5*0+1]
SelfEnergyL0g000_250101050 = dataL0g000_250101050[:,][:,5*0+2]
EigenValReL0g000_250101050 = dataL0g000_250101050[:,][:,5*0+3]
EigenValImL0g000_250101050 = dataL0g000_250101050[:,][:,5*0+4]

MaxEigenValImL0g000_251Inf = np.zeros((6))

MaxEigenValImL0g000_251Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_250011010),np.max(EigenValImL0g000_250011020),np.max(EigenValImL0g000_250011030),np.max(EigenValImL0g000_250011040),np.max(EigenValImL0g000_250011050)], 1)[[1]]
MaxEigenValImL0g000_251Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_250021010),np.max(EigenValImL0g000_250021020),np.max(EigenValImL0g000_250021030),np.max(EigenValImL0g000_250021040),np.max(EigenValImL0g000_250021050)], 1)[[1]]
MaxEigenValImL0g000_251Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_250031010),np.max(EigenValImL0g000_250031020),np.max(EigenValImL0g000_250031030),np.max(EigenValImL0g000_250031040),np.max(EigenValImL0g000_250031050)], 1)[[1]]
MaxEigenValImL0g000_251Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_250051010),np.max(EigenValImL0g000_250051020),np.max(EigenValImL0g000_250051030),np.max(EigenValImL0g000_250051040),np.max(EigenValImL0g000_250051050)], 1)[[1]]
MaxEigenValImL0g000_251Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_250071010),np.max(EigenValImL0g000_250071020),np.max(EigenValImL0g000_250071030),np.max(EigenValImL0g000_250071040),np.max(EigenValImL0g000_250071050)], 1)[[1]]
MaxEigenValImL0g000_251Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_250101010),np.max(EigenValImL0g000_250101020),np.max(EigenValImL0g000_250101030),np.max(EigenValImL0g000_250101040),np.max(EigenValImL0g000_250101050)], 1)[[1]]

########################################################################

dataL0g000_30011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK001/N010/HamVals.txt')

MomentumAxL0g000_30011010 = dataL0g000_30011010[:,][:,5*0+0]
KineticEneL0g000_30011010 = dataL0g000_30011010[:,][:,5*0+1]
SelfEnergyL0g000_30011010 = dataL0g000_30011010[:,][:,5*0+2]
EigenValReL0g000_30011010 = dataL0g000_30011010[:,][:,5*0+3]
EigenValImL0g000_30011010 = dataL0g000_30011010[:,][:,5*0+4]

dataL0g000_30011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK001/N020/HamVals.txt')

MomentumAxL0g000_30011020 = dataL0g000_30011020[:,][:,5*0+0]
KineticEneL0g000_30011020 = dataL0g000_30011020[:,][:,5*0+1]
SelfEnergyL0g000_30011020 = dataL0g000_30011020[:,][:,5*0+2]
EigenValReL0g000_30011020 = dataL0g000_30011020[:,][:,5*0+3]
EigenValImL0g000_30011020 = dataL0g000_30011020[:,][:,5*0+4]

dataL0g000_30011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK001/N030/HamVals.txt')

MomentumAxL0g000_30011030 = dataL0g000_30011030[:,][:,5*0+0]
KineticEneL0g000_30011030 = dataL0g000_30011030[:,][:,5*0+1]
SelfEnergyL0g000_30011030 = dataL0g000_30011030[:,][:,5*0+2]
EigenValReL0g000_30011030 = dataL0g000_30011030[:,][:,5*0+3]
EigenValImL0g000_30011030 = dataL0g000_30011030[:,][:,5*0+4]

dataL0g000_30011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK001/N040/HamVals.txt')

MomentumAxL0g000_30011040 = dataL0g000_30011040[:,][:,5*0+0]
KineticEneL0g000_30011040 = dataL0g000_30011040[:,][:,5*0+1]
SelfEnergyL0g000_30011040 = dataL0g000_30011040[:,][:,5*0+2]
EigenValReL0g000_30011040 = dataL0g000_30011040[:,][:,5*0+3]
EigenValImL0g000_30011040 = dataL0g000_30011040[:,][:,5*0+4]

dataL0g000_30011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK001/N050/HamVals.txt')

MomentumAxL0g000_30011050 = dataL0g000_30011050[:,][:,5*0+0]
KineticEneL0g000_30011050 = dataL0g000_30011050[:,][:,5*0+1]
SelfEnergyL0g000_30011050 = dataL0g000_30011050[:,][:,5*0+2]
EigenValReL0g000_30011050 = dataL0g000_30011050[:,][:,5*0+3]
EigenValImL0g000_30011050 = dataL0g000_30011050[:,][:,5*0+4]

dataL0g000_30021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK002/N010/HamVals.txt')

MomentumAxL0g000_30021010 = dataL0g000_30021010[:,][:,5*0+0]
KineticEneL0g000_30021010 = dataL0g000_30021010[:,][:,5*0+1]
SelfEnergyL0g000_30021010 = dataL0g000_30021010[:,][:,5*0+2]
EigenValReL0g000_30021010 = dataL0g000_30021010[:,][:,5*0+3]
EigenValImL0g000_30021010 = dataL0g000_30021010[:,][:,5*0+4]

dataL0g000_30021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK002/N020/HamVals.txt')

MomentumAxL0g000_30021020 = dataL0g000_30021020[:,][:,5*0+0]
KineticEneL0g000_30021020 = dataL0g000_30021020[:,][:,5*0+1]
SelfEnergyL0g000_30021020 = dataL0g000_30021020[:,][:,5*0+2]
EigenValReL0g000_30021020 = dataL0g000_30021020[:,][:,5*0+3]
EigenValImL0g000_30021020 = dataL0g000_30021020[:,][:,5*0+4]

dataL0g000_30021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK002/N030/HamVals.txt')

MomentumAxL0g000_30021030 = dataL0g000_30021030[:,][:,5*0+0]
KineticEneL0g000_30021030 = dataL0g000_30021030[:,][:,5*0+1]
SelfEnergyL0g000_30021030 = dataL0g000_30021030[:,][:,5*0+2]
EigenValReL0g000_30021030 = dataL0g000_30021030[:,][:,5*0+3]
EigenValImL0g000_30021030 = dataL0g000_30021030[:,][:,5*0+4]

dataL0g000_30021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK002/N040/HamVals.txt')

MomentumAxL0g000_30021040 = dataL0g000_30021040[:,][:,5*0+0]
KineticEneL0g000_30021040 = dataL0g000_30021040[:,][:,5*0+1]
SelfEnergyL0g000_30021040 = dataL0g000_30021040[:,][:,5*0+2]
EigenValReL0g000_30021040 = dataL0g000_30021040[:,][:,5*0+3]
EigenValImL0g000_30021040 = dataL0g000_30021040[:,][:,5*0+4]

dataL0g000_30021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK002/N050/HamVals.txt')

MomentumAxL0g000_30021050 = dataL0g000_30021050[:,][:,5*0+0]
KineticEneL0g000_30021050 = dataL0g000_30021050[:,][:,5*0+1]
SelfEnergyL0g000_30021050 = dataL0g000_30021050[:,][:,5*0+2]
EigenValReL0g000_30021050 = dataL0g000_30021050[:,][:,5*0+3]
EigenValImL0g000_30021050 = dataL0g000_30021050[:,][:,5*0+4]

dataL0g000_30051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK005/N010/HamVals.txt')

MomentumAxL0g000_30051010 = dataL0g000_30051010[:,][:,5*0+0]
KineticEneL0g000_30051010 = dataL0g000_30051010[:,][:,5*0+1]
SelfEnergyL0g000_30051010 = dataL0g000_30051010[:,][:,5*0+2]
EigenValReL0g000_30051010 = dataL0g000_30051010[:,][:,5*0+3]
EigenValImL0g000_30051010 = dataL0g000_30051010[:,][:,5*0+4]

dataL0g000_30051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK005/N020/HamVals.txt')

MomentumAxL0g000_30051020 = dataL0g000_30051020[:,][:,5*0+0]
KineticEneL0g000_30051020 = dataL0g000_30051020[:,][:,5*0+1]
SelfEnergyL0g000_30051020 = dataL0g000_30051020[:,][:,5*0+2]
EigenValReL0g000_30051020 = dataL0g000_30051020[:,][:,5*0+3]
EigenValImL0g000_30051020 = dataL0g000_30051020[:,][:,5*0+4]

dataL0g000_30051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK005/N030/HamVals.txt')

MomentumAxL0g000_30051030 = dataL0g000_30051030[:,][:,5*0+0]
KineticEneL0g000_30051030 = dataL0g000_30051030[:,][:,5*0+1]
SelfEnergyL0g000_30051030 = dataL0g000_30051030[:,][:,5*0+2]
EigenValReL0g000_30051030 = dataL0g000_30051030[:,][:,5*0+3]
EigenValImL0g000_30051030 = dataL0g000_30051030[:,][:,5*0+4]

dataL0g000_30051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK005/N040/HamVals.txt')

MomentumAxL0g000_30051040 = dataL0g000_30051040[:,][:,5*0+0]
KineticEneL0g000_30051040 = dataL0g000_30051040[:,][:,5*0+1]
SelfEnergyL0g000_30051040 = dataL0g000_30051040[:,][:,5*0+2]
EigenValReL0g000_30051040 = dataL0g000_30051040[:,][:,5*0+3]
EigenValImL0g000_30051040 = dataL0g000_30051040[:,][:,5*0+4]

dataL0g000_30051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK005/N050/HamVals.txt')

MomentumAxL0g000_30051050 = dataL0g000_30051050[:,][:,5*0+0]
KineticEneL0g000_30051050 = dataL0g000_30051050[:,][:,5*0+1]
SelfEnergyL0g000_30051050 = dataL0g000_30051050[:,][:,5*0+2]
EigenValReL0g000_30051050 = dataL0g000_30051050[:,][:,5*0+3]
EigenValImL0g000_30051050 = dataL0g000_30051050[:,][:,5*0+4]

dataL0g000_30101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK010/N010/HamVals.txt')

MomentumAxL0g000_30101010 = dataL0g000_30101010[:,][:,5*0+0]
KineticEneL0g000_30101010 = dataL0g000_30101010[:,][:,5*0+1]
SelfEnergyL0g000_30101010 = dataL0g000_30101010[:,][:,5*0+2]
EigenValReL0g000_30101010 = dataL0g000_30101010[:,][:,5*0+3]
EigenValImL0g000_30101010 = dataL0g000_30101010[:,][:,5*0+4]

dataL0g000_30101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK010/N020/HamVals.txt')

MomentumAxL0g000_30101020 = dataL0g000_30101020[:,][:,5*0+0]
KineticEneL0g000_30101020 = dataL0g000_30101020[:,][:,5*0+1]
SelfEnergyL0g000_30101020 = dataL0g000_30101020[:,][:,5*0+2]
EigenValReL0g000_30101020 = dataL0g000_30101020[:,][:,5*0+3]
EigenValImL0g000_30101020 = dataL0g000_30101020[:,][:,5*0+4]

dataL0g000_30101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK010/N030/HamVals.txt')

MomentumAxL0g000_30101030 = dataL0g000_30101030[:,][:,5*0+0]
KineticEneL0g000_30101030 = dataL0g000_30101030[:,][:,5*0+1]
SelfEnergyL0g000_30101030 = dataL0g000_30101030[:,][:,5*0+2]
EigenValReL0g000_30101030 = dataL0g000_30101030[:,][:,5*0+3]
EigenValImL0g000_30101030 = dataL0g000_30101030[:,][:,5*0+4]

dataL0g000_30101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK010/N040/HamVals.txt')

MomentumAxL0g000_30101040 = dataL0g000_30101040[:,][:,5*0+0]
KineticEneL0g000_30101040 = dataL0g000_30101040[:,][:,5*0+1]
SelfEnergyL0g000_30101040 = dataL0g000_30101040[:,][:,5*0+2]
EigenValReL0g000_30101040 = dataL0g000_30101040[:,][:,5*0+3]
EigenValImL0g000_30101040 = dataL0g000_30101040[:,][:,5*0+4]

dataL0g000_30101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK010/N050/HamVals.txt')

MomentumAxL0g000_30101050 = dataL0g000_30101050[:,][:,5*0+0]
KineticEneL0g000_30101050 = dataL0g000_30101050[:,][:,5*0+1]
SelfEnergyL0g000_30101050 = dataL0g000_30101050[:,][:,5*0+2]
EigenValReL0g000_30101050 = dataL0g000_30101050[:,][:,5*0+3]
EigenValImL0g000_30101050 = dataL0g000_30101050[:,][:,5*0+4]

dataL0g000_30031010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK003/N010/HamVals.txt')

MomentumAxL0g000_30031010 = dataL0g000_30031010[:,][:,5*0+0]
KineticEneL0g000_30031010 = dataL0g000_30031010[:,][:,5*0+1]
SelfEnergyL0g000_30031010 = dataL0g000_30031010[:,][:,5*0+2]
EigenValReL0g000_30031010 = dataL0g000_30031010[:,][:,5*0+3]
EigenValImL0g000_30031010 = dataL0g000_30031010[:,][:,5*0+4]

dataL0g000_30031020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK003/N020/HamVals.txt')

MomentumAxL0g000_30031020 = dataL0g000_30031020[:,][:,5*0+0]
KineticEneL0g000_30031020 = dataL0g000_30031020[:,][:,5*0+1]
SelfEnergyL0g000_30031020 = dataL0g000_30031020[:,][:,5*0+2]
EigenValReL0g000_30031020 = dataL0g000_30031020[:,][:,5*0+3]
EigenValImL0g000_30031020 = dataL0g000_30031020[:,][:,5*0+4]

dataL0g000_30031030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK003/N030/HamVals.txt')

MomentumAxL0g000_30031030 = dataL0g000_30031030[:,][:,5*0+0]
KineticEneL0g000_30031030 = dataL0g000_30031030[:,][:,5*0+1]
SelfEnergyL0g000_30031030 = dataL0g000_30031030[:,][:,5*0+2]
EigenValReL0g000_30031030 = dataL0g000_30031030[:,][:,5*0+3]
EigenValImL0g000_30031030 = dataL0g000_30031030[:,][:,5*0+4]

dataL0g000_30031040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK003/N040/HamVals.txt')

MomentumAxL0g000_30031040 = dataL0g000_30031040[:,][:,5*0+0]
KineticEneL0g000_30031040 = dataL0g000_30031040[:,][:,5*0+1]
SelfEnergyL0g000_30031040 = dataL0g000_30031040[:,][:,5*0+2]
EigenValReL0g000_30031040 = dataL0g000_30031040[:,][:,5*0+3]
EigenValImL0g000_30031040 = dataL0g000_30031040[:,][:,5*0+4]

dataL0g000_30031050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK003/N050/HamVals.txt')

MomentumAxL0g000_30031050 = dataL0g000_30031050[:,][:,5*0+0]
KineticEneL0g000_30031050 = dataL0g000_30031050[:,][:,5*0+1]
SelfEnergyL0g000_30031050 = dataL0g000_30031050[:,][:,5*0+2]
EigenValReL0g000_30031050 = dataL0g000_30031050[:,][:,5*0+3]
EigenValImL0g000_30031050 = dataL0g000_30031050[:,][:,5*0+4]

dataL0g000_30071010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK007/N010/HamVals.txt')

MomentumAxL0g000_30071010 = dataL0g000_30071010[:,][:,5*0+0]
KineticEneL0g000_30071010 = dataL0g000_30071010[:,][:,5*0+1]
SelfEnergyL0g000_30071010 = dataL0g000_30071010[:,][:,5*0+2]
EigenValReL0g000_30071010 = dataL0g000_30071010[:,][:,5*0+3]
EigenValImL0g000_30071010 = dataL0g000_30071010[:,][:,5*0+4]

dataL0g000_30071020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK007/N020/HamVals.txt')

MomentumAxL0g000_30071020 = dataL0g000_30071020[:,][:,5*0+0]
KineticEneL0g000_30071020 = dataL0g000_30071020[:,][:,5*0+1]
SelfEnergyL0g000_30071020 = dataL0g000_30071020[:,][:,5*0+2]
EigenValReL0g000_30071020 = dataL0g000_30071020[:,][:,5*0+3]
EigenValImL0g000_30071020 = dataL0g000_30071020[:,][:,5*0+4]

dataL0g000_30071030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK007/N030/HamVals.txt')

MomentumAxL0g000_30071030 = dataL0g000_30071030[:,][:,5*0+0]
KineticEneL0g000_30071030 = dataL0g000_30071030[:,][:,5*0+1]
SelfEnergyL0g000_30071030 = dataL0g000_30071030[:,][:,5*0+2]
EigenValReL0g000_30071030 = dataL0g000_30071030[:,][:,5*0+3]
EigenValImL0g000_30071030 = dataL0g000_30071030[:,][:,5*0+4]

dataL0g000_30071040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK007/N040/HamVals.txt')

MomentumAxL0g000_30071040 = dataL0g000_30071040[:,][:,5*0+0]
KineticEneL0g000_30071040 = dataL0g000_30071040[:,][:,5*0+1]
SelfEnergyL0g000_30071040 = dataL0g000_30071040[:,][:,5*0+2]
EigenValReL0g000_30071040 = dataL0g000_30071040[:,][:,5*0+3]
EigenValImL0g000_30071040 = dataL0g000_30071040[:,][:,5*0+4]

dataL0g000_30071050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK007/N050/HamVals.txt')

MomentumAxL0g000_30071050 = dataL0g000_30071050[:,][:,5*0+0]
KineticEneL0g000_30071050 = dataL0g000_30071050[:,][:,5*0+1]
SelfEnergyL0g000_30071050 = dataL0g000_30071050[:,][:,5*0+2]
EigenValReL0g000_30071050 = dataL0g000_30071050[:,][:,5*0+3]
EigenValImL0g000_30071050 = dataL0g000_30071050[:,][:,5*0+4]

MaxEigenValImL0g000_31Inf = np.zeros((6))

MaxEigenValImL0g000_31Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_30011010),np.max(EigenValImL0g000_30011020),np.max(EigenValImL0g000_30011030),np.max(EigenValImL0g000_30011040),np.max(EigenValImL0g000_30011050)], 1)[[1]]
MaxEigenValImL0g000_31Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_30021010),np.max(EigenValImL0g000_30021020),np.max(EigenValImL0g000_30021030),np.max(EigenValImL0g000_30021040),np.max(EigenValImL0g000_30021050)], 1)[[1]]
MaxEigenValImL0g000_31Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_30031010),np.max(EigenValImL0g000_30031020),np.max(EigenValImL0g000_30031030),np.max(EigenValImL0g000_30031040),np.max(EigenValImL0g000_30031050)], 1)[[1]]
MaxEigenValImL0g000_31Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_30051010),np.max(EigenValImL0g000_30051020),np.max(EigenValImL0g000_30051030),np.max(EigenValImL0g000_30051040),np.max(EigenValImL0g000_30051050)], 1)[[1]]
MaxEigenValImL0g000_31Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_30071010),np.max(EigenValImL0g000_30071020),np.max(EigenValImL0g000_30071030),np.max(EigenValImL0g000_30071040),np.max(EigenValImL0g000_30071050)], 1)[[1]]
MaxEigenValImL0g000_31Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_30101010),np.max(EigenValImL0g000_30101020),np.max(EigenValImL0g000_30101030),np.max(EigenValImL0g000_30101040),np.max(EigenValImL0g000_30101050)], 1)[[1]]

########################################################################

dataL0g000_350011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK001/N010/HamVals.txt')

MomentumAxL0g000_350011010 = dataL0g000_350011010[:,][:,5*0+0]
KineticEneL0g000_350011010 = dataL0g000_350011010[:,][:,5*0+1]
SelfEnergyL0g000_350011010 = dataL0g000_350011010[:,][:,5*0+2]
EigenValReL0g000_350011010 = dataL0g000_350011010[:,][:,5*0+3]
EigenValImL0g000_350011010 = dataL0g000_350011010[:,][:,5*0+4]

dataL0g000_350011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK001/N020/HamVals.txt')

MomentumAxL0g000_350011020 = dataL0g000_350011020[:,][:,5*0+0]
KineticEneL0g000_350011020 = dataL0g000_350011020[:,][:,5*0+1]
SelfEnergyL0g000_350011020 = dataL0g000_350011020[:,][:,5*0+2]
EigenValReL0g000_350011020 = dataL0g000_350011020[:,][:,5*0+3]
EigenValImL0g000_350011020 = dataL0g000_350011020[:,][:,5*0+4]

dataL0g000_350011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK001/N030/HamVals.txt')

MomentumAxL0g000_350011030 = dataL0g000_350011030[:,][:,5*0+0]
KineticEneL0g000_350011030 = dataL0g000_350011030[:,][:,5*0+1]
SelfEnergyL0g000_350011030 = dataL0g000_350011030[:,][:,5*0+2]
EigenValReL0g000_350011030 = dataL0g000_350011030[:,][:,5*0+3]
EigenValImL0g000_350011030 = dataL0g000_350011030[:,][:,5*0+4]

dataL0g000_350011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK001/N040/HamVals.txt')

MomentumAxL0g000_350011040 = dataL0g000_350011040[:,][:,5*0+0]
KineticEneL0g000_350011040 = dataL0g000_350011040[:,][:,5*0+1]
SelfEnergyL0g000_350011040 = dataL0g000_350011040[:,][:,5*0+2]
EigenValReL0g000_350011040 = dataL0g000_350011040[:,][:,5*0+3]
EigenValImL0g000_350011040 = dataL0g000_350011040[:,][:,5*0+4]

dataL0g000_350011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK001/N050/HamVals.txt')

MomentumAxL0g000_350011050 = dataL0g000_350011050[:,][:,5*0+0]
KineticEneL0g000_350011050 = dataL0g000_350011050[:,][:,5*0+1]
SelfEnergyL0g000_350011050 = dataL0g000_350011050[:,][:,5*0+2]
EigenValReL0g000_350011050 = dataL0g000_350011050[:,][:,5*0+3]
EigenValImL0g000_350011050 = dataL0g000_350011050[:,][:,5*0+4]

dataL0g000_350021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK002/N010/HamVals.txt')

MomentumAxL0g000_350021010 = dataL0g000_350021010[:,][:,5*0+0]
KineticEneL0g000_350021010 = dataL0g000_350021010[:,][:,5*0+1]
SelfEnergyL0g000_350021010 = dataL0g000_350021010[:,][:,5*0+2]
EigenValReL0g000_350021010 = dataL0g000_350021010[:,][:,5*0+3]
EigenValImL0g000_350021010 = dataL0g000_350021010[:,][:,5*0+4]

dataL0g000_350021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK002/N020/HamVals.txt')

MomentumAxL0g000_350021020 = dataL0g000_350021020[:,][:,5*0+0]
KineticEneL0g000_350021020 = dataL0g000_350021020[:,][:,5*0+1]
SelfEnergyL0g000_350021020 = dataL0g000_350021020[:,][:,5*0+2]
EigenValReL0g000_350021020 = dataL0g000_350021020[:,][:,5*0+3]
EigenValImL0g000_350021020 = dataL0g000_350021020[:,][:,5*0+4]

dataL0g000_350021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK002/N030/HamVals.txt')

MomentumAxL0g000_350021030 = dataL0g000_350021030[:,][:,5*0+0]
KineticEneL0g000_350021030 = dataL0g000_350021030[:,][:,5*0+1]
SelfEnergyL0g000_350021030 = dataL0g000_350021030[:,][:,5*0+2]
EigenValReL0g000_350021030 = dataL0g000_350021030[:,][:,5*0+3]
EigenValImL0g000_350021030 = dataL0g000_350021030[:,][:,5*0+4]

dataL0g000_350021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK002/N040/HamVals.txt')

MomentumAxL0g000_350021040 = dataL0g000_350021040[:,][:,5*0+0]
KineticEneL0g000_350021040 = dataL0g000_350021040[:,][:,5*0+1]
SelfEnergyL0g000_350021040 = dataL0g000_350021040[:,][:,5*0+2]
EigenValReL0g000_350021040 = dataL0g000_350021040[:,][:,5*0+3]
EigenValImL0g000_350021040 = dataL0g000_350021040[:,][:,5*0+4]

dataL0g000_350021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK002/N050/HamVals.txt')

MomentumAxL0g000_350021050 = dataL0g000_350021050[:,][:,5*0+0]
KineticEneL0g000_350021050 = dataL0g000_350021050[:,][:,5*0+1]
SelfEnergyL0g000_350021050 = dataL0g000_350021050[:,][:,5*0+2]
EigenValReL0g000_350021050 = dataL0g000_350021050[:,][:,5*0+3]
EigenValImL0g000_350021050 = dataL0g000_350021050[:,][:,5*0+4]

dataL0g000_350051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK005/N010/HamVals.txt')

MomentumAxL0g000_350051010 = dataL0g000_350051010[:,][:,5*0+0]
KineticEneL0g000_350051010 = dataL0g000_350051010[:,][:,5*0+1]
SelfEnergyL0g000_350051010 = dataL0g000_350051010[:,][:,5*0+2]
EigenValReL0g000_350051010 = dataL0g000_350051010[:,][:,5*0+3]
EigenValImL0g000_350051010 = dataL0g000_350051010[:,][:,5*0+4]

dataL0g000_350051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK005/N020/HamVals.txt')

MomentumAxL0g000_350051020 = dataL0g000_350051020[:,][:,5*0+0]
KineticEneL0g000_350051020 = dataL0g000_350051020[:,][:,5*0+1]
SelfEnergyL0g000_350051020 = dataL0g000_350051020[:,][:,5*0+2]
EigenValReL0g000_350051020 = dataL0g000_350051020[:,][:,5*0+3]
EigenValImL0g000_350051020 = dataL0g000_350051020[:,][:,5*0+4]

dataL0g000_350051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK005/N030/HamVals.txt')

MomentumAxL0g000_350051030 = dataL0g000_350051030[:,][:,5*0+0]
KineticEneL0g000_350051030 = dataL0g000_350051030[:,][:,5*0+1]
SelfEnergyL0g000_350051030 = dataL0g000_350051030[:,][:,5*0+2]
EigenValReL0g000_350051030 = dataL0g000_350051030[:,][:,5*0+3]
EigenValImL0g000_350051030 = dataL0g000_350051030[:,][:,5*0+4]

dataL0g000_350051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK005/N040/HamVals.txt')

MomentumAxL0g000_350051040 = dataL0g000_350051040[:,][:,5*0+0]
KineticEneL0g000_350051040 = dataL0g000_350051040[:,][:,5*0+1]
SelfEnergyL0g000_350051040 = dataL0g000_350051040[:,][:,5*0+2]
EigenValReL0g000_350051040 = dataL0g000_350051040[:,][:,5*0+3]
EigenValImL0g000_350051040 = dataL0g000_350051040[:,][:,5*0+4]

dataL0g000_350051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK005/N050/HamVals.txt')

MomentumAxL0g000_350051050 = dataL0g000_350051050[:,][:,5*0+0]
KineticEneL0g000_350051050 = dataL0g000_350051050[:,][:,5*0+1]
SelfEnergyL0g000_350051050 = dataL0g000_350051050[:,][:,5*0+2]
EigenValReL0g000_350051050 = dataL0g000_350051050[:,][:,5*0+3]
EigenValImL0g000_350051050 = dataL0g000_350051050[:,][:,5*0+4]

dataL0g000_350101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK010/N010/HamVals.txt')

MomentumAxL0g000_350101010 = dataL0g000_350101010[:,][:,5*0+0]
KineticEneL0g000_350101010 = dataL0g000_350101010[:,][:,5*0+1]
SelfEnergyL0g000_350101010 = dataL0g000_350101010[:,][:,5*0+2]
EigenValReL0g000_350101010 = dataL0g000_350101010[:,][:,5*0+3]
EigenValImL0g000_350101010 = dataL0g000_350101010[:,][:,5*0+4]

dataL0g000_350101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK010/N020/HamVals.txt')

MomentumAxL0g000_350101020 = dataL0g000_350101020[:,][:,5*0+0]
KineticEneL0g000_350101020 = dataL0g000_350101020[:,][:,5*0+1]
SelfEnergyL0g000_350101020 = dataL0g000_350101020[:,][:,5*0+2]
EigenValReL0g000_350101020 = dataL0g000_350101020[:,][:,5*0+3]
EigenValImL0g000_350101020 = dataL0g000_350101020[:,][:,5*0+4]

dataL0g000_350101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK010/N030/HamVals.txt')

MomentumAxL0g000_350101030 = dataL0g000_350101030[:,][:,5*0+0]
KineticEneL0g000_350101030 = dataL0g000_350101030[:,][:,5*0+1]
SelfEnergyL0g000_350101030 = dataL0g000_350101030[:,][:,5*0+2]
EigenValReL0g000_350101030 = dataL0g000_350101030[:,][:,5*0+3]
EigenValImL0g000_350101030 = dataL0g000_350101030[:,][:,5*0+4]

dataL0g000_350101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK010/N040/HamVals.txt')

MomentumAxL0g000_350101040 = dataL0g000_350101040[:,][:,5*0+0]
KineticEneL0g000_350101040 = dataL0g000_350101040[:,][:,5*0+1]
SelfEnergyL0g000_350101040 = dataL0g000_350101040[:,][:,5*0+2]
EigenValReL0g000_350101040 = dataL0g000_350101040[:,][:,5*0+3]
EigenValImL0g000_350101040 = dataL0g000_350101040[:,][:,5*0+4]

dataL0g000_350101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK010/N050/HamVals.txt')

MomentumAxL0g000_350101050 = dataL0g000_350101050[:,][:,5*0+0]
KineticEneL0g000_350101050 = dataL0g000_350101050[:,][:,5*0+1]
SelfEnergyL0g000_350101050 = dataL0g000_350101050[:,][:,5*0+2]
EigenValReL0g000_350101050 = dataL0g000_350101050[:,][:,5*0+3]
EigenValImL0g000_350101050 = dataL0g000_350101050[:,][:,5*0+4]

dataL0g000_350031010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK003/N010/HamVals.txt')

MomentumAxL0g000_350031010 = dataL0g000_350031010[:,][:,5*0+0]
KineticEneL0g000_350031010 = dataL0g000_350031010[:,][:,5*0+1]
SelfEnergyL0g000_350031010 = dataL0g000_350031010[:,][:,5*0+2]
EigenValReL0g000_350031010 = dataL0g000_350031010[:,][:,5*0+3]
EigenValImL0g000_350031010 = dataL0g000_350031010[:,][:,5*0+4]

dataL0g000_350031020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK003/N020/HamVals.txt')

MomentumAxL0g000_350031020 = dataL0g000_350031020[:,][:,5*0+0]
KineticEneL0g000_350031020 = dataL0g000_350031020[:,][:,5*0+1]
SelfEnergyL0g000_350031020 = dataL0g000_350031020[:,][:,5*0+2]
EigenValReL0g000_350031020 = dataL0g000_350031020[:,][:,5*0+3]
EigenValImL0g000_350031020 = dataL0g000_350031020[:,][:,5*0+4]

dataL0g000_350031030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK003/N030/HamVals.txt')

MomentumAxL0g000_350031030 = dataL0g000_350031030[:,][:,5*0+0]
KineticEneL0g000_350031030 = dataL0g000_350031030[:,][:,5*0+1]
SelfEnergyL0g000_350031030 = dataL0g000_350031030[:,][:,5*0+2]
EigenValReL0g000_350031030 = dataL0g000_350031030[:,][:,5*0+3]
EigenValImL0g000_350031030 = dataL0g000_350031030[:,][:,5*0+4]

dataL0g000_350031040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK003/N040/HamVals.txt')

MomentumAxL0g000_350031040 = dataL0g000_350031040[:,][:,5*0+0]
KineticEneL0g000_350031040 = dataL0g000_350031040[:,][:,5*0+1]
SelfEnergyL0g000_350031040 = dataL0g000_350031040[:,][:,5*0+2]
EigenValReL0g000_350031040 = dataL0g000_350031040[:,][:,5*0+3]
EigenValImL0g000_350031040 = dataL0g000_350031040[:,][:,5*0+4]

dataL0g000_350031050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK003/N050/HamVals.txt')

MomentumAxL0g000_350031050 = dataL0g000_350031050[:,][:,5*0+0]
KineticEneL0g000_350031050 = dataL0g000_350031050[:,][:,5*0+1]
SelfEnergyL0g000_350031050 = dataL0g000_350031050[:,][:,5*0+2]
EigenValReL0g000_350031050 = dataL0g000_350031050[:,][:,5*0+3]
EigenValImL0g000_350031050 = dataL0g000_350031050[:,][:,5*0+4]

dataL0g000_350071010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK007/N010/HamVals.txt')

MomentumAxL0g000_350071010 = dataL0g000_350071010[:,][:,5*0+0]
KineticEneL0g000_350071010 = dataL0g000_350071010[:,][:,5*0+1]
SelfEnergyL0g000_350071010 = dataL0g000_350071010[:,][:,5*0+2]
EigenValReL0g000_350071010 = dataL0g000_350071010[:,][:,5*0+3]
EigenValImL0g000_350071010 = dataL0g000_350071010[:,][:,5*0+4]

dataL0g000_350071020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK007/N020/HamVals.txt')

MomentumAxL0g000_350071020 = dataL0g000_350071020[:,][:,5*0+0]
KineticEneL0g000_350071020 = dataL0g000_350071020[:,][:,5*0+1]
SelfEnergyL0g000_350071020 = dataL0g000_350071020[:,][:,5*0+2]
EigenValReL0g000_350071020 = dataL0g000_350071020[:,][:,5*0+3]
EigenValImL0g000_350071020 = dataL0g000_350071020[:,][:,5*0+4]

dataL0g000_350071030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK007/N030/HamVals.txt')

MomentumAxL0g000_350071030 = dataL0g000_350071030[:,][:,5*0+0]
KineticEneL0g000_350071030 = dataL0g000_350071030[:,][:,5*0+1]
SelfEnergyL0g000_350071030 = dataL0g000_350071030[:,][:,5*0+2]
EigenValReL0g000_350071030 = dataL0g000_350071030[:,][:,5*0+3]
EigenValImL0g000_350071030 = dataL0g000_350071030[:,][:,5*0+4]

dataL0g000_350071040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK007/N040/HamVals.txt')

MomentumAxL0g000_350071040 = dataL0g000_350071040[:,][:,5*0+0]
KineticEneL0g000_350071040 = dataL0g000_350071040[:,][:,5*0+1]
SelfEnergyL0g000_350071040 = dataL0g000_350071040[:,][:,5*0+2]
EigenValReL0g000_350071040 = dataL0g000_350071040[:,][:,5*0+3]
EigenValImL0g000_350071040 = dataL0g000_350071040[:,][:,5*0+4]

dataL0g000_350071050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-35/aK007/N050/HamVals.txt')

MomentumAxL0g000_350071050 = dataL0g000_350071050[:,][:,5*0+0]
KineticEneL0g000_350071050 = dataL0g000_350071050[:,][:,5*0+1]
SelfEnergyL0g000_350071050 = dataL0g000_350071050[:,][:,5*0+2]
EigenValReL0g000_350071050 = dataL0g000_350071050[:,][:,5*0+3]
EigenValImL0g000_350071050 = dataL0g000_350071050[:,][:,5*0+4]

MaxEigenValImL0g000_351Inf = np.zeros((6))

MaxEigenValImL0g000_351Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_350011010),np.max(EigenValImL0g000_350011020),np.max(EigenValImL0g000_350011030),np.max(EigenValImL0g000_350011040),np.max(EigenValImL0g000_350011050)], 1)[[1]]
MaxEigenValImL0g000_351Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_350021010),np.max(EigenValImL0g000_350021020),np.max(EigenValImL0g000_350021030),np.max(EigenValImL0g000_350021040),np.max(EigenValImL0g000_350021050)], 1)[[1]]
MaxEigenValImL0g000_351Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_350031010),np.max(EigenValImL0g000_350031020),np.max(EigenValImL0g000_350031030),np.max(EigenValImL0g000_350031040),np.max(EigenValImL0g000_350031050)], 1)[[1]]
MaxEigenValImL0g000_351Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_350051010),np.max(EigenValImL0g000_350051020),np.max(EigenValImL0g000_350051030),np.max(EigenValImL0g000_350051040),np.max(EigenValImL0g000_350051050)], 1)[[1]]
MaxEigenValImL0g000_351Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_350071010),np.max(EigenValImL0g000_350071020),np.max(EigenValImL0g000_350071030),np.max(EigenValImL0g000_350071040),np.max(EigenValImL0g000_350071050)], 1)[[1]]
MaxEigenValImL0g000_351Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_350101010),np.max(EigenValImL0g000_350101020),np.max(EigenValImL0g000_350101030),np.max(EigenValImL0g000_350101040),np.max(EigenValImL0g000_350101050)], 1)[[1]]

########################################################################

dataL0g000_40011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK001/N010/HamVals.txt')

MomentumAxL0g000_40011010 = dataL0g000_40011010[:,][:,5*0+0]
KineticEneL0g000_40011010 = dataL0g000_40011010[:,][:,5*0+1]
SelfEnergyL0g000_40011010 = dataL0g000_40011010[:,][:,5*0+2]
EigenValReL0g000_40011010 = dataL0g000_40011010[:,][:,5*0+3]
EigenValImL0g000_40011010 = dataL0g000_40011010[:,][:,5*0+4]

dataL0g000_40011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK001/N020/HamVals.txt')

MomentumAxL0g000_40011020 = dataL0g000_40011020[:,][:,5*0+0]
KineticEneL0g000_40011020 = dataL0g000_40011020[:,][:,5*0+1]
SelfEnergyL0g000_40011020 = dataL0g000_40011020[:,][:,5*0+2]
EigenValReL0g000_40011020 = dataL0g000_40011020[:,][:,5*0+3]
EigenValImL0g000_40011020 = dataL0g000_40011020[:,][:,5*0+4]

dataL0g000_40011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK001/N030/HamVals.txt')

MomentumAxL0g000_40011030 = dataL0g000_40011030[:,][:,5*0+0]
KineticEneL0g000_40011030 = dataL0g000_40011030[:,][:,5*0+1]
SelfEnergyL0g000_40011030 = dataL0g000_40011030[:,][:,5*0+2]
EigenValReL0g000_40011030 = dataL0g000_40011030[:,][:,5*0+3]
EigenValImL0g000_40011030 = dataL0g000_40011030[:,][:,5*0+4]

dataL0g000_40011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK001/N040/HamVals.txt')

MomentumAxL0g000_40011040 = dataL0g000_40011040[:,][:,5*0+0]
KineticEneL0g000_40011040 = dataL0g000_40011040[:,][:,5*0+1]
SelfEnergyL0g000_40011040 = dataL0g000_40011040[:,][:,5*0+2]
EigenValReL0g000_40011040 = dataL0g000_40011040[:,][:,5*0+3]
EigenValImL0g000_40011040 = dataL0g000_40011040[:,][:,5*0+4]

dataL0g000_40011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK001/N050/HamVals.txt')

MomentumAxL0g000_40011050 = dataL0g000_40011050[:,][:,5*0+0]
KineticEneL0g000_40011050 = dataL0g000_40011050[:,][:,5*0+1]
SelfEnergyL0g000_40011050 = dataL0g000_40011050[:,][:,5*0+2]
EigenValReL0g000_40011050 = dataL0g000_40011050[:,][:,5*0+3]
EigenValImL0g000_40011050 = dataL0g000_40011050[:,][:,5*0+4]

dataL0g000_40021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK002/N010/HamVals.txt')

MomentumAxL0g000_40021010 = dataL0g000_40021010[:,][:,5*0+0]
KineticEneL0g000_40021010 = dataL0g000_40021010[:,][:,5*0+1]
SelfEnergyL0g000_40021010 = dataL0g000_40021010[:,][:,5*0+2]
EigenValReL0g000_40021010 = dataL0g000_40021010[:,][:,5*0+3]
EigenValImL0g000_40021010 = dataL0g000_40021010[:,][:,5*0+4]

dataL0g000_40021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK002/N020/HamVals.txt')

MomentumAxL0g000_40021020 = dataL0g000_40021020[:,][:,5*0+0]
KineticEneL0g000_40021020 = dataL0g000_40021020[:,][:,5*0+1]
SelfEnergyL0g000_40021020 = dataL0g000_40021020[:,][:,5*0+2]
EigenValReL0g000_40021020 = dataL0g000_40021020[:,][:,5*0+3]
EigenValImL0g000_40021020 = dataL0g000_40021020[:,][:,5*0+4]

dataL0g000_40021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK002/N030/HamVals.txt')

MomentumAxL0g000_40021030 = dataL0g000_40021030[:,][:,5*0+0]
KineticEneL0g000_40021030 = dataL0g000_40021030[:,][:,5*0+1]
SelfEnergyL0g000_40021030 = dataL0g000_40021030[:,][:,5*0+2]
EigenValReL0g000_40021030 = dataL0g000_40021030[:,][:,5*0+3]
EigenValImL0g000_40021030 = dataL0g000_40021030[:,][:,5*0+4]

dataL0g000_40021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK002/N040/HamVals.txt')

MomentumAxL0g000_40021040 = dataL0g000_40021040[:,][:,5*0+0]
KineticEneL0g000_40021040 = dataL0g000_40021040[:,][:,5*0+1]
SelfEnergyL0g000_40021040 = dataL0g000_40021040[:,][:,5*0+2]
EigenValReL0g000_40021040 = dataL0g000_40021040[:,][:,5*0+3]
EigenValImL0g000_40021040 = dataL0g000_40021040[:,][:,5*0+4]

dataL0g000_40021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK002/N050/HamVals.txt')

MomentumAxL0g000_40021050 = dataL0g000_40021050[:,][:,5*0+0]
KineticEneL0g000_40021050 = dataL0g000_40021050[:,][:,5*0+1]
SelfEnergyL0g000_40021050 = dataL0g000_40021050[:,][:,5*0+2]
EigenValReL0g000_40021050 = dataL0g000_40021050[:,][:,5*0+3]
EigenValImL0g000_40021050 = dataL0g000_40021050[:,][:,5*0+4]

dataL0g000_40051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK005/N010/HamVals.txt')

MomentumAxL0g000_40051010 = dataL0g000_40051010[:,][:,5*0+0]
KineticEneL0g000_40051010 = dataL0g000_40051010[:,][:,5*0+1]
SelfEnergyL0g000_40051010 = dataL0g000_40051010[:,][:,5*0+2]
EigenValReL0g000_40051010 = dataL0g000_40051010[:,][:,5*0+3]
EigenValImL0g000_40051010 = dataL0g000_40051010[:,][:,5*0+4]

dataL0g000_40051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK005/N020/HamVals.txt')

MomentumAxL0g000_40051020 = dataL0g000_40051020[:,][:,5*0+0]
KineticEneL0g000_40051020 = dataL0g000_40051020[:,][:,5*0+1]
SelfEnergyL0g000_40051020 = dataL0g000_40051020[:,][:,5*0+2]
EigenValReL0g000_40051020 = dataL0g000_40051020[:,][:,5*0+3]
EigenValImL0g000_40051020 = dataL0g000_40051020[:,][:,5*0+4]

dataL0g000_40051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK005/N030/HamVals.txt')

MomentumAxL0g000_40051030 = dataL0g000_40051030[:,][:,5*0+0]
KineticEneL0g000_40051030 = dataL0g000_40051030[:,][:,5*0+1]
SelfEnergyL0g000_40051030 = dataL0g000_40051030[:,][:,5*0+2]
EigenValReL0g000_40051030 = dataL0g000_40051030[:,][:,5*0+3]
EigenValImL0g000_40051030 = dataL0g000_40051030[:,][:,5*0+4]

dataL0g000_40051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK005/N040/HamVals.txt')

MomentumAxL0g000_40051040 = dataL0g000_40051040[:,][:,5*0+0]
KineticEneL0g000_40051040 = dataL0g000_40051040[:,][:,5*0+1]
SelfEnergyL0g000_40051040 = dataL0g000_40051040[:,][:,5*0+2]
EigenValReL0g000_40051040 = dataL0g000_40051040[:,][:,5*0+3]
EigenValImL0g000_40051040 = dataL0g000_40051040[:,][:,5*0+4]

dataL0g000_40051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK005/N050/HamVals.txt')

MomentumAxL0g000_40051050 = dataL0g000_40051050[:,][:,5*0+0]
KineticEneL0g000_40051050 = dataL0g000_40051050[:,][:,5*0+1]
SelfEnergyL0g000_40051050 = dataL0g000_40051050[:,][:,5*0+2]
EigenValReL0g000_40051050 = dataL0g000_40051050[:,][:,5*0+3]
EigenValImL0g000_40051050 = dataL0g000_40051050[:,][:,5*0+4]

dataL0g000_40101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK010/N010/HamVals.txt')

MomentumAxL0g000_40101010 = dataL0g000_40101010[:,][:,5*0+0]
KineticEneL0g000_40101010 = dataL0g000_40101010[:,][:,5*0+1]
SelfEnergyL0g000_40101010 = dataL0g000_40101010[:,][:,5*0+2]
EigenValReL0g000_40101010 = dataL0g000_40101010[:,][:,5*0+3]
EigenValImL0g000_40101010 = dataL0g000_40101010[:,][:,5*0+4]

dataL0g000_40101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK010/N020/HamVals.txt')

MomentumAxL0g000_40101020 = dataL0g000_40101020[:,][:,5*0+0]
KineticEneL0g000_40101020 = dataL0g000_40101020[:,][:,5*0+1]
SelfEnergyL0g000_40101020 = dataL0g000_40101020[:,][:,5*0+2]
EigenValReL0g000_40101020 = dataL0g000_40101020[:,][:,5*0+3]
EigenValImL0g000_40101020 = dataL0g000_40101020[:,][:,5*0+4]

dataL0g000_40101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK010/N030/HamVals.txt')

MomentumAxL0g000_40101030 = dataL0g000_40101030[:,][:,5*0+0]
KineticEneL0g000_40101030 = dataL0g000_40101030[:,][:,5*0+1]
SelfEnergyL0g000_40101030 = dataL0g000_40101030[:,][:,5*0+2]
EigenValReL0g000_40101030 = dataL0g000_40101030[:,][:,5*0+3]
EigenValImL0g000_40101030 = dataL0g000_40101030[:,][:,5*0+4]

dataL0g000_40101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK010/N040/HamVals.txt')

MomentumAxL0g000_40101040 = dataL0g000_40101040[:,][:,5*0+0]
KineticEneL0g000_40101040 = dataL0g000_40101040[:,][:,5*0+1]
SelfEnergyL0g000_40101040 = dataL0g000_40101040[:,][:,5*0+2]
EigenValReL0g000_40101040 = dataL0g000_40101040[:,][:,5*0+3]
EigenValImL0g000_40101040 = dataL0g000_40101040[:,][:,5*0+4]

dataL0g000_40101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK010/N050/HamVals.txt')

MomentumAxL0g000_40101050 = dataL0g000_40101050[:,][:,5*0+0]
KineticEneL0g000_40101050 = dataL0g000_40101050[:,][:,5*0+1]
SelfEnergyL0g000_40101050 = dataL0g000_40101050[:,][:,5*0+2]
EigenValReL0g000_40101050 = dataL0g000_40101050[:,][:,5*0+3]
EigenValImL0g000_40101050 = dataL0g000_40101050[:,][:,5*0+4]

dataL0g000_40031010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK003/N010/HamVals.txt')

MomentumAxL0g000_40031010 = dataL0g000_40031010[:,][:,5*0+0]
KineticEneL0g000_40031010 = dataL0g000_40031010[:,][:,5*0+1]
SelfEnergyL0g000_40031010 = dataL0g000_40031010[:,][:,5*0+2]
EigenValReL0g000_40031010 = dataL0g000_40031010[:,][:,5*0+3]
EigenValImL0g000_40031010 = dataL0g000_40031010[:,][:,5*0+4]

dataL0g000_40031020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK003/N020/HamVals.txt')

MomentumAxL0g000_40031020 = dataL0g000_40031020[:,][:,5*0+0]
KineticEneL0g000_40031020 = dataL0g000_40031020[:,][:,5*0+1]
SelfEnergyL0g000_40031020 = dataL0g000_40031020[:,][:,5*0+2]
EigenValReL0g000_40031020 = dataL0g000_40031020[:,][:,5*0+3]
EigenValImL0g000_40031020 = dataL0g000_40031020[:,][:,5*0+4]

dataL0g000_40031030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK003/N030/HamVals.txt')

MomentumAxL0g000_40031030 = dataL0g000_40031030[:,][:,5*0+0]
KineticEneL0g000_40031030 = dataL0g000_40031030[:,][:,5*0+1]
SelfEnergyL0g000_40031030 = dataL0g000_40031030[:,][:,5*0+2]
EigenValReL0g000_40031030 = dataL0g000_40031030[:,][:,5*0+3]
EigenValImL0g000_40031030 = dataL0g000_40031030[:,][:,5*0+4]

dataL0g000_40031040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK003/N040/HamVals.txt')

MomentumAxL0g000_40031040 = dataL0g000_40031040[:,][:,5*0+0]
KineticEneL0g000_40031040 = dataL0g000_40031040[:,][:,5*0+1]
SelfEnergyL0g000_40031040 = dataL0g000_40031040[:,][:,5*0+2]
EigenValReL0g000_40031040 = dataL0g000_40031040[:,][:,5*0+3]
EigenValImL0g000_40031040 = dataL0g000_40031040[:,][:,5*0+4]

dataL0g000_40031050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK003/N050/HamVals.txt')

MomentumAxL0g000_40031050 = dataL0g000_40031050[:,][:,5*0+0]
KineticEneL0g000_40031050 = dataL0g000_40031050[:,][:,5*0+1]
SelfEnergyL0g000_40031050 = dataL0g000_40031050[:,][:,5*0+2]
EigenValReL0g000_40031050 = dataL0g000_40031050[:,][:,5*0+3]
EigenValImL0g000_40031050 = dataL0g000_40031050[:,][:,5*0+4]

dataL0g000_40071010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK007/N010/HamVals.txt')

MomentumAxL0g000_40071010 = dataL0g000_40071010[:,][:,5*0+0]
KineticEneL0g000_40071010 = dataL0g000_40071010[:,][:,5*0+1]
SelfEnergyL0g000_40071010 = dataL0g000_40071010[:,][:,5*0+2]
EigenValReL0g000_40071010 = dataL0g000_40071010[:,][:,5*0+3]
EigenValImL0g000_40071010 = dataL0g000_40071010[:,][:,5*0+4]

dataL0g000_40071020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK007/N020/HamVals.txt')

MomentumAxL0g000_40071020 = dataL0g000_40071020[:,][:,5*0+0]
KineticEneL0g000_40071020 = dataL0g000_40071020[:,][:,5*0+1]
SelfEnergyL0g000_40071020 = dataL0g000_40071020[:,][:,5*0+2]
EigenValReL0g000_40071020 = dataL0g000_40071020[:,][:,5*0+3]
EigenValImL0g000_40071020 = dataL0g000_40071020[:,][:,5*0+4]

dataL0g000_40071030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK007/N030/HamVals.txt')

MomentumAxL0g000_40071030 = dataL0g000_40071030[:,][:,5*0+0]
KineticEneL0g000_40071030 = dataL0g000_40071030[:,][:,5*0+1]
SelfEnergyL0g000_40071030 = dataL0g000_40071030[:,][:,5*0+2]
EigenValReL0g000_40071030 = dataL0g000_40071030[:,][:,5*0+3]
EigenValImL0g000_40071030 = dataL0g000_40071030[:,][:,5*0+4]

dataL0g000_40071040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK007/N040/HamVals.txt')

MomentumAxL0g000_40071040 = dataL0g000_40071040[:,][:,5*0+0]
KineticEneL0g000_40071040 = dataL0g000_40071040[:,][:,5*0+1]
SelfEnergyL0g000_40071040 = dataL0g000_40071040[:,][:,5*0+2]
EigenValReL0g000_40071040 = dataL0g000_40071040[:,][:,5*0+3]
EigenValImL0g000_40071040 = dataL0g000_40071040[:,][:,5*0+4]

dataL0g000_40071050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK007/N050/HamVals.txt')

MomentumAxL0g000_40071050 = dataL0g000_40071050[:,][:,5*0+0]
KineticEneL0g000_40071050 = dataL0g000_40071050[:,][:,5*0+1]
SelfEnergyL0g000_40071050 = dataL0g000_40071050[:,][:,5*0+2]
EigenValReL0g000_40071050 = dataL0g000_40071050[:,][:,5*0+3]
EigenValImL0g000_40071050 = dataL0g000_40071050[:,][:,5*0+4]

MaxEigenValImL0g000_41Inf = np.zeros((6))

MaxEigenValImL0g000_41Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_40011010),np.max(EigenValImL0g000_40011020),np.max(EigenValImL0g000_40011030),np.max(EigenValImL0g000_40011040),np.max(EigenValImL0g000_40011050)], 1)[[1]]
MaxEigenValImL0g000_41Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_40021010),np.max(EigenValImL0g000_40021020),np.max(EigenValImL0g000_40021030),np.max(EigenValImL0g000_40021040),np.max(EigenValImL0g000_40021050)], 1)[[1]]
MaxEigenValImL0g000_41Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_40031010),np.max(EigenValImL0g000_40031020),np.max(EigenValImL0g000_40031030),np.max(EigenValImL0g000_40031040),np.max(EigenValImL0g000_40031050)], 1)[[1]]
MaxEigenValImL0g000_41Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_40051010),np.max(EigenValImL0g000_40051020),np.max(EigenValImL0g000_40051030),np.max(EigenValImL0g000_40051040),np.max(EigenValImL0g000_40051050)], 1)[[1]]
MaxEigenValImL0g000_41Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_40071010),np.max(EigenValImL0g000_40071020),np.max(EigenValImL0g000_40071030),np.max(EigenValImL0g000_40071040),np.max(EigenValImL0g000_40071050)], 1)[[1]]
MaxEigenValImL0g000_41Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_40101010),np.max(EigenValImL0g000_40101020),np.max(EigenValImL0g000_40101030),np.max(EigenValImL0g000_40101040),np.max(EigenValImL0g000_40101050)], 1)[[1]]

########################################################################

dataL0g000_450011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK001/N010/HamVals.txt')

MomentumAxL0g000_450011010 = dataL0g000_450011010[:,][:,5*0+0]
KineticEneL0g000_450011010 = dataL0g000_450011010[:,][:,5*0+1]
SelfEnergyL0g000_450011010 = dataL0g000_450011010[:,][:,5*0+2]
EigenValReL0g000_450011010 = dataL0g000_450011010[:,][:,5*0+3]
EigenValImL0g000_450011010 = dataL0g000_450011010[:,][:,5*0+4]

dataL0g000_450011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK001/N020/HamVals.txt')

MomentumAxL0g000_450011020 = dataL0g000_450011020[:,][:,5*0+0]
KineticEneL0g000_450011020 = dataL0g000_450011020[:,][:,5*0+1]
SelfEnergyL0g000_450011020 = dataL0g000_450011020[:,][:,5*0+2]
EigenValReL0g000_450011020 = dataL0g000_450011020[:,][:,5*0+3]
EigenValImL0g000_450011020 = dataL0g000_450011020[:,][:,5*0+4]

dataL0g000_450011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK001/N030/HamVals.txt')

MomentumAxL0g000_450011030 = dataL0g000_450011030[:,][:,5*0+0]
KineticEneL0g000_450011030 = dataL0g000_450011030[:,][:,5*0+1]
SelfEnergyL0g000_450011030 = dataL0g000_450011030[:,][:,5*0+2]
EigenValReL0g000_450011030 = dataL0g000_450011030[:,][:,5*0+3]
EigenValImL0g000_450011030 = dataL0g000_450011030[:,][:,5*0+4]

dataL0g000_450011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK001/N040/HamVals.txt')

MomentumAxL0g000_450011040 = dataL0g000_450011040[:,][:,5*0+0]
KineticEneL0g000_450011040 = dataL0g000_450011040[:,][:,5*0+1]
SelfEnergyL0g000_450011040 = dataL0g000_450011040[:,][:,5*0+2]
EigenValReL0g000_450011040 = dataL0g000_450011040[:,][:,5*0+3]
EigenValImL0g000_450011040 = dataL0g000_450011040[:,][:,5*0+4]

dataL0g000_450011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK001/N050/HamVals.txt')

MomentumAxL0g000_450011050 = dataL0g000_450011050[:,][:,5*0+0]
KineticEneL0g000_450011050 = dataL0g000_450011050[:,][:,5*0+1]
SelfEnergyL0g000_450011050 = dataL0g000_450011050[:,][:,5*0+2]
EigenValReL0g000_450011050 = dataL0g000_450011050[:,][:,5*0+3]
EigenValImL0g000_450011050 = dataL0g000_450011050[:,][:,5*0+4]

dataL0g000_450021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK002/N010/HamVals.txt')

MomentumAxL0g000_450021010 = dataL0g000_450021010[:,][:,5*0+0]
KineticEneL0g000_450021010 = dataL0g000_450021010[:,][:,5*0+1]
SelfEnergyL0g000_450021010 = dataL0g000_450021010[:,][:,5*0+2]
EigenValReL0g000_450021010 = dataL0g000_450021010[:,][:,5*0+3]
EigenValImL0g000_450021010 = dataL0g000_450021010[:,][:,5*0+4]

dataL0g000_450021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK002/N020/HamVals.txt')

MomentumAxL0g000_450021020 = dataL0g000_450021020[:,][:,5*0+0]
KineticEneL0g000_450021020 = dataL0g000_450021020[:,][:,5*0+1]
SelfEnergyL0g000_450021020 = dataL0g000_450021020[:,][:,5*0+2]
EigenValReL0g000_450021020 = dataL0g000_450021020[:,][:,5*0+3]
EigenValImL0g000_450021020 = dataL0g000_450021020[:,][:,5*0+4]

dataL0g000_450021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK002/N030/HamVals.txt')

MomentumAxL0g000_450021030 = dataL0g000_450021030[:,][:,5*0+0]
KineticEneL0g000_450021030 = dataL0g000_450021030[:,][:,5*0+1]
SelfEnergyL0g000_450021030 = dataL0g000_450021030[:,][:,5*0+2]
EigenValReL0g000_450021030 = dataL0g000_450021030[:,][:,5*0+3]
EigenValImL0g000_450021030 = dataL0g000_450021030[:,][:,5*0+4]

dataL0g000_450021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK002/N040/HamVals.txt')

MomentumAxL0g000_450021040 = dataL0g000_450021040[:,][:,5*0+0]
KineticEneL0g000_450021040 = dataL0g000_450021040[:,][:,5*0+1]
SelfEnergyL0g000_450021040 = dataL0g000_450021040[:,][:,5*0+2]
EigenValReL0g000_450021040 = dataL0g000_450021040[:,][:,5*0+3]
EigenValImL0g000_450021040 = dataL0g000_450021040[:,][:,5*0+4]

dataL0g000_450021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK002/N050/HamVals.txt')

MomentumAxL0g000_450021050 = dataL0g000_450021050[:,][:,5*0+0]
KineticEneL0g000_450021050 = dataL0g000_450021050[:,][:,5*0+1]
SelfEnergyL0g000_450021050 = dataL0g000_450021050[:,][:,5*0+2]
EigenValReL0g000_450021050 = dataL0g000_450021050[:,][:,5*0+3]
EigenValImL0g000_450021050 = dataL0g000_450021050[:,][:,5*0+4]

dataL0g000_450031010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK003/N010/HamVals.txt')

MomentumAxL0g000_450031010 = dataL0g000_450031010[:,][:,5*0+0]
KineticEneL0g000_450031010 = dataL0g000_450031010[:,][:,5*0+1]
SelfEnergyL0g000_450031010 = dataL0g000_450031010[:,][:,5*0+2]
EigenValReL0g000_450031010 = dataL0g000_450031010[:,][:,5*0+3]
EigenValImL0g000_450031010 = dataL0g000_450031010[:,][:,5*0+4]

dataL0g000_450031020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK003/N020/HamVals.txt')

MomentumAxL0g000_450031020 = dataL0g000_450031020[:,][:,5*0+0]
KineticEneL0g000_450031020 = dataL0g000_450031020[:,][:,5*0+1]
SelfEnergyL0g000_450031020 = dataL0g000_450031020[:,][:,5*0+2]
EigenValReL0g000_450031020 = dataL0g000_450031020[:,][:,5*0+3]
EigenValImL0g000_450031020 = dataL0g000_450031020[:,][:,5*0+4]

dataL0g000_450031030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK003/N030/HamVals.txt')

MomentumAxL0g000_450031030 = dataL0g000_450031030[:,][:,5*0+0]
KineticEneL0g000_450031030 = dataL0g000_450031030[:,][:,5*0+1]
SelfEnergyL0g000_450031030 = dataL0g000_450031030[:,][:,5*0+2]
EigenValReL0g000_450031030 = dataL0g000_450031030[:,][:,5*0+3]
EigenValImL0g000_450031030 = dataL0g000_450031030[:,][:,5*0+4]

dataL0g000_450031040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK003/N040/HamVals.txt')

MomentumAxL0g000_450031040 = dataL0g000_450031040[:,][:,5*0+0]
KineticEneL0g000_450031040 = dataL0g000_450031040[:,][:,5*0+1]
SelfEnergyL0g000_450031040 = dataL0g000_450031040[:,][:,5*0+2]
EigenValReL0g000_450031040 = dataL0g000_450031040[:,][:,5*0+3]
EigenValImL0g000_450031040 = dataL0g000_450031040[:,][:,5*0+4]

dataL0g000_450031050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK003/N050/HamVals.txt')

MomentumAxL0g000_450031050 = dataL0g000_450031050[:,][:,5*0+0]
KineticEneL0g000_450031050 = dataL0g000_450031050[:,][:,5*0+1]
SelfEnergyL0g000_450031050 = dataL0g000_450031050[:,][:,5*0+2]
EigenValReL0g000_450031050 = dataL0g000_450031050[:,][:,5*0+3]
EigenValImL0g000_450031050 = dataL0g000_450031050[:,][:,5*0+4]

dataL0g000_450051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK005/N010/HamVals.txt')

MomentumAxL0g000_450051010 = dataL0g000_450051010[:,][:,5*0+0]
KineticEneL0g000_450051010 = dataL0g000_450051010[:,][:,5*0+1]
SelfEnergyL0g000_450051010 = dataL0g000_450051010[:,][:,5*0+2]
EigenValReL0g000_450051010 = dataL0g000_450051010[:,][:,5*0+3]
EigenValImL0g000_450051010 = dataL0g000_450051010[:,][:,5*0+4]

dataL0g000_450051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK005/N020/HamVals.txt')

MomentumAxL0g000_450051020 = dataL0g000_450051020[:,][:,5*0+0]
KineticEneL0g000_450051020 = dataL0g000_450051020[:,][:,5*0+1]
SelfEnergyL0g000_450051020 = dataL0g000_450051020[:,][:,5*0+2]
EigenValReL0g000_450051020 = dataL0g000_450051020[:,][:,5*0+3]
EigenValImL0g000_450051020 = dataL0g000_450051020[:,][:,5*0+4]

dataL0g000_450051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK005/N030/HamVals.txt')

MomentumAxL0g000_450051030 = dataL0g000_450051030[:,][:,5*0+0]
KineticEneL0g000_450051030 = dataL0g000_450051030[:,][:,5*0+1]
SelfEnergyL0g000_450051030 = dataL0g000_450051030[:,][:,5*0+2]
EigenValReL0g000_450051030 = dataL0g000_450051030[:,][:,5*0+3]
EigenValImL0g000_450051030 = dataL0g000_450051030[:,][:,5*0+4]

dataL0g000_450051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK005/N040/HamVals.txt')

MomentumAxL0g000_450051040 = dataL0g000_450051040[:,][:,5*0+0]
KineticEneL0g000_450051040 = dataL0g000_450051040[:,][:,5*0+1]
SelfEnergyL0g000_450051040 = dataL0g000_450051040[:,][:,5*0+2]
EigenValReL0g000_450051040 = dataL0g000_450051040[:,][:,5*0+3]
EigenValImL0g000_450051040 = dataL0g000_450051040[:,][:,5*0+4]

dataL0g000_450051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK005/N050/HamVals.txt')

MomentumAxL0g000_450051050 = dataL0g000_450051050[:,][:,5*0+0]
KineticEneL0g000_450051050 = dataL0g000_450051050[:,][:,5*0+1]
SelfEnergyL0g000_450051050 = dataL0g000_450051050[:,][:,5*0+2]
EigenValReL0g000_450051050 = dataL0g000_450051050[:,][:,5*0+3]
EigenValImL0g000_450051050 = dataL0g000_450051050[:,][:,5*0+4]

dataL0g000_450071010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK007/N010/HamVals.txt')

MomentumAxL0g000_450071010 = dataL0g000_450071010[:,][:,5*0+0]
KineticEneL0g000_450071010 = dataL0g000_450071010[:,][:,5*0+1]
SelfEnergyL0g000_450071010 = dataL0g000_450071010[:,][:,5*0+2]
EigenValReL0g000_450071010 = dataL0g000_450071010[:,][:,5*0+3]
EigenValImL0g000_450071010 = dataL0g000_450071010[:,][:,5*0+4]

dataL0g000_450071020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK007/N020/HamVals.txt')

MomentumAxL0g000_450071020 = dataL0g000_450071020[:,][:,5*0+0]
KineticEneL0g000_450071020 = dataL0g000_450071020[:,][:,5*0+1]
SelfEnergyL0g000_450071020 = dataL0g000_450071020[:,][:,5*0+2]
EigenValReL0g000_450071020 = dataL0g000_450071020[:,][:,5*0+3]
EigenValImL0g000_450071020 = dataL0g000_450071020[:,][:,5*0+4]

dataL0g000_450071030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK007/N030/HamVals.txt')

MomentumAxL0g000_450071030 = dataL0g000_450071030[:,][:,5*0+0]
KineticEneL0g000_450071030 = dataL0g000_450071030[:,][:,5*0+1]
SelfEnergyL0g000_450071030 = dataL0g000_450071030[:,][:,5*0+2]
EigenValReL0g000_450071030 = dataL0g000_450071030[:,][:,5*0+3]
EigenValImL0g000_450071030 = dataL0g000_450071030[:,][:,5*0+4]

dataL0g000_450071040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK007/N040/HamVals.txt')

MomentumAxL0g000_450071040 = dataL0g000_450071040[:,][:,5*0+0]
KineticEneL0g000_450071040 = dataL0g000_450071040[:,][:,5*0+1]
SelfEnergyL0g000_450071040 = dataL0g000_450071040[:,][:,5*0+2]
EigenValReL0g000_450071040 = dataL0g000_450071040[:,][:,5*0+3]
EigenValImL0g000_450071040 = dataL0g000_450071040[:,][:,5*0+4]

dataL0g000_450071050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK007/N050/HamVals.txt')

MomentumAxL0g000_450071050 = dataL0g000_450071050[:,][:,5*0+0]
KineticEneL0g000_450071050 = dataL0g000_450071050[:,][:,5*0+1]
SelfEnergyL0g000_450071050 = dataL0g000_450071050[:,][:,5*0+2]
EigenValReL0g000_450071050 = dataL0g000_450071050[:,][:,5*0+3]
EigenValImL0g000_450071050 = dataL0g000_450071050[:,][:,5*0+4]

dataL0g000_450101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK010/N010/HamVals.txt')

MomentumAxL0g000_450101010 = dataL0g000_450101010[:,][:,5*0+0]
KineticEneL0g000_450101010 = dataL0g000_450101010[:,][:,5*0+1]
SelfEnergyL0g000_450101010 = dataL0g000_450101010[:,][:,5*0+2]
EigenValReL0g000_450101010 = dataL0g000_450101010[:,][:,5*0+3]
EigenValImL0g000_450101010 = dataL0g000_450101010[:,][:,5*0+4]

dataL0g000_450101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK010/N020/HamVals.txt')

MomentumAxL0g000_450101020 = dataL0g000_450101020[:,][:,5*0+0]
KineticEneL0g000_450101020 = dataL0g000_450101020[:,][:,5*0+1]
SelfEnergyL0g000_450101020 = dataL0g000_450101020[:,][:,5*0+2]
EigenValReL0g000_450101020 = dataL0g000_450101020[:,][:,5*0+3]
EigenValImL0g000_450101020 = dataL0g000_450101020[:,][:,5*0+4]

dataL0g000_450101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK010/N030/HamVals.txt')

MomentumAxL0g000_450101030 = dataL0g000_450101030[:,][:,5*0+0]
KineticEneL0g000_450101030 = dataL0g000_450101030[:,][:,5*0+1]
SelfEnergyL0g000_450101030 = dataL0g000_450101030[:,][:,5*0+2]
EigenValReL0g000_450101030 = dataL0g000_450101030[:,][:,5*0+3]
EigenValImL0g000_450101030 = dataL0g000_450101030[:,][:,5*0+4]

dataL0g000_450101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK010/N040/HamVals.txt')

MomentumAxL0g000_450101040 = dataL0g000_450101040[:,][:,5*0+0]
KineticEneL0g000_450101040 = dataL0g000_450101040[:,][:,5*0+1]
SelfEnergyL0g000_450101040 = dataL0g000_450101040[:,][:,5*0+2]
EigenValReL0g000_450101040 = dataL0g000_450101040[:,][:,5*0+3]
EigenValImL0g000_450101040 = dataL0g000_450101040[:,][:,5*0+4]

dataL0g000_450101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-45/aK010/N050/HamVals.txt')

MomentumAxL0g000_450101050 = dataL0g000_450101050[:,][:,5*0+0]
KineticEneL0g000_450101050 = dataL0g000_450101050[:,][:,5*0+1]
SelfEnergyL0g000_450101050 = dataL0g000_450101050[:,][:,5*0+2]
EigenValReL0g000_450101050 = dataL0g000_450101050[:,][:,5*0+3]
EigenValImL0g000_450101050 = dataL0g000_450101050[:,][:,5*0+4]

MaxEigenValImL0g000_451Inf = np.zeros((6))

MaxEigenValImL0g000_451Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_450011010),np.max(EigenValImL0g000_450011020),np.max(EigenValImL0g000_450011030),np.max(EigenValImL0g000_450011040),np.max(EigenValImL0g000_450011050)], 1)[[1]]
MaxEigenValImL0g000_451Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_450021010),np.max(EigenValImL0g000_450021020),np.max(EigenValImL0g000_450021030),np.max(EigenValImL0g000_450021040),np.max(EigenValImL0g000_450021050)], 1)[[1]]
MaxEigenValImL0g000_451Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_450031010),np.max(EigenValImL0g000_450031020),np.max(EigenValImL0g000_450031030),np.max(EigenValImL0g000_450031040),np.max(EigenValImL0g000_450031050)], 1)[[1]]
MaxEigenValImL0g000_451Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_450051010),np.max(EigenValImL0g000_450051020),np.max(EigenValImL0g000_450051030),np.max(EigenValImL0g000_450051040),np.max(EigenValImL0g000_450051050)], 1)[[1]]
MaxEigenValImL0g000_451Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_450071010),np.max(EigenValImL0g000_450071020),np.max(EigenValImL0g000_450071030),np.max(EigenValImL0g000_450071040),np.max(EigenValImL0g000_450071050)], 1)[[1]]
MaxEigenValImL0g000_451Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_450101010),np.max(EigenValImL0g000_450101020),np.max(EigenValImL0g000_450101030),np.max(EigenValImL0g000_450101040),np.max(EigenValImL0g000_450101050)], 1)[[1]]

########################################################################

dataL0g000_50011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK001/N010/HamVals.txt')

MomentumAxL0g000_50011010 = dataL0g000_50011010[:,][:,5*0+0]
KineticEneL0g000_50011010 = dataL0g000_50011010[:,][:,5*0+1]
SelfEnergyL0g000_50011010 = dataL0g000_50011010[:,][:,5*0+2]
EigenValReL0g000_50011010 = dataL0g000_50011010[:,][:,5*0+3]
EigenValImL0g000_50011010 = dataL0g000_50011010[:,][:,5*0+4]

dataL0g000_50011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK001/N020/HamVals.txt')

MomentumAxL0g000_50011020 = dataL0g000_50011020[:,][:,5*0+0]
KineticEneL0g000_50011020 = dataL0g000_50011020[:,][:,5*0+1]
SelfEnergyL0g000_50011020 = dataL0g000_50011020[:,][:,5*0+2]
EigenValReL0g000_50011020 = dataL0g000_50011020[:,][:,5*0+3]
EigenValImL0g000_50011020 = dataL0g000_50011020[:,][:,5*0+4]

dataL0g000_50011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK001/N030/HamVals.txt')

MomentumAxL0g000_50011030 = dataL0g000_50011030[:,][:,5*0+0]
KineticEneL0g000_50011030 = dataL0g000_50011030[:,][:,5*0+1]
SelfEnergyL0g000_50011030 = dataL0g000_50011030[:,][:,5*0+2]
EigenValReL0g000_50011030 = dataL0g000_50011030[:,][:,5*0+3]
EigenValImL0g000_50011030 = dataL0g000_50011030[:,][:,5*0+4]

dataL0g000_50011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK001/N040/HamVals.txt')

MomentumAxL0g000_50011040 = dataL0g000_50011040[:,][:,5*0+0]
KineticEneL0g000_50011040 = dataL0g000_50011040[:,][:,5*0+1]
SelfEnergyL0g000_50011040 = dataL0g000_50011040[:,][:,5*0+2]
EigenValReL0g000_50011040 = dataL0g000_50011040[:,][:,5*0+3]
EigenValImL0g000_50011040 = dataL0g000_50011040[:,][:,5*0+4]

dataL0g000_50011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK001/N050/HamVals.txt')

MomentumAxL0g000_50011050 = dataL0g000_50011050[:,][:,5*0+0]
KineticEneL0g000_50011050 = dataL0g000_50011050[:,][:,5*0+1]
SelfEnergyL0g000_50011050 = dataL0g000_50011050[:,][:,5*0+2]
EigenValReL0g000_50011050 = dataL0g000_50011050[:,][:,5*0+3]
EigenValImL0g000_50011050 = dataL0g000_50011050[:,][:,5*0+4]

dataL0g000_50021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK002/N010/HamVals.txt')

MomentumAxL0g000_50021010 = dataL0g000_50021010[:,][:,5*0+0]
KineticEneL0g000_50021010 = dataL0g000_50021010[:,][:,5*0+1]
SelfEnergyL0g000_50021010 = dataL0g000_50021010[:,][:,5*0+2]
EigenValReL0g000_50021010 = dataL0g000_50021010[:,][:,5*0+3]
EigenValImL0g000_50021010 = dataL0g000_50021010[:,][:,5*0+4]

dataL0g000_50021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK002/N020/HamVals.txt')

MomentumAxL0g000_50021020 = dataL0g000_50021020[:,][:,5*0+0]
KineticEneL0g000_50021020 = dataL0g000_50021020[:,][:,5*0+1]
SelfEnergyL0g000_50021020 = dataL0g000_50021020[:,][:,5*0+2]
EigenValReL0g000_50021020 = dataL0g000_50021020[:,][:,5*0+3]
EigenValImL0g000_50021020 = dataL0g000_50021020[:,][:,5*0+4]

dataL0g000_50021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK002/N030/HamVals.txt')

MomentumAxL0g000_50021030 = dataL0g000_50021030[:,][:,5*0+0]
KineticEneL0g000_50021030 = dataL0g000_50021030[:,][:,5*0+1]
SelfEnergyL0g000_50021030 = dataL0g000_50021030[:,][:,5*0+2]
EigenValReL0g000_50021030 = dataL0g000_50021030[:,][:,5*0+3]
EigenValImL0g000_50021030 = dataL0g000_50021030[:,][:,5*0+4]

dataL0g000_50021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK002/N040/HamVals.txt')

MomentumAxL0g000_50021040 = dataL0g000_50021040[:,][:,5*0+0]
KineticEneL0g000_50021040 = dataL0g000_50021040[:,][:,5*0+1]
SelfEnergyL0g000_50021040 = dataL0g000_50021040[:,][:,5*0+2]
EigenValReL0g000_50021040 = dataL0g000_50021040[:,][:,5*0+3]
EigenValImL0g000_50021040 = dataL0g000_50021040[:,][:,5*0+4]

dataL0g000_50021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK002/N050/HamVals.txt')

MomentumAxL0g000_50021050 = dataL0g000_50021050[:,][:,5*0+0]
KineticEneL0g000_50021050 = dataL0g000_50021050[:,][:,5*0+1]
SelfEnergyL0g000_50021050 = dataL0g000_50021050[:,][:,5*0+2]
EigenValReL0g000_50021050 = dataL0g000_50021050[:,][:,5*0+3]
EigenValImL0g000_50021050 = dataL0g000_50021050[:,][:,5*0+4]

dataL0g000_50051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK005/N010/HamVals.txt')

MomentumAxL0g000_50051010 = dataL0g000_50051010[:,][:,5*0+0]
KineticEneL0g000_50051010 = dataL0g000_50051010[:,][:,5*0+1]
SelfEnergyL0g000_50051010 = dataL0g000_50051010[:,][:,5*0+2]
EigenValReL0g000_50051010 = dataL0g000_50051010[:,][:,5*0+3]
EigenValImL0g000_50051010 = dataL0g000_50051010[:,][:,5*0+4]

dataL0g000_50051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK005/N020/HamVals.txt')

MomentumAxL0g000_50051020 = dataL0g000_50051020[:,][:,5*0+0]
KineticEneL0g000_50051020 = dataL0g000_50051020[:,][:,5*0+1]
SelfEnergyL0g000_50051020 = dataL0g000_50051020[:,][:,5*0+2]
EigenValReL0g000_50051020 = dataL0g000_50051020[:,][:,5*0+3]
EigenValImL0g000_50051020 = dataL0g000_50051020[:,][:,5*0+4]

dataL0g000_50051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK005/N030/HamVals.txt')

MomentumAxL0g000_50051030 = dataL0g000_50051030[:,][:,5*0+0]
KineticEneL0g000_50051030 = dataL0g000_50051030[:,][:,5*0+1]
SelfEnergyL0g000_50051030 = dataL0g000_50051030[:,][:,5*0+2]
EigenValReL0g000_50051030 = dataL0g000_50051030[:,][:,5*0+3]
EigenValImL0g000_50051030 = dataL0g000_50051030[:,][:,5*0+4]

dataL0g000_50051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK005/N040/HamVals.txt')

MomentumAxL0g000_50051040 = dataL0g000_50051040[:,][:,5*0+0]
KineticEneL0g000_50051040 = dataL0g000_50051040[:,][:,5*0+1]
SelfEnergyL0g000_50051040 = dataL0g000_50051040[:,][:,5*0+2]
EigenValReL0g000_50051040 = dataL0g000_50051040[:,][:,5*0+3]
EigenValImL0g000_50051040 = dataL0g000_50051040[:,][:,5*0+4]

dataL0g000_50051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK005/N050/HamVals.txt')

MomentumAxL0g000_50051050 = dataL0g000_50051050[:,][:,5*0+0]
KineticEneL0g000_50051050 = dataL0g000_50051050[:,][:,5*0+1]
SelfEnergyL0g000_50051050 = dataL0g000_50051050[:,][:,5*0+2]
EigenValReL0g000_50051050 = dataL0g000_50051050[:,][:,5*0+3]
EigenValImL0g000_50051050 = dataL0g000_50051050[:,][:,5*0+4]

dataL0g000_50101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK010/N010/HamVals.txt')

MomentumAxL0g000_50101010 = dataL0g000_50101010[:,][:,5*0+0]
KineticEneL0g000_50101010 = dataL0g000_50101010[:,][:,5*0+1]
SelfEnergyL0g000_50101010 = dataL0g000_50101010[:,][:,5*0+2]
EigenValReL0g000_50101010 = dataL0g000_50101010[:,][:,5*0+3]
EigenValImL0g000_50101010 = dataL0g000_50101010[:,][:,5*0+4]

dataL0g000_50101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK010/N020/HamVals.txt')

MomentumAxL0g000_50101020 = dataL0g000_50101020[:,][:,5*0+0]
KineticEneL0g000_50101020 = dataL0g000_50101020[:,][:,5*0+1]
SelfEnergyL0g000_50101020 = dataL0g000_50101020[:,][:,5*0+2]
EigenValReL0g000_50101020 = dataL0g000_50101020[:,][:,5*0+3]
EigenValImL0g000_50101020 = dataL0g000_50101020[:,][:,5*0+4]

dataL0g000_50101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK010/N030/HamVals.txt')

MomentumAxL0g000_50101030 = dataL0g000_50101030[:,][:,5*0+0]
KineticEneL0g000_50101030 = dataL0g000_50101030[:,][:,5*0+1]
SelfEnergyL0g000_50101030 = dataL0g000_50101030[:,][:,5*0+2]
EigenValReL0g000_50101030 = dataL0g000_50101030[:,][:,5*0+3]
EigenValImL0g000_50101030 = dataL0g000_50101030[:,][:,5*0+4]

dataL0g000_50101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK010/N040/HamVals.txt')

MomentumAxL0g000_50101040 = dataL0g000_50101040[:,][:,5*0+0]
KineticEneL0g000_50101040 = dataL0g000_50101040[:,][:,5*0+1]
SelfEnergyL0g000_50101040 = dataL0g000_50101040[:,][:,5*0+2]
EigenValReL0g000_50101040 = dataL0g000_50101040[:,][:,5*0+3]
EigenValImL0g000_50101040 = dataL0g000_50101040[:,][:,5*0+4]

dataL0g000_50101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK010/N050/HamVals.txt')

MomentumAxL0g000_50101050 = dataL0g000_50101050[:,][:,5*0+0]
KineticEneL0g000_50101050 = dataL0g000_50101050[:,][:,5*0+1]
SelfEnergyL0g000_50101050 = dataL0g000_50101050[:,][:,5*0+2]
EigenValReL0g000_50101050 = dataL0g000_50101050[:,][:,5*0+3]
EigenValImL0g000_50101050 = dataL0g000_50101050[:,][:,5*0+4]

dataL0g000_50031010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK003/N010/HamVals.txt')

MomentumAxL0g000_50031010 = dataL0g000_50031010[:,][:,5*0+0]
KineticEneL0g000_50031010 = dataL0g000_50031010[:,][:,5*0+1]
SelfEnergyL0g000_50031010 = dataL0g000_50031010[:,][:,5*0+2]
EigenValReL0g000_50031010 = dataL0g000_50031010[:,][:,5*0+3]
EigenValImL0g000_50031010 = dataL0g000_50031010[:,][:,5*0+4]

dataL0g000_50031020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK003/N020/HamVals.txt')

MomentumAxL0g000_50031020 = dataL0g000_50031020[:,][:,5*0+0]
KineticEneL0g000_50031020 = dataL0g000_50031020[:,][:,5*0+1]
SelfEnergyL0g000_50031020 = dataL0g000_50031020[:,][:,5*0+2]
EigenValReL0g000_50031020 = dataL0g000_50031020[:,][:,5*0+3]
EigenValImL0g000_50031020 = dataL0g000_50031020[:,][:,5*0+4]

dataL0g000_50031030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK003/N030/HamVals.txt')

MomentumAxL0g000_50031030 = dataL0g000_50031030[:,][:,5*0+0]
KineticEneL0g000_50031030 = dataL0g000_50031030[:,][:,5*0+1]
SelfEnergyL0g000_50031030 = dataL0g000_50031030[:,][:,5*0+2]
EigenValReL0g000_50031030 = dataL0g000_50031030[:,][:,5*0+3]
EigenValImL0g000_50031030 = dataL0g000_50031030[:,][:,5*0+4]

dataL0g000_50031040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK003/N040/HamVals.txt')

MomentumAxL0g000_50031040 = dataL0g000_50031040[:,][:,5*0+0]
KineticEneL0g000_50031040 = dataL0g000_50031040[:,][:,5*0+1]
SelfEnergyL0g000_50031040 = dataL0g000_50031040[:,][:,5*0+2]
EigenValReL0g000_50031040 = dataL0g000_50031040[:,][:,5*0+3]
EigenValImL0g000_50031040 = dataL0g000_50031040[:,][:,5*0+4]

dataL0g000_50031050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK003/N050/HamVals.txt')

MomentumAxL0g000_50031050 = dataL0g000_50031050[:,][:,5*0+0]
KineticEneL0g000_50031050 = dataL0g000_50031050[:,][:,5*0+1]
SelfEnergyL0g000_50031050 = dataL0g000_50031050[:,][:,5*0+2]
EigenValReL0g000_50031050 = dataL0g000_50031050[:,][:,5*0+3]
EigenValImL0g000_50031050 = dataL0g000_50031050[:,][:,5*0+4]

dataL0g000_50071010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK007/N010/HamVals.txt')

MomentumAxL0g000_50071010 = dataL0g000_50071010[:,][:,5*0+0]
KineticEneL0g000_50071010 = dataL0g000_50071010[:,][:,5*0+1]
SelfEnergyL0g000_50071010 = dataL0g000_50071010[:,][:,5*0+2]
EigenValReL0g000_50071010 = dataL0g000_50071010[:,][:,5*0+3]
EigenValImL0g000_50071010 = dataL0g000_50071010[:,][:,5*0+4]

dataL0g000_50071020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK007/N020/HamVals.txt')

MomentumAxL0g000_50071020 = dataL0g000_50071020[:,][:,5*0+0]
KineticEneL0g000_50071020 = dataL0g000_50071020[:,][:,5*0+1]
SelfEnergyL0g000_50071020 = dataL0g000_50071020[:,][:,5*0+2]
EigenValReL0g000_50071020 = dataL0g000_50071020[:,][:,5*0+3]
EigenValImL0g000_50071020 = dataL0g000_50071020[:,][:,5*0+4]

dataL0g000_50071030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK007/N030/HamVals.txt')

MomentumAxL0g000_50071030 = dataL0g000_50071030[:,][:,5*0+0]
KineticEneL0g000_50071030 = dataL0g000_50071030[:,][:,5*0+1]
SelfEnergyL0g000_50071030 = dataL0g000_50071030[:,][:,5*0+2]
EigenValReL0g000_50071030 = dataL0g000_50071030[:,][:,5*0+3]
EigenValImL0g000_50071030 = dataL0g000_50071030[:,][:,5*0+4]

dataL0g000_50071040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK007/N040/HamVals.txt')

MomentumAxL0g000_50071040 = dataL0g000_50071040[:,][:,5*0+0]
KineticEneL0g000_50071040 = dataL0g000_50071040[:,][:,5*0+1]
SelfEnergyL0g000_50071040 = dataL0g000_50071040[:,][:,5*0+2]
EigenValReL0g000_50071040 = dataL0g000_50071040[:,][:,5*0+3]
EigenValImL0g000_50071040 = dataL0g000_50071040[:,][:,5*0+4]

dataL0g000_50071050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK007/N050/HamVals.txt')

MomentumAxL0g000_50071050 = dataL0g000_50071050[:,][:,5*0+0]
KineticEneL0g000_50071050 = dataL0g000_50071050[:,][:,5*0+1]
SelfEnergyL0g000_50071050 = dataL0g000_50071050[:,][:,5*0+2]
EigenValReL0g000_50071050 = dataL0g000_50071050[:,][:,5*0+3]
EigenValImL0g000_50071050 = dataL0g000_50071050[:,][:,5*0+4]

MaxEigenValImL0g000_51Inf = np.zeros((6))

MaxEigenValImL0g000_51Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_50011010),np.max(EigenValImL0g000_50011020),np.max(EigenValImL0g000_50011030),np.max(EigenValImL0g000_50011040),np.max(EigenValImL0g000_50011050)], 1)[[1]]
MaxEigenValImL0g000_51Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_50021010),np.max(EigenValImL0g000_50021020),np.max(EigenValImL0g000_50021030),np.max(EigenValImL0g000_50021040),np.max(EigenValImL0g000_50021050)], 1)[[1]]
MaxEigenValImL0g000_51Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_50031010),np.max(EigenValImL0g000_50031020),np.max(EigenValImL0g000_50031030),np.max(EigenValImL0g000_50031040),np.max(EigenValImL0g000_50031050)], 1)[[1]]
MaxEigenValImL0g000_51Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_50051010),np.max(EigenValImL0g000_50051020),np.max(EigenValImL0g000_50051030),np.max(EigenValImL0g000_50051040),np.max(EigenValImL0g000_50051050)], 1)[[1]]
MaxEigenValImL0g000_51Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_50071010),np.max(EigenValImL0g000_50071020),np.max(EigenValImL0g000_50071030),np.max(EigenValImL0g000_50071040),np.max(EigenValImL0g000_50071050)], 1)[[1]]
MaxEigenValImL0g000_51Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL0g000_50101010),np.max(EigenValImL0g000_50101020),np.max(EigenValImL0g000_50101030),np.max(EigenValImL0g000_50101040),np.max(EigenValImL0g000_50101050)], 1)[[1]]

########################################################################

dataL0g0010011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK001/N010/HamVals.txt')

MomentumAxL0g0010011010 = dataL0g0010011010[:,][:,5*0+0]
KineticEneL0g0010011010 = dataL0g0010011010[:,][:,5*0+1]
SelfEnergyL0g0010011010 = dataL0g0010011010[:,][:,5*0+2]
EigenValReL0g0010011010 = dataL0g0010011010[:,][:,5*0+3]
EigenValImL0g0010011010 = dataL0g0010011010[:,][:,5*0+4]

dataL0g0010011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK001/N020/HamVals.txt')

MomentumAxL0g0010011020 = dataL0g0010011020[:,][:,5*0+0]
KineticEneL0g0010011020 = dataL0g0010011020[:,][:,5*0+1]
SelfEnergyL0g0010011020 = dataL0g0010011020[:,][:,5*0+2]
EigenValReL0g0010011020 = dataL0g0010011020[:,][:,5*0+3]
EigenValImL0g0010011020 = dataL0g0010011020[:,][:,5*0+4]

dataL0g0010011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK001/N030/HamVals.txt')

MomentumAxL0g0010011030 = dataL0g0010011030[:,][:,5*0+0]
KineticEneL0g0010011030 = dataL0g0010011030[:,][:,5*0+1]
SelfEnergyL0g0010011030 = dataL0g0010011030[:,][:,5*0+2]
EigenValReL0g0010011030 = dataL0g0010011030[:,][:,5*0+3]
EigenValImL0g0010011030 = dataL0g0010011030[:,][:,5*0+4]

dataL0g0010011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK001/N040/HamVals.txt')

MomentumAxL0g0010011040 = dataL0g0010011040[:,][:,5*0+0]
KineticEneL0g0010011040 = dataL0g0010011040[:,][:,5*0+1]
SelfEnergyL0g0010011040 = dataL0g0010011040[:,][:,5*0+2]
EigenValReL0g0010011040 = dataL0g0010011040[:,][:,5*0+3]
EigenValImL0g0010011040 = dataL0g0010011040[:,][:,5*0+4]

dataL0g0010011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK001/N050/HamVals.txt')

MomentumAxL0g0010011050 = dataL0g0010011050[:,][:,5*0+0]
KineticEneL0g0010011050 = dataL0g0010011050[:,][:,5*0+1]
SelfEnergyL0g0010011050 = dataL0g0010011050[:,][:,5*0+2]
EigenValReL0g0010011050 = dataL0g0010011050[:,][:,5*0+3]
EigenValImL0g0010011050 = dataL0g0010011050[:,][:,5*0+4]

dataL0g0010021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK002/N010/HamVals.txt')

MomentumAxL0g0010021010 = dataL0g0010021010[:,][:,5*0+0]
KineticEneL0g0010021010 = dataL0g0010021010[:,][:,5*0+1]
SelfEnergyL0g0010021010 = dataL0g0010021010[:,][:,5*0+2]
EigenValReL0g0010021010 = dataL0g0010021010[:,][:,5*0+3]
EigenValImL0g0010021010 = dataL0g0010021010[:,][:,5*0+4]

dataL0g0010021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK002/N020/HamVals.txt')

MomentumAxL0g0010021020 = dataL0g0010021020[:,][:,5*0+0]
KineticEneL0g0010021020 = dataL0g0010021020[:,][:,5*0+1]
SelfEnergyL0g0010021020 = dataL0g0010021020[:,][:,5*0+2]
EigenValReL0g0010021020 = dataL0g0010021020[:,][:,5*0+3]
EigenValImL0g0010021020 = dataL0g0010021020[:,][:,5*0+4]

dataL0g0010021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK002/N030/HamVals.txt')

MomentumAxL0g0010021030 = dataL0g0010021030[:,][:,5*0+0]
KineticEneL0g0010021030 = dataL0g0010021030[:,][:,5*0+1]
SelfEnergyL0g0010021030 = dataL0g0010021030[:,][:,5*0+2]
EigenValReL0g0010021030 = dataL0g0010021030[:,][:,5*0+3]
EigenValImL0g0010021030 = dataL0g0010021030[:,][:,5*0+4]

dataL0g0010021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK002/N040/HamVals.txt')

MomentumAxL0g0010021040 = dataL0g0010021040[:,][:,5*0+0]
KineticEneL0g0010021040 = dataL0g0010021040[:,][:,5*0+1]
SelfEnergyL0g0010021040 = dataL0g0010021040[:,][:,5*0+2]
EigenValReL0g0010021040 = dataL0g0010021040[:,][:,5*0+3]
EigenValImL0g0010021040 = dataL0g0010021040[:,][:,5*0+4]

dataL0g0010021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK002/N050/HamVals.txt')

MomentumAxL0g0010021050 = dataL0g0010021050[:,][:,5*0+0]
KineticEneL0g0010021050 = dataL0g0010021050[:,][:,5*0+1]
SelfEnergyL0g0010021050 = dataL0g0010021050[:,][:,5*0+2]
EigenValReL0g0010021050 = dataL0g0010021050[:,][:,5*0+3]
EigenValImL0g0010021050 = dataL0g0010021050[:,][:,5*0+4]

dataL0g0010031010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK003/N010/HamVals.txt')

MomentumAxL0g0010031010 = dataL0g0010031010[:,][:,5*0+0]
KineticEneL0g0010031010 = dataL0g0010031010[:,][:,5*0+1]
SelfEnergyL0g0010031010 = dataL0g0010031010[:,][:,5*0+2]
EigenValReL0g0010031010 = dataL0g0010031010[:,][:,5*0+3]
EigenValImL0g0010031010 = dataL0g0010031010[:,][:,5*0+4]

dataL0g0010031020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK003/N020/HamVals.txt')

MomentumAxL0g0010031020 = dataL0g0010031020[:,][:,5*0+0]
KineticEneL0g0010031020 = dataL0g0010031020[:,][:,5*0+1]
SelfEnergyL0g0010031020 = dataL0g0010031020[:,][:,5*0+2]
EigenValReL0g0010031020 = dataL0g0010031020[:,][:,5*0+3]
EigenValImL0g0010031020 = dataL0g0010031020[:,][:,5*0+4]

dataL0g0010031030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK003/N030/HamVals.txt')

MomentumAxL0g0010031030 = dataL0g0010031030[:,][:,5*0+0]
KineticEneL0g0010031030 = dataL0g0010031030[:,][:,5*0+1]
SelfEnergyL0g0010031030 = dataL0g0010031030[:,][:,5*0+2]
EigenValReL0g0010031030 = dataL0g0010031030[:,][:,5*0+3]
EigenValImL0g0010031030 = dataL0g0010031030[:,][:,5*0+4]

dataL0g0010031040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK003/N040/HamVals.txt')

MomentumAxL0g0010031040 = dataL0g0010031040[:,][:,5*0+0]
KineticEneL0g0010031040 = dataL0g0010031040[:,][:,5*0+1]
SelfEnergyL0g0010031040 = dataL0g0010031040[:,][:,5*0+2]
EigenValReL0g0010031040 = dataL0g0010031040[:,][:,5*0+3]
EigenValImL0g0010031040 = dataL0g0010031040[:,][:,5*0+4]

dataL0g0010031050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK003/N050/HamVals.txt')

MomentumAxL0g0010031050 = dataL0g0010031050[:,][:,5*0+0]
KineticEneL0g0010031050 = dataL0g0010031050[:,][:,5*0+1]
SelfEnergyL0g0010031050 = dataL0g0010031050[:,][:,5*0+2]
EigenValReL0g0010031050 = dataL0g0010031050[:,][:,5*0+3]
EigenValImL0g0010031050 = dataL0g0010031050[:,][:,5*0+4]

dataL0g0010051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK005/N010/HamVals.txt')

MomentumAxL0g0010051010 = dataL0g0010051010[:,][:,5*0+0]
KineticEneL0g0010051010 = dataL0g0010051010[:,][:,5*0+1]
SelfEnergyL0g0010051010 = dataL0g0010051010[:,][:,5*0+2]
EigenValReL0g0010051010 = dataL0g0010051010[:,][:,5*0+3]
EigenValImL0g0010051010 = dataL0g0010051010[:,][:,5*0+4]

dataL0g0010051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK005/N020/HamVals.txt')

MomentumAxL0g0010051020 = dataL0g0010051020[:,][:,5*0+0]
KineticEneL0g0010051020 = dataL0g0010051020[:,][:,5*0+1]
SelfEnergyL0g0010051020 = dataL0g0010051020[:,][:,5*0+2]
EigenValReL0g0010051020 = dataL0g0010051020[:,][:,5*0+3]
EigenValImL0g0010051020 = dataL0g0010051020[:,][:,5*0+4]

dataL0g0010051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK005/N030/HamVals.txt')

MomentumAxL0g0010051030 = dataL0g0010051030[:,][:,5*0+0]
KineticEneL0g0010051030 = dataL0g0010051030[:,][:,5*0+1]
SelfEnergyL0g0010051030 = dataL0g0010051030[:,][:,5*0+2]
EigenValReL0g0010051030 = dataL0g0010051030[:,][:,5*0+3]
EigenValImL0g0010051030 = dataL0g0010051030[:,][:,5*0+4]

dataL0g0010051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK005/N040/HamVals.txt')

MomentumAxL0g0010051040 = dataL0g0010051040[:,][:,5*0+0]
KineticEneL0g0010051040 = dataL0g0010051040[:,][:,5*0+1]
SelfEnergyL0g0010051040 = dataL0g0010051040[:,][:,5*0+2]
EigenValReL0g0010051040 = dataL0g0010051040[:,][:,5*0+3]
EigenValImL0g0010051040 = dataL0g0010051040[:,][:,5*0+4]

dataL0g0010051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK005/N050/HamVals.txt')

MomentumAxL0g0010051050 = dataL0g0010051050[:,][:,5*0+0]
KineticEneL0g0010051050 = dataL0g0010051050[:,][:,5*0+1]
SelfEnergyL0g0010051050 = dataL0g0010051050[:,][:,5*0+2]
EigenValReL0g0010051050 = dataL0g0010051050[:,][:,5*0+3]
EigenValImL0g0010051050 = dataL0g0010051050[:,][:,5*0+4]

dataL0g0010071010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK007/N010/HamVals.txt')

MomentumAxL0g0010071010 = dataL0g0010071010[:,][:,5*0+0]
KineticEneL0g0010071010 = dataL0g0010071010[:,][:,5*0+1]
SelfEnergyL0g0010071010 = dataL0g0010071010[:,][:,5*0+2]
EigenValReL0g0010071010 = dataL0g0010071010[:,][:,5*0+3]
EigenValImL0g0010071010 = dataL0g0010071010[:,][:,5*0+4]

dataL0g0010071020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK007/N020/HamVals.txt')

MomentumAxL0g0010071020 = dataL0g0010071020[:,][:,5*0+0]
KineticEneL0g0010071020 = dataL0g0010071020[:,][:,5*0+1]
SelfEnergyL0g0010071020 = dataL0g0010071020[:,][:,5*0+2]
EigenValReL0g0010071020 = dataL0g0010071020[:,][:,5*0+3]
EigenValImL0g0010071020 = dataL0g0010071020[:,][:,5*0+4]

dataL0g0010071030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK007/N030/HamVals.txt')

MomentumAxL0g0010071030 = dataL0g0010071030[:,][:,5*0+0]
KineticEneL0g0010071030 = dataL0g0010071030[:,][:,5*0+1]
SelfEnergyL0g0010071030 = dataL0g0010071030[:,][:,5*0+2]
EigenValReL0g0010071030 = dataL0g0010071030[:,][:,5*0+3]
EigenValImL0g0010071030 = dataL0g0010071030[:,][:,5*0+4]

dataL0g0010071040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK007/N040/HamVals.txt')

MomentumAxL0g0010071040 = dataL0g0010071040[:,][:,5*0+0]
KineticEneL0g0010071040 = dataL0g0010071040[:,][:,5*0+1]
SelfEnergyL0g0010071040 = dataL0g0010071040[:,][:,5*0+2]
EigenValReL0g0010071040 = dataL0g0010071040[:,][:,5*0+3]
EigenValImL0g0010071040 = dataL0g0010071040[:,][:,5*0+4]

dataL0g0010071050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK007/N050/HamVals.txt')

MomentumAxL0g0010071050 = dataL0g0010071050[:,][:,5*0+0]
KineticEneL0g0010071050 = dataL0g0010071050[:,][:,5*0+1]
SelfEnergyL0g0010071050 = dataL0g0010071050[:,][:,5*0+2]
EigenValReL0g0010071050 = dataL0g0010071050[:,][:,5*0+3]
EigenValImL0g0010071050 = dataL0g0010071050[:,][:,5*0+4]

dataL0g0010101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK010/N010/HamVals.txt')

MomentumAxL0g0010101010 = dataL0g0010101010[:,][:,5*0+0]
KineticEneL0g0010101010 = dataL0g0010101010[:,][:,5*0+1]
SelfEnergyL0g0010101010 = dataL0g0010101010[:,][:,5*0+2]
EigenValReL0g0010101010 = dataL0g0010101010[:,][:,5*0+3]
EigenValImL0g0010101010 = dataL0g0010101010[:,][:,5*0+4]

dataL0g0010101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK010/N020/HamVals.txt')

MomentumAxL0g0010101020 = dataL0g0010101020[:,][:,5*0+0]
KineticEneL0g0010101020 = dataL0g0010101020[:,][:,5*0+1]
SelfEnergyL0g0010101020 = dataL0g0010101020[:,][:,5*0+2]
EigenValReL0g0010101020 = dataL0g0010101020[:,][:,5*0+3]
EigenValImL0g0010101020 = dataL0g0010101020[:,][:,5*0+4]

dataL0g0010101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK010/N030/HamVals.txt')

MomentumAxL0g0010101030 = dataL0g0010101030[:,][:,5*0+0]
KineticEneL0g0010101030 = dataL0g0010101030[:,][:,5*0+1]
SelfEnergyL0g0010101030 = dataL0g0010101030[:,][:,5*0+2]
EigenValReL0g0010101030 = dataL0g0010101030[:,][:,5*0+3]
EigenValImL0g0010101030 = dataL0g0010101030[:,][:,5*0+4]

dataL0g0010101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK010/N040/HamVals.txt')

MomentumAxL0g0010101040 = dataL0g0010101040[:,][:,5*0+0]
KineticEneL0g0010101040 = dataL0g0010101040[:,][:,5*0+1]
SelfEnergyL0g0010101040 = dataL0g0010101040[:,][:,5*0+2]
EigenValReL0g0010101040 = dataL0g0010101040[:,][:,5*0+3]
EigenValImL0g0010101040 = dataL0g0010101040[:,][:,5*0+4]

dataL0g0010101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK010/N050/HamVals.txt')

MomentumAxL0g0010101050 = dataL0g0010101050[:,][:,5*0+0]
KineticEneL0g0010101050 = dataL0g0010101050[:,][:,5*0+1]
SelfEnergyL0g0010101050 = dataL0g0010101050[:,][:,5*0+2]
EigenValReL0g0010101050 = dataL0g0010101050[:,][:,5*0+3]
EigenValImL0g0010101050 = dataL0g0010101050[:,][:,5*0+4]

MaxEigenValImL0g0011Inf = np.zeros((6))

MaxEigenValImL0g0011Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0010011010),np.max(EigenValImL0g0010011020),np.max(EigenValImL0g0010011030),np.max(EigenValImL0g0010011040),np.max(EigenValImL0g0010011050)], 1)[[1]]
MaxEigenValImL0g0011Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0010021010),np.max(EigenValImL0g0010021020),np.max(EigenValImL0g0010021030),np.max(EigenValImL0g0010021040),np.max(EigenValImL0g0010021050)], 1)[[1]]
MaxEigenValImL0g0011Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0010031010),np.max(EigenValImL0g0010031020),np.max(EigenValImL0g0010031030),np.max(EigenValImL0g0010031040),np.max(EigenValImL0g0010031050)], 1)[[1]]
MaxEigenValImL0g0011Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0010051010),np.max(EigenValImL0g0010051020),np.max(EigenValImL0g0010051030),np.max(EigenValImL0g0010051040),np.max(EigenValImL0g0010051050)], 1)[[1]]
MaxEigenValImL0g0011Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0010071010),np.max(EigenValImL0g0010071020),np.max(EigenValImL0g0010071030),np.max(EigenValImL0g0010071040),np.max(EigenValImL0g0010071050)], 1)[[1]]
MaxEigenValImL0g0011Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0010101010),np.max(EigenValImL0g0010101020),np.max(EigenValImL0g0010101030),np.max(EigenValImL0g0010101040),np.max(EigenValImL0g0010101050)], 1)[[1]]

########################################################################

dataL0g0020011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK001/N010/HamVals.txt')

MomentumAxL0g0020011010 = dataL0g0020011010[:,][:,5*0+0]
KineticEneL0g0020011010 = dataL0g0020011010[:,][:,5*0+1]
SelfEnergyL0g0020011010 = dataL0g0020011010[:,][:,5*0+2]
EigenValReL0g0020011010 = dataL0g0020011010[:,][:,5*0+3]
EigenValImL0g0020011010 = dataL0g0020011010[:,][:,5*0+4]

dataL0g0020011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK001/N020/HamVals.txt')

MomentumAxL0g0020011020 = dataL0g0020011020[:,][:,5*0+0]
KineticEneL0g0020011020 = dataL0g0020011020[:,][:,5*0+1]
SelfEnergyL0g0020011020 = dataL0g0020011020[:,][:,5*0+2]
EigenValReL0g0020011020 = dataL0g0020011020[:,][:,5*0+3]
EigenValImL0g0020011020 = dataL0g0020011020[:,][:,5*0+4]

dataL0g0020011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK001/N030/HamVals.txt')

MomentumAxL0g0020011030 = dataL0g0020011030[:,][:,5*0+0]
KineticEneL0g0020011030 = dataL0g0020011030[:,][:,5*0+1]
SelfEnergyL0g0020011030 = dataL0g0020011030[:,][:,5*0+2]
EigenValReL0g0020011030 = dataL0g0020011030[:,][:,5*0+3]
EigenValImL0g0020011030 = dataL0g0020011030[:,][:,5*0+4]

dataL0g0020011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK001/N040/HamVals.txt')

MomentumAxL0g0020011040 = dataL0g0020011040[:,][:,5*0+0]
KineticEneL0g0020011040 = dataL0g0020011040[:,][:,5*0+1]
SelfEnergyL0g0020011040 = dataL0g0020011040[:,][:,5*0+2]
EigenValReL0g0020011040 = dataL0g0020011040[:,][:,5*0+3]
EigenValImL0g0020011040 = dataL0g0020011040[:,][:,5*0+4]

dataL0g0020011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK001/N050/HamVals.txt')

MomentumAxL0g0020011050 = dataL0g0020011050[:,][:,5*0+0]
KineticEneL0g0020011050 = dataL0g0020011050[:,][:,5*0+1]
SelfEnergyL0g0020011050 = dataL0g0020011050[:,][:,5*0+2]
EigenValReL0g0020011050 = dataL0g0020011050[:,][:,5*0+3]
EigenValImL0g0020011050 = dataL0g0020011050[:,][:,5*0+4]

dataL0g0020021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK002/N010/HamVals.txt')

MomentumAxL0g0020021010 = dataL0g0020021010[:,][:,5*0+0]
KineticEneL0g0020021010 = dataL0g0020021010[:,][:,5*0+1]
SelfEnergyL0g0020021010 = dataL0g0020021010[:,][:,5*0+2]
EigenValReL0g0020021010 = dataL0g0020021010[:,][:,5*0+3]
EigenValImL0g0020021010 = dataL0g0020021010[:,][:,5*0+4]

dataL0g0020021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK002/N020/HamVals.txt')

MomentumAxL0g0020021020 = dataL0g0020021020[:,][:,5*0+0]
KineticEneL0g0020021020 = dataL0g0020021020[:,][:,5*0+1]
SelfEnergyL0g0020021020 = dataL0g0020021020[:,][:,5*0+2]
EigenValReL0g0020021020 = dataL0g0020021020[:,][:,5*0+3]
EigenValImL0g0020021020 = dataL0g0020021020[:,][:,5*0+4]

dataL0g0020021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK002/N030/HamVals.txt')

MomentumAxL0g0020021030 = dataL0g0020021030[:,][:,5*0+0]
KineticEneL0g0020021030 = dataL0g0020021030[:,][:,5*0+1]
SelfEnergyL0g0020021030 = dataL0g0020021030[:,][:,5*0+2]
EigenValReL0g0020021030 = dataL0g0020021030[:,][:,5*0+3]
EigenValImL0g0020021030 = dataL0g0020021030[:,][:,5*0+4]

dataL0g0020021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK002/N040/HamVals.txt')

MomentumAxL0g0020021040 = dataL0g0020021040[:,][:,5*0+0]
KineticEneL0g0020021040 = dataL0g0020021040[:,][:,5*0+1]
SelfEnergyL0g0020021040 = dataL0g0020021040[:,][:,5*0+2]
EigenValReL0g0020021040 = dataL0g0020021040[:,][:,5*0+3]
EigenValImL0g0020021040 = dataL0g0020021040[:,][:,5*0+4]

dataL0g0020021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK002/N050/HamVals.txt')

MomentumAxL0g0020021050 = dataL0g0020021050[:,][:,5*0+0]
KineticEneL0g0020021050 = dataL0g0020021050[:,][:,5*0+1]
SelfEnergyL0g0020021050 = dataL0g0020021050[:,][:,5*0+2]
EigenValReL0g0020021050 = dataL0g0020021050[:,][:,5*0+3]
EigenValImL0g0020021050 = dataL0g0020021050[:,][:,5*0+4]

dataL0g0020031010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK003/N010/HamVals.txt')

MomentumAxL0g0020031010 = dataL0g0020031010[:,][:,5*0+0]
KineticEneL0g0020031010 = dataL0g0020031010[:,][:,5*0+1]
SelfEnergyL0g0020031010 = dataL0g0020031010[:,][:,5*0+2]
EigenValReL0g0020031010 = dataL0g0020031010[:,][:,5*0+3]
EigenValImL0g0020031010 = dataL0g0020031010[:,][:,5*0+4]

dataL0g0020031020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK003/N020/HamVals.txt')

MomentumAxL0g0020031020 = dataL0g0020031020[:,][:,5*0+0]
KineticEneL0g0020031020 = dataL0g0020031020[:,][:,5*0+1]
SelfEnergyL0g0020031020 = dataL0g0020031020[:,][:,5*0+2]
EigenValReL0g0020031020 = dataL0g0020031020[:,][:,5*0+3]
EigenValImL0g0020031020 = dataL0g0020031020[:,][:,5*0+4]

dataL0g0020031030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK003/N030/HamVals.txt')

MomentumAxL0g0020031030 = dataL0g0020031030[:,][:,5*0+0]
KineticEneL0g0020031030 = dataL0g0020031030[:,][:,5*0+1]
SelfEnergyL0g0020031030 = dataL0g0020031030[:,][:,5*0+2]
EigenValReL0g0020031030 = dataL0g0020031030[:,][:,5*0+3]
EigenValImL0g0020031030 = dataL0g0020031030[:,][:,5*0+4]

dataL0g0020031040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK003/N040/HamVals.txt')

MomentumAxL0g0020031040 = dataL0g0020031040[:,][:,5*0+0]
KineticEneL0g0020031040 = dataL0g0020031040[:,][:,5*0+1]
SelfEnergyL0g0020031040 = dataL0g0020031040[:,][:,5*0+2]
EigenValReL0g0020031040 = dataL0g0020031040[:,][:,5*0+3]
EigenValImL0g0020031040 = dataL0g0020031040[:,][:,5*0+4]

dataL0g0020031050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK003/N050/HamVals.txt')

MomentumAxL0g0020031050 = dataL0g0020031050[:,][:,5*0+0]
KineticEneL0g0020031050 = dataL0g0020031050[:,][:,5*0+1]
SelfEnergyL0g0020031050 = dataL0g0020031050[:,][:,5*0+2]
EigenValReL0g0020031050 = dataL0g0020031050[:,][:,5*0+3]
EigenValImL0g0020031050 = dataL0g0020031050[:,][:,5*0+4]

dataL0g0020051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK005/N010/HamVals.txt')

MomentumAxL0g0020051010 = dataL0g0020051010[:,][:,5*0+0]
KineticEneL0g0020051010 = dataL0g0020051010[:,][:,5*0+1]
SelfEnergyL0g0020051010 = dataL0g0020051010[:,][:,5*0+2]
EigenValReL0g0020051010 = dataL0g0020051010[:,][:,5*0+3]
EigenValImL0g0020051010 = dataL0g0020051010[:,][:,5*0+4]

dataL0g0020051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK005/N020/HamVals.txt')

MomentumAxL0g0020051020 = dataL0g0020051020[:,][:,5*0+0]
KineticEneL0g0020051020 = dataL0g0020051020[:,][:,5*0+1]
SelfEnergyL0g0020051020 = dataL0g0020051020[:,][:,5*0+2]
EigenValReL0g0020051020 = dataL0g0020051020[:,][:,5*0+3]
EigenValImL0g0020051020 = dataL0g0020051020[:,][:,5*0+4]

dataL0g0020051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK005/N030/HamVals.txt')

MomentumAxL0g0020051030 = dataL0g0020051030[:,][:,5*0+0]
KineticEneL0g0020051030 = dataL0g0020051030[:,][:,5*0+1]
SelfEnergyL0g0020051030 = dataL0g0020051030[:,][:,5*0+2]
EigenValReL0g0020051030 = dataL0g0020051030[:,][:,5*0+3]
EigenValImL0g0020051030 = dataL0g0020051030[:,][:,5*0+4]

dataL0g0020051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK005/N040/HamVals.txt')

MomentumAxL0g0020051040 = dataL0g0020051040[:,][:,5*0+0]
KineticEneL0g0020051040 = dataL0g0020051040[:,][:,5*0+1]
SelfEnergyL0g0020051040 = dataL0g0020051040[:,][:,5*0+2]
EigenValReL0g0020051040 = dataL0g0020051040[:,][:,5*0+3]
EigenValImL0g0020051040 = dataL0g0020051040[:,][:,5*0+4]

dataL0g0020051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK005/N050/HamVals.txt')

MomentumAxL0g0020051050 = dataL0g0020051050[:,][:,5*0+0]
KineticEneL0g0020051050 = dataL0g0020051050[:,][:,5*0+1]
SelfEnergyL0g0020051050 = dataL0g0020051050[:,][:,5*0+2]
EigenValReL0g0020051050 = dataL0g0020051050[:,][:,5*0+3]
EigenValImL0g0020051050 = dataL0g0020051050[:,][:,5*0+4]

dataL0g0020071010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK007/N010/HamVals.txt')

MomentumAxL0g0020071010 = dataL0g0020071010[:,][:,5*0+0]
KineticEneL0g0020071010 = dataL0g0020071010[:,][:,5*0+1]
SelfEnergyL0g0020071010 = dataL0g0020071010[:,][:,5*0+2]
EigenValReL0g0020071010 = dataL0g0020071010[:,][:,5*0+3]
EigenValImL0g0020071010 = dataL0g0020071010[:,][:,5*0+4]

dataL0g0020071020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK007/N020/HamVals.txt')

MomentumAxL0g0020071020 = dataL0g0020071020[:,][:,5*0+0]
KineticEneL0g0020071020 = dataL0g0020071020[:,][:,5*0+1]
SelfEnergyL0g0020071020 = dataL0g0020071020[:,][:,5*0+2]
EigenValReL0g0020071020 = dataL0g0020071020[:,][:,5*0+3]
EigenValImL0g0020071020 = dataL0g0020071020[:,][:,5*0+4]

dataL0g0020071030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK007/N030/HamVals.txt')

MomentumAxL0g0020071030 = dataL0g0020071030[:,][:,5*0+0]
KineticEneL0g0020071030 = dataL0g0020071030[:,][:,5*0+1]
SelfEnergyL0g0020071030 = dataL0g0020071030[:,][:,5*0+2]
EigenValReL0g0020071030 = dataL0g0020071030[:,][:,5*0+3]
EigenValImL0g0020071030 = dataL0g0020071030[:,][:,5*0+4]

dataL0g0020071040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK007/N040/HamVals.txt')

MomentumAxL0g0020071040 = dataL0g0020071040[:,][:,5*0+0]
KineticEneL0g0020071040 = dataL0g0020071040[:,][:,5*0+1]
SelfEnergyL0g0020071040 = dataL0g0020071040[:,][:,5*0+2]
EigenValReL0g0020071040 = dataL0g0020071040[:,][:,5*0+3]
EigenValImL0g0020071040 = dataL0g0020071040[:,][:,5*0+4]

dataL0g0020071050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK007/N050/HamVals.txt')

MomentumAxL0g0020071050 = dataL0g0020071050[:,][:,5*0+0]
KineticEneL0g0020071050 = dataL0g0020071050[:,][:,5*0+1]
SelfEnergyL0g0020071050 = dataL0g0020071050[:,][:,5*0+2]
EigenValReL0g0020071050 = dataL0g0020071050[:,][:,5*0+3]
EigenValImL0g0020071050 = dataL0g0020071050[:,][:,5*0+4]

dataL0g0020101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK010/N010/HamVals.txt')

MomentumAxL0g0020101010 = dataL0g0020101010[:,][:,5*0+0]
KineticEneL0g0020101010 = dataL0g0020101010[:,][:,5*0+1]
SelfEnergyL0g0020101010 = dataL0g0020101010[:,][:,5*0+2]
EigenValReL0g0020101010 = dataL0g0020101010[:,][:,5*0+3]
EigenValImL0g0020101010 = dataL0g0020101010[:,][:,5*0+4]

dataL0g0020101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK010/N020/HamVals.txt')

MomentumAxL0g0020101020 = dataL0g0020101020[:,][:,5*0+0]
KineticEneL0g0020101020 = dataL0g0020101020[:,][:,5*0+1]
SelfEnergyL0g0020101020 = dataL0g0020101020[:,][:,5*0+2]
EigenValReL0g0020101020 = dataL0g0020101020[:,][:,5*0+3]
EigenValImL0g0020101020 = dataL0g0020101020[:,][:,5*0+4]

dataL0g0020101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK010/N030/HamVals.txt')

MomentumAxL0g0020101030 = dataL0g0020101030[:,][:,5*0+0]
KineticEneL0g0020101030 = dataL0g0020101030[:,][:,5*0+1]
SelfEnergyL0g0020101030 = dataL0g0020101030[:,][:,5*0+2]
EigenValReL0g0020101030 = dataL0g0020101030[:,][:,5*0+3]
EigenValImL0g0020101030 = dataL0g0020101030[:,][:,5*0+4]

dataL0g0020101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK010/N040/HamVals.txt')

MomentumAxL0g0020101040 = dataL0g0020101040[:,][:,5*0+0]
KineticEneL0g0020101040 = dataL0g0020101040[:,][:,5*0+1]
SelfEnergyL0g0020101040 = dataL0g0020101040[:,][:,5*0+2]
EigenValReL0g0020101040 = dataL0g0020101040[:,][:,5*0+3]
EigenValImL0g0020101040 = dataL0g0020101040[:,][:,5*0+4]

dataL0g0020101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK010/N050/HamVals.txt')

MomentumAxL0g0020101050 = dataL0g0020101050[:,][:,5*0+0]
KineticEneL0g0020101050 = dataL0g0020101050[:,][:,5*0+1]
SelfEnergyL0g0020101050 = dataL0g0020101050[:,][:,5*0+2]
EigenValReL0g0020101050 = dataL0g0020101050[:,][:,5*0+3]
EigenValImL0g0020101050 = dataL0g0020101050[:,][:,5*0+4]

MaxEigenValImL0g0021Inf = np.zeros((6))

MaxEigenValImL0g0021Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0020011010),np.max(EigenValImL0g0020011020),np.max(EigenValImL0g0020011030),np.max(EigenValImL0g0020011040),np.max(EigenValImL0g0020011050)], 1)[[1]]
MaxEigenValImL0g0021Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0020021010),np.max(EigenValImL0g0020021020),np.max(EigenValImL0g0020021030),np.max(EigenValImL0g0020021040),np.max(EigenValImL0g0020021050)], 1)[[1]]
MaxEigenValImL0g0021Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0020031010),np.max(EigenValImL0g0020031020),np.max(EigenValImL0g0020031030),np.max(EigenValImL0g0020031040),np.max(EigenValImL0g0020031050)], 1)[[1]]
MaxEigenValImL0g0021Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0020051010),np.max(EigenValImL0g0020051020),np.max(EigenValImL0g0020051030),np.max(EigenValImL0g0020051040),np.max(EigenValImL0g0020051050)], 1)[[1]]
MaxEigenValImL0g0021Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0020071010),np.max(EigenValImL0g0020071020),np.max(EigenValImL0g0020071030),np.max(EigenValImL0g0020071040),np.max(EigenValImL0g0020071050)], 1)[[1]]
MaxEigenValImL0g0021Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0020101010),np.max(EigenValImL0g0020101020),np.max(EigenValImL0g0020101030),np.max(EigenValImL0g0020101040),np.max(EigenValImL0g0020101050)], 1)[[1]]

########################################################################

dataL0g0050011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK001/N010/HamVals.txt')

MomentumAxL0g0050011010 = dataL0g0050011010[:,][:,5*0+0]
KineticEneL0g0050011010 = dataL0g0050011010[:,][:,5*0+1]
SelfEnergyL0g0050011010 = dataL0g0050011010[:,][:,5*0+2]
EigenValReL0g0050011010 = dataL0g0050011010[:,][:,5*0+3]
EigenValImL0g0050011010 = dataL0g0050011010[:,][:,5*0+4]

dataL0g0050011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK001/N020/HamVals.txt')

MomentumAxL0g0050011020 = dataL0g0050011020[:,][:,5*0+0]
KineticEneL0g0050011020 = dataL0g0050011020[:,][:,5*0+1]
SelfEnergyL0g0050011020 = dataL0g0050011020[:,][:,5*0+2]
EigenValReL0g0050011020 = dataL0g0050011020[:,][:,5*0+3]
EigenValImL0g0050011020 = dataL0g0050011020[:,][:,5*0+4]

dataL0g0050011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK001/N030/HamVals.txt')

MomentumAxL0g0050011030 = dataL0g0050011030[:,][:,5*0+0]
KineticEneL0g0050011030 = dataL0g0050011030[:,][:,5*0+1]
SelfEnergyL0g0050011030 = dataL0g0050011030[:,][:,5*0+2]
EigenValReL0g0050011030 = dataL0g0050011030[:,][:,5*0+3]
EigenValImL0g0050011030 = dataL0g0050011030[:,][:,5*0+4]

dataL0g0050011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK001/N040/HamVals.txt')

MomentumAxL0g0050011040 = dataL0g0050011040[:,][:,5*0+0]
KineticEneL0g0050011040 = dataL0g0050011040[:,][:,5*0+1]
SelfEnergyL0g0050011040 = dataL0g0050011040[:,][:,5*0+2]
EigenValReL0g0050011040 = dataL0g0050011040[:,][:,5*0+3]
EigenValImL0g0050011040 = dataL0g0050011040[:,][:,5*0+4]

dataL0g0050011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK001/N050/HamVals.txt')

MomentumAxL0g0050011050 = dataL0g0050011050[:,][:,5*0+0]
KineticEneL0g0050011050 = dataL0g0050011050[:,][:,5*0+1]
SelfEnergyL0g0050011050 = dataL0g0050011050[:,][:,5*0+2]
EigenValReL0g0050011050 = dataL0g0050011050[:,][:,5*0+3]
EigenValImL0g0050011050 = dataL0g0050011050[:,][:,5*0+4]

dataL0g0050021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK002/N010/HamVals.txt')

MomentumAxL0g0050021010 = dataL0g0050021010[:,][:,5*0+0]
KineticEneL0g0050021010 = dataL0g0050021010[:,][:,5*0+1]
SelfEnergyL0g0050021010 = dataL0g0050021010[:,][:,5*0+2]
EigenValReL0g0050021010 = dataL0g0050021010[:,][:,5*0+3]
EigenValImL0g0050021010 = dataL0g0050021010[:,][:,5*0+4]

dataL0g0050021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK002/N020/HamVals.txt')

MomentumAxL0g0050021020 = dataL0g0050021020[:,][:,5*0+0]
KineticEneL0g0050021020 = dataL0g0050021020[:,][:,5*0+1]
SelfEnergyL0g0050021020 = dataL0g0050021020[:,][:,5*0+2]
EigenValReL0g0050021020 = dataL0g0050021020[:,][:,5*0+3]
EigenValImL0g0050021020 = dataL0g0050021020[:,][:,5*0+4]

dataL0g0050021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK002/N030/HamVals.txt')

MomentumAxL0g0050021030 = dataL0g0050021030[:,][:,5*0+0]
KineticEneL0g0050021030 = dataL0g0050021030[:,][:,5*0+1]
SelfEnergyL0g0050021030 = dataL0g0050021030[:,][:,5*0+2]
EigenValReL0g0050021030 = dataL0g0050021030[:,][:,5*0+3]
EigenValImL0g0050021030 = dataL0g0050021030[:,][:,5*0+4]

dataL0g0050021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK002/N040/HamVals.txt')

MomentumAxL0g0050021040 = dataL0g0050021040[:,][:,5*0+0]
KineticEneL0g0050021040 = dataL0g0050021040[:,][:,5*0+1]
SelfEnergyL0g0050021040 = dataL0g0050021040[:,][:,5*0+2]
EigenValReL0g0050021040 = dataL0g0050021040[:,][:,5*0+3]
EigenValImL0g0050021040 = dataL0g0050021040[:,][:,5*0+4]

dataL0g0050021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK002/N050/HamVals.txt')

MomentumAxL0g0050021050 = dataL0g0050021050[:,][:,5*0+0]
KineticEneL0g0050021050 = dataL0g0050021050[:,][:,5*0+1]
SelfEnergyL0g0050021050 = dataL0g0050021050[:,][:,5*0+2]
EigenValReL0g0050021050 = dataL0g0050021050[:,][:,5*0+3]
EigenValImL0g0050021050 = dataL0g0050021050[:,][:,5*0+4]

dataL0g0050031010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK003/N010/HamVals.txt')

MomentumAxL0g0050031010 = dataL0g0050031010[:,][:,5*0+0]
KineticEneL0g0050031010 = dataL0g0050031010[:,][:,5*0+1]
SelfEnergyL0g0050031010 = dataL0g0050031010[:,][:,5*0+2]
EigenValReL0g0050031010 = dataL0g0050031010[:,][:,5*0+3]
EigenValImL0g0050031010 = dataL0g0050031010[:,][:,5*0+4]

dataL0g0050031020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK003/N020/HamVals.txt')

MomentumAxL0g0050031020 = dataL0g0050031020[:,][:,5*0+0]
KineticEneL0g0050031020 = dataL0g0050031020[:,][:,5*0+1]
SelfEnergyL0g0050031020 = dataL0g0050031020[:,][:,5*0+2]
EigenValReL0g0050031020 = dataL0g0050031020[:,][:,5*0+3]
EigenValImL0g0050031020 = dataL0g0050031020[:,][:,5*0+4]

dataL0g0050031030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK003/N030/HamVals.txt')

MomentumAxL0g0050031030 = dataL0g0050031030[:,][:,5*0+0]
KineticEneL0g0050031030 = dataL0g0050031030[:,][:,5*0+1]
SelfEnergyL0g0050031030 = dataL0g0050031030[:,][:,5*0+2]
EigenValReL0g0050031030 = dataL0g0050031030[:,][:,5*0+3]
EigenValImL0g0050031030 = dataL0g0050031030[:,][:,5*0+4]

dataL0g0050031040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK003/N040/HamVals.txt')

MomentumAxL0g0050031040 = dataL0g0050031040[:,][:,5*0+0]
KineticEneL0g0050031040 = dataL0g0050031040[:,][:,5*0+1]
SelfEnergyL0g0050031040 = dataL0g0050031040[:,][:,5*0+2]
EigenValReL0g0050031040 = dataL0g0050031040[:,][:,5*0+3]
EigenValImL0g0050031040 = dataL0g0050031040[:,][:,5*0+4]

dataL0g0050031050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK003/N050/HamVals.txt')

MomentumAxL0g0050031050 = dataL0g0050031050[:,][:,5*0+0]
KineticEneL0g0050031050 = dataL0g0050031050[:,][:,5*0+1]
SelfEnergyL0g0050031050 = dataL0g0050031050[:,][:,5*0+2]
EigenValReL0g0050031050 = dataL0g0050031050[:,][:,5*0+3]
EigenValImL0g0050031050 = dataL0g0050031050[:,][:,5*0+4]

dataL0g0050051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK005/N010/HamVals.txt')

MomentumAxL0g0050051010 = dataL0g0050051010[:,][:,5*0+0]
KineticEneL0g0050051010 = dataL0g0050051010[:,][:,5*0+1]
SelfEnergyL0g0050051010 = dataL0g0050051010[:,][:,5*0+2]
EigenValReL0g0050051010 = dataL0g0050051010[:,][:,5*0+3]
EigenValImL0g0050051010 = dataL0g0050051010[:,][:,5*0+4]

dataL0g0050051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK005/N020/HamVals.txt')

MomentumAxL0g0050051020 = dataL0g0050051020[:,][:,5*0+0]
KineticEneL0g0050051020 = dataL0g0050051020[:,][:,5*0+1]
SelfEnergyL0g0050051020 = dataL0g0050051020[:,][:,5*0+2]
EigenValReL0g0050051020 = dataL0g0050051020[:,][:,5*0+3]
EigenValImL0g0050051020 = dataL0g0050051020[:,][:,5*0+4]

dataL0g0050051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK005/N030/HamVals.txt')

MomentumAxL0g0050051030 = dataL0g0050051030[:,][:,5*0+0]
KineticEneL0g0050051030 = dataL0g0050051030[:,][:,5*0+1]
SelfEnergyL0g0050051030 = dataL0g0050051030[:,][:,5*0+2]
EigenValReL0g0050051030 = dataL0g0050051030[:,][:,5*0+3]
EigenValImL0g0050051030 = dataL0g0050051030[:,][:,5*0+4]

dataL0g0050051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK005/N040/HamVals.txt')

MomentumAxL0g0050051040 = dataL0g0050051040[:,][:,5*0+0]
KineticEneL0g0050051040 = dataL0g0050051040[:,][:,5*0+1]
SelfEnergyL0g0050051040 = dataL0g0050051040[:,][:,5*0+2]
EigenValReL0g0050051040 = dataL0g0050051040[:,][:,5*0+3]
EigenValImL0g0050051040 = dataL0g0050051040[:,][:,5*0+4]

dataL0g0050051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK005/N050/HamVals.txt')

MomentumAxL0g0050051050 = dataL0g0050051050[:,][:,5*0+0]
KineticEneL0g0050051050 = dataL0g0050051050[:,][:,5*0+1]
SelfEnergyL0g0050051050 = dataL0g0050051050[:,][:,5*0+2]
EigenValReL0g0050051050 = dataL0g0050051050[:,][:,5*0+3]
EigenValImL0g0050051050 = dataL0g0050051050[:,][:,5*0+4]

dataL0g0050071010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK007/N010/HamVals.txt')

MomentumAxL0g0050071010 = dataL0g0050071010[:,][:,5*0+0]
KineticEneL0g0050071010 = dataL0g0050071010[:,][:,5*0+1]
SelfEnergyL0g0050071010 = dataL0g0050071010[:,][:,5*0+2]
EigenValReL0g0050071010 = dataL0g0050071010[:,][:,5*0+3]
EigenValImL0g0050071010 = dataL0g0050071010[:,][:,5*0+4]

dataL0g0050071020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK007/N020/HamVals.txt')

MomentumAxL0g0050071020 = dataL0g0050071020[:,][:,5*0+0]
KineticEneL0g0050071020 = dataL0g0050071020[:,][:,5*0+1]
SelfEnergyL0g0050071020 = dataL0g0050071020[:,][:,5*0+2]
EigenValReL0g0050071020 = dataL0g0050071020[:,][:,5*0+3]
EigenValImL0g0050071020 = dataL0g0050071020[:,][:,5*0+4]

dataL0g0050071030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK007/N030/HamVals.txt')

MomentumAxL0g0050071030 = dataL0g0050071030[:,][:,5*0+0]
KineticEneL0g0050071030 = dataL0g0050071030[:,][:,5*0+1]
SelfEnergyL0g0050071030 = dataL0g0050071030[:,][:,5*0+2]
EigenValReL0g0050071030 = dataL0g0050071030[:,][:,5*0+3]
EigenValImL0g0050071030 = dataL0g0050071030[:,][:,5*0+4]

dataL0g0050071040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK007/N040/HamVals.txt')

MomentumAxL0g0050071040 = dataL0g0050071040[:,][:,5*0+0]
KineticEneL0g0050071040 = dataL0g0050071040[:,][:,5*0+1]
SelfEnergyL0g0050071040 = dataL0g0050071040[:,][:,5*0+2]
EigenValReL0g0050071040 = dataL0g0050071040[:,][:,5*0+3]
EigenValImL0g0050071040 = dataL0g0050071040[:,][:,5*0+4]

dataL0g0050071050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK007/N050/HamVals.txt')

MomentumAxL0g0050071050 = dataL0g0050071050[:,][:,5*0+0]
KineticEneL0g0050071050 = dataL0g0050071050[:,][:,5*0+1]
SelfEnergyL0g0050071050 = dataL0g0050071050[:,][:,5*0+2]
EigenValReL0g0050071050 = dataL0g0050071050[:,][:,5*0+3]
EigenValImL0g0050071050 = dataL0g0050071050[:,][:,5*0+4]

dataL0g0050101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK010/N010/HamVals.txt')

MomentumAxL0g0050101010 = dataL0g0050101010[:,][:,5*0+0]
KineticEneL0g0050101010 = dataL0g0050101010[:,][:,5*0+1]
SelfEnergyL0g0050101010 = dataL0g0050101010[:,][:,5*0+2]
EigenValReL0g0050101010 = dataL0g0050101010[:,][:,5*0+3]
EigenValImL0g0050101010 = dataL0g0050101010[:,][:,5*0+4]

dataL0g0050101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK010/N020/HamVals.txt')

MomentumAxL0g0050101020 = dataL0g0050101020[:,][:,5*0+0]
KineticEneL0g0050101020 = dataL0g0050101020[:,][:,5*0+1]
SelfEnergyL0g0050101020 = dataL0g0050101020[:,][:,5*0+2]
EigenValReL0g0050101020 = dataL0g0050101020[:,][:,5*0+3]
EigenValImL0g0050101020 = dataL0g0050101020[:,][:,5*0+4]

dataL0g0050101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK010/N030/HamVals.txt')

MomentumAxL0g0050101030 = dataL0g0050101030[:,][:,5*0+0]
KineticEneL0g0050101030 = dataL0g0050101030[:,][:,5*0+1]
SelfEnergyL0g0050101030 = dataL0g0050101030[:,][:,5*0+2]
EigenValReL0g0050101030 = dataL0g0050101030[:,][:,5*0+3]
EigenValImL0g0050101030 = dataL0g0050101030[:,][:,5*0+4]

dataL0g0050101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK010/N040/HamVals.txt')

MomentumAxL0g0050101040 = dataL0g0050101040[:,][:,5*0+0]
KineticEneL0g0050101040 = dataL0g0050101040[:,][:,5*0+1]
SelfEnergyL0g0050101040 = dataL0g0050101040[:,][:,5*0+2]
EigenValReL0g0050101040 = dataL0g0050101040[:,][:,5*0+3]
EigenValImL0g0050101040 = dataL0g0050101040[:,][:,5*0+4]

dataL0g0050101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK010/N050/HamVals.txt')

MomentumAxL0g0050101050 = dataL0g0050101050[:,][:,5*0+0]
KineticEneL0g0050101050 = dataL0g0050101050[:,][:,5*0+1]
SelfEnergyL0g0050101050 = dataL0g0050101050[:,][:,5*0+2]
EigenValReL0g0050101050 = dataL0g0050101050[:,][:,5*0+3]
EigenValImL0g0050101050 = dataL0g0050101050[:,][:,5*0+4]

MaxEigenValImL0g0051Inf = np.zeros((6))

MaxEigenValImL0g0051Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0050011010),np.max(EigenValImL0g0050011020),np.max(EigenValImL0g0050011030),np.max(EigenValImL0g0050011040),np.max(EigenValImL0g0050011050)], 1)[[1]]
MaxEigenValImL0g0051Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0050021010),np.max(EigenValImL0g0050021020),np.max(EigenValImL0g0050021030),np.max(EigenValImL0g0050021040),np.max(EigenValImL0g0050021050)], 1)[[1]]
MaxEigenValImL0g0051Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0050031010),np.max(EigenValImL0g0050031020),np.max(EigenValImL0g0050031030),np.max(EigenValImL0g0050031040),np.max(EigenValImL0g0050031050)], 1)[[1]]
MaxEigenValImL0g0051Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0050051010),np.max(EigenValImL0g0050051020),np.max(EigenValImL0g0050051030),np.max(EigenValImL0g0050051040),np.max(EigenValImL0g0050051050)], 1)[[1]]
MaxEigenValImL0g0051Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0050071010),np.max(EigenValImL0g0050071020),np.max(EigenValImL0g0050071030),np.max(EigenValImL0g0050071040),np.max(EigenValImL0g0050071050)], 1)[[1]]
MaxEigenValImL0g0051Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0050101010),np.max(EigenValImL0g0050101020),np.max(EigenValImL0g0050101030),np.max(EigenValImL0g0050101040),np.max(EigenValImL0g0050101050)], 1)[[1]]

########################################################################

dataL0g0100011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK001/N010/HamVals.txt')

MomentumAxL0g0100011010 = dataL0g0100011010[:,][:,5*0+0]
KineticEneL0g0100011010 = dataL0g0100011010[:,][:,5*0+1]
SelfEnergyL0g0100011010 = dataL0g0100011010[:,][:,5*0+2]
EigenValReL0g0100011010 = dataL0g0100011010[:,][:,5*0+3]
EigenValImL0g0100011010 = dataL0g0100011010[:,][:,5*0+4]

dataL0g0100011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK001/N020/HamVals.txt')

MomentumAxL0g0100011020 = dataL0g0100011020[:,][:,5*0+0]
KineticEneL0g0100011020 = dataL0g0100011020[:,][:,5*0+1]
SelfEnergyL0g0100011020 = dataL0g0100011020[:,][:,5*0+2]
EigenValReL0g0100011020 = dataL0g0100011020[:,][:,5*0+3]
EigenValImL0g0100011020 = dataL0g0100011020[:,][:,5*0+4]

dataL0g0100011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK001/N030/HamVals.txt')

MomentumAxL0g0100011030 = dataL0g0100011030[:,][:,5*0+0]
KineticEneL0g0100011030 = dataL0g0100011030[:,][:,5*0+1]
SelfEnergyL0g0100011030 = dataL0g0100011030[:,][:,5*0+2]
EigenValReL0g0100011030 = dataL0g0100011030[:,][:,5*0+3]
EigenValImL0g0100011030 = dataL0g0100011030[:,][:,5*0+4]

dataL0g0100011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK001/N040/HamVals.txt')

MomentumAxL0g0100011040 = dataL0g0100011040[:,][:,5*0+0]
KineticEneL0g0100011040 = dataL0g0100011040[:,][:,5*0+1]
SelfEnergyL0g0100011040 = dataL0g0100011040[:,][:,5*0+2]
EigenValReL0g0100011040 = dataL0g0100011040[:,][:,5*0+3]
EigenValImL0g0100011040 = dataL0g0100011040[:,][:,5*0+4]

dataL0g0100011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK001/N050/HamVals.txt')

MomentumAxL0g0100011050 = dataL0g0100011050[:,][:,5*0+0]
KineticEneL0g0100011050 = dataL0g0100011050[:,][:,5*0+1]
SelfEnergyL0g0100011050 = dataL0g0100011050[:,][:,5*0+2]
EigenValReL0g0100011050 = dataL0g0100011050[:,][:,5*0+3]
EigenValImL0g0100011050 = dataL0g0100011050[:,][:,5*0+4]

dataL0g0100021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK002/N010/HamVals.txt')

MomentumAxL0g0100021010 = dataL0g0100021010[:,][:,5*0+0]
KineticEneL0g0100021010 = dataL0g0100021010[:,][:,5*0+1]
SelfEnergyL0g0100021010 = dataL0g0100021010[:,][:,5*0+2]
EigenValReL0g0100021010 = dataL0g0100021010[:,][:,5*0+3]
EigenValImL0g0100021010 = dataL0g0100021010[:,][:,5*0+4]

dataL0g0100021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK002/N020/HamVals.txt')

MomentumAxL0g0100021020 = dataL0g0100021020[:,][:,5*0+0]
KineticEneL0g0100021020 = dataL0g0100021020[:,][:,5*0+1]
SelfEnergyL0g0100021020 = dataL0g0100021020[:,][:,5*0+2]
EigenValReL0g0100021020 = dataL0g0100021020[:,][:,5*0+3]
EigenValImL0g0100021020 = dataL0g0100021020[:,][:,5*0+4]

dataL0g0100021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK002/N030/HamVals.txt')

MomentumAxL0g0100021030 = dataL0g0100021030[:,][:,5*0+0]
KineticEneL0g0100021030 = dataL0g0100021030[:,][:,5*0+1]
SelfEnergyL0g0100021030 = dataL0g0100021030[:,][:,5*0+2]
EigenValReL0g0100021030 = dataL0g0100021030[:,][:,5*0+3]
EigenValImL0g0100021030 = dataL0g0100021030[:,][:,5*0+4]

dataL0g0100021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK002/N040/HamVals.txt')

MomentumAxL0g0100021040 = dataL0g0100021040[:,][:,5*0+0]
KineticEneL0g0100021040 = dataL0g0100021040[:,][:,5*0+1]
SelfEnergyL0g0100021040 = dataL0g0100021040[:,][:,5*0+2]
EigenValReL0g0100021040 = dataL0g0100021040[:,][:,5*0+3]
EigenValImL0g0100021040 = dataL0g0100021040[:,][:,5*0+4]

dataL0g0100021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK002/N050/HamVals.txt')

MomentumAxL0g0100021050 = dataL0g0100021050[:,][:,5*0+0]
KineticEneL0g0100021050 = dataL0g0100021050[:,][:,5*0+1]
SelfEnergyL0g0100021050 = dataL0g0100021050[:,][:,5*0+2]
EigenValReL0g0100021050 = dataL0g0100021050[:,][:,5*0+3]
EigenValImL0g0100021050 = dataL0g0100021050[:,][:,5*0+4]

dataL0g0100031010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK003/N010/HamVals.txt')

MomentumAxL0g0100031010 = dataL0g0100031010[:,][:,5*0+0]
KineticEneL0g0100031010 = dataL0g0100031010[:,][:,5*0+1]
SelfEnergyL0g0100031010 = dataL0g0100031010[:,][:,5*0+2]
EigenValReL0g0100031010 = dataL0g0100031010[:,][:,5*0+3]
EigenValImL0g0100031010 = dataL0g0100031010[:,][:,5*0+4]

dataL0g0100031020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK003/N020/HamVals.txt')

MomentumAxL0g0100031020 = dataL0g0100031020[:,][:,5*0+0]
KineticEneL0g0100031020 = dataL0g0100031020[:,][:,5*0+1]
SelfEnergyL0g0100031020 = dataL0g0100031020[:,][:,5*0+2]
EigenValReL0g0100031020 = dataL0g0100031020[:,][:,5*0+3]
EigenValImL0g0100031020 = dataL0g0100031020[:,][:,5*0+4]

dataL0g0100031030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK003/N030/HamVals.txt')

MomentumAxL0g0100031030 = dataL0g0100031030[:,][:,5*0+0]
KineticEneL0g0100031030 = dataL0g0100031030[:,][:,5*0+1]
SelfEnergyL0g0100031030 = dataL0g0100031030[:,][:,5*0+2]
EigenValReL0g0100031030 = dataL0g0100031030[:,][:,5*0+3]
EigenValImL0g0100031030 = dataL0g0100031030[:,][:,5*0+4]

dataL0g0100031040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK003/N040/HamVals.txt')

MomentumAxL0g0100031040 = dataL0g0100031040[:,][:,5*0+0]
KineticEneL0g0100031040 = dataL0g0100031040[:,][:,5*0+1]
SelfEnergyL0g0100031040 = dataL0g0100031040[:,][:,5*0+2]
EigenValReL0g0100031040 = dataL0g0100031040[:,][:,5*0+3]
EigenValImL0g0100031040 = dataL0g0100031040[:,][:,5*0+4]

dataL0g0100031050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK003/N050/HamVals.txt')

MomentumAxL0g0100031050 = dataL0g0100031050[:,][:,5*0+0]
KineticEneL0g0100031050 = dataL0g0100031050[:,][:,5*0+1]
SelfEnergyL0g0100031050 = dataL0g0100031050[:,][:,5*0+2]
EigenValReL0g0100031050 = dataL0g0100031050[:,][:,5*0+3]
EigenValImL0g0100031050 = dataL0g0100031050[:,][:,5*0+4]

dataL0g0100051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK005/N010/HamVals.txt')

MomentumAxL0g0100051010 = dataL0g0100051010[:,][:,5*0+0]
KineticEneL0g0100051010 = dataL0g0100051010[:,][:,5*0+1]
SelfEnergyL0g0100051010 = dataL0g0100051010[:,][:,5*0+2]
EigenValReL0g0100051010 = dataL0g0100051010[:,][:,5*0+3]
EigenValImL0g0100051010 = dataL0g0100051010[:,][:,5*0+4]

dataL0g0100051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK005/N020/HamVals.txt')

MomentumAxL0g0100051020 = dataL0g0100051020[:,][:,5*0+0]
KineticEneL0g0100051020 = dataL0g0100051020[:,][:,5*0+1]
SelfEnergyL0g0100051020 = dataL0g0100051020[:,][:,5*0+2]
EigenValReL0g0100051020 = dataL0g0100051020[:,][:,5*0+3]
EigenValImL0g0100051020 = dataL0g0100051020[:,][:,5*0+4]

dataL0g0100051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK005/N030/HamVals.txt')

MomentumAxL0g0100051030 = dataL0g0100051030[:,][:,5*0+0]
KineticEneL0g0100051030 = dataL0g0100051030[:,][:,5*0+1]
SelfEnergyL0g0100051030 = dataL0g0100051030[:,][:,5*0+2]
EigenValReL0g0100051030 = dataL0g0100051030[:,][:,5*0+3]
EigenValImL0g0100051030 = dataL0g0100051030[:,][:,5*0+4]

dataL0g0100051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK005/N040/HamVals.txt')

MomentumAxL0g0100051040 = dataL0g0100051040[:,][:,5*0+0]
KineticEneL0g0100051040 = dataL0g0100051040[:,][:,5*0+1]
SelfEnergyL0g0100051040 = dataL0g0100051040[:,][:,5*0+2]
EigenValReL0g0100051040 = dataL0g0100051040[:,][:,5*0+3]
EigenValImL0g0100051040 = dataL0g0100051040[:,][:,5*0+4]

dataL0g0100051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK005/N050/HamVals.txt')

MomentumAxL0g0100051050 = dataL0g0100051050[:,][:,5*0+0]
KineticEneL0g0100051050 = dataL0g0100051050[:,][:,5*0+1]
SelfEnergyL0g0100051050 = dataL0g0100051050[:,][:,5*0+2]
EigenValReL0g0100051050 = dataL0g0100051050[:,][:,5*0+3]
EigenValImL0g0100051050 = dataL0g0100051050[:,][:,5*0+4]

dataL0g0100071010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK007/N010/HamVals.txt')

MomentumAxL0g0100071010 = dataL0g0100071010[:,][:,5*0+0]
KineticEneL0g0100071010 = dataL0g0100071010[:,][:,5*0+1]
SelfEnergyL0g0100071010 = dataL0g0100071010[:,][:,5*0+2]
EigenValReL0g0100071010 = dataL0g0100071010[:,][:,5*0+3]
EigenValImL0g0100071010 = dataL0g0100071010[:,][:,5*0+4]

dataL0g0100071020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK007/N020/HamVals.txt')

MomentumAxL0g0100071020 = dataL0g0100071020[:,][:,5*0+0]
KineticEneL0g0100071020 = dataL0g0100071020[:,][:,5*0+1]
SelfEnergyL0g0100071020 = dataL0g0100071020[:,][:,5*0+2]
EigenValReL0g0100071020 = dataL0g0100071020[:,][:,5*0+3]
EigenValImL0g0100071020 = dataL0g0100071020[:,][:,5*0+4]

dataL0g0100071030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK007/N030/HamVals.txt')

MomentumAxL0g0100071030 = dataL0g0100071030[:,][:,5*0+0]
KineticEneL0g0100071030 = dataL0g0100071030[:,][:,5*0+1]
SelfEnergyL0g0100071030 = dataL0g0100071030[:,][:,5*0+2]
EigenValReL0g0100071030 = dataL0g0100071030[:,][:,5*0+3]
EigenValImL0g0100071030 = dataL0g0100071030[:,][:,5*0+4]

dataL0g0100071040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK007/N040/HamVals.txt')

MomentumAxL0g0100071040 = dataL0g0100071040[:,][:,5*0+0]
KineticEneL0g0100071040 = dataL0g0100071040[:,][:,5*0+1]
SelfEnergyL0g0100071040 = dataL0g0100071040[:,][:,5*0+2]
EigenValReL0g0100071040 = dataL0g0100071040[:,][:,5*0+3]
EigenValImL0g0100071040 = dataL0g0100071040[:,][:,5*0+4]

dataL0g0100071050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK007/N050/HamVals.txt')

MomentumAxL0g0100071050 = dataL0g0100071050[:,][:,5*0+0]
KineticEneL0g0100071050 = dataL0g0100071050[:,][:,5*0+1]
SelfEnergyL0g0100071050 = dataL0g0100071050[:,][:,5*0+2]
EigenValReL0g0100071050 = dataL0g0100071050[:,][:,5*0+3]
EigenValImL0g0100071050 = dataL0g0100071050[:,][:,5*0+4]

dataL0g0100101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK010/N010/HamVals.txt')

MomentumAxL0g0100101010 = dataL0g0100101010[:,][:,5*0+0]
KineticEneL0g0100101010 = dataL0g0100101010[:,][:,5*0+1]
SelfEnergyL0g0100101010 = dataL0g0100101010[:,][:,5*0+2]
EigenValReL0g0100101010 = dataL0g0100101010[:,][:,5*0+3]
EigenValImL0g0100101010 = dataL0g0100101010[:,][:,5*0+4]

dataL0g0100101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK010/N020/HamVals.txt')

MomentumAxL0g0100101020 = dataL0g0100101020[:,][:,5*0+0]
KineticEneL0g0100101020 = dataL0g0100101020[:,][:,5*0+1]
SelfEnergyL0g0100101020 = dataL0g0100101020[:,][:,5*0+2]
EigenValReL0g0100101020 = dataL0g0100101020[:,][:,5*0+3]
EigenValImL0g0100101020 = dataL0g0100101020[:,][:,5*0+4]

dataL0g0100101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK010/N030/HamVals.txt')

MomentumAxL0g0100101030 = dataL0g0100101030[:,][:,5*0+0]
KineticEneL0g0100101030 = dataL0g0100101030[:,][:,5*0+1]
SelfEnergyL0g0100101030 = dataL0g0100101030[:,][:,5*0+2]
EigenValReL0g0100101030 = dataL0g0100101030[:,][:,5*0+3]
EigenValImL0g0100101030 = dataL0g0100101030[:,][:,5*0+4]

dataL0g0100101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK010/N040/HamVals.txt')

MomentumAxL0g0100101040 = dataL0g0100101040[:,][:,5*0+0]
KineticEneL0g0100101040 = dataL0g0100101040[:,][:,5*0+1]
SelfEnergyL0g0100101040 = dataL0g0100101040[:,][:,5*0+2]
EigenValReL0g0100101040 = dataL0g0100101040[:,][:,5*0+3]
EigenValImL0g0100101040 = dataL0g0100101040[:,][:,5*0+4]

dataL0g0100101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK010/N050/HamVals.txt')

MomentumAxL0g0100101050 = dataL0g0100101050[:,][:,5*0+0]
KineticEneL0g0100101050 = dataL0g0100101050[:,][:,5*0+1]
SelfEnergyL0g0100101050 = dataL0g0100101050[:,][:,5*0+2]
EigenValReL0g0100101050 = dataL0g0100101050[:,][:,5*0+3]
EigenValImL0g0100101050 = dataL0g0100101050[:,][:,5*0+4]

MaxEigenValImL0g0101Inf = np.zeros((6))

MaxEigenValImL0g0101Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0100011010),np.max(EigenValImL0g0100011020),np.max(EigenValImL0g0100011030),np.max(EigenValImL0g0100011040),np.max(EigenValImL0g0100011050)], 1)[[1]]
MaxEigenValImL0g0101Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0100021010),np.max(EigenValImL0g0100021020),np.max(EigenValImL0g0100021030),np.max(EigenValImL0g0100021040),np.max(EigenValImL0g0100021050)], 1)[[1]]
MaxEigenValImL0g0101Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0100031010),np.max(EigenValImL0g0100031020),np.max(EigenValImL0g0100031030),np.max(EigenValImL0g0100031040),np.max(EigenValImL0g0100031050)], 1)[[1]]
MaxEigenValImL0g0101Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0100051010),np.max(EigenValImL0g0100051020),np.max(EigenValImL0g0100051030),np.max(EigenValImL0g0100051040),np.max(EigenValImL0g0100051050)], 1)[[1]]
MaxEigenValImL0g0101Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0100071010),np.max(EigenValImL0g0100071020),np.max(EigenValImL0g0100071030),np.max(EigenValImL0g0100071040),np.max(EigenValImL0g0100071050)], 1)[[1]]
MaxEigenValImL0g0101Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL0g0100101010),np.max(EigenValImL0g0100101020),np.max(EigenValImL0g0100101030),np.max(EigenValImL0g0100101040),np.max(EigenValImL0g0100101050)], 1)[[1]]


########################################################################
########################################################################
























































































































########################################################################
########################################################################

dataL2g000_30011010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK001/N030/HamVals.txt')

MomentumAxL2g000_30011010 = dataL2g000_30011010[:,][:,5*0+0]
KineticEneL2g000_30011010 = dataL2g000_30011010[:,][:,5*0+1]
SelfEnergyL2g000_30011010 = dataL2g000_30011010[:,][:,5*0+2]
EigenValReL2g000_30011010 = dataL2g000_30011010[:,][:,5*0+3]
EigenValImL2g000_30011010 = dataL2g000_30011010[:,][:,5*0+4]

dataL2g000_30011020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK001/N040/HamVals.txt')

MomentumAxL2g000_30011020 = dataL2g000_30011020[:,][:,5*0+0]
KineticEneL2g000_30011020 = dataL2g000_30011020[:,][:,5*0+1]
SelfEnergyL2g000_30011020 = dataL2g000_30011020[:,][:,5*0+2]
EigenValReL2g000_30011020 = dataL2g000_30011020[:,][:,5*0+3]
EigenValImL2g000_30011020 = dataL2g000_30011020[:,][:,5*0+4]

dataL2g000_30011030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK001/N050/HamVals.txt')

MomentumAxL2g000_30011030 = dataL2g000_30011030[:,][:,5*0+0]
KineticEneL2g000_30011030 = dataL2g000_30011030[:,][:,5*0+1]
SelfEnergyL2g000_30011030 = dataL2g000_30011030[:,][:,5*0+2]
EigenValReL2g000_30011030 = dataL2g000_30011030[:,][:,5*0+3]
EigenValImL2g000_30011030 = dataL2g000_30011030[:,][:,5*0+4]

dataL2g000_30011040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK001/N060/HamVals.txt')

MomentumAxL2g000_30011040 = dataL2g000_30011040[:,][:,5*0+0]
KineticEneL2g000_30011040 = dataL2g000_30011040[:,][:,5*0+1]
SelfEnergyL2g000_30011040 = dataL2g000_30011040[:,][:,5*0+2]
EigenValReL2g000_30011040 = dataL2g000_30011040[:,][:,5*0+3]
EigenValImL2g000_30011040 = dataL2g000_30011040[:,][:,5*0+4]

dataL2g000_30011050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK001/N070/HamVals.txt')

MomentumAxL2g000_30011050 = dataL2g000_30011050[:,][:,5*0+0]
KineticEneL2g000_30011050 = dataL2g000_30011050[:,][:,5*0+1]
SelfEnergyL2g000_30011050 = dataL2g000_30011050[:,][:,5*0+2]
EigenValReL2g000_30011050 = dataL2g000_30011050[:,][:,5*0+3]
EigenValImL2g000_30011050 = dataL2g000_30011050[:,][:,5*0+4]

dataL2g000_30021010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK002/N030/HamVals.txt')

MomentumAxL2g000_30021010 = dataL2g000_30021010[:,][:,5*0+0]
KineticEneL2g000_30021010 = dataL2g000_30021010[:,][:,5*0+1]
SelfEnergyL2g000_30021010 = dataL2g000_30021010[:,][:,5*0+2]
EigenValReL2g000_30021010 = dataL2g000_30021010[:,][:,5*0+3]
EigenValImL2g000_30021010 = dataL2g000_30021010[:,][:,5*0+4]

dataL2g000_30021020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK002/N040/HamVals.txt')

MomentumAxL2g000_30021020 = dataL2g000_30021020[:,][:,5*0+0]
KineticEneL2g000_30021020 = dataL2g000_30021020[:,][:,5*0+1]
SelfEnergyL2g000_30021020 = dataL2g000_30021020[:,][:,5*0+2]
EigenValReL2g000_30021020 = dataL2g000_30021020[:,][:,5*0+3]
EigenValImL2g000_30021020 = dataL2g000_30021020[:,][:,5*0+4]

dataL2g000_30021030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK002/N050/HamVals.txt')

MomentumAxL2g000_30021030 = dataL2g000_30021030[:,][:,5*0+0]
KineticEneL2g000_30021030 = dataL2g000_30021030[:,][:,5*0+1]
SelfEnergyL2g000_30021030 = dataL2g000_30021030[:,][:,5*0+2]
EigenValReL2g000_30021030 = dataL2g000_30021030[:,][:,5*0+3]
EigenValImL2g000_30021030 = dataL2g000_30021030[:,][:,5*0+4]

dataL2g000_30021040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK002/N060/HamVals.txt')

MomentumAxL2g000_30021040 = dataL2g000_30021040[:,][:,5*0+0]
KineticEneL2g000_30021040 = dataL2g000_30021040[:,][:,5*0+1]
SelfEnergyL2g000_30021040 = dataL2g000_30021040[:,][:,5*0+2]
EigenValReL2g000_30021040 = dataL2g000_30021040[:,][:,5*0+3]
EigenValImL2g000_30021040 = dataL2g000_30021040[:,][:,5*0+4]

dataL2g000_30021050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK002/N070/HamVals.txt')

MomentumAxL2g000_30021050 = dataL2g000_30021050[:,][:,5*0+0]
KineticEneL2g000_30021050 = dataL2g000_30021050[:,][:,5*0+1]
SelfEnergyL2g000_30021050 = dataL2g000_30021050[:,][:,5*0+2]
EigenValReL2g000_30021050 = dataL2g000_30021050[:,][:,5*0+3]
EigenValImL2g000_30021050 = dataL2g000_30021050[:,][:,5*0+4]

dataL2g000_30051010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK005/N010/HamVals.txt')

MomentumAxL2g000_30051010 = dataL2g000_30051010[:,][:,5*0+0]
KineticEneL2g000_30051010 = dataL2g000_30051010[:,][:,5*0+1]
SelfEnergyL2g000_30051010 = dataL2g000_30051010[:,][:,5*0+2]
EigenValReL2g000_30051010 = dataL2g000_30051010[:,][:,5*0+3]
EigenValImL2g000_30051010 = dataL2g000_30051010[:,][:,5*0+4]

dataL2g000_30051020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK005/N020/HamVals.txt')

MomentumAxL2g000_30051020 = dataL2g000_30051020[:,][:,5*0+0]
KineticEneL2g000_30051020 = dataL2g000_30051020[:,][:,5*0+1]
SelfEnergyL2g000_30051020 = dataL2g000_30051020[:,][:,5*0+2]
EigenValReL2g000_30051020 = dataL2g000_30051020[:,][:,5*0+3]
EigenValImL2g000_30051020 = dataL2g000_30051020[:,][:,5*0+4]

dataL2g000_30051030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK005/N030/HamVals.txt')

MomentumAxL2g000_30051030 = dataL2g000_30051030[:,][:,5*0+0]
KineticEneL2g000_30051030 = dataL2g000_30051030[:,][:,5*0+1]
SelfEnergyL2g000_30051030 = dataL2g000_30051030[:,][:,5*0+2]
EigenValReL2g000_30051030 = dataL2g000_30051030[:,][:,5*0+3]
EigenValImL2g000_30051030 = dataL2g000_30051030[:,][:,5*0+4]

dataL2g000_30051040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK005/N040/HamVals.txt')

MomentumAxL2g000_30051040 = dataL2g000_30051040[:,][:,5*0+0]
KineticEneL2g000_30051040 = dataL2g000_30051040[:,][:,5*0+1]
SelfEnergyL2g000_30051040 = dataL2g000_30051040[:,][:,5*0+2]
EigenValReL2g000_30051040 = dataL2g000_30051040[:,][:,5*0+3]
EigenValImL2g000_30051040 = dataL2g000_30051040[:,][:,5*0+4]

dataL2g000_30051050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK005/N050/HamVals.txt')

MomentumAxL2g000_30051050 = dataL2g000_30051050[:,][:,5*0+0]
KineticEneL2g000_30051050 = dataL2g000_30051050[:,][:,5*0+1]
SelfEnergyL2g000_30051050 = dataL2g000_30051050[:,][:,5*0+2]
EigenValReL2g000_30051050 = dataL2g000_30051050[:,][:,5*0+3]
EigenValImL2g000_30051050 = dataL2g000_30051050[:,][:,5*0+4]

dataL2g000_30101010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK010/N010/HamVals.txt')

MomentumAxL2g000_30101010 = dataL2g000_30101010[:,][:,5*0+0]
KineticEneL2g000_30101010 = dataL2g000_30101010[:,][:,5*0+1]
SelfEnergyL2g000_30101010 = dataL2g000_30101010[:,][:,5*0+2]
EigenValReL2g000_30101010 = dataL2g000_30101010[:,][:,5*0+3]
EigenValImL2g000_30101010 = dataL2g000_30101010[:,][:,5*0+4]

dataL2g000_30101020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK010/N020/HamVals.txt')

MomentumAxL2g000_30101020 = dataL2g000_30101020[:,][:,5*0+0]
KineticEneL2g000_30101020 = dataL2g000_30101020[:,][:,5*0+1]
SelfEnergyL2g000_30101020 = dataL2g000_30101020[:,][:,5*0+2]
EigenValReL2g000_30101020 = dataL2g000_30101020[:,][:,5*0+3]
EigenValImL2g000_30101020 = dataL2g000_30101020[:,][:,5*0+4]

dataL2g000_30101030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK010/N030/HamVals.txt')

MomentumAxL2g000_30101030 = dataL2g000_30101030[:,][:,5*0+0]
KineticEneL2g000_30101030 = dataL2g000_30101030[:,][:,5*0+1]
SelfEnergyL2g000_30101030 = dataL2g000_30101030[:,][:,5*0+2]
EigenValReL2g000_30101030 = dataL2g000_30101030[:,][:,5*0+3]
EigenValImL2g000_30101030 = dataL2g000_30101030[:,][:,5*0+4]

dataL2g000_30101040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK010/N040/HamVals.txt')

MomentumAxL2g000_30101040 = dataL2g000_30101040[:,][:,5*0+0]
KineticEneL2g000_30101040 = dataL2g000_30101040[:,][:,5*0+1]
SelfEnergyL2g000_30101040 = dataL2g000_30101040[:,][:,5*0+2]
EigenValReL2g000_30101040 = dataL2g000_30101040[:,][:,5*0+3]
EigenValImL2g000_30101040 = dataL2g000_30101040[:,][:,5*0+4]

dataL2g000_30101050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK010/N050/HamVals.txt')

MomentumAxL2g000_30101050 = dataL2g000_30101050[:,][:,5*0+0]
KineticEneL2g000_30101050 = dataL2g000_30101050[:,][:,5*0+1]
SelfEnergyL2g000_30101050 = dataL2g000_30101050[:,][:,5*0+2]
EigenValReL2g000_30101050 = dataL2g000_30101050[:,][:,5*0+3]
EigenValImL2g000_30101050 = dataL2g000_30101050[:,][:,5*0+4]

"""
dataL2g000_30201010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK020/N010/HamVals.txt')

MomentumAxL2g000_30201010 = dataL2g000_30201010[:,][:,5*0+0]
KineticEneL2g000_30201010 = dataL2g000_30201010[:,][:,5*0+1]
SelfEnergyL2g000_30201010 = dataL2g000_30201010[:,][:,5*0+2]
EigenValReL2g000_30201010 = dataL2g000_30201010[:,][:,5*0+3]
EigenValImL2g000_30201010 = dataL2g000_30201010[:,][:,5*0+4]

dataL2g000_30201020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK020/N020/HamVals.txt')

MomentumAxL2g000_30201020 = dataL2g000_30201020[:,][:,5*0+0]
KineticEneL2g000_30201020 = dataL2g000_30201020[:,][:,5*0+1]
SelfEnergyL2g000_30201020 = dataL2g000_30201020[:,][:,5*0+2]
EigenValReL2g000_30201020 = dataL2g000_30201020[:,][:,5*0+3]
EigenValImL2g000_30201020 = dataL2g000_30201020[:,][:,5*0+4]

dataL2g000_30201030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK020/N030/HamVals.txt')

MomentumAxL2g000_30201030 = dataL2g000_30201030[:,][:,5*0+0]
KineticEneL2g000_30201030 = dataL2g000_30201030[:,][:,5*0+1]
SelfEnergyL2g000_30201030 = dataL2g000_30201030[:,][:,5*0+2]
EigenValReL2g000_30201030 = dataL2g000_30201030[:,][:,5*0+3]
EigenValImL2g000_30201030 = dataL2g000_30201030[:,][:,5*0+4]

dataL2g000_30201040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK020/N040/HamVals.txt')

MomentumAxL2g000_30201040 = dataL2g000_30201040[:,][:,5*0+0]
KineticEneL2g000_30201040 = dataL2g000_30201040[:,][:,5*0+1]
SelfEnergyL2g000_30201040 = dataL2g000_30201040[:,][:,5*0+2]
EigenValReL2g000_30201040 = dataL2g000_30201040[:,][:,5*0+3]
EigenValImL2g000_30201040 = dataL2g000_30201040[:,][:,5*0+4]

dataL2g000_30201050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-30/aK020/N050/HamVals.txt')

MomentumAxL2g000_30201050 = dataL2g000_30201050[:,][:,5*0+0]
KineticEneL2g000_30201050 = dataL2g000_30201050[:,][:,5*0+1]
SelfEnergyL2g000_30201050 = dataL2g000_30201050[:,][:,5*0+2]
EigenValReL2g000_30201050 = dataL2g000_30201050[:,][:,5*0+3]
EigenValImL2g000_30201050 = dataL2g000_30201050[:,][:,5*0+4]
"""

MaxEigenValImL2g000_31010 = np.zeros((4))
MaxEigenValImL2g000_31020 = np.zeros((4))
MaxEigenValImL2g000_31030 = np.zeros((4))
MaxEigenValImL2g000_31040 = np.zeros((4))
MaxEigenValImL2g000_31050 = np.zeros((4))
MaxEigenValImL2g000_31Inf = np.zeros((4))

MaxEigenValImL2g000_31010[0] = np.max(EigenValImL2g000_30011010)
MaxEigenValImL2g000_31010[1] = np.max(EigenValImL2g000_30021010)
MaxEigenValImL2g000_31010[2] = np.max(EigenValImL2g000_30051010)
MaxEigenValImL2g000_31010[3] = np.max(EigenValImL2g000_30101010)
#MaxEigenValImL2g000_31010[4] = np.max(EigenValImL2g000_30201010)

MaxEigenValImL2g000_31020[0] = np.max(EigenValImL2g000_30011020)
MaxEigenValImL2g000_31020[1] = np.max(EigenValImL2g000_30021020)
MaxEigenValImL2g000_31020[2] = np.max(EigenValImL2g000_30051020)
MaxEigenValImL2g000_31020[3] = np.max(EigenValImL2g000_30101020)
#MaxEigenValImL2g000_31020[4] = np.max(EigenValImL2g000_30201020)

MaxEigenValImL2g000_31030[0] = np.max(EigenValImL2g000_30011030)
MaxEigenValImL2g000_31030[1] = np.max(EigenValImL2g000_30021030)
MaxEigenValImL2g000_31030[2] = np.max(EigenValImL2g000_30051030)
MaxEigenValImL2g000_31030[3] = np.max(EigenValImL2g000_30101030)
#MaxEigenValImL2g000_31030[4] = np.max(EigenValImL2g000_30201030)

MaxEigenValImL2g000_31040[0] = np.max(EigenValImL2g000_30011040)
MaxEigenValImL2g000_31040[1] = np.max(EigenValImL2g000_30021040)
MaxEigenValImL2g000_31040[2] = np.max(EigenValImL2g000_30051040)
MaxEigenValImL2g000_31040[3] = np.max(EigenValImL2g000_30101040)
#MaxEigenValImL2g000_31040[4] = np.max(EigenValImL2g000_30201040)

MaxEigenValImL2g000_31050[0] = np.max(EigenValImL2g000_30011050)
MaxEigenValImL2g000_31050[1] = np.max(EigenValImL2g000_30021050)
MaxEigenValImL2g000_31050[2] = np.max(EigenValImL2g000_30051050)
MaxEigenValImL2g000_31050[3] = np.max(EigenValImL2g000_30101050)
#MaxEigenValImL2g000_31050[4] = np.max(EigenValImL2g000_30201050)

MaxEigenValImL2g000_31Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_31010[0],MaxEigenValImL2g000_31020[0],MaxEigenValImL2g000_31030[0],MaxEigenValImL2g000_31040[0],MaxEigenValImL2g000_31050[0]], 1)[[1]]
MaxEigenValImL2g000_31Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_31010[1],MaxEigenValImL2g000_31020[1],MaxEigenValImL2g000_31030[1],MaxEigenValImL2g000_31040[1],MaxEigenValImL2g000_31050[1]], 1)[[1]]
MaxEigenValImL2g000_31Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_31010[2],MaxEigenValImL2g000_31020[2],MaxEigenValImL2g000_31030[2],MaxEigenValImL2g000_31040[2],MaxEigenValImL2g000_31050[2]], 1)[[1]]
MaxEigenValImL2g000_31Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_31010[3],MaxEigenValImL2g000_31020[3],MaxEigenValImL2g000_31030[3],MaxEigenValImL2g000_31040[3],MaxEigenValImL2g000_31050[3]], 1)[[1]]
#MaxEigenValImL2g000_31Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_31010[4],MaxEigenValImL2g000_31020[4],MaxEigenValImL2g000_31030[4],MaxEigenValImL2g000_31040[4],MaxEigenValImL2g000_31050[4]], 1)[[1]]

########################################################################

dataL2g000_40011010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK001/N060/HamVals.txt')

MomentumAxL2g000_40011010 = dataL2g000_40011010[:,][:,5*0+0]
KineticEneL2g000_40011010 = dataL2g000_40011010[:,][:,5*0+1]
SelfEnergyL2g000_40011010 = dataL2g000_40011010[:,][:,5*0+2]
EigenValReL2g000_40011010 = dataL2g000_40011010[:,][:,5*0+3]
EigenValImL2g000_40011010 = dataL2g000_40011010[:,][:,5*0+4]

dataL2g000_40011020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK001/N070/HamVals.txt')

MomentumAxL2g000_40011020 = dataL2g000_40011020[:,][:,5*0+0]
KineticEneL2g000_40011020 = dataL2g000_40011020[:,][:,5*0+1]
SelfEnergyL2g000_40011020 = dataL2g000_40011020[:,][:,5*0+2]
EigenValReL2g000_40011020 = dataL2g000_40011020[:,][:,5*0+3]
EigenValImL2g000_40011020 = dataL2g000_40011020[:,][:,5*0+4]

dataL2g000_40011030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK001/N080/HamVals.txt')

MomentumAxL2g000_40011030 = dataL2g000_40011030[:,][:,5*0+0]
KineticEneL2g000_40011030 = dataL2g000_40011030[:,][:,5*0+1]
SelfEnergyL2g000_40011030 = dataL2g000_40011030[:,][:,5*0+2]
EigenValReL2g000_40011030 = dataL2g000_40011030[:,][:,5*0+3]
EigenValImL2g000_40011030 = dataL2g000_40011030[:,][:,5*0+4]

dataL2g000_40011040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK001/N090/HamVals.txt')

MomentumAxL2g000_40011040 = dataL2g000_40011040[:,][:,5*0+0]
KineticEneL2g000_40011040 = dataL2g000_40011040[:,][:,5*0+1]
SelfEnergyL2g000_40011040 = dataL2g000_40011040[:,][:,5*0+2]
EigenValReL2g000_40011040 = dataL2g000_40011040[:,][:,5*0+3]
EigenValImL2g000_40011040 = dataL2g000_40011040[:,][:,5*0+4]

dataL2g000_40011050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK001/N100/HamVals.txt')

MomentumAxL2g000_40011050 = dataL2g000_40011050[:,][:,5*0+0]
KineticEneL2g000_40011050 = dataL2g000_40011050[:,][:,5*0+1]
SelfEnergyL2g000_40011050 = dataL2g000_40011050[:,][:,5*0+2]
EigenValReL2g000_40011050 = dataL2g000_40011050[:,][:,5*0+3]
EigenValImL2g000_40011050 = dataL2g000_40011050[:,][:,5*0+4]

dataL2g000_40021010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK002/N010/HamVals.txt')

MomentumAxL2g000_40021010 = dataL2g000_40021010[:,][:,5*0+0]
KineticEneL2g000_40021010 = dataL2g000_40021010[:,][:,5*0+1]
SelfEnergyL2g000_40021010 = dataL2g000_40021010[:,][:,5*0+2]
EigenValReL2g000_40021010 = dataL2g000_40021010[:,][:,5*0+3]
EigenValImL2g000_40021010 = dataL2g000_40021010[:,][:,5*0+4]

dataL2g000_40021020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK002/N020/HamVals.txt')

MomentumAxL2g000_40021020 = dataL2g000_40021020[:,][:,5*0+0]
KineticEneL2g000_40021020 = dataL2g000_40021020[:,][:,5*0+1]
SelfEnergyL2g000_40021020 = dataL2g000_40021020[:,][:,5*0+2]
EigenValReL2g000_40021020 = dataL2g000_40021020[:,][:,5*0+3]
EigenValImL2g000_40021020 = dataL2g000_40021020[:,][:,5*0+4]

dataL2g000_40021030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK002/N030/HamVals.txt')

MomentumAxL2g000_40021030 = dataL2g000_40021030[:,][:,5*0+0]
KineticEneL2g000_40021030 = dataL2g000_40021030[:,][:,5*0+1]
SelfEnergyL2g000_40021030 = dataL2g000_40021030[:,][:,5*0+2]
EigenValReL2g000_40021030 = dataL2g000_40021030[:,][:,5*0+3]
EigenValImL2g000_40021030 = dataL2g000_40021030[:,][:,5*0+4]

dataL2g000_40021040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK002/N040/HamVals.txt')

MomentumAxL2g000_40021040 = dataL2g000_40021040[:,][:,5*0+0]
KineticEneL2g000_40021040 = dataL2g000_40021040[:,][:,5*0+1]
SelfEnergyL2g000_40021040 = dataL2g000_40021040[:,][:,5*0+2]
EigenValReL2g000_40021040 = dataL2g000_40021040[:,][:,5*0+3]
EigenValImL2g000_40021040 = dataL2g000_40021040[:,][:,5*0+4]

dataL2g000_40021050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK002/N050/HamVals.txt')

MomentumAxL2g000_40021050 = dataL2g000_40021050[:,][:,5*0+0]
KineticEneL2g000_40021050 = dataL2g000_40021050[:,][:,5*0+1]
SelfEnergyL2g000_40021050 = dataL2g000_40021050[:,][:,5*0+2]
EigenValReL2g000_40021050 = dataL2g000_40021050[:,][:,5*0+3]
EigenValImL2g000_40021050 = dataL2g000_40021050[:,][:,5*0+4]

dataL2g000_40051010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK005/N010/HamVals.txt')

MomentumAxL2g000_40051010 = dataL2g000_40051010[:,][:,5*0+0]
KineticEneL2g000_40051010 = dataL2g000_40051010[:,][:,5*0+1]
SelfEnergyL2g000_40051010 = dataL2g000_40051010[:,][:,5*0+2]
EigenValReL2g000_40051010 = dataL2g000_40051010[:,][:,5*0+3]
EigenValImL2g000_40051010 = dataL2g000_40051010[:,][:,5*0+4]

dataL2g000_40051020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK005/N020/HamVals.txt')

MomentumAxL2g000_40051020 = dataL2g000_40051020[:,][:,5*0+0]
KineticEneL2g000_40051020 = dataL2g000_40051020[:,][:,5*0+1]
SelfEnergyL2g000_40051020 = dataL2g000_40051020[:,][:,5*0+2]
EigenValReL2g000_40051020 = dataL2g000_40051020[:,][:,5*0+3]
EigenValImL2g000_40051020 = dataL2g000_40051020[:,][:,5*0+4]

dataL2g000_40051030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK005/N030/HamVals.txt')

MomentumAxL2g000_40051030 = dataL2g000_40051030[:,][:,5*0+0]
KineticEneL2g000_40051030 = dataL2g000_40051030[:,][:,5*0+1]
SelfEnergyL2g000_40051030 = dataL2g000_40051030[:,][:,5*0+2]
EigenValReL2g000_40051030 = dataL2g000_40051030[:,][:,5*0+3]
EigenValImL2g000_40051030 = dataL2g000_40051030[:,][:,5*0+4]

dataL2g000_40051040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK005/N040/HamVals.txt')

MomentumAxL2g000_40051040 = dataL2g000_40051040[:,][:,5*0+0]
KineticEneL2g000_40051040 = dataL2g000_40051040[:,][:,5*0+1]
SelfEnergyL2g000_40051040 = dataL2g000_40051040[:,][:,5*0+2]
EigenValReL2g000_40051040 = dataL2g000_40051040[:,][:,5*0+3]
EigenValImL2g000_40051040 = dataL2g000_40051040[:,][:,5*0+4]

dataL2g000_40051050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK005/N050/HamVals.txt')

MomentumAxL2g000_40051050 = dataL2g000_40051050[:,][:,5*0+0]
KineticEneL2g000_40051050 = dataL2g000_40051050[:,][:,5*0+1]
SelfEnergyL2g000_40051050 = dataL2g000_40051050[:,][:,5*0+2]
EigenValReL2g000_40051050 = dataL2g000_40051050[:,][:,5*0+3]
EigenValImL2g000_40051050 = dataL2g000_40051050[:,][:,5*0+4]

dataL2g000_40101010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK010/N010/HamVals.txt')

MomentumAxL2g000_40101010 = dataL2g000_40101010[:,][:,5*0+0]
KineticEneL2g000_40101010 = dataL2g000_40101010[:,][:,5*0+1]
SelfEnergyL2g000_40101010 = dataL2g000_40101010[:,][:,5*0+2]
EigenValReL2g000_40101010 = dataL2g000_40101010[:,][:,5*0+3]
EigenValImL2g000_40101010 = dataL2g000_40101010[:,][:,5*0+4]

dataL2g000_40101020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK010/N020/HamVals.txt')

MomentumAxL2g000_40101020 = dataL2g000_40101020[:,][:,5*0+0]
KineticEneL2g000_40101020 = dataL2g000_40101020[:,][:,5*0+1]
SelfEnergyL2g000_40101020 = dataL2g000_40101020[:,][:,5*0+2]
EigenValReL2g000_40101020 = dataL2g000_40101020[:,][:,5*0+3]
EigenValImL2g000_40101020 = dataL2g000_40101020[:,][:,5*0+4]

dataL2g000_40101030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK010/N030/HamVals.txt')

MomentumAxL2g000_40101030 = dataL2g000_40101030[:,][:,5*0+0]
KineticEneL2g000_40101030 = dataL2g000_40101030[:,][:,5*0+1]
SelfEnergyL2g000_40101030 = dataL2g000_40101030[:,][:,5*0+2]
EigenValReL2g000_40101030 = dataL2g000_40101030[:,][:,5*0+3]
EigenValImL2g000_40101030 = dataL2g000_40101030[:,][:,5*0+4]

dataL2g000_40101040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK010/N040/HamVals.txt')

MomentumAxL2g000_40101040 = dataL2g000_40101040[:,][:,5*0+0]
KineticEneL2g000_40101040 = dataL2g000_40101040[:,][:,5*0+1]
SelfEnergyL2g000_40101040 = dataL2g000_40101040[:,][:,5*0+2]
EigenValReL2g000_40101040 = dataL2g000_40101040[:,][:,5*0+3]
EigenValImL2g000_40101040 = dataL2g000_40101040[:,][:,5*0+4]

dataL2g000_40101050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK010/N050/HamVals.txt')

MomentumAxL2g000_40101050 = dataL2g000_40101050[:,][:,5*0+0]
KineticEneL2g000_40101050 = dataL2g000_40101050[:,][:,5*0+1]
SelfEnergyL2g000_40101050 = dataL2g000_40101050[:,][:,5*0+2]
EigenValReL2g000_40101050 = dataL2g000_40101050[:,][:,5*0+3]
EigenValImL2g000_40101050 = dataL2g000_40101050[:,][:,5*0+4]
"""
dataL2g000_40201010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK020/N010/HamVals.txt')

MomentumAxL2g000_40201010 = dataL2g000_40201010[:,][:,5*0+0]
KineticEneL2g000_40201010 = dataL2g000_40201010[:,][:,5*0+1]
SelfEnergyL2g000_40201010 = dataL2g000_40201010[:,][:,5*0+2]
EigenValReL2g000_40201010 = dataL2g000_40201010[:,][:,5*0+3]
EigenValImL2g000_40201010 = dataL2g000_40201010[:,][:,5*0+4]

dataL2g000_40201020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK020/N020/HamVals.txt')

MomentumAxL2g000_40201020 = dataL2g000_40201020[:,][:,5*0+0]
KineticEneL2g000_40201020 = dataL2g000_40201020[:,][:,5*0+1]
SelfEnergyL2g000_40201020 = dataL2g000_40201020[:,][:,5*0+2]
EigenValReL2g000_40201020 = dataL2g000_40201020[:,][:,5*0+3]
EigenValImL2g000_40201020 = dataL2g000_40201020[:,][:,5*0+4]

dataL2g000_40201030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK020/N030/HamVals.txt')

MomentumAxL2g000_40201030 = dataL2g000_40201030[:,][:,5*0+0]
KineticEneL2g000_40201030 = dataL2g000_40201030[:,][:,5*0+1]
SelfEnergyL2g000_40201030 = dataL2g000_40201030[:,][:,5*0+2]
EigenValReL2g000_40201030 = dataL2g000_40201030[:,][:,5*0+3]
EigenValImL2g000_40201030 = dataL2g000_40201030[:,][:,5*0+4]

dataL2g000_40201040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK020/N040/HamVals.txt')

MomentumAxL2g000_40201040 = dataL2g000_40201040[:,][:,5*0+0]
KineticEneL2g000_40201040 = dataL2g000_40201040[:,][:,5*0+1]
SelfEnergyL2g000_40201040 = dataL2g000_40201040[:,][:,5*0+2]
EigenValReL2g000_40201040 = dataL2g000_40201040[:,][:,5*0+3]
EigenValImL2g000_40201040 = dataL2g000_40201040[:,][:,5*0+4]

dataL2g000_40201050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-40/aK020/N050/HamVals.txt')

MomentumAxL2g000_40201050 = dataL2g000_40201050[:,][:,5*0+0]
KineticEneL2g000_40201050 = dataL2g000_40201050[:,][:,5*0+1]
SelfEnergyL2g000_40201050 = dataL2g000_40201050[:,][:,5*0+2]
EigenValReL2g000_40201050 = dataL2g000_40201050[:,][:,5*0+3]
EigenValImL2g000_40201050 = dataL2g000_40201050[:,][:,5*0+4]
"""
MaxEigenValImL2g000_41010 = np.zeros((4))
MaxEigenValImL2g000_41020 = np.zeros((4))
MaxEigenValImL2g000_41030 = np.zeros((4))
MaxEigenValImL2g000_41040 = np.zeros((4))
MaxEigenValImL2g000_41050 = np.zeros((4))
MaxEigenValImL2g000_41Inf = np.zeros((4))

MaxEigenValImL2g000_41010[0] = np.max(EigenValImL2g000_40011010)
MaxEigenValImL2g000_41010[1] = np.max(EigenValImL2g000_40021010)
MaxEigenValImL2g000_41010[2] = np.max(EigenValImL2g000_40051010)
MaxEigenValImL2g000_41010[3] = np.max(EigenValImL2g000_40101010)
#MaxEigenValImL2g000_41010[4] = np.max(EigenValImL2g000_40201010)

MaxEigenValImL2g000_41020[0] = np.max(EigenValImL2g000_40011020)
MaxEigenValImL2g000_41020[1] = np.max(EigenValImL2g000_40021020)
MaxEigenValImL2g000_41020[2] = np.max(EigenValImL2g000_40051020)
MaxEigenValImL2g000_41020[3] = np.max(EigenValImL2g000_40101020)
#MaxEigenValImL2g000_41020[4] = np.max(EigenValImL2g000_40201020)

MaxEigenValImL2g000_41030[0] = np.max(EigenValImL2g000_40011030)
MaxEigenValImL2g000_41030[1] = np.max(EigenValImL2g000_40021030)
MaxEigenValImL2g000_41030[2] = np.max(EigenValImL2g000_40051030)
MaxEigenValImL2g000_41030[3] = np.max(EigenValImL2g000_40101030)
#MaxEigenValImL2g000_41030[4] = np.max(EigenValImL2g000_40201030)

MaxEigenValImL2g000_41040[0] = np.max(EigenValImL2g000_40011040)
MaxEigenValImL2g000_41040[1] = np.max(EigenValImL2g000_40021040)
MaxEigenValImL2g000_41040[2] = np.max(EigenValImL2g000_40051040)
MaxEigenValImL2g000_41040[3] = np.max(EigenValImL2g000_40101040)
#MaxEigenValImL2g000_41040[4] = np.max(EigenValImL2g000_40201040)

MaxEigenValImL2g000_41050[0] = np.max(EigenValImL2g000_40011050)
MaxEigenValImL2g000_41050[1] = np.max(EigenValImL2g000_40021050)
MaxEigenValImL2g000_41050[2] = np.max(EigenValImL2g000_40051050)
MaxEigenValImL2g000_41050[3] = np.max(EigenValImL2g000_40101050)
#MaxEigenValImL2g000_41050[4] = np.max(EigenValImL2g000_40201050)

fiveSizesA = [1./60,1./70,1./80,1./90,1./100]
fiveSizesB = [1./70,1./80,1./90]

#MaxEigenValImL2g000_41Inf[0] = np.polyfit(fiveSizesA, [MaxEigenValImL2g000_41010[0],MaxEigenValImL2g000_41020[0],MaxEigenValImL2g000_41030[0],MaxEigenValImL2g000_41040[0],MaxEigenValImL2g000_41050[0]], 1)[[1]]
MaxEigenValImL2g000_41Inf[0] = np.polyfit(fiveSizesB, [MaxEigenValImL2g000_41020[0],MaxEigenValImL2g000_41030[0],MaxEigenValImL2g000_41040[0]], 1)[[1]]
MaxEigenValImL2g000_41Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_41010[1],MaxEigenValImL2g000_41020[1],MaxEigenValImL2g000_41030[1],MaxEigenValImL2g000_41040[1],MaxEigenValImL2g000_41050[1]], 1)[[1]]
MaxEigenValImL2g000_41Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_41010[2],MaxEigenValImL2g000_41020[2],MaxEigenValImL2g000_41030[2],MaxEigenValImL2g000_41040[2],MaxEigenValImL2g000_41050[2]], 1)[[1]]
MaxEigenValImL2g000_41Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_41010[3],MaxEigenValImL2g000_41020[3],MaxEigenValImL2g000_41030[3],MaxEigenValImL2g000_41040[3],MaxEigenValImL2g000_41050[3]], 1)[[1]]
#MaxEigenValImL2g000_41Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_41010[4],MaxEigenValImL2g000_41020[4],MaxEigenValImL2g000_41030[4],MaxEigenValImL2g000_41040[4],MaxEigenValImL2g000_41050[4]], 1)[[1]]

########################################################################

dataL2g000_50011010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK001/N010/HamVals.txt')

MomentumAxL2g000_50011010 = dataL2g000_50011010[:,][:,5*0+0]
KineticEneL2g000_50011010 = dataL2g000_50011010[:,][:,5*0+1]
SelfEnergyL2g000_50011010 = dataL2g000_50011010[:,][:,5*0+2]
EigenValReL2g000_50011010 = dataL2g000_50011010[:,][:,5*0+3]
EigenValImL2g000_50011010 = dataL2g000_50011010[:,][:,5*0+4]

dataL2g000_50011020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK001/N020/HamVals.txt')

MomentumAxL2g000_50011020 = dataL2g000_50011020[:,][:,5*0+0]
KineticEneL2g000_50011020 = dataL2g000_50011020[:,][:,5*0+1]
SelfEnergyL2g000_50011020 = dataL2g000_50011020[:,][:,5*0+2]
EigenValReL2g000_50011020 = dataL2g000_50011020[:,][:,5*0+3]
EigenValImL2g000_50011020 = dataL2g000_50011020[:,][:,5*0+4]

dataL2g000_50011030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK001/N030/HamVals.txt')

MomentumAxL2g000_50011030 = dataL2g000_50011030[:,][:,5*0+0]
KineticEneL2g000_50011030 = dataL2g000_50011030[:,][:,5*0+1]
SelfEnergyL2g000_50011030 = dataL2g000_50011030[:,][:,5*0+2]
EigenValReL2g000_50011030 = dataL2g000_50011030[:,][:,5*0+3]
EigenValImL2g000_50011030 = dataL2g000_50011030[:,][:,5*0+4]

dataL2g000_50011040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK001/N040/HamVals.txt')

MomentumAxL2g000_50011040 = dataL2g000_50011040[:,][:,5*0+0]
KineticEneL2g000_50011040 = dataL2g000_50011040[:,][:,5*0+1]
SelfEnergyL2g000_50011040 = dataL2g000_50011040[:,][:,5*0+2]
EigenValReL2g000_50011040 = dataL2g000_50011040[:,][:,5*0+3]
EigenValImL2g000_50011040 = dataL2g000_50011040[:,][:,5*0+4]

dataL2g000_50011050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK001/N050/HamVals.txt')

MomentumAxL2g000_50011050 = dataL2g000_50011050[:,][:,5*0+0]
KineticEneL2g000_50011050 = dataL2g000_50011050[:,][:,5*0+1]
SelfEnergyL2g000_50011050 = dataL2g000_50011050[:,][:,5*0+2]
EigenValReL2g000_50011050 = dataL2g000_50011050[:,][:,5*0+3]
EigenValImL2g000_50011050 = dataL2g000_50011050[:,][:,5*0+4]

dataL2g000_50021010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK002/N010/HamVals.txt')

MomentumAxL2g000_50021010 = dataL2g000_50021010[:,][:,5*0+0]
KineticEneL2g000_50021010 = dataL2g000_50021010[:,][:,5*0+1]
SelfEnergyL2g000_50021010 = dataL2g000_50021010[:,][:,5*0+2]
EigenValReL2g000_50021010 = dataL2g000_50021010[:,][:,5*0+3]
EigenValImL2g000_50021010 = dataL2g000_50021010[:,][:,5*0+4]

dataL2g000_50021020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK002/N020/HamVals.txt')

MomentumAxL2g000_50021020 = dataL2g000_50021020[:,][:,5*0+0]
KineticEneL2g000_50021020 = dataL2g000_50021020[:,][:,5*0+1]
SelfEnergyL2g000_50021020 = dataL2g000_50021020[:,][:,5*0+2]
EigenValReL2g000_50021020 = dataL2g000_50021020[:,][:,5*0+3]
EigenValImL2g000_50021020 = dataL2g000_50021020[:,][:,5*0+4]

dataL2g000_50021030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK002/N030/HamVals.txt')

MomentumAxL2g000_50021030 = dataL2g000_50021030[:,][:,5*0+0]
KineticEneL2g000_50021030 = dataL2g000_50021030[:,][:,5*0+1]
SelfEnergyL2g000_50021030 = dataL2g000_50021030[:,][:,5*0+2]
EigenValReL2g000_50021030 = dataL2g000_50021030[:,][:,5*0+3]
EigenValImL2g000_50021030 = dataL2g000_50021030[:,][:,5*0+4]

dataL2g000_50021040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK002/N040/HamVals.txt')

MomentumAxL2g000_50021040 = dataL2g000_50021040[:,][:,5*0+0]
KineticEneL2g000_50021040 = dataL2g000_50021040[:,][:,5*0+1]
SelfEnergyL2g000_50021040 = dataL2g000_50021040[:,][:,5*0+2]
EigenValReL2g000_50021040 = dataL2g000_50021040[:,][:,5*0+3]
EigenValImL2g000_50021040 = dataL2g000_50021040[:,][:,5*0+4]

dataL2g000_50021050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK002/N050/HamVals.txt')

MomentumAxL2g000_50021050 = dataL2g000_50021050[:,][:,5*0+0]
KineticEneL2g000_50021050 = dataL2g000_50021050[:,][:,5*0+1]
SelfEnergyL2g000_50021050 = dataL2g000_50021050[:,][:,5*0+2]
EigenValReL2g000_50021050 = dataL2g000_50021050[:,][:,5*0+3]
EigenValImL2g000_50021050 = dataL2g000_50021050[:,][:,5*0+4]

dataL2g000_50031010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK003/N010/HamVals.txt')

MomentumAxL2g000_50031010 = dataL2g000_50031010[:,][:,5*0+0]
KineticEneL2g000_50031010 = dataL2g000_50031010[:,][:,5*0+1]
SelfEnergyL2g000_50031010 = dataL2g000_50031010[:,][:,5*0+2]
EigenValReL2g000_50031010 = dataL2g000_50031010[:,][:,5*0+3]
EigenValImL2g000_50031010 = dataL2g000_50031010[:,][:,5*0+4]

dataL2g000_50031020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK003/N020/HamVals.txt')

MomentumAxL2g000_50031020 = dataL2g000_50031020[:,][:,5*0+0]
KineticEneL2g000_50031020 = dataL2g000_50031020[:,][:,5*0+1]
SelfEnergyL2g000_50031020 = dataL2g000_50031020[:,][:,5*0+2]
EigenValReL2g000_50031020 = dataL2g000_50031020[:,][:,5*0+3]
EigenValImL2g000_50031020 = dataL2g000_50031020[:,][:,5*0+4]

dataL2g000_50031030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK003/N030/HamVals.txt')

MomentumAxL2g000_50031030 = dataL2g000_50031030[:,][:,5*0+0]
KineticEneL2g000_50031030 = dataL2g000_50031030[:,][:,5*0+1]
SelfEnergyL2g000_50031030 = dataL2g000_50031030[:,][:,5*0+2]
EigenValReL2g000_50031030 = dataL2g000_50031030[:,][:,5*0+3]
EigenValImL2g000_50031030 = dataL2g000_50031030[:,][:,5*0+4]

dataL2g000_50031040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK003/N040/HamVals.txt')

MomentumAxL2g000_50031040 = dataL2g000_50031040[:,][:,5*0+0]
KineticEneL2g000_50031040 = dataL2g000_50031040[:,][:,5*0+1]
SelfEnergyL2g000_50031040 = dataL2g000_50031040[:,][:,5*0+2]
EigenValReL2g000_50031040 = dataL2g000_50031040[:,][:,5*0+3]
EigenValImL2g000_50031040 = dataL2g000_50031040[:,][:,5*0+4]

dataL2g000_50031050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK003/N050/HamVals.txt')

MomentumAxL2g000_50031050 = dataL2g000_50031050[:,][:,5*0+0]
KineticEneL2g000_50031050 = dataL2g000_50031050[:,][:,5*0+1]
SelfEnergyL2g000_50031050 = dataL2g000_50031050[:,][:,5*0+2]
EigenValReL2g000_50031050 = dataL2g000_50031050[:,][:,5*0+3]
EigenValImL2g000_50031050 = dataL2g000_50031050[:,][:,5*0+4]

dataL2g000_50051010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK005/N010/HamVals.txt')

MomentumAxL2g000_50051010 = dataL2g000_50051010[:,][:,5*0+0]
KineticEneL2g000_50051010 = dataL2g000_50051010[:,][:,5*0+1]
SelfEnergyL2g000_50051010 = dataL2g000_50051010[:,][:,5*0+2]
EigenValReL2g000_50051010 = dataL2g000_50051010[:,][:,5*0+3]
EigenValImL2g000_50051010 = dataL2g000_50051010[:,][:,5*0+4]

dataL2g000_50051020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK005/N020/HamVals.txt')

MomentumAxL2g000_50051020 = dataL2g000_50051020[:,][:,5*0+0]
KineticEneL2g000_50051020 = dataL2g000_50051020[:,][:,5*0+1]
SelfEnergyL2g000_50051020 = dataL2g000_50051020[:,][:,5*0+2]
EigenValReL2g000_50051020 = dataL2g000_50051020[:,][:,5*0+3]
EigenValImL2g000_50051020 = dataL2g000_50051020[:,][:,5*0+4]

dataL2g000_50051030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK005/N030/HamVals.txt')

MomentumAxL2g000_50051030 = dataL2g000_50051030[:,][:,5*0+0]
KineticEneL2g000_50051030 = dataL2g000_50051030[:,][:,5*0+1]
SelfEnergyL2g000_50051030 = dataL2g000_50051030[:,][:,5*0+2]
EigenValReL2g000_50051030 = dataL2g000_50051030[:,][:,5*0+3]
EigenValImL2g000_50051030 = dataL2g000_50051030[:,][:,5*0+4]

dataL2g000_50051040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK005/N040/HamVals.txt')

MomentumAxL2g000_50051040 = dataL2g000_50051040[:,][:,5*0+0]
KineticEneL2g000_50051040 = dataL2g000_50051040[:,][:,5*0+1]
SelfEnergyL2g000_50051040 = dataL2g000_50051040[:,][:,5*0+2]
EigenValReL2g000_50051040 = dataL2g000_50051040[:,][:,5*0+3]
EigenValImL2g000_50051040 = dataL2g000_50051040[:,][:,5*0+4]

dataL2g000_50051050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK005/N050/HamVals.txt')

MomentumAxL2g000_50051050 = dataL2g000_50051050[:,][:,5*0+0]
KineticEneL2g000_50051050 = dataL2g000_50051050[:,][:,5*0+1]
SelfEnergyL2g000_50051050 = dataL2g000_50051050[:,][:,5*0+2]
EigenValReL2g000_50051050 = dataL2g000_50051050[:,][:,5*0+3]
EigenValImL2g000_50051050 = dataL2g000_50051050[:,][:,5*0+4]

dataL2g000_50071010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK007/N010/HamVals.txt')

MomentumAxL2g000_50071010 = dataL2g000_50071010[:,][:,5*0+0]
KineticEneL2g000_50071010 = dataL2g000_50071010[:,][:,5*0+1]
SelfEnergyL2g000_50071010 = dataL2g000_50071010[:,][:,5*0+2]
EigenValReL2g000_50071010 = dataL2g000_50071010[:,][:,5*0+3]
EigenValImL2g000_50071010 = dataL2g000_50071010[:,][:,5*0+4]

dataL2g000_50071020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK007/N020/HamVals.txt')

MomentumAxL2g000_50071020 = dataL2g000_50071020[:,][:,5*0+0]
KineticEneL2g000_50071020 = dataL2g000_50071020[:,][:,5*0+1]
SelfEnergyL2g000_50071020 = dataL2g000_50071020[:,][:,5*0+2]
EigenValReL2g000_50071020 = dataL2g000_50071020[:,][:,5*0+3]
EigenValImL2g000_50071020 = dataL2g000_50071020[:,][:,5*0+4]

dataL2g000_50071030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK007/N030/HamVals.txt')

MomentumAxL2g000_50071030 = dataL2g000_50071030[:,][:,5*0+0]
KineticEneL2g000_50071030 = dataL2g000_50071030[:,][:,5*0+1]
SelfEnergyL2g000_50071030 = dataL2g000_50071030[:,][:,5*0+2]
EigenValReL2g000_50071030 = dataL2g000_50071030[:,][:,5*0+3]
EigenValImL2g000_50071030 = dataL2g000_50071030[:,][:,5*0+4]

dataL2g000_50071040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK007/N040/HamVals.txt')

MomentumAxL2g000_50071040 = dataL2g000_50071040[:,][:,5*0+0]
KineticEneL2g000_50071040 = dataL2g000_50071040[:,][:,5*0+1]
SelfEnergyL2g000_50071040 = dataL2g000_50071040[:,][:,5*0+2]
EigenValReL2g000_50071040 = dataL2g000_50071040[:,][:,5*0+3]
EigenValImL2g000_50071040 = dataL2g000_50071040[:,][:,5*0+4]

dataL2g000_50071050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK007/N050/HamVals.txt')

MomentumAxL2g000_50071050 = dataL2g000_50071050[:,][:,5*0+0]
KineticEneL2g000_50071050 = dataL2g000_50071050[:,][:,5*0+1]
SelfEnergyL2g000_50071050 = dataL2g000_50071050[:,][:,5*0+2]
EigenValReL2g000_50071050 = dataL2g000_50071050[:,][:,5*0+3]
EigenValImL2g000_50071050 = dataL2g000_50071050[:,][:,5*0+4]

dataL2g000_50101010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK010/N010/HamVals.txt')

MomentumAxL2g000_50101010 = dataL2g000_50101010[:,][:,5*0+0]
KineticEneL2g000_50101010 = dataL2g000_50101010[:,][:,5*0+1]
SelfEnergyL2g000_50101010 = dataL2g000_50101010[:,][:,5*0+2]
EigenValReL2g000_50101010 = dataL2g000_50101010[:,][:,5*0+3]
EigenValImL2g000_50101010 = dataL2g000_50101010[:,][:,5*0+4]

dataL2g000_50101020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK010/N020/HamVals.txt')

MomentumAxL2g000_50101020 = dataL2g000_50101020[:,][:,5*0+0]
KineticEneL2g000_50101020 = dataL2g000_50101020[:,][:,5*0+1]
SelfEnergyL2g000_50101020 = dataL2g000_50101020[:,][:,5*0+2]
EigenValReL2g000_50101020 = dataL2g000_50101020[:,][:,5*0+3]
EigenValImL2g000_50101020 = dataL2g000_50101020[:,][:,5*0+4]

dataL2g000_50101030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK010/N030/HamVals.txt')

MomentumAxL2g000_50101030 = dataL2g000_50101030[:,][:,5*0+0]
KineticEneL2g000_50101030 = dataL2g000_50101030[:,][:,5*0+1]
SelfEnergyL2g000_50101030 = dataL2g000_50101030[:,][:,5*0+2]
EigenValReL2g000_50101030 = dataL2g000_50101030[:,][:,5*0+3]
EigenValImL2g000_50101030 = dataL2g000_50101030[:,][:,5*0+4]

dataL2g000_50101040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK010/N040/HamVals.txt')

MomentumAxL2g000_50101040 = dataL2g000_50101040[:,][:,5*0+0]
KineticEneL2g000_50101040 = dataL2g000_50101040[:,][:,5*0+1]
SelfEnergyL2g000_50101040 = dataL2g000_50101040[:,][:,5*0+2]
EigenValReL2g000_50101040 = dataL2g000_50101040[:,][:,5*0+3]
EigenValImL2g000_50101040 = dataL2g000_50101040[:,][:,5*0+4]

dataL2g000_50101050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK010/N050/HamVals.txt')

MomentumAxL2g000_50101050 = dataL2g000_50101050[:,][:,5*0+0]
KineticEneL2g000_50101050 = dataL2g000_50101050[:,][:,5*0+1]
SelfEnergyL2g000_50101050 = dataL2g000_50101050[:,][:,5*0+2]
EigenValReL2g000_50101050 = dataL2g000_50101050[:,][:,5*0+3]
EigenValImL2g000_50101050 = dataL2g000_50101050[:,][:,5*0+4]
"""
dataL2g000_50201010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK020/N010/HamVals.txt')

MomentumAxL2g000_50201010 = dataL2g000_50201010[:,][:,5*0+0]
KineticEneL2g000_50201010 = dataL2g000_50201010[:,][:,5*0+1]
SelfEnergyL2g000_50201010 = dataL2g000_50201010[:,][:,5*0+2]
EigenValReL2g000_50201010 = dataL2g000_50201010[:,][:,5*0+3]
EigenValImL2g000_50201010 = dataL2g000_50201010[:,][:,5*0+4]

dataL2g000_50201020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK020/N020/HamVals.txt')

MomentumAxL2g000_50201020 = dataL2g000_50201020[:,][:,5*0+0]
KineticEneL2g000_50201020 = dataL2g000_50201020[:,][:,5*0+1]
SelfEnergyL2g000_50201020 = dataL2g000_50201020[:,][:,5*0+2]
EigenValReL2g000_50201020 = dataL2g000_50201020[:,][:,5*0+3]
EigenValImL2g000_50201020 = dataL2g000_50201020[:,][:,5*0+4]

dataL2g000_50201030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK020/N030/HamVals.txt')

MomentumAxL2g000_50201030 = dataL2g000_50201030[:,][:,5*0+0]
KineticEneL2g000_50201030 = dataL2g000_50201030[:,][:,5*0+1]
SelfEnergyL2g000_50201030 = dataL2g000_50201030[:,][:,5*0+2]
EigenValReL2g000_50201030 = dataL2g000_50201030[:,][:,5*0+3]
EigenValImL2g000_50201030 = dataL2g000_50201030[:,][:,5*0+4]

dataL2g000_50201040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK020/N040/HamVals.txt')

MomentumAxL2g000_50201040 = dataL2g000_50201040[:,][:,5*0+0]
KineticEneL2g000_50201040 = dataL2g000_50201040[:,][:,5*0+1]
SelfEnergyL2g000_50201040 = dataL2g000_50201040[:,][:,5*0+2]
EigenValReL2g000_50201040 = dataL2g000_50201040[:,][:,5*0+3]
EigenValImL2g000_50201040 = dataL2g000_50201040[:,][:,5*0+4]

dataL2g000_50201050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-50/aK020/N050/HamVals.txt')

MomentumAxL2g000_50201050 = dataL2g000_50201050[:,][:,5*0+0]
KineticEneL2g000_50201050 = dataL2g000_50201050[:,][:,5*0+1]
SelfEnergyL2g000_50201050 = dataL2g000_50201050[:,][:,5*0+2]
EigenValReL2g000_50201050 = dataL2g000_50201050[:,][:,5*0+3]
EigenValImL2g000_50201050 = dataL2g000_50201050[:,][:,5*0+4]
"""
MaxEigenValImL2g000_51Inf = np.zeros((6))

MaxEigenValImL2g000_51Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_50011010),np.max(EigenValImL2g000_50011020),np.max(EigenValImL2g000_50011030),np.max(EigenValImL2g000_50011040),np.max(EigenValImL2g000_50011050)], 1)[[1]]
MaxEigenValImL2g000_51Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_50021010),np.max(EigenValImL2g000_50021020),np.max(EigenValImL2g000_50021030),np.max(EigenValImL2g000_50021040),np.max(EigenValImL2g000_50021050)], 1)[[1]]
MaxEigenValImL2g000_51Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_50031010),np.max(EigenValImL2g000_50031020),np.max(EigenValImL2g000_50031030),np.max(EigenValImL2g000_50031040),np.max(EigenValImL2g000_50031050)], 1)[[1]]
MaxEigenValImL2g000_51Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_50051010),np.max(EigenValImL2g000_50051020),np.max(EigenValImL2g000_50051030),np.max(EigenValImL2g000_50051040),np.max(EigenValImL2g000_50051050)], 1)[[1]]
MaxEigenValImL2g000_51Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_50071010),np.max(EigenValImL2g000_50071020),np.max(EigenValImL2g000_50071030),np.max(EigenValImL2g000_50071040),np.max(EigenValImL2g000_50071050)], 1)[[1]]
MaxEigenValImL2g000_51Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_50101010),np.max(EigenValImL2g000_50101020),np.max(EigenValImL2g000_50101030),np.max(EigenValImL2g000_50101040),np.max(EigenValImL2g000_50101050)], 1)[[1]]
print "MaxEigenValImL2g000_51Inf"
print MaxEigenValImL2g000_51Inf
print [np.max(EigenValImL2g000_50011010),np.max(EigenValImL2g000_50011020),np.max(EigenValImL2g000_50011030),np.max(EigenValImL2g000_50011040),np.max(EigenValImL2g000_50011050)]
print [np.max(EigenValImL2g000_50021010),np.max(EigenValImL2g000_50021020),np.max(EigenValImL2g000_50021030),np.max(EigenValImL2g000_50021040),np.max(EigenValImL2g000_50021050)]
print [np.max(EigenValImL2g000_50031010),np.max(EigenValImL2g000_50031020),np.max(EigenValImL2g000_50031030),np.max(EigenValImL2g000_50031040),np.max(EigenValImL2g000_50031050)]
print [np.max(EigenValImL2g000_50051010),np.max(EigenValImL2g000_50051020),np.max(EigenValImL2g000_50051030),np.max(EigenValImL2g000_50051040),np.max(EigenValImL2g000_50051050)]
print [np.max(EigenValImL2g000_50071010),np.max(EigenValImL2g000_50071020),np.max(EigenValImL2g000_50071030),np.max(EigenValImL2g000_50071040),np.max(EigenValImL2g000_50071050)]
print [np.max(EigenValImL2g000_50101010),np.max(EigenValImL2g000_50101020),np.max(EigenValImL2g000_50101030),np.max(EigenValImL2g000_50101040),np.max(EigenValImL2g000_50101050)]
########################################################################

dataL2g000_60011010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK001/N010/HamVals.txt')

MomentumAxL2g000_60011010 = dataL2g000_60011010[:,][:,5*0+0]
KineticEneL2g000_60011010 = dataL2g000_60011010[:,][:,5*0+1]
SelfEnergyL2g000_60011010 = dataL2g000_60011010[:,][:,5*0+2]
EigenValReL2g000_60011010 = dataL2g000_60011010[:,][:,5*0+3]
EigenValImL2g000_60011010 = dataL2g000_60011010[:,][:,5*0+4]

dataL2g000_60011020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK001/N020/HamVals.txt')

MomentumAxL2g000_60011020 = dataL2g000_60011020[:,][:,5*0+0]
KineticEneL2g000_60011020 = dataL2g000_60011020[:,][:,5*0+1]
SelfEnergyL2g000_60011020 = dataL2g000_60011020[:,][:,5*0+2]
EigenValReL2g000_60011020 = dataL2g000_60011020[:,][:,5*0+3]
EigenValImL2g000_60011020 = dataL2g000_60011020[:,][:,5*0+4]

dataL2g000_60011030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK001/N030/HamVals.txt')

MomentumAxL2g000_60011030 = dataL2g000_60011030[:,][:,5*0+0]
KineticEneL2g000_60011030 = dataL2g000_60011030[:,][:,5*0+1]
SelfEnergyL2g000_60011030 = dataL2g000_60011030[:,][:,5*0+2]
EigenValReL2g000_60011030 = dataL2g000_60011030[:,][:,5*0+3]
EigenValImL2g000_60011030 = dataL2g000_60011030[:,][:,5*0+4]

dataL2g000_60011040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK001/N040/HamVals.txt')

MomentumAxL2g000_60011040 = dataL2g000_60011040[:,][:,5*0+0]
KineticEneL2g000_60011040 = dataL2g000_60011040[:,][:,5*0+1]
SelfEnergyL2g000_60011040 = dataL2g000_60011040[:,][:,5*0+2]
EigenValReL2g000_60011040 = dataL2g000_60011040[:,][:,5*0+3]
EigenValImL2g000_60011040 = dataL2g000_60011040[:,][:,5*0+4]

dataL2g000_60011050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK001/N050/HamVals.txt')

MomentumAxL2g000_60011050 = dataL2g000_60011050[:,][:,5*0+0]
KineticEneL2g000_60011050 = dataL2g000_60011050[:,][:,5*0+1]
SelfEnergyL2g000_60011050 = dataL2g000_60011050[:,][:,5*0+2]
EigenValReL2g000_60011050 = dataL2g000_60011050[:,][:,5*0+3]
EigenValImL2g000_60011050 = dataL2g000_60011050[:,][:,5*0+4]

dataL2g000_60021010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK002/N010/HamVals.txt')

MomentumAxL2g000_60021010 = dataL2g000_60021010[:,][:,5*0+0]
KineticEneL2g000_60021010 = dataL2g000_60021010[:,][:,5*0+1]
SelfEnergyL2g000_60021010 = dataL2g000_60021010[:,][:,5*0+2]
EigenValReL2g000_60021010 = dataL2g000_60021010[:,][:,5*0+3]
EigenValImL2g000_60021010 = dataL2g000_60021010[:,][:,5*0+4]

dataL2g000_60021020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK002/N020/HamVals.txt')

MomentumAxL2g000_60021020 = dataL2g000_60021020[:,][:,5*0+0]
KineticEneL2g000_60021020 = dataL2g000_60021020[:,][:,5*0+1]
SelfEnergyL2g000_60021020 = dataL2g000_60021020[:,][:,5*0+2]
EigenValReL2g000_60021020 = dataL2g000_60021020[:,][:,5*0+3]
EigenValImL2g000_60021020 = dataL2g000_60021020[:,][:,5*0+4]

dataL2g000_60021030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK002/N030/HamVals.txt')

MomentumAxL2g000_60021030 = dataL2g000_60021030[:,][:,5*0+0]
KineticEneL2g000_60021030 = dataL2g000_60021030[:,][:,5*0+1]
SelfEnergyL2g000_60021030 = dataL2g000_60021030[:,][:,5*0+2]
EigenValReL2g000_60021030 = dataL2g000_60021030[:,][:,5*0+3]
EigenValImL2g000_60021030 = dataL2g000_60021030[:,][:,5*0+4]

dataL2g000_60021040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK002/N040/HamVals.txt')

MomentumAxL2g000_60021040 = dataL2g000_60021040[:,][:,5*0+0]
KineticEneL2g000_60021040 = dataL2g000_60021040[:,][:,5*0+1]
SelfEnergyL2g000_60021040 = dataL2g000_60021040[:,][:,5*0+2]
EigenValReL2g000_60021040 = dataL2g000_60021040[:,][:,5*0+3]
EigenValImL2g000_60021040 = dataL2g000_60021040[:,][:,5*0+4]

dataL2g000_60021050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK002/N050/HamVals.txt')

MomentumAxL2g000_60021050 = dataL2g000_60021050[:,][:,5*0+0]
KineticEneL2g000_60021050 = dataL2g000_60021050[:,][:,5*0+1]
SelfEnergyL2g000_60021050 = dataL2g000_60021050[:,][:,5*0+2]
EigenValReL2g000_60021050 = dataL2g000_60021050[:,][:,5*0+3]
EigenValImL2g000_60021050 = dataL2g000_60021050[:,][:,5*0+4]

dataL2g000_60051010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK005/N010/HamVals.txt')

MomentumAxL2g000_60051010 = dataL2g000_60051010[:,][:,5*0+0]
KineticEneL2g000_60051010 = dataL2g000_60051010[:,][:,5*0+1]
SelfEnergyL2g000_60051010 = dataL2g000_60051010[:,][:,5*0+2]
EigenValReL2g000_60051010 = dataL2g000_60051010[:,][:,5*0+3]
EigenValImL2g000_60051010 = dataL2g000_60051010[:,][:,5*0+4]

dataL2g000_60051020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK005/N020/HamVals.txt')

MomentumAxL2g000_60051020 = dataL2g000_60051020[:,][:,5*0+0]
KineticEneL2g000_60051020 = dataL2g000_60051020[:,][:,5*0+1]
SelfEnergyL2g000_60051020 = dataL2g000_60051020[:,][:,5*0+2]
EigenValReL2g000_60051020 = dataL2g000_60051020[:,][:,5*0+3]
EigenValImL2g000_60051020 = dataL2g000_60051020[:,][:,5*0+4]

dataL2g000_60051030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK005/N030/HamVals.txt')

MomentumAxL2g000_60051030 = dataL2g000_60051030[:,][:,5*0+0]
KineticEneL2g000_60051030 = dataL2g000_60051030[:,][:,5*0+1]
SelfEnergyL2g000_60051030 = dataL2g000_60051030[:,][:,5*0+2]
EigenValReL2g000_60051030 = dataL2g000_60051030[:,][:,5*0+3]
EigenValImL2g000_60051030 = dataL2g000_60051030[:,][:,5*0+4]

dataL2g000_60051040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK005/N040/HamVals.txt')

MomentumAxL2g000_60051040 = dataL2g000_60051040[:,][:,5*0+0]
KineticEneL2g000_60051040 = dataL2g000_60051040[:,][:,5*0+1]
SelfEnergyL2g000_60051040 = dataL2g000_60051040[:,][:,5*0+2]
EigenValReL2g000_60051040 = dataL2g000_60051040[:,][:,5*0+3]
EigenValImL2g000_60051040 = dataL2g000_60051040[:,][:,5*0+4]

dataL2g000_60051050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK005/N050/HamVals.txt')

MomentumAxL2g000_60051050 = dataL2g000_60051050[:,][:,5*0+0]
KineticEneL2g000_60051050 = dataL2g000_60051050[:,][:,5*0+1]
SelfEnergyL2g000_60051050 = dataL2g000_60051050[:,][:,5*0+2]
EigenValReL2g000_60051050 = dataL2g000_60051050[:,][:,5*0+3]
EigenValImL2g000_60051050 = dataL2g000_60051050[:,][:,5*0+4]

dataL2g000_60101010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK010/N010/HamVals.txt')

MomentumAxL2g000_60101010 = dataL2g000_60101010[:,][:,5*0+0]
KineticEneL2g000_60101010 = dataL2g000_60101010[:,][:,5*0+1]
SelfEnergyL2g000_60101010 = dataL2g000_60101010[:,][:,5*0+2]
EigenValReL2g000_60101010 = dataL2g000_60101010[:,][:,5*0+3]
EigenValImL2g000_60101010 = dataL2g000_60101010[:,][:,5*0+4]

dataL2g000_60101020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK010/N020/HamVals.txt')

MomentumAxL2g000_60101020 = dataL2g000_60101020[:,][:,5*0+0]
KineticEneL2g000_60101020 = dataL2g000_60101020[:,][:,5*0+1]
SelfEnergyL2g000_60101020 = dataL2g000_60101020[:,][:,5*0+2]
EigenValReL2g000_60101020 = dataL2g000_60101020[:,][:,5*0+3]
EigenValImL2g000_60101020 = dataL2g000_60101020[:,][:,5*0+4]

dataL2g000_60101030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK010/N030/HamVals.txt')

MomentumAxL2g000_60101030 = dataL2g000_60101030[:,][:,5*0+0]
KineticEneL2g000_60101030 = dataL2g000_60101030[:,][:,5*0+1]
SelfEnergyL2g000_60101030 = dataL2g000_60101030[:,][:,5*0+2]
EigenValReL2g000_60101030 = dataL2g000_60101030[:,][:,5*0+3]
EigenValImL2g000_60101030 = dataL2g000_60101030[:,][:,5*0+4]

dataL2g000_60101040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK010/N040/HamVals.txt')

MomentumAxL2g000_60101040 = dataL2g000_60101040[:,][:,5*0+0]
KineticEneL2g000_60101040 = dataL2g000_60101040[:,][:,5*0+1]
SelfEnergyL2g000_60101040 = dataL2g000_60101040[:,][:,5*0+2]
EigenValReL2g000_60101040 = dataL2g000_60101040[:,][:,5*0+3]
EigenValImL2g000_60101040 = dataL2g000_60101040[:,][:,5*0+4]

dataL2g000_60101050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK010/N050/HamVals.txt')

MomentumAxL2g000_60101050 = dataL2g000_60101050[:,][:,5*0+0]
KineticEneL2g000_60101050 = dataL2g000_60101050[:,][:,5*0+1]
SelfEnergyL2g000_60101050 = dataL2g000_60101050[:,][:,5*0+2]
EigenValReL2g000_60101050 = dataL2g000_60101050[:,][:,5*0+3]
EigenValImL2g000_60101050 = dataL2g000_60101050[:,][:,5*0+4]

dataL2g000_60031010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK003/N010/HamVals.txt')

MomentumAxL2g000_60031010 = dataL2g000_60031010[:,][:,5*0+0]
KineticEneL2g000_60031010 = dataL2g000_60031010[:,][:,5*0+1]
SelfEnergyL2g000_60031010 = dataL2g000_60031010[:,][:,5*0+2]
EigenValReL2g000_60031010 = dataL2g000_60031010[:,][:,5*0+3]
EigenValImL2g000_60031010 = dataL2g000_60031010[:,][:,5*0+4]

dataL2g000_60031020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK003/N020/HamVals.txt')

MomentumAxL2g000_60031020 = dataL2g000_60031020[:,][:,5*0+0]
KineticEneL2g000_60031020 = dataL2g000_60031020[:,][:,5*0+1]
SelfEnergyL2g000_60031020 = dataL2g000_60031020[:,][:,5*0+2]
EigenValReL2g000_60031020 = dataL2g000_60031020[:,][:,5*0+3]
EigenValImL2g000_60031020 = dataL2g000_60031020[:,][:,5*0+4]

dataL2g000_60031030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK003/N030/HamVals.txt')

MomentumAxL2g000_60031030 = dataL2g000_60031030[:,][:,5*0+0]
KineticEneL2g000_60031030 = dataL2g000_60031030[:,][:,5*0+1]
SelfEnergyL2g000_60031030 = dataL2g000_60031030[:,][:,5*0+2]
EigenValReL2g000_60031030 = dataL2g000_60031030[:,][:,5*0+3]
EigenValImL2g000_60031030 = dataL2g000_60031030[:,][:,5*0+4]

dataL2g000_60031040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK003/N040/HamVals.txt')

MomentumAxL2g000_60031040 = dataL2g000_60031040[:,][:,5*0+0]
KineticEneL2g000_60031040 = dataL2g000_60031040[:,][:,5*0+1]
SelfEnergyL2g000_60031040 = dataL2g000_60031040[:,][:,5*0+2]
EigenValReL2g000_60031040 = dataL2g000_60031040[:,][:,5*0+3]
EigenValImL2g000_60031040 = dataL2g000_60031040[:,][:,5*0+4]

dataL2g000_60031050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK003/N050/HamVals.txt')

MomentumAxL2g000_60031050 = dataL2g000_60031050[:,][:,5*0+0]
KineticEneL2g000_60031050 = dataL2g000_60031050[:,][:,5*0+1]
SelfEnergyL2g000_60031050 = dataL2g000_60031050[:,][:,5*0+2]
EigenValReL2g000_60031050 = dataL2g000_60031050[:,][:,5*0+3]
EigenValImL2g000_60031050 = dataL2g000_60031050[:,][:,5*0+4]

dataL2g000_60071010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK007/N010/HamVals.txt')

MomentumAxL2g000_60071010 = dataL2g000_60071010[:,][:,5*0+0]
KineticEneL2g000_60071010 = dataL2g000_60071010[:,][:,5*0+1]
SelfEnergyL2g000_60071010 = dataL2g000_60071010[:,][:,5*0+2]
EigenValReL2g000_60071010 = dataL2g000_60071010[:,][:,5*0+3]
EigenValImL2g000_60071010 = dataL2g000_60071010[:,][:,5*0+4]

dataL2g000_60071020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK007/N020/HamVals.txt')

MomentumAxL2g000_60071020 = dataL2g000_60071020[:,][:,5*0+0]
KineticEneL2g000_60071020 = dataL2g000_60071020[:,][:,5*0+1]
SelfEnergyL2g000_60071020 = dataL2g000_60071020[:,][:,5*0+2]
EigenValReL2g000_60071020 = dataL2g000_60071020[:,][:,5*0+3]
EigenValImL2g000_60071020 = dataL2g000_60071020[:,][:,5*0+4]

dataL2g000_60071030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK007/N030/HamVals.txt')

MomentumAxL2g000_60071030 = dataL2g000_60071030[:,][:,5*0+0]
KineticEneL2g000_60071030 = dataL2g000_60071030[:,][:,5*0+1]
SelfEnergyL2g000_60071030 = dataL2g000_60071030[:,][:,5*0+2]
EigenValReL2g000_60071030 = dataL2g000_60071030[:,][:,5*0+3]
EigenValImL2g000_60071030 = dataL2g000_60071030[:,][:,5*0+4]

dataL2g000_60071040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK007/N040/HamVals.txt')

MomentumAxL2g000_60071040 = dataL2g000_60071040[:,][:,5*0+0]
KineticEneL2g000_60071040 = dataL2g000_60071040[:,][:,5*0+1]
SelfEnergyL2g000_60071040 = dataL2g000_60071040[:,][:,5*0+2]
EigenValReL2g000_60071040 = dataL2g000_60071040[:,][:,5*0+3]
EigenValImL2g000_60071040 = dataL2g000_60071040[:,][:,5*0+4]

dataL2g000_60071050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK007/N050/HamVals.txt')

MomentumAxL2g000_60071050 = dataL2g000_60071050[:,][:,5*0+0]
KineticEneL2g000_60071050 = dataL2g000_60071050[:,][:,5*0+1]
SelfEnergyL2g000_60071050 = dataL2g000_60071050[:,][:,5*0+2]
EigenValReL2g000_60071050 = dataL2g000_60071050[:,][:,5*0+3]
EigenValImL2g000_60071050 = dataL2g000_60071050[:,][:,5*0+4]

"""
dataL2g000_60201010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK020/N010/HamVals.txt')

MomentumAxL2g000_60201010 = dataL2g000_60201010[:,][:,5*0+0]
KineticEneL2g000_60201010 = dataL2g000_60201010[:,][:,5*0+1]
SelfEnergyL2g000_60201010 = dataL2g000_60201010[:,][:,5*0+2]
EigenValReL2g000_60201010 = dataL2g000_60201010[:,][:,5*0+3]
EigenValImL2g000_60201010 = dataL2g000_60201010[:,][:,5*0+4]

dataL2g000_60201020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK020/N020/HamVals.txt')

MomentumAxL2g000_60201020 = dataL2g000_60201020[:,][:,5*0+0]
KineticEneL2g000_60201020 = dataL2g000_60201020[:,][:,5*0+1]
SelfEnergyL2g000_60201020 = dataL2g000_60201020[:,][:,5*0+2]
EigenValReL2g000_60201020 = dataL2g000_60201020[:,][:,5*0+3]
EigenValImL2g000_60201020 = dataL2g000_60201020[:,][:,5*0+4]

dataL2g000_60201030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK020/N030/HamVals.txt')

MomentumAxL2g000_60201030 = dataL2g000_60201030[:,][:,5*0+0]
KineticEneL2g000_60201030 = dataL2g000_60201030[:,][:,5*0+1]
SelfEnergyL2g000_60201030 = dataL2g000_60201030[:,][:,5*0+2]
EigenValReL2g000_60201030 = dataL2g000_60201030[:,][:,5*0+3]
EigenValImL2g000_60201030 = dataL2g000_60201030[:,][:,5*0+4]

dataL2g000_60201040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK020/N040/HamVals.txt')

MomentumAxL2g000_60201040 = dataL2g000_60201040[:,][:,5*0+0]
KineticEneL2g000_60201040 = dataL2g000_60201040[:,][:,5*0+1]
SelfEnergyL2g000_60201040 = dataL2g000_60201040[:,][:,5*0+2]
EigenValReL2g000_60201040 = dataL2g000_60201040[:,][:,5*0+3]
EigenValImL2g000_60201040 = dataL2g000_60201040[:,][:,5*0+4]

dataL2g000_60201050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-60/aK020/N050/HamVals.txt')

MomentumAxL2g000_60201050 = dataL2g000_60201050[:,][:,5*0+0]
KineticEneL2g000_60201050 = dataL2g000_60201050[:,][:,5*0+1]
SelfEnergyL2g000_60201050 = dataL2g000_60201050[:,][:,5*0+2]
EigenValReL2g000_60201050 = dataL2g000_60201050[:,][:,5*0+3]
EigenValImL2g000_60201050 = dataL2g000_60201050[:,][:,5*0+4]
"""
MaxEigenValImL2g000_61Inf = np.zeros((6))

MaxEigenValImL2g000_61Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_60011010),np.max(EigenValImL2g000_60011020),np.max(EigenValImL2g000_60011030),np.max(EigenValImL2g000_60011040),np.max(EigenValImL2g000_60011050)], 1)[[1]]
MaxEigenValImL2g000_61Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_60021010),np.max(EigenValImL2g000_60021020),np.max(EigenValImL2g000_60021030),np.max(EigenValImL2g000_60021040),np.max(EigenValImL2g000_60021050)], 1)[[1]]
MaxEigenValImL2g000_61Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_60031010),np.max(EigenValImL2g000_60031020),np.max(EigenValImL2g000_60031030),np.max(EigenValImL2g000_60031040),np.max(EigenValImL2g000_60031050)], 1)[[1]]
MaxEigenValImL2g000_61Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_60051010),np.max(EigenValImL2g000_60051020),np.max(EigenValImL2g000_60051030),np.max(EigenValImL2g000_60051040),np.max(EigenValImL2g000_60051050)], 1)[[1]]
MaxEigenValImL2g000_61Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_60071010),np.max(EigenValImL2g000_60071020),np.max(EigenValImL2g000_60071030),np.max(EigenValImL2g000_60071040),np.max(EigenValImL2g000_60071050)], 1)[[1]]
MaxEigenValImL2g000_61Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_60101010),np.max(EigenValImL2g000_60101020),np.max(EigenValImL2g000_60101030),np.max(EigenValImL2g000_60101040),np.max(EigenValImL2g000_60101050)], 1)[[1]]

########################################################################

dataL2g000_70011010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK001/N010/HamVals.txt')

MomentumAxL2g000_70011010 = dataL2g000_70011010[:,][:,5*0+0]
KineticEneL2g000_70011010 = dataL2g000_70011010[:,][:,5*0+1]
SelfEnergyL2g000_70011010 = dataL2g000_70011010[:,][:,5*0+2]
EigenValReL2g000_70011010 = dataL2g000_70011010[:,][:,5*0+3]
EigenValImL2g000_70011010 = dataL2g000_70011010[:,][:,5*0+4]

dataL2g000_70011020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK001/N020/HamVals.txt')

MomentumAxL2g000_70011020 = dataL2g000_70011020[:,][:,5*0+0]
KineticEneL2g000_70011020 = dataL2g000_70011020[:,][:,5*0+1]
SelfEnergyL2g000_70011020 = dataL2g000_70011020[:,][:,5*0+2]
EigenValReL2g000_70011020 = dataL2g000_70011020[:,][:,5*0+3]
EigenValImL2g000_70011020 = dataL2g000_70011020[:,][:,5*0+4]

dataL2g000_70011030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK001/N030/HamVals.txt')

MomentumAxL2g000_70011030 = dataL2g000_70011030[:,][:,5*0+0]
KineticEneL2g000_70011030 = dataL2g000_70011030[:,][:,5*0+1]
SelfEnergyL2g000_70011030 = dataL2g000_70011030[:,][:,5*0+2]
EigenValReL2g000_70011030 = dataL2g000_70011030[:,][:,5*0+3]
EigenValImL2g000_70011030 = dataL2g000_70011030[:,][:,5*0+4]

dataL2g000_70011040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK001/N040/HamVals.txt')

MomentumAxL2g000_70011040 = dataL2g000_70011040[:,][:,5*0+0]
KineticEneL2g000_70011040 = dataL2g000_70011040[:,][:,5*0+1]
SelfEnergyL2g000_70011040 = dataL2g000_70011040[:,][:,5*0+2]
EigenValReL2g000_70011040 = dataL2g000_70011040[:,][:,5*0+3]
EigenValImL2g000_70011040 = dataL2g000_70011040[:,][:,5*0+4]

dataL2g000_70011050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK001/N050/HamVals.txt')

MomentumAxL2g000_70011050 = dataL2g000_70011050[:,][:,5*0+0]
KineticEneL2g000_70011050 = dataL2g000_70011050[:,][:,5*0+1]
SelfEnergyL2g000_70011050 = dataL2g000_70011050[:,][:,5*0+2]
EigenValReL2g000_70011050 = dataL2g000_70011050[:,][:,5*0+3]
EigenValImL2g000_70011050 = dataL2g000_70011050[:,][:,5*0+4]

dataL2g000_70021010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK002/N010/HamVals.txt')

MomentumAxL2g000_70021010 = dataL2g000_70021010[:,][:,5*0+0]
KineticEneL2g000_70021010 = dataL2g000_70021010[:,][:,5*0+1]
SelfEnergyL2g000_70021010 = dataL2g000_70021010[:,][:,5*0+2]
EigenValReL2g000_70021010 = dataL2g000_70021010[:,][:,5*0+3]
EigenValImL2g000_70021010 = dataL2g000_70021010[:,][:,5*0+4]

dataL2g000_70021020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK002/N020/HamVals.txt')

MomentumAxL2g000_70021020 = dataL2g000_70021020[:,][:,5*0+0]
KineticEneL2g000_70021020 = dataL2g000_70021020[:,][:,5*0+1]
SelfEnergyL2g000_70021020 = dataL2g000_70021020[:,][:,5*0+2]
EigenValReL2g000_70021020 = dataL2g000_70021020[:,][:,5*0+3]
EigenValImL2g000_70021020 = dataL2g000_70021020[:,][:,5*0+4]

dataL2g000_70021030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK002/N030/HamVals.txt')

MomentumAxL2g000_70021030 = dataL2g000_70021030[:,][:,5*0+0]
KineticEneL2g000_70021030 = dataL2g000_70021030[:,][:,5*0+1]
SelfEnergyL2g000_70021030 = dataL2g000_70021030[:,][:,5*0+2]
EigenValReL2g000_70021030 = dataL2g000_70021030[:,][:,5*0+3]
EigenValImL2g000_70021030 = dataL2g000_70021030[:,][:,5*0+4]

dataL2g000_70021040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK002/N040/HamVals.txt')

MomentumAxL2g000_70021040 = dataL2g000_70021040[:,][:,5*0+0]
KineticEneL2g000_70021040 = dataL2g000_70021040[:,][:,5*0+1]
SelfEnergyL2g000_70021040 = dataL2g000_70021040[:,][:,5*0+2]
EigenValReL2g000_70021040 = dataL2g000_70021040[:,][:,5*0+3]
EigenValImL2g000_70021040 = dataL2g000_70021040[:,][:,5*0+4]

dataL2g000_70021050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK002/N050/HamVals.txt')

MomentumAxL2g000_70021050 = dataL2g000_70021050[:,][:,5*0+0]
KineticEneL2g000_70021050 = dataL2g000_70021050[:,][:,5*0+1]
SelfEnergyL2g000_70021050 = dataL2g000_70021050[:,][:,5*0+2]
EigenValReL2g000_70021050 = dataL2g000_70021050[:,][:,5*0+3]
EigenValImL2g000_70021050 = dataL2g000_70021050[:,][:,5*0+4]

dataL2g000_70051010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK005/N010/HamVals.txt')

MomentumAxL2g000_70051010 = dataL2g000_70051010[:,][:,5*0+0]
KineticEneL2g000_70051010 = dataL2g000_70051010[:,][:,5*0+1]
SelfEnergyL2g000_70051010 = dataL2g000_70051010[:,][:,5*0+2]
EigenValReL2g000_70051010 = dataL2g000_70051010[:,][:,5*0+3]
EigenValImL2g000_70051010 = dataL2g000_70051010[:,][:,5*0+4]

dataL2g000_70051020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK005/N020/HamVals.txt')

MomentumAxL2g000_70051020 = dataL2g000_70051020[:,][:,5*0+0]
KineticEneL2g000_70051020 = dataL2g000_70051020[:,][:,5*0+1]
SelfEnergyL2g000_70051020 = dataL2g000_70051020[:,][:,5*0+2]
EigenValReL2g000_70051020 = dataL2g000_70051020[:,][:,5*0+3]
EigenValImL2g000_70051020 = dataL2g000_70051020[:,][:,5*0+4]

dataL2g000_70051030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK005/N030/HamVals.txt')

MomentumAxL2g000_70051030 = dataL2g000_70051030[:,][:,5*0+0]
KineticEneL2g000_70051030 = dataL2g000_70051030[:,][:,5*0+1]
SelfEnergyL2g000_70051030 = dataL2g000_70051030[:,][:,5*0+2]
EigenValReL2g000_70051030 = dataL2g000_70051030[:,][:,5*0+3]
EigenValImL2g000_70051030 = dataL2g000_70051030[:,][:,5*0+4]

dataL2g000_70051040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK005/N040/HamVals.txt')

MomentumAxL2g000_70051040 = dataL2g000_70051040[:,][:,5*0+0]
KineticEneL2g000_70051040 = dataL2g000_70051040[:,][:,5*0+1]
SelfEnergyL2g000_70051040 = dataL2g000_70051040[:,][:,5*0+2]
EigenValReL2g000_70051040 = dataL2g000_70051040[:,][:,5*0+3]
EigenValImL2g000_70051040 = dataL2g000_70051040[:,][:,5*0+4]

dataL2g000_70051050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK005/N050/HamVals.txt')

MomentumAxL2g000_70051050 = dataL2g000_70051050[:,][:,5*0+0]
KineticEneL2g000_70051050 = dataL2g000_70051050[:,][:,5*0+1]
SelfEnergyL2g000_70051050 = dataL2g000_70051050[:,][:,5*0+2]
EigenValReL2g000_70051050 = dataL2g000_70051050[:,][:,5*0+3]
EigenValImL2g000_70051050 = dataL2g000_70051050[:,][:,5*0+4]

dataL2g000_70101010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK010/N010/HamVals.txt')

MomentumAxL2g000_70101010 = dataL2g000_70101010[:,][:,5*0+0]
KineticEneL2g000_70101010 = dataL2g000_70101010[:,][:,5*0+1]
SelfEnergyL2g000_70101010 = dataL2g000_70101010[:,][:,5*0+2]
EigenValReL2g000_70101010 = dataL2g000_70101010[:,][:,5*0+3]
EigenValImL2g000_70101010 = dataL2g000_70101010[:,][:,5*0+4]

dataL2g000_70101020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK010/N020/HamVals.txt')

MomentumAxL2g000_70101020 = dataL2g000_70101020[:,][:,5*0+0]
KineticEneL2g000_70101020 = dataL2g000_70101020[:,][:,5*0+1]
SelfEnergyL2g000_70101020 = dataL2g000_70101020[:,][:,5*0+2]
EigenValReL2g000_70101020 = dataL2g000_70101020[:,][:,5*0+3]
EigenValImL2g000_70101020 = dataL2g000_70101020[:,][:,5*0+4]

dataL2g000_70101030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK010/N030/HamVals.txt')

MomentumAxL2g000_70101030 = dataL2g000_70101030[:,][:,5*0+0]
KineticEneL2g000_70101030 = dataL2g000_70101030[:,][:,5*0+1]
SelfEnergyL2g000_70101030 = dataL2g000_70101030[:,][:,5*0+2]
EigenValReL2g000_70101030 = dataL2g000_70101030[:,][:,5*0+3]
EigenValImL2g000_70101030 = dataL2g000_70101030[:,][:,5*0+4]

dataL2g000_70101040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK010/N040/HamVals.txt')

MomentumAxL2g000_70101040 = dataL2g000_70101040[:,][:,5*0+0]
KineticEneL2g000_70101040 = dataL2g000_70101040[:,][:,5*0+1]
SelfEnergyL2g000_70101040 = dataL2g000_70101040[:,][:,5*0+2]
EigenValReL2g000_70101040 = dataL2g000_70101040[:,][:,5*0+3]
EigenValImL2g000_70101040 = dataL2g000_70101040[:,][:,5*0+4]

dataL2g000_70101050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK010/N050/HamVals.txt')

MomentumAxL2g000_70101050 = dataL2g000_70101050[:,][:,5*0+0]
KineticEneL2g000_70101050 = dataL2g000_70101050[:,][:,5*0+1]
SelfEnergyL2g000_70101050 = dataL2g000_70101050[:,][:,5*0+2]
EigenValReL2g000_70101050 = dataL2g000_70101050[:,][:,5*0+3]
EigenValImL2g000_70101050 = dataL2g000_70101050[:,][:,5*0+4]

dataL2g000_70031010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK003/N010/HamVals.txt')

MomentumAxL2g000_70031010 = dataL2g000_70031010[:,][:,5*0+0]
KineticEneL2g000_70031010 = dataL2g000_70031010[:,][:,5*0+1]
SelfEnergyL2g000_70031010 = dataL2g000_70031010[:,][:,5*0+2]
EigenValReL2g000_70031010 = dataL2g000_70031010[:,][:,5*0+3]
EigenValImL2g000_70031010 = dataL2g000_70031010[:,][:,5*0+4]

dataL2g000_70031020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK003/N020/HamVals.txt')

MomentumAxL2g000_70031020 = dataL2g000_70031020[:,][:,5*0+0]
KineticEneL2g000_70031020 = dataL2g000_70031020[:,][:,5*0+1]
SelfEnergyL2g000_70031020 = dataL2g000_70031020[:,][:,5*0+2]
EigenValReL2g000_70031020 = dataL2g000_70031020[:,][:,5*0+3]
EigenValImL2g000_70031020 = dataL2g000_70031020[:,][:,5*0+4]

dataL2g000_70031030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK003/N030/HamVals.txt')

MomentumAxL2g000_70031030 = dataL2g000_70031030[:,][:,5*0+0]
KineticEneL2g000_70031030 = dataL2g000_70031030[:,][:,5*0+1]
SelfEnergyL2g000_70031030 = dataL2g000_70031030[:,][:,5*0+2]
EigenValReL2g000_70031030 = dataL2g000_70031030[:,][:,5*0+3]
EigenValImL2g000_70031030 = dataL2g000_70031030[:,][:,5*0+4]

dataL2g000_70031040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK003/N040/HamVals.txt')

MomentumAxL2g000_70031040 = dataL2g000_70031040[:,][:,5*0+0]
KineticEneL2g000_70031040 = dataL2g000_70031040[:,][:,5*0+1]
SelfEnergyL2g000_70031040 = dataL2g000_70031040[:,][:,5*0+2]
EigenValReL2g000_70031040 = dataL2g000_70031040[:,][:,5*0+3]
EigenValImL2g000_70031040 = dataL2g000_70031040[:,][:,5*0+4]

dataL2g000_70031050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK003/N050/HamVals.txt')

MomentumAxL2g000_70031050 = dataL2g000_70031050[:,][:,5*0+0]
KineticEneL2g000_70031050 = dataL2g000_70031050[:,][:,5*0+1]
SelfEnergyL2g000_70031050 = dataL2g000_70031050[:,][:,5*0+2]
EigenValReL2g000_70031050 = dataL2g000_70031050[:,][:,5*0+3]
EigenValImL2g000_70031050 = dataL2g000_70031050[:,][:,5*0+4]

dataL2g000_70071010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK007/N010/HamVals.txt')

MomentumAxL2g000_70071010 = dataL2g000_70071010[:,][:,5*0+0]
KineticEneL2g000_70071010 = dataL2g000_70071010[:,][:,5*0+1]
SelfEnergyL2g000_70071010 = dataL2g000_70071010[:,][:,5*0+2]
EigenValReL2g000_70071010 = dataL2g000_70071010[:,][:,5*0+3]
EigenValImL2g000_70071010 = dataL2g000_70071010[:,][:,5*0+4]

dataL2g000_70071020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK007/N020/HamVals.txt')

MomentumAxL2g000_70071020 = dataL2g000_70071020[:,][:,5*0+0]
KineticEneL2g000_70071020 = dataL2g000_70071020[:,][:,5*0+1]
SelfEnergyL2g000_70071020 = dataL2g000_70071020[:,][:,5*0+2]
EigenValReL2g000_70071020 = dataL2g000_70071020[:,][:,5*0+3]
EigenValImL2g000_70071020 = dataL2g000_70071020[:,][:,5*0+4]

dataL2g000_70071030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK007/N030/HamVals.txt')

MomentumAxL2g000_70071030 = dataL2g000_70071030[:,][:,5*0+0]
KineticEneL2g000_70071030 = dataL2g000_70071030[:,][:,5*0+1]
SelfEnergyL2g000_70071030 = dataL2g000_70071030[:,][:,5*0+2]
EigenValReL2g000_70071030 = dataL2g000_70071030[:,][:,5*0+3]
EigenValImL2g000_70071030 = dataL2g000_70071030[:,][:,5*0+4]

dataL2g000_70071040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK007/N040/HamVals.txt')

MomentumAxL2g000_70071040 = dataL2g000_70071040[:,][:,5*0+0]
KineticEneL2g000_70071040 = dataL2g000_70071040[:,][:,5*0+1]
SelfEnergyL2g000_70071040 = dataL2g000_70071040[:,][:,5*0+2]
EigenValReL2g000_70071040 = dataL2g000_70071040[:,][:,5*0+3]
EigenValImL2g000_70071040 = dataL2g000_70071040[:,][:,5*0+4]

dataL2g000_70071050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK007/N050/HamVals.txt')

MomentumAxL2g000_70071050 = dataL2g000_70071050[:,][:,5*0+0]
KineticEneL2g000_70071050 = dataL2g000_70071050[:,][:,5*0+1]
SelfEnergyL2g000_70071050 = dataL2g000_70071050[:,][:,5*0+2]
EigenValReL2g000_70071050 = dataL2g000_70071050[:,][:,5*0+3]
EigenValImL2g000_70071050 = dataL2g000_70071050[:,][:,5*0+4]

"""
dataL2g000_70201010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK020/N010/HamVals.txt')

MomentumAxL2g000_70201010 = dataL2g000_70201010[:,][:,5*0+0]
KineticEneL2g000_70201010 = dataL2g000_70201010[:,][:,5*0+1]
SelfEnergyL2g000_70201010 = dataL2g000_70201010[:,][:,5*0+2]
EigenValReL2g000_70201010 = dataL2g000_70201010[:,][:,5*0+3]
EigenValImL2g000_70201010 = dataL2g000_70201010[:,][:,5*0+4]

dataL2g000_70201020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK020/N020/HamVals.txt')

MomentumAxL2g000_70201020 = dataL2g000_70201020[:,][:,5*0+0]
KineticEneL2g000_70201020 = dataL2g000_70201020[:,][:,5*0+1]
SelfEnergyL2g000_70201020 = dataL2g000_70201020[:,][:,5*0+2]
EigenValReL2g000_70201020 = dataL2g000_70201020[:,][:,5*0+3]
EigenValImL2g000_70201020 = dataL2g000_70201020[:,][:,5*0+4]

dataL2g000_70201030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK020/N030/HamVals.txt')

MomentumAxL2g000_70201030 = dataL2g000_70201030[:,][:,5*0+0]
KineticEneL2g000_70201030 = dataL2g000_70201030[:,][:,5*0+1]
SelfEnergyL2g000_70201030 = dataL2g000_70201030[:,][:,5*0+2]
EigenValReL2g000_70201030 = dataL2g000_70201030[:,][:,5*0+3]
EigenValImL2g000_70201030 = dataL2g000_70201030[:,][:,5*0+4]

dataL2g000_70201040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK020/N040/HamVals.txt')

MomentumAxL2g000_70201040 = dataL2g000_70201040[:,][:,5*0+0]
KineticEneL2g000_70201040 = dataL2g000_70201040[:,][:,5*0+1]
SelfEnergyL2g000_70201040 = dataL2g000_70201040[:,][:,5*0+2]
EigenValReL2g000_70201040 = dataL2g000_70201040[:,][:,5*0+3]
EigenValImL2g000_70201040 = dataL2g000_70201040[:,][:,5*0+4]

dataL2g000_70201050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-70/aK020/N050/HamVals.txt')

MomentumAxL2g000_70201050 = dataL2g000_70201050[:,][:,5*0+0]
KineticEneL2g000_70201050 = dataL2g000_70201050[:,][:,5*0+1]
SelfEnergyL2g000_70201050 = dataL2g000_70201050[:,][:,5*0+2]
EigenValReL2g000_70201050 = dataL2g000_70201050[:,][:,5*0+3]
EigenValImL2g000_70201050 = dataL2g000_70201050[:,][:,5*0+4]
"""
MaxEigenValImL2g000_71Inf = np.zeros((6))

MaxEigenValImL2g000_71Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_70011010),np.max(EigenValImL2g000_70011020),np.max(EigenValImL2g000_70011030),np.max(EigenValImL2g000_70011040),np.max(EigenValImL2g000_70011050)], 1)[[1]]
MaxEigenValImL2g000_71Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_70021010),np.max(EigenValImL2g000_70021020),np.max(EigenValImL2g000_70021030),np.max(EigenValImL2g000_70021040),np.max(EigenValImL2g000_70021050)], 1)[[1]]
MaxEigenValImL2g000_71Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_70031010),np.max(EigenValImL2g000_70031020),np.max(EigenValImL2g000_70031030),np.max(EigenValImL2g000_70031040),np.max(EigenValImL2g000_70031050)], 1)[[1]]
MaxEigenValImL2g000_71Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_70051010),np.max(EigenValImL2g000_70051020),np.max(EigenValImL2g000_70051030),np.max(EigenValImL2g000_70051040),np.max(EigenValImL2g000_70051050)], 1)[[1]]
MaxEigenValImL2g000_71Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_70071010),np.max(EigenValImL2g000_70071020),np.max(EigenValImL2g000_70071030),np.max(EigenValImL2g000_70071040),np.max(EigenValImL2g000_70071050)], 1)[[1]]
MaxEigenValImL2g000_71Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_70101010),np.max(EigenValImL2g000_70101020),np.max(EigenValImL2g000_70101030),np.max(EigenValImL2g000_70101040),np.max(EigenValImL2g000_70101050)], 1)[[1]]

########################################################################

dataL2g000_80011010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK001/N010/HamVals.txt')

MomentumAxL2g000_80011010 = dataL2g000_80011010[:,][:,5*0+0]
KineticEneL2g000_80011010 = dataL2g000_80011010[:,][:,5*0+1]
SelfEnergyL2g000_80011010 = dataL2g000_80011010[:,][:,5*0+2]
EigenValReL2g000_80011010 = dataL2g000_80011010[:,][:,5*0+3]
EigenValImL2g000_80011010 = dataL2g000_80011010[:,][:,5*0+4]

dataL2g000_80011020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK001/N020/HamVals.txt')

MomentumAxL2g000_80011020 = dataL2g000_80011020[:,][:,5*0+0]
KineticEneL2g000_80011020 = dataL2g000_80011020[:,][:,5*0+1]
SelfEnergyL2g000_80011020 = dataL2g000_80011020[:,][:,5*0+2]
EigenValReL2g000_80011020 = dataL2g000_80011020[:,][:,5*0+3]
EigenValImL2g000_80011020 = dataL2g000_80011020[:,][:,5*0+4]

dataL2g000_80011030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK001/N030/HamVals.txt')

MomentumAxL2g000_80011030 = dataL2g000_80011030[:,][:,5*0+0]
KineticEneL2g000_80011030 = dataL2g000_80011030[:,][:,5*0+1]
SelfEnergyL2g000_80011030 = dataL2g000_80011030[:,][:,5*0+2]
EigenValReL2g000_80011030 = dataL2g000_80011030[:,][:,5*0+3]
EigenValImL2g000_80011030 = dataL2g000_80011030[:,][:,5*0+4]

dataL2g000_80011040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK001/N040/HamVals.txt')

MomentumAxL2g000_80011040 = dataL2g000_80011040[:,][:,5*0+0]
KineticEneL2g000_80011040 = dataL2g000_80011040[:,][:,5*0+1]
SelfEnergyL2g000_80011040 = dataL2g000_80011040[:,][:,5*0+2]
EigenValReL2g000_80011040 = dataL2g000_80011040[:,][:,5*0+3]
EigenValImL2g000_80011040 = dataL2g000_80011040[:,][:,5*0+4]

dataL2g000_80011050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK001/N050/HamVals.txt')

MomentumAxL2g000_80011050 = dataL2g000_80011050[:,][:,5*0+0]
KineticEneL2g000_80011050 = dataL2g000_80011050[:,][:,5*0+1]
SelfEnergyL2g000_80011050 = dataL2g000_80011050[:,][:,5*0+2]
EigenValReL2g000_80011050 = dataL2g000_80011050[:,][:,5*0+3]
EigenValImL2g000_80011050 = dataL2g000_80011050[:,][:,5*0+4]

dataL2g000_80021010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK002/N010/HamVals.txt')

MomentumAxL2g000_80021010 = dataL2g000_80021010[:,][:,5*0+0]
KineticEneL2g000_80021010 = dataL2g000_80021010[:,][:,5*0+1]
SelfEnergyL2g000_80021010 = dataL2g000_80021010[:,][:,5*0+2]
EigenValReL2g000_80021010 = dataL2g000_80021010[:,][:,5*0+3]
EigenValImL2g000_80021010 = dataL2g000_80021010[:,][:,5*0+4]

dataL2g000_80021020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK002/N020/HamVals.txt')

MomentumAxL2g000_80021020 = dataL2g000_80021020[:,][:,5*0+0]
KineticEneL2g000_80021020 = dataL2g000_80021020[:,][:,5*0+1]
SelfEnergyL2g000_80021020 = dataL2g000_80021020[:,][:,5*0+2]
EigenValReL2g000_80021020 = dataL2g000_80021020[:,][:,5*0+3]
EigenValImL2g000_80021020 = dataL2g000_80021020[:,][:,5*0+4]

dataL2g000_80021030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK002/N030/HamVals.txt')

MomentumAxL2g000_80021030 = dataL2g000_80021030[:,][:,5*0+0]
KineticEneL2g000_80021030 = dataL2g000_80021030[:,][:,5*0+1]
SelfEnergyL2g000_80021030 = dataL2g000_80021030[:,][:,5*0+2]
EigenValReL2g000_80021030 = dataL2g000_80021030[:,][:,5*0+3]
EigenValImL2g000_80021030 = dataL2g000_80021030[:,][:,5*0+4]

dataL2g000_80021040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK002/N040/HamVals.txt')

MomentumAxL2g000_80021040 = dataL2g000_80021040[:,][:,5*0+0]
KineticEneL2g000_80021040 = dataL2g000_80021040[:,][:,5*0+1]
SelfEnergyL2g000_80021040 = dataL2g000_80021040[:,][:,5*0+2]
EigenValReL2g000_80021040 = dataL2g000_80021040[:,][:,5*0+3]
EigenValImL2g000_80021040 = dataL2g000_80021040[:,][:,5*0+4]

dataL2g000_80021050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK002/N050/HamVals.txt')

MomentumAxL2g000_80021050 = dataL2g000_80021050[:,][:,5*0+0]
KineticEneL2g000_80021050 = dataL2g000_80021050[:,][:,5*0+1]
SelfEnergyL2g000_80021050 = dataL2g000_80021050[:,][:,5*0+2]
EigenValReL2g000_80021050 = dataL2g000_80021050[:,][:,5*0+3]
EigenValImL2g000_80021050 = dataL2g000_80021050[:,][:,5*0+4]

dataL2g000_80051010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK005/N010/HamVals.txt')

MomentumAxL2g000_80051010 = dataL2g000_80051010[:,][:,5*0+0]
KineticEneL2g000_80051010 = dataL2g000_80051010[:,][:,5*0+1]
SelfEnergyL2g000_80051010 = dataL2g000_80051010[:,][:,5*0+2]
EigenValReL2g000_80051010 = dataL2g000_80051010[:,][:,5*0+3]
EigenValImL2g000_80051010 = dataL2g000_80051010[:,][:,5*0+4]

dataL2g000_80051020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK005/N020/HamVals.txt')

MomentumAxL2g000_80051020 = dataL2g000_80051020[:,][:,5*0+0]
KineticEneL2g000_80051020 = dataL2g000_80051020[:,][:,5*0+1]
SelfEnergyL2g000_80051020 = dataL2g000_80051020[:,][:,5*0+2]
EigenValReL2g000_80051020 = dataL2g000_80051020[:,][:,5*0+3]
EigenValImL2g000_80051020 = dataL2g000_80051020[:,][:,5*0+4]

dataL2g000_80051030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK005/N030/HamVals.txt')

MomentumAxL2g000_80051030 = dataL2g000_80051030[:,][:,5*0+0]
KineticEneL2g000_80051030 = dataL2g000_80051030[:,][:,5*0+1]
SelfEnergyL2g000_80051030 = dataL2g000_80051030[:,][:,5*0+2]
EigenValReL2g000_80051030 = dataL2g000_80051030[:,][:,5*0+3]
EigenValImL2g000_80051030 = dataL2g000_80051030[:,][:,5*0+4]

dataL2g000_80051040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK005/N040/HamVals.txt')

MomentumAxL2g000_80051040 = dataL2g000_80051040[:,][:,5*0+0]
KineticEneL2g000_80051040 = dataL2g000_80051040[:,][:,5*0+1]
SelfEnergyL2g000_80051040 = dataL2g000_80051040[:,][:,5*0+2]
EigenValReL2g000_80051040 = dataL2g000_80051040[:,][:,5*0+3]
EigenValImL2g000_80051040 = dataL2g000_80051040[:,][:,5*0+4]

dataL2g000_80051050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK005/N050/HamVals.txt')

MomentumAxL2g000_80051050 = dataL2g000_80051050[:,][:,5*0+0]
KineticEneL2g000_80051050 = dataL2g000_80051050[:,][:,5*0+1]
SelfEnergyL2g000_80051050 = dataL2g000_80051050[:,][:,5*0+2]
EigenValReL2g000_80051050 = dataL2g000_80051050[:,][:,5*0+3]
EigenValImL2g000_80051050 = dataL2g000_80051050[:,][:,5*0+4]

dataL2g000_80101010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK010/N010/HamVals.txt')

MomentumAxL2g000_80101010 = dataL2g000_80101010[:,][:,5*0+0]
KineticEneL2g000_80101010 = dataL2g000_80101010[:,][:,5*0+1]
SelfEnergyL2g000_80101010 = dataL2g000_80101010[:,][:,5*0+2]
EigenValReL2g000_80101010 = dataL2g000_80101010[:,][:,5*0+3]
EigenValImL2g000_80101010 = dataL2g000_80101010[:,][:,5*0+4]

dataL2g000_80101020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK010/N020/HamVals.txt')

MomentumAxL2g000_80101020 = dataL2g000_80101020[:,][:,5*0+0]
KineticEneL2g000_80101020 = dataL2g000_80101020[:,][:,5*0+1]
SelfEnergyL2g000_80101020 = dataL2g000_80101020[:,][:,5*0+2]
EigenValReL2g000_80101020 = dataL2g000_80101020[:,][:,5*0+3]
EigenValImL2g000_80101020 = dataL2g000_80101020[:,][:,5*0+4]

dataL2g000_80101030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK010/N030/HamVals.txt')

MomentumAxL2g000_80101030 = dataL2g000_80101030[:,][:,5*0+0]
KineticEneL2g000_80101030 = dataL2g000_80101030[:,][:,5*0+1]
SelfEnergyL2g000_80101030 = dataL2g000_80101030[:,][:,5*0+2]
EigenValReL2g000_80101030 = dataL2g000_80101030[:,][:,5*0+3]
EigenValImL2g000_80101030 = dataL2g000_80101030[:,][:,5*0+4]

dataL2g000_80101040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK010/N040/HamVals.txt')

MomentumAxL2g000_80101040 = dataL2g000_80101040[:,][:,5*0+0]
KineticEneL2g000_80101040 = dataL2g000_80101040[:,][:,5*0+1]
SelfEnergyL2g000_80101040 = dataL2g000_80101040[:,][:,5*0+2]
EigenValReL2g000_80101040 = dataL2g000_80101040[:,][:,5*0+3]
EigenValImL2g000_80101040 = dataL2g000_80101040[:,][:,5*0+4]

dataL2g000_80101050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK010/N050/HamVals.txt')

MomentumAxL2g000_80101050 = dataL2g000_80101050[:,][:,5*0+0]
KineticEneL2g000_80101050 = dataL2g000_80101050[:,][:,5*0+1]
SelfEnergyL2g000_80101050 = dataL2g000_80101050[:,][:,5*0+2]
EigenValReL2g000_80101050 = dataL2g000_80101050[:,][:,5*0+3]
EigenValImL2g000_80101050 = dataL2g000_80101050[:,][:,5*0+4]

dataL2g000_80031010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK003/N010/HamVals.txt')

MomentumAxL2g000_80031010 = dataL2g000_80031010[:,][:,5*0+0]
KineticEneL2g000_80031010 = dataL2g000_80031010[:,][:,5*0+1]
SelfEnergyL2g000_80031010 = dataL2g000_80031010[:,][:,5*0+2]
EigenValReL2g000_80031010 = dataL2g000_80031010[:,][:,5*0+3]
EigenValImL2g000_80031010 = dataL2g000_80031010[:,][:,5*0+4]

dataL2g000_80031020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK003/N020/HamVals.txt')

MomentumAxL2g000_80031020 = dataL2g000_80031020[:,][:,5*0+0]
KineticEneL2g000_80031020 = dataL2g000_80031020[:,][:,5*0+1]
SelfEnergyL2g000_80031020 = dataL2g000_80031020[:,][:,5*0+2]
EigenValReL2g000_80031020 = dataL2g000_80031020[:,][:,5*0+3]
EigenValImL2g000_80031020 = dataL2g000_80031020[:,][:,5*0+4]

dataL2g000_80031030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK003/N030/HamVals.txt')

MomentumAxL2g000_80031030 = dataL2g000_80031030[:,][:,5*0+0]
KineticEneL2g000_80031030 = dataL2g000_80031030[:,][:,5*0+1]
SelfEnergyL2g000_80031030 = dataL2g000_80031030[:,][:,5*0+2]
EigenValReL2g000_80031030 = dataL2g000_80031030[:,][:,5*0+3]
EigenValImL2g000_80031030 = dataL2g000_80031030[:,][:,5*0+4]

dataL2g000_80031040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK003/N040/HamVals.txt')

MomentumAxL2g000_80031040 = dataL2g000_80031040[:,][:,5*0+0]
KineticEneL2g000_80031040 = dataL2g000_80031040[:,][:,5*0+1]
SelfEnergyL2g000_80031040 = dataL2g000_80031040[:,][:,5*0+2]
EigenValReL2g000_80031040 = dataL2g000_80031040[:,][:,5*0+3]
EigenValImL2g000_80031040 = dataL2g000_80031040[:,][:,5*0+4]

dataL2g000_80031050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK003/N050/HamVals.txt')

MomentumAxL2g000_80031050 = dataL2g000_80031050[:,][:,5*0+0]
KineticEneL2g000_80031050 = dataL2g000_80031050[:,][:,5*0+1]
SelfEnergyL2g000_80031050 = dataL2g000_80031050[:,][:,5*0+2]
EigenValReL2g000_80031050 = dataL2g000_80031050[:,][:,5*0+3]
EigenValImL2g000_80031050 = dataL2g000_80031050[:,][:,5*0+4]

dataL2g000_80071010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK007/N010/HamVals.txt')

MomentumAxL2g000_80071010 = dataL2g000_80071010[:,][:,5*0+0]
KineticEneL2g000_80071010 = dataL2g000_80071010[:,][:,5*0+1]
SelfEnergyL2g000_80071010 = dataL2g000_80071010[:,][:,5*0+2]
EigenValReL2g000_80071010 = dataL2g000_80071010[:,][:,5*0+3]
EigenValImL2g000_80071010 = dataL2g000_80071010[:,][:,5*0+4]

dataL2g000_80071020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK007/N020/HamVals.txt')

MomentumAxL2g000_80071020 = dataL2g000_80071020[:,][:,5*0+0]
KineticEneL2g000_80071020 = dataL2g000_80071020[:,][:,5*0+1]
SelfEnergyL2g000_80071020 = dataL2g000_80071020[:,][:,5*0+2]
EigenValReL2g000_80071020 = dataL2g000_80071020[:,][:,5*0+3]
EigenValImL2g000_80071020 = dataL2g000_80071020[:,][:,5*0+4]

dataL2g000_80071030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK007/N030/HamVals.txt')

MomentumAxL2g000_80071030 = dataL2g000_80071030[:,][:,5*0+0]
KineticEneL2g000_80071030 = dataL2g000_80071030[:,][:,5*0+1]
SelfEnergyL2g000_80071030 = dataL2g000_80071030[:,][:,5*0+2]
EigenValReL2g000_80071030 = dataL2g000_80071030[:,][:,5*0+3]
EigenValImL2g000_80071030 = dataL2g000_80071030[:,][:,5*0+4]

dataL2g000_80071040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK007/N040/HamVals.txt')

MomentumAxL2g000_80071040 = dataL2g000_80071040[:,][:,5*0+0]
KineticEneL2g000_80071040 = dataL2g000_80071040[:,][:,5*0+1]
SelfEnergyL2g000_80071040 = dataL2g000_80071040[:,][:,5*0+2]
EigenValReL2g000_80071040 = dataL2g000_80071040[:,][:,5*0+3]
EigenValImL2g000_80071040 = dataL2g000_80071040[:,][:,5*0+4]

dataL2g000_80071050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK007/N050/HamVals.txt')

MomentumAxL2g000_80071050 = dataL2g000_80071050[:,][:,5*0+0]
KineticEneL2g000_80071050 = dataL2g000_80071050[:,][:,5*0+1]
SelfEnergyL2g000_80071050 = dataL2g000_80071050[:,][:,5*0+2]
EigenValReL2g000_80071050 = dataL2g000_80071050[:,][:,5*0+3]
EigenValImL2g000_80071050 = dataL2g000_80071050[:,][:,5*0+4]

"""
dataL2g000_80201010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK020/N010/HamVals.txt')

MomentumAxL2g000_80201010 = dataL2g000_80201010[:,][:,5*0+0]
KineticEneL2g000_80201010 = dataL2g000_80201010[:,][:,5*0+1]
SelfEnergyL2g000_80201010 = dataL2g000_80201010[:,][:,5*0+2]
EigenValReL2g000_80201010 = dataL2g000_80201010[:,][:,5*0+3]
EigenValImL2g000_80201010 = dataL2g000_80201010[:,][:,5*0+4]

dataL2g000_80201020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK020/N020/HamVals.txt')

MomentumAxL2g000_80201020 = dataL2g000_80201020[:,][:,5*0+0]
KineticEneL2g000_80201020 = dataL2g000_80201020[:,][:,5*0+1]
SelfEnergyL2g000_80201020 = dataL2g000_80201020[:,][:,5*0+2]
EigenValReL2g000_80201020 = dataL2g000_80201020[:,][:,5*0+3]
EigenValImL2g000_80201020 = dataL2g000_80201020[:,][:,5*0+4]

dataL2g000_80201030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK020/N030/HamVals.txt')

MomentumAxL2g000_80201030 = dataL2g000_80201030[:,][:,5*0+0]
KineticEneL2g000_80201030 = dataL2g000_80201030[:,][:,5*0+1]
SelfEnergyL2g000_80201030 = dataL2g000_80201030[:,][:,5*0+2]
EigenValReL2g000_80201030 = dataL2g000_80201030[:,][:,5*0+3]
EigenValImL2g000_80201030 = dataL2g000_80201030[:,][:,5*0+4]

dataL2g000_80201040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK020/N040/HamVals.txt')

MomentumAxL2g000_80201040 = dataL2g000_80201040[:,][:,5*0+0]
KineticEneL2g000_80201040 = dataL2g000_80201040[:,][:,5*0+1]
SelfEnergyL2g000_80201040 = dataL2g000_80201040[:,][:,5*0+2]
EigenValReL2g000_80201040 = dataL2g000_80201040[:,][:,5*0+3]
EigenValImL2g000_80201040 = dataL2g000_80201040[:,][:,5*0+4]

dataL2g000_80201050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-80/aK020/N050/HamVals.txt')

MomentumAxL2g000_80201050 = dataL2g000_80201050[:,][:,5*0+0]
KineticEneL2g000_80201050 = dataL2g000_80201050[:,][:,5*0+1]
SelfEnergyL2g000_80201050 = dataL2g000_80201050[:,][:,5*0+2]
EigenValReL2g000_80201050 = dataL2g000_80201050[:,][:,5*0+3]
EigenValImL2g000_80201050 = dataL2g000_80201050[:,][:,5*0+4]
"""

MaxEigenValImL2g000_81Inf = np.zeros((6))

MaxEigenValImL2g000_81Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_80011010),np.max(EigenValImL2g000_80011020),np.max(EigenValImL2g000_80011030),np.max(EigenValImL2g000_80011040),np.max(EigenValImL2g000_80011050)], 1)[[1]]
MaxEigenValImL2g000_81Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_80021010),np.max(EigenValImL2g000_80021020),np.max(EigenValImL2g000_80021030),np.max(EigenValImL2g000_80021040),np.max(EigenValImL2g000_80021050)], 1)[[1]]
MaxEigenValImL2g000_81Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_80031010),np.max(EigenValImL2g000_80031020),np.max(EigenValImL2g000_80031030),np.max(EigenValImL2g000_80031040),np.max(EigenValImL2g000_80031050)], 1)[[1]]
MaxEigenValImL2g000_81Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_80051010),np.max(EigenValImL2g000_80051020),np.max(EigenValImL2g000_80051030),np.max(EigenValImL2g000_80051040),np.max(EigenValImL2g000_80051050)], 1)[[1]]
MaxEigenValImL2g000_81Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_80071010),np.max(EigenValImL2g000_80071020),np.max(EigenValImL2g000_80071030),np.max(EigenValImL2g000_80071040),np.max(EigenValImL2g000_80071050)], 1)[[1]]
MaxEigenValImL2g000_81Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_80101010),np.max(EigenValImL2g000_80101020),np.max(EigenValImL2g000_80101030),np.max(EigenValImL2g000_80101040),np.max(EigenValImL2g000_80101050)], 1)[[1]]

########################################################################

dataL2g000_90011010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK001/N010/HamVals.txt')

MomentumAxL2g000_90011010 = dataL2g000_90011010[:,][:,5*0+0]
KineticEneL2g000_90011010 = dataL2g000_90011010[:,][:,5*0+1]
SelfEnergyL2g000_90011010 = dataL2g000_90011010[:,][:,5*0+2]
EigenValReL2g000_90011010 = dataL2g000_90011010[:,][:,5*0+3]
EigenValImL2g000_90011010 = dataL2g000_90011010[:,][:,5*0+4]

dataL2g000_90011020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK001/N020/HamVals.txt')

MomentumAxL2g000_90011020 = dataL2g000_90011020[:,][:,5*0+0]
KineticEneL2g000_90011020 = dataL2g000_90011020[:,][:,5*0+1]
SelfEnergyL2g000_90011020 = dataL2g000_90011020[:,][:,5*0+2]
EigenValReL2g000_90011020 = dataL2g000_90011020[:,][:,5*0+3]
EigenValImL2g000_90011020 = dataL2g000_90011020[:,][:,5*0+4]

dataL2g000_90011030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK001/N030/HamVals.txt')

MomentumAxL2g000_90011030 = dataL2g000_90011030[:,][:,5*0+0]
KineticEneL2g000_90011030 = dataL2g000_90011030[:,][:,5*0+1]
SelfEnergyL2g000_90011030 = dataL2g000_90011030[:,][:,5*0+2]
EigenValReL2g000_90011030 = dataL2g000_90011030[:,][:,5*0+3]
EigenValImL2g000_90011030 = dataL2g000_90011030[:,][:,5*0+4]

dataL2g000_90011040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK001/N040/HamVals.txt')

MomentumAxL2g000_90011040 = dataL2g000_90011040[:,][:,5*0+0]
KineticEneL2g000_90011040 = dataL2g000_90011040[:,][:,5*0+1]
SelfEnergyL2g000_90011040 = dataL2g000_90011040[:,][:,5*0+2]
EigenValReL2g000_90011040 = dataL2g000_90011040[:,][:,5*0+3]
EigenValImL2g000_90011040 = dataL2g000_90011040[:,][:,5*0+4]

dataL2g000_90011050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK001/N050/HamVals.txt')

MomentumAxL2g000_90011050 = dataL2g000_90011050[:,][:,5*0+0]
KineticEneL2g000_90011050 = dataL2g000_90011050[:,][:,5*0+1]
SelfEnergyL2g000_90011050 = dataL2g000_90011050[:,][:,5*0+2]
EigenValReL2g000_90011050 = dataL2g000_90011050[:,][:,5*0+3]
EigenValImL2g000_90011050 = dataL2g000_90011050[:,][:,5*0+4]

dataL2g000_90021010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK002/N010/HamVals.txt')

MomentumAxL2g000_90021010 = dataL2g000_90021010[:,][:,5*0+0]
KineticEneL2g000_90021010 = dataL2g000_90021010[:,][:,5*0+1]
SelfEnergyL2g000_90021010 = dataL2g000_90021010[:,][:,5*0+2]
EigenValReL2g000_90021010 = dataL2g000_90021010[:,][:,5*0+3]
EigenValImL2g000_90021010 = dataL2g000_90021010[:,][:,5*0+4]

dataL2g000_90021020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK002/N020/HamVals.txt')

MomentumAxL2g000_90021020 = dataL2g000_90021020[:,][:,5*0+0]
KineticEneL2g000_90021020 = dataL2g000_90021020[:,][:,5*0+1]
SelfEnergyL2g000_90021020 = dataL2g000_90021020[:,][:,5*0+2]
EigenValReL2g000_90021020 = dataL2g000_90021020[:,][:,5*0+3]
EigenValImL2g000_90021020 = dataL2g000_90021020[:,][:,5*0+4]

dataL2g000_90021030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK002/N030/HamVals.txt')

MomentumAxL2g000_90021030 = dataL2g000_90021030[:,][:,5*0+0]
KineticEneL2g000_90021030 = dataL2g000_90021030[:,][:,5*0+1]
SelfEnergyL2g000_90021030 = dataL2g000_90021030[:,][:,5*0+2]
EigenValReL2g000_90021030 = dataL2g000_90021030[:,][:,5*0+3]
EigenValImL2g000_90021030 = dataL2g000_90021030[:,][:,5*0+4]

dataL2g000_90021040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK002/N040/HamVals.txt')

MomentumAxL2g000_90021040 = dataL2g000_90021040[:,][:,5*0+0]
KineticEneL2g000_90021040 = dataL2g000_90021040[:,][:,5*0+1]
SelfEnergyL2g000_90021040 = dataL2g000_90021040[:,][:,5*0+2]
EigenValReL2g000_90021040 = dataL2g000_90021040[:,][:,5*0+3]
EigenValImL2g000_90021040 = dataL2g000_90021040[:,][:,5*0+4]

dataL2g000_90021050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK002/N050/HamVals.txt')

MomentumAxL2g000_90021050 = dataL2g000_90021050[:,][:,5*0+0]
KineticEneL2g000_90021050 = dataL2g000_90021050[:,][:,5*0+1]
SelfEnergyL2g000_90021050 = dataL2g000_90021050[:,][:,5*0+2]
EigenValReL2g000_90021050 = dataL2g000_90021050[:,][:,5*0+3]
EigenValImL2g000_90021050 = dataL2g000_90021050[:,][:,5*0+4]

dataL2g000_90031010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK003/N010/HamVals.txt')

MomentumAxL2g000_90031010 = dataL2g000_90031010[:,][:,5*0+0]
KineticEneL2g000_90031010 = dataL2g000_90031010[:,][:,5*0+1]
SelfEnergyL2g000_90031010 = dataL2g000_90031010[:,][:,5*0+2]
EigenValReL2g000_90031010 = dataL2g000_90031010[:,][:,5*0+3]
EigenValImL2g000_90031010 = dataL2g000_90031010[:,][:,5*0+4]

dataL2g000_90031020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK003/N020/HamVals.txt')

MomentumAxL2g000_90031020 = dataL2g000_90031020[:,][:,5*0+0]
KineticEneL2g000_90031020 = dataL2g000_90031020[:,][:,5*0+1]
SelfEnergyL2g000_90031020 = dataL2g000_90031020[:,][:,5*0+2]
EigenValReL2g000_90031020 = dataL2g000_90031020[:,][:,5*0+3]
EigenValImL2g000_90031020 = dataL2g000_90031020[:,][:,5*0+4]

dataL2g000_90031030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK003/N030/HamVals.txt')

MomentumAxL2g000_90031030 = dataL2g000_90031030[:,][:,5*0+0]
KineticEneL2g000_90031030 = dataL2g000_90031030[:,][:,5*0+1]
SelfEnergyL2g000_90031030 = dataL2g000_90031030[:,][:,5*0+2]
EigenValReL2g000_90031030 = dataL2g000_90031030[:,][:,5*0+3]
EigenValImL2g000_90031030 = dataL2g000_90031030[:,][:,5*0+4]

dataL2g000_90031040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK003/N040/HamVals.txt')

MomentumAxL2g000_90031040 = dataL2g000_90031040[:,][:,5*0+0]
KineticEneL2g000_90031040 = dataL2g000_90031040[:,][:,5*0+1]
SelfEnergyL2g000_90031040 = dataL2g000_90031040[:,][:,5*0+2]
EigenValReL2g000_90031040 = dataL2g000_90031040[:,][:,5*0+3]
EigenValImL2g000_90031040 = dataL2g000_90031040[:,][:,5*0+4]

dataL2g000_90031050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK003/N050/HamVals.txt')

MomentumAxL2g000_90031050 = dataL2g000_90031050[:,][:,5*0+0]
KineticEneL2g000_90031050 = dataL2g000_90031050[:,][:,5*0+1]
SelfEnergyL2g000_90031050 = dataL2g000_90031050[:,][:,5*0+2]
EigenValReL2g000_90031050 = dataL2g000_90031050[:,][:,5*0+3]
EigenValImL2g000_90031050 = dataL2g000_90031050[:,][:,5*0+4]

dataL2g000_90051010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK005/N010/HamVals.txt')

MomentumAxL2g000_90051010 = dataL2g000_90051010[:,][:,5*0+0]
KineticEneL2g000_90051010 = dataL2g000_90051010[:,][:,5*0+1]
SelfEnergyL2g000_90051010 = dataL2g000_90051010[:,][:,5*0+2]
EigenValReL2g000_90051010 = dataL2g000_90051010[:,][:,5*0+3]
EigenValImL2g000_90051010 = dataL2g000_90051010[:,][:,5*0+4]

dataL2g000_90051020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK005/N020/HamVals.txt')

MomentumAxL2g000_90051020 = dataL2g000_90051020[:,][:,5*0+0]
KineticEneL2g000_90051020 = dataL2g000_90051020[:,][:,5*0+1]
SelfEnergyL2g000_90051020 = dataL2g000_90051020[:,][:,5*0+2]
EigenValReL2g000_90051020 = dataL2g000_90051020[:,][:,5*0+3]
EigenValImL2g000_90051020 = dataL2g000_90051020[:,][:,5*0+4]

dataL2g000_90051030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK005/N030/HamVals.txt')

MomentumAxL2g000_90051030 = dataL2g000_90051030[:,][:,5*0+0]
KineticEneL2g000_90051030 = dataL2g000_90051030[:,][:,5*0+1]
SelfEnergyL2g000_90051030 = dataL2g000_90051030[:,][:,5*0+2]
EigenValReL2g000_90051030 = dataL2g000_90051030[:,][:,5*0+3]
EigenValImL2g000_90051030 = dataL2g000_90051030[:,][:,5*0+4]

dataL2g000_90051040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK005/N040/HamVals.txt')

MomentumAxL2g000_90051040 = dataL2g000_90051040[:,][:,5*0+0]
KineticEneL2g000_90051040 = dataL2g000_90051040[:,][:,5*0+1]
SelfEnergyL2g000_90051040 = dataL2g000_90051040[:,][:,5*0+2]
EigenValReL2g000_90051040 = dataL2g000_90051040[:,][:,5*0+3]
EigenValImL2g000_90051040 = dataL2g000_90051040[:,][:,5*0+4]

dataL2g000_90051050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK005/N050/HamVals.txt')

MomentumAxL2g000_90051050 = dataL2g000_90051050[:,][:,5*0+0]
KineticEneL2g000_90051050 = dataL2g000_90051050[:,][:,5*0+1]
SelfEnergyL2g000_90051050 = dataL2g000_90051050[:,][:,5*0+2]
EigenValReL2g000_90051050 = dataL2g000_90051050[:,][:,5*0+3]
EigenValImL2g000_90051050 = dataL2g000_90051050[:,][:,5*0+4]

dataL2g000_90071010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK007/N010/HamVals.txt')

MomentumAxL2g000_90071010 = dataL2g000_90071010[:,][:,5*0+0]
KineticEneL2g000_90071010 = dataL2g000_90071010[:,][:,5*0+1]
SelfEnergyL2g000_90071010 = dataL2g000_90071010[:,][:,5*0+2]
EigenValReL2g000_90071010 = dataL2g000_90071010[:,][:,5*0+3]
EigenValImL2g000_90071010 = dataL2g000_90071010[:,][:,5*0+4]

dataL2g000_90071020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK007/N020/HamVals.txt')

MomentumAxL2g000_90071020 = dataL2g000_90071020[:,][:,5*0+0]
KineticEneL2g000_90071020 = dataL2g000_90071020[:,][:,5*0+1]
SelfEnergyL2g000_90071020 = dataL2g000_90071020[:,][:,5*0+2]
EigenValReL2g000_90071020 = dataL2g000_90071020[:,][:,5*0+3]
EigenValImL2g000_90071020 = dataL2g000_90071020[:,][:,5*0+4]

dataL2g000_90071030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK007/N030/HamVals.txt')

MomentumAxL2g000_90071030 = dataL2g000_90071030[:,][:,5*0+0]
KineticEneL2g000_90071030 = dataL2g000_90071030[:,][:,5*0+1]
SelfEnergyL2g000_90071030 = dataL2g000_90071030[:,][:,5*0+2]
EigenValReL2g000_90071030 = dataL2g000_90071030[:,][:,5*0+3]
EigenValImL2g000_90071030 = dataL2g000_90071030[:,][:,5*0+4]

dataL2g000_90071040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK007/N040/HamVals.txt')

MomentumAxL2g000_90071040 = dataL2g000_90071040[:,][:,5*0+0]
KineticEneL2g000_90071040 = dataL2g000_90071040[:,][:,5*0+1]
SelfEnergyL2g000_90071040 = dataL2g000_90071040[:,][:,5*0+2]
EigenValReL2g000_90071040 = dataL2g000_90071040[:,][:,5*0+3]
EigenValImL2g000_90071040 = dataL2g000_90071040[:,][:,5*0+4]

dataL2g000_90071050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK007/N050/HamVals.txt')

MomentumAxL2g000_90071050 = dataL2g000_90071050[:,][:,5*0+0]
KineticEneL2g000_90071050 = dataL2g000_90071050[:,][:,5*0+1]
SelfEnergyL2g000_90071050 = dataL2g000_90071050[:,][:,5*0+2]
EigenValReL2g000_90071050 = dataL2g000_90071050[:,][:,5*0+3]
EigenValImL2g000_90071050 = dataL2g000_90071050[:,][:,5*0+4]

dataL2g000_90101010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK010/N010/HamVals.txt')

MomentumAxL2g000_90101010 = dataL2g000_90101010[:,][:,5*0+0]
KineticEneL2g000_90101010 = dataL2g000_90101010[:,][:,5*0+1]
SelfEnergyL2g000_90101010 = dataL2g000_90101010[:,][:,5*0+2]
EigenValReL2g000_90101010 = dataL2g000_90101010[:,][:,5*0+3]
EigenValImL2g000_90101010 = dataL2g000_90101010[:,][:,5*0+4]

dataL2g000_90101020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK010/N020/HamVals.txt')

MomentumAxL2g000_90101020 = dataL2g000_90101020[:,][:,5*0+0]
KineticEneL2g000_90101020 = dataL2g000_90101020[:,][:,5*0+1]
SelfEnergyL2g000_90101020 = dataL2g000_90101020[:,][:,5*0+2]
EigenValReL2g000_90101020 = dataL2g000_90101020[:,][:,5*0+3]
EigenValImL2g000_90101020 = dataL2g000_90101020[:,][:,5*0+4]

dataL2g000_90101030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK010/N030/HamVals.txt')

MomentumAxL2g000_90101030 = dataL2g000_90101030[:,][:,5*0+0]
KineticEneL2g000_90101030 = dataL2g000_90101030[:,][:,5*0+1]
SelfEnergyL2g000_90101030 = dataL2g000_90101030[:,][:,5*0+2]
EigenValReL2g000_90101030 = dataL2g000_90101030[:,][:,5*0+3]
EigenValImL2g000_90101030 = dataL2g000_90101030[:,][:,5*0+4]

dataL2g000_90101040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK010/N040/HamVals.txt')

MomentumAxL2g000_90101040 = dataL2g000_90101040[:,][:,5*0+0]
KineticEneL2g000_90101040 = dataL2g000_90101040[:,][:,5*0+1]
SelfEnergyL2g000_90101040 = dataL2g000_90101040[:,][:,5*0+2]
EigenValReL2g000_90101040 = dataL2g000_90101040[:,][:,5*0+3]
EigenValImL2g000_90101040 = dataL2g000_90101040[:,][:,5*0+4]

dataL2g000_90101050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK000-90/aK010/N050/HamVals.txt')

MomentumAxL2g000_90101050 = dataL2g000_90101050[:,][:,5*0+0]
KineticEneL2g000_90101050 = dataL2g000_90101050[:,][:,5*0+1]
SelfEnergyL2g000_90101050 = dataL2g000_90101050[:,][:,5*0+2]
EigenValReL2g000_90101050 = dataL2g000_90101050[:,][:,5*0+3]
EigenValImL2g000_90101050 = dataL2g000_90101050[:,][:,5*0+4]

MaxEigenValImL2g000_91Inf = np.zeros((6))

MaxEigenValImL2g000_91Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_90011010),np.max(EigenValImL2g000_90011020),np.max(EigenValImL2g000_90011030),np.max(EigenValImL2g000_90011040),np.max(EigenValImL2g000_90011050)], 1)[[1]]
MaxEigenValImL2g000_91Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_90021010),np.max(EigenValImL2g000_90021020),np.max(EigenValImL2g000_90021030),np.max(EigenValImL2g000_90021040),np.max(EigenValImL2g000_90021050)], 1)[[1]]
MaxEigenValImL2g000_91Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_90031010),np.max(EigenValImL2g000_90031020),np.max(EigenValImL2g000_90031030),np.max(EigenValImL2g000_90031040),np.max(EigenValImL2g000_90031050)], 1)[[1]]
MaxEigenValImL2g000_91Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_90051010),np.max(EigenValImL2g000_90051020),np.max(EigenValImL2g000_90051030),np.max(EigenValImL2g000_90051040),np.max(EigenValImL2g000_90051050)], 1)[[1]]
MaxEigenValImL2g000_91Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_90071010),np.max(EigenValImL2g000_90071020),np.max(EigenValImL2g000_90071030),np.max(EigenValImL2g000_90071040),np.max(EigenValImL2g000_90071050)], 1)[[1]]
MaxEigenValImL2g000_91Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL2g000_90101010),np.max(EigenValImL2g000_90101020),np.max(EigenValImL2g000_90101030),np.max(EigenValImL2g000_90101040),np.max(EigenValImL2g000_90101050)], 1)[[1]]

########################################################################

dataL2g0010011010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK001/N010/HamVals.txt')

MomentumAxL2g0010011010 = dataL2g0010011010[:,][:,5*0+0]
KineticEneL2g0010011010 = dataL2g0010011010[:,][:,5*0+1]
SelfEnergyL2g0010011010 = dataL2g0010011010[:,][:,5*0+2]
EigenValReL2g0010011010 = dataL2g0010011010[:,][:,5*0+3]
EigenValImL2g0010011010 = dataL2g0010011010[:,][:,5*0+4]

dataL2g0010011020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK001/N020/HamVals.txt')

MomentumAxL2g0010011020 = dataL2g0010011020[:,][:,5*0+0]
KineticEneL2g0010011020 = dataL2g0010011020[:,][:,5*0+1]
SelfEnergyL2g0010011020 = dataL2g0010011020[:,][:,5*0+2]
EigenValReL2g0010011020 = dataL2g0010011020[:,][:,5*0+3]
EigenValImL2g0010011020 = dataL2g0010011020[:,][:,5*0+4]

dataL2g0010011030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK001/N030/HamVals.txt')

MomentumAxL2g0010011030 = dataL2g0010011030[:,][:,5*0+0]
KineticEneL2g0010011030 = dataL2g0010011030[:,][:,5*0+1]
SelfEnergyL2g0010011030 = dataL2g0010011030[:,][:,5*0+2]
EigenValReL2g0010011030 = dataL2g0010011030[:,][:,5*0+3]
EigenValImL2g0010011030 = dataL2g0010011030[:,][:,5*0+4]

dataL2g0010011040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK001/N040/HamVals.txt')

MomentumAxL2g0010011040 = dataL2g0010011040[:,][:,5*0+0]
KineticEneL2g0010011040 = dataL2g0010011040[:,][:,5*0+1]
SelfEnergyL2g0010011040 = dataL2g0010011040[:,][:,5*0+2]
EigenValReL2g0010011040 = dataL2g0010011040[:,][:,5*0+3]
EigenValImL2g0010011040 = dataL2g0010011040[:,][:,5*0+4]

dataL2g0010011050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK001/N050/HamVals.txt')

MomentumAxL2g0010011050 = dataL2g0010011050[:,][:,5*0+0]
KineticEneL2g0010011050 = dataL2g0010011050[:,][:,5*0+1]
SelfEnergyL2g0010011050 = dataL2g0010011050[:,][:,5*0+2]
EigenValReL2g0010011050 = dataL2g0010011050[:,][:,5*0+3]
EigenValImL2g0010011050 = dataL2g0010011050[:,][:,5*0+4]

dataL2g0010021010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK002/N010/HamVals.txt')

MomentumAxL2g0010021010 = dataL2g0010021010[:,][:,5*0+0]
KineticEneL2g0010021010 = dataL2g0010021010[:,][:,5*0+1]
SelfEnergyL2g0010021010 = dataL2g0010021010[:,][:,5*0+2]
EigenValReL2g0010021010 = dataL2g0010021010[:,][:,5*0+3]
EigenValImL2g0010021010 = dataL2g0010021010[:,][:,5*0+4]

dataL2g0010021020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK002/N020/HamVals.txt')

MomentumAxL2g0010021020 = dataL2g0010021020[:,][:,5*0+0]
KineticEneL2g0010021020 = dataL2g0010021020[:,][:,5*0+1]
SelfEnergyL2g0010021020 = dataL2g0010021020[:,][:,5*0+2]
EigenValReL2g0010021020 = dataL2g0010021020[:,][:,5*0+3]
EigenValImL2g0010021020 = dataL2g0010021020[:,][:,5*0+4]

dataL2g0010021030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK002/N030/HamVals.txt')

MomentumAxL2g0010021030 = dataL2g0010021030[:,][:,5*0+0]
KineticEneL2g0010021030 = dataL2g0010021030[:,][:,5*0+1]
SelfEnergyL2g0010021030 = dataL2g0010021030[:,][:,5*0+2]
EigenValReL2g0010021030 = dataL2g0010021030[:,][:,5*0+3]
EigenValImL2g0010021030 = dataL2g0010021030[:,][:,5*0+4]

dataL2g0010021040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK002/N040/HamVals.txt')

MomentumAxL2g0010021040 = dataL2g0010021040[:,][:,5*0+0]
KineticEneL2g0010021040 = dataL2g0010021040[:,][:,5*0+1]
SelfEnergyL2g0010021040 = dataL2g0010021040[:,][:,5*0+2]
EigenValReL2g0010021040 = dataL2g0010021040[:,][:,5*0+3]
EigenValImL2g0010021040 = dataL2g0010021040[:,][:,5*0+4]

dataL2g0010021050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK002/N050/HamVals.txt')

MomentumAxL2g0010021050 = dataL2g0010021050[:,][:,5*0+0]
KineticEneL2g0010021050 = dataL2g0010021050[:,][:,5*0+1]
SelfEnergyL2g0010021050 = dataL2g0010021050[:,][:,5*0+2]
EigenValReL2g0010021050 = dataL2g0010021050[:,][:,5*0+3]
EigenValImL2g0010021050 = dataL2g0010021050[:,][:,5*0+4]

dataL2g0010031010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK003/N010/HamVals.txt')

MomentumAxL2g0010031010 = dataL2g0010031010[:,][:,5*0+0]
KineticEneL2g0010031010 = dataL2g0010031010[:,][:,5*0+1]
SelfEnergyL2g0010031010 = dataL2g0010031010[:,][:,5*0+2]
EigenValReL2g0010031010 = dataL2g0010031010[:,][:,5*0+3]
EigenValImL2g0010031010 = dataL2g0010031010[:,][:,5*0+4]

dataL2g0010031020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK003/N020/HamVals.txt')

MomentumAxL2g0010031020 = dataL2g0010031020[:,][:,5*0+0]
KineticEneL2g0010031020 = dataL2g0010031020[:,][:,5*0+1]
SelfEnergyL2g0010031020 = dataL2g0010031020[:,][:,5*0+2]
EigenValReL2g0010031020 = dataL2g0010031020[:,][:,5*0+3]
EigenValImL2g0010031020 = dataL2g0010031020[:,][:,5*0+4]

dataL2g0010031030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK003/N030/HamVals.txt')

MomentumAxL2g0010031030 = dataL2g0010031030[:,][:,5*0+0]
KineticEneL2g0010031030 = dataL2g0010031030[:,][:,5*0+1]
SelfEnergyL2g0010031030 = dataL2g0010031030[:,][:,5*0+2]
EigenValReL2g0010031030 = dataL2g0010031030[:,][:,5*0+3]
EigenValImL2g0010031030 = dataL2g0010031030[:,][:,5*0+4]

dataL2g0010031040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK003/N040/HamVals.txt')

MomentumAxL2g0010031040 = dataL2g0010031040[:,][:,5*0+0]
KineticEneL2g0010031040 = dataL2g0010031040[:,][:,5*0+1]
SelfEnergyL2g0010031040 = dataL2g0010031040[:,][:,5*0+2]
EigenValReL2g0010031040 = dataL2g0010031040[:,][:,5*0+3]
EigenValImL2g0010031040 = dataL2g0010031040[:,][:,5*0+4]

dataL2g0010031050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK003/N050/HamVals.txt')

MomentumAxL2g0010031050 = dataL2g0010031050[:,][:,5*0+0]
KineticEneL2g0010031050 = dataL2g0010031050[:,][:,5*0+1]
SelfEnergyL2g0010031050 = dataL2g0010031050[:,][:,5*0+2]
EigenValReL2g0010031050 = dataL2g0010031050[:,][:,5*0+3]
EigenValImL2g0010031050 = dataL2g0010031050[:,][:,5*0+4]

dataL2g0010051010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK005/N010/HamVals.txt')

MomentumAxL2g0010051010 = dataL2g0010051010[:,][:,5*0+0]
KineticEneL2g0010051010 = dataL2g0010051010[:,][:,5*0+1]
SelfEnergyL2g0010051010 = dataL2g0010051010[:,][:,5*0+2]
EigenValReL2g0010051010 = dataL2g0010051010[:,][:,5*0+3]
EigenValImL2g0010051010 = dataL2g0010051010[:,][:,5*0+4]

dataL2g0010051020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK005/N020/HamVals.txt')

MomentumAxL2g0010051020 = dataL2g0010051020[:,][:,5*0+0]
KineticEneL2g0010051020 = dataL2g0010051020[:,][:,5*0+1]
SelfEnergyL2g0010051020 = dataL2g0010051020[:,][:,5*0+2]
EigenValReL2g0010051020 = dataL2g0010051020[:,][:,5*0+3]
EigenValImL2g0010051020 = dataL2g0010051020[:,][:,5*0+4]

dataL2g0010051030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK005/N030/HamVals.txt')

MomentumAxL2g0010051030 = dataL2g0010051030[:,][:,5*0+0]
KineticEneL2g0010051030 = dataL2g0010051030[:,][:,5*0+1]
SelfEnergyL2g0010051030 = dataL2g0010051030[:,][:,5*0+2]
EigenValReL2g0010051030 = dataL2g0010051030[:,][:,5*0+3]
EigenValImL2g0010051030 = dataL2g0010051030[:,][:,5*0+4]

dataL2g0010051040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK005/N040/HamVals.txt')

MomentumAxL2g0010051040 = dataL2g0010051040[:,][:,5*0+0]
KineticEneL2g0010051040 = dataL2g0010051040[:,][:,5*0+1]
SelfEnergyL2g0010051040 = dataL2g0010051040[:,][:,5*0+2]
EigenValReL2g0010051040 = dataL2g0010051040[:,][:,5*0+3]
EigenValImL2g0010051040 = dataL2g0010051040[:,][:,5*0+4]

dataL2g0010051050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK005/N050/HamVals.txt')

MomentumAxL2g0010051050 = dataL2g0010051050[:,][:,5*0+0]
KineticEneL2g0010051050 = dataL2g0010051050[:,][:,5*0+1]
SelfEnergyL2g0010051050 = dataL2g0010051050[:,][:,5*0+2]
EigenValReL2g0010051050 = dataL2g0010051050[:,][:,5*0+3]
EigenValImL2g0010051050 = dataL2g0010051050[:,][:,5*0+4]

dataL2g0010071010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK007/N010/HamVals.txt')

MomentumAxL2g0010071010 = dataL2g0010071010[:,][:,5*0+0]
KineticEneL2g0010071010 = dataL2g0010071010[:,][:,5*0+1]
SelfEnergyL2g0010071010 = dataL2g0010071010[:,][:,5*0+2]
EigenValReL2g0010071010 = dataL2g0010071010[:,][:,5*0+3]
EigenValImL2g0010071010 = dataL2g0010071010[:,][:,5*0+4]

dataL2g0010071020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK007/N020/HamVals.txt')

MomentumAxL2g0010071020 = dataL2g0010071020[:,][:,5*0+0]
KineticEneL2g0010071020 = dataL2g0010071020[:,][:,5*0+1]
SelfEnergyL2g0010071020 = dataL2g0010071020[:,][:,5*0+2]
EigenValReL2g0010071020 = dataL2g0010071020[:,][:,5*0+3]
EigenValImL2g0010071020 = dataL2g0010071020[:,][:,5*0+4]

dataL2g0010071030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK007/N030/HamVals.txt')

MomentumAxL2g0010071030 = dataL2g0010071030[:,][:,5*0+0]
KineticEneL2g0010071030 = dataL2g0010071030[:,][:,5*0+1]
SelfEnergyL2g0010071030 = dataL2g0010071030[:,][:,5*0+2]
EigenValReL2g0010071030 = dataL2g0010071030[:,][:,5*0+3]
EigenValImL2g0010071030 = dataL2g0010071030[:,][:,5*0+4]

dataL2g0010071040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK007/N040/HamVals.txt')

MomentumAxL2g0010071040 = dataL2g0010071040[:,][:,5*0+0]
KineticEneL2g0010071040 = dataL2g0010071040[:,][:,5*0+1]
SelfEnergyL2g0010071040 = dataL2g0010071040[:,][:,5*0+2]
EigenValReL2g0010071040 = dataL2g0010071040[:,][:,5*0+3]
EigenValImL2g0010071040 = dataL2g0010071040[:,][:,5*0+4]

dataL2g0010071050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK007/N050/HamVals.txt')

MomentumAxL2g0010071050 = dataL2g0010071050[:,][:,5*0+0]
KineticEneL2g0010071050 = dataL2g0010071050[:,][:,5*0+1]
SelfEnergyL2g0010071050 = dataL2g0010071050[:,][:,5*0+2]
EigenValReL2g0010071050 = dataL2g0010071050[:,][:,5*0+3]
EigenValImL2g0010071050 = dataL2g0010071050[:,][:,5*0+4]

dataL2g0010101010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK010/N010/HamVals.txt')

MomentumAxL2g0010101010 = dataL2g0010101010[:,][:,5*0+0]
KineticEneL2g0010101010 = dataL2g0010101010[:,][:,5*0+1]
SelfEnergyL2g0010101010 = dataL2g0010101010[:,][:,5*0+2]
EigenValReL2g0010101010 = dataL2g0010101010[:,][:,5*0+3]
EigenValImL2g0010101010 = dataL2g0010101010[:,][:,5*0+4]

dataL2g0010101020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK010/N020/HamVals.txt')

MomentumAxL2g0010101020 = dataL2g0010101020[:,][:,5*0+0]
KineticEneL2g0010101020 = dataL2g0010101020[:,][:,5*0+1]
SelfEnergyL2g0010101020 = dataL2g0010101020[:,][:,5*0+2]
EigenValReL2g0010101020 = dataL2g0010101020[:,][:,5*0+3]
EigenValImL2g0010101020 = dataL2g0010101020[:,][:,5*0+4]

dataL2g0010101030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK010/N030/HamVals.txt')

MomentumAxL2g0010101030 = dataL2g0010101030[:,][:,5*0+0]
KineticEneL2g0010101030 = dataL2g0010101030[:,][:,5*0+1]
SelfEnergyL2g0010101030 = dataL2g0010101030[:,][:,5*0+2]
EigenValReL2g0010101030 = dataL2g0010101030[:,][:,5*0+3]
EigenValImL2g0010101030 = dataL2g0010101030[:,][:,5*0+4]

dataL2g0010101040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK010/N040/HamVals.txt')

MomentumAxL2g0010101040 = dataL2g0010101040[:,][:,5*0+0]
KineticEneL2g0010101040 = dataL2g0010101040[:,][:,5*0+1]
SelfEnergyL2g0010101040 = dataL2g0010101040[:,][:,5*0+2]
EigenValReL2g0010101040 = dataL2g0010101040[:,][:,5*0+3]
EigenValImL2g0010101040 = dataL2g0010101040[:,][:,5*0+4]

dataL2g0010101050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK010/N050/HamVals.txt')

MomentumAxL2g0010101050 = dataL2g0010101050[:,][:,5*0+0]
KineticEneL2g0010101050 = dataL2g0010101050[:,][:,5*0+1]
SelfEnergyL2g0010101050 = dataL2g0010101050[:,][:,5*0+2]
EigenValReL2g0010101050 = dataL2g0010101050[:,][:,5*0+3]
EigenValImL2g0010101050 = dataL2g0010101050[:,][:,5*0+4]

MaxEigenValImL2g0011Inf = np.zeros((6))

MaxEigenValImL2g0011Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0010011010),np.max(EigenValImL2g0010011020),np.max(EigenValImL2g0010011030),np.max(EigenValImL2g0010011040),np.max(EigenValImL2g0010011050)], 1)[[1]]
MaxEigenValImL2g0011Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0010021010),np.max(EigenValImL2g0010021020),np.max(EigenValImL2g0010021030),np.max(EigenValImL2g0010021040),np.max(EigenValImL2g0010021050)], 1)[[1]]
MaxEigenValImL2g0011Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0010031010),np.max(EigenValImL2g0010031020),np.max(EigenValImL2g0010031030),np.max(EigenValImL2g0010031040),np.max(EigenValImL2g0010031050)], 1)[[1]]
MaxEigenValImL2g0011Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0010051010),np.max(EigenValImL2g0010051020),np.max(EigenValImL2g0010051030),np.max(EigenValImL2g0010051040),np.max(EigenValImL2g0010051050)], 1)[[1]]
MaxEigenValImL2g0011Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0010071010),np.max(EigenValImL2g0010071020),np.max(EigenValImL2g0010071030),np.max(EigenValImL2g0010071040),np.max(EigenValImL2g0010071050)], 1)[[1]]
MaxEigenValImL2g0011Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0010101010),np.max(EigenValImL2g0010101020),np.max(EigenValImL2g0010101030),np.max(EigenValImL2g0010101040),np.max(EigenValImL2g0010101050)], 1)[[1]]

########################################################################

dataL2g0020011010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK001/N010/HamVals.txt')

MomentumAxL2g0020011010 = dataL2g0020011010[:,][:,5*0+0]
KineticEneL2g0020011010 = dataL2g0020011010[:,][:,5*0+1]
SelfEnergyL2g0020011010 = dataL2g0020011010[:,][:,5*0+2]
EigenValReL2g0020011010 = dataL2g0020011010[:,][:,5*0+3]
EigenValImL2g0020011010 = dataL2g0020011010[:,][:,5*0+4]

dataL2g0020011020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK001/N020/HamVals.txt')

MomentumAxL2g0020011020 = dataL2g0020011020[:,][:,5*0+0]
KineticEneL2g0020011020 = dataL2g0020011020[:,][:,5*0+1]
SelfEnergyL2g0020011020 = dataL2g0020011020[:,][:,5*0+2]
EigenValReL2g0020011020 = dataL2g0020011020[:,][:,5*0+3]
EigenValImL2g0020011020 = dataL2g0020011020[:,][:,5*0+4]

dataL2g0020011030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK001/N030/HamVals.txt')

MomentumAxL2g0020011030 = dataL2g0020011030[:,][:,5*0+0]
KineticEneL2g0020011030 = dataL2g0020011030[:,][:,5*0+1]
SelfEnergyL2g0020011030 = dataL2g0020011030[:,][:,5*0+2]
EigenValReL2g0020011030 = dataL2g0020011030[:,][:,5*0+3]
EigenValImL2g0020011030 = dataL2g0020011030[:,][:,5*0+4]

dataL2g0020011040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK001/N040/HamVals.txt')

MomentumAxL2g0020011040 = dataL2g0020011040[:,][:,5*0+0]
KineticEneL2g0020011040 = dataL2g0020011040[:,][:,5*0+1]
SelfEnergyL2g0020011040 = dataL2g0020011040[:,][:,5*0+2]
EigenValReL2g0020011040 = dataL2g0020011040[:,][:,5*0+3]
EigenValImL2g0020011040 = dataL2g0020011040[:,][:,5*0+4]

dataL2g0020011050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK001/N050/HamVals.txt')

MomentumAxL2g0020011050 = dataL2g0020011050[:,][:,5*0+0]
KineticEneL2g0020011050 = dataL2g0020011050[:,][:,5*0+1]
SelfEnergyL2g0020011050 = dataL2g0020011050[:,][:,5*0+2]
EigenValReL2g0020011050 = dataL2g0020011050[:,][:,5*0+3]
EigenValImL2g0020011050 = dataL2g0020011050[:,][:,5*0+4]

dataL2g0020021010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK002/N010/HamVals.txt')

MomentumAxL2g0020021010 = dataL2g0020021010[:,][:,5*0+0]
KineticEneL2g0020021010 = dataL2g0020021010[:,][:,5*0+1]
SelfEnergyL2g0020021010 = dataL2g0020021010[:,][:,5*0+2]
EigenValReL2g0020021010 = dataL2g0020021010[:,][:,5*0+3]
EigenValImL2g0020021010 = dataL2g0020021010[:,][:,5*0+4]

dataL2g0020021020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK002/N020/HamVals.txt')

MomentumAxL2g0020021020 = dataL2g0020021020[:,][:,5*0+0]
KineticEneL2g0020021020 = dataL2g0020021020[:,][:,5*0+1]
SelfEnergyL2g0020021020 = dataL2g0020021020[:,][:,5*0+2]
EigenValReL2g0020021020 = dataL2g0020021020[:,][:,5*0+3]
EigenValImL2g0020021020 = dataL2g0020021020[:,][:,5*0+4]

dataL2g0020021030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK002/N030/HamVals.txt')

MomentumAxL2g0020021030 = dataL2g0020021030[:,][:,5*0+0]
KineticEneL2g0020021030 = dataL2g0020021030[:,][:,5*0+1]
SelfEnergyL2g0020021030 = dataL2g0020021030[:,][:,5*0+2]
EigenValReL2g0020021030 = dataL2g0020021030[:,][:,5*0+3]
EigenValImL2g0020021030 = dataL2g0020021030[:,][:,5*0+4]

dataL2g0020021040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK002/N040/HamVals.txt')

MomentumAxL2g0020021040 = dataL2g0020021040[:,][:,5*0+0]
KineticEneL2g0020021040 = dataL2g0020021040[:,][:,5*0+1]
SelfEnergyL2g0020021040 = dataL2g0020021040[:,][:,5*0+2]
EigenValReL2g0020021040 = dataL2g0020021040[:,][:,5*0+3]
EigenValImL2g0020021040 = dataL2g0020021040[:,][:,5*0+4]

dataL2g0020021050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK002/N050/HamVals.txt')

MomentumAxL2g0020021050 = dataL2g0020021050[:,][:,5*0+0]
KineticEneL2g0020021050 = dataL2g0020021050[:,][:,5*0+1]
SelfEnergyL2g0020021050 = dataL2g0020021050[:,][:,5*0+2]
EigenValReL2g0020021050 = dataL2g0020021050[:,][:,5*0+3]
EigenValImL2g0020021050 = dataL2g0020021050[:,][:,5*0+4]

dataL2g0020031010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK003/N010/HamVals.txt')

MomentumAxL2g0020031010 = dataL2g0020031010[:,][:,5*0+0]
KineticEneL2g0020031010 = dataL2g0020031010[:,][:,5*0+1]
SelfEnergyL2g0020031010 = dataL2g0020031010[:,][:,5*0+2]
EigenValReL2g0020031010 = dataL2g0020031010[:,][:,5*0+3]
EigenValImL2g0020031010 = dataL2g0020031010[:,][:,5*0+4]

dataL2g0020031020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK003/N020/HamVals.txt')

MomentumAxL2g0020031020 = dataL2g0020031020[:,][:,5*0+0]
KineticEneL2g0020031020 = dataL2g0020031020[:,][:,5*0+1]
SelfEnergyL2g0020031020 = dataL2g0020031020[:,][:,5*0+2]
EigenValReL2g0020031020 = dataL2g0020031020[:,][:,5*0+3]
EigenValImL2g0020031020 = dataL2g0020031020[:,][:,5*0+4]

dataL2g0020031030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK003/N030/HamVals.txt')

MomentumAxL2g0020031030 = dataL2g0020031030[:,][:,5*0+0]
KineticEneL2g0020031030 = dataL2g0020031030[:,][:,5*0+1]
SelfEnergyL2g0020031030 = dataL2g0020031030[:,][:,5*0+2]
EigenValReL2g0020031030 = dataL2g0020031030[:,][:,5*0+3]
EigenValImL2g0020031030 = dataL2g0020031030[:,][:,5*0+4]

dataL2g0020031040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK003/N040/HamVals.txt')

MomentumAxL2g0020031040 = dataL2g0020031040[:,][:,5*0+0]
KineticEneL2g0020031040 = dataL2g0020031040[:,][:,5*0+1]
SelfEnergyL2g0020031040 = dataL2g0020031040[:,][:,5*0+2]
EigenValReL2g0020031040 = dataL2g0020031040[:,][:,5*0+3]
EigenValImL2g0020031040 = dataL2g0020031040[:,][:,5*0+4]

dataL2g0020031050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK003/N050/HamVals.txt')

MomentumAxL2g0020031050 = dataL2g0020031050[:,][:,5*0+0]
KineticEneL2g0020031050 = dataL2g0020031050[:,][:,5*0+1]
SelfEnergyL2g0020031050 = dataL2g0020031050[:,][:,5*0+2]
EigenValReL2g0020031050 = dataL2g0020031050[:,][:,5*0+3]
EigenValImL2g0020031050 = dataL2g0020031050[:,][:,5*0+4]

dataL2g0020051010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK005/N010/HamVals.txt')

MomentumAxL2g0020051010 = dataL2g0020051010[:,][:,5*0+0]
KineticEneL2g0020051010 = dataL2g0020051010[:,][:,5*0+1]
SelfEnergyL2g0020051010 = dataL2g0020051010[:,][:,5*0+2]
EigenValReL2g0020051010 = dataL2g0020051010[:,][:,5*0+3]
EigenValImL2g0020051010 = dataL2g0020051010[:,][:,5*0+4]

dataL2g0020051020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK005/N020/HamVals.txt')

MomentumAxL2g0020051020 = dataL2g0020051020[:,][:,5*0+0]
KineticEneL2g0020051020 = dataL2g0020051020[:,][:,5*0+1]
SelfEnergyL2g0020051020 = dataL2g0020051020[:,][:,5*0+2]
EigenValReL2g0020051020 = dataL2g0020051020[:,][:,5*0+3]
EigenValImL2g0020051020 = dataL2g0020051020[:,][:,5*0+4]

dataL2g0020051030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK005/N030/HamVals.txt')

MomentumAxL2g0020051030 = dataL2g0020051030[:,][:,5*0+0]
KineticEneL2g0020051030 = dataL2g0020051030[:,][:,5*0+1]
SelfEnergyL2g0020051030 = dataL2g0020051030[:,][:,5*0+2]
EigenValReL2g0020051030 = dataL2g0020051030[:,][:,5*0+3]
EigenValImL2g0020051030 = dataL2g0020051030[:,][:,5*0+4]

dataL2g0020051040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK005/N040/HamVals.txt')

MomentumAxL2g0020051040 = dataL2g0020051040[:,][:,5*0+0]
KineticEneL2g0020051040 = dataL2g0020051040[:,][:,5*0+1]
SelfEnergyL2g0020051040 = dataL2g0020051040[:,][:,5*0+2]
EigenValReL2g0020051040 = dataL2g0020051040[:,][:,5*0+3]
EigenValImL2g0020051040 = dataL2g0020051040[:,][:,5*0+4]

dataL2g0020051050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK005/N050/HamVals.txt')

MomentumAxL2g0020051050 = dataL2g0020051050[:,][:,5*0+0]
KineticEneL2g0020051050 = dataL2g0020051050[:,][:,5*0+1]
SelfEnergyL2g0020051050 = dataL2g0020051050[:,][:,5*0+2]
EigenValReL2g0020051050 = dataL2g0020051050[:,][:,5*0+3]
EigenValImL2g0020051050 = dataL2g0020051050[:,][:,5*0+4]

dataL2g0020071010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK007/N010/HamVals.txt')

MomentumAxL2g0020071010 = dataL2g0020071010[:,][:,5*0+0]
KineticEneL2g0020071010 = dataL2g0020071010[:,][:,5*0+1]
SelfEnergyL2g0020071010 = dataL2g0020071010[:,][:,5*0+2]
EigenValReL2g0020071010 = dataL2g0020071010[:,][:,5*0+3]
EigenValImL2g0020071010 = dataL2g0020071010[:,][:,5*0+4]

dataL2g0020071020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK007/N020/HamVals.txt')

MomentumAxL2g0020071020 = dataL2g0020071020[:,][:,5*0+0]
KineticEneL2g0020071020 = dataL2g0020071020[:,][:,5*0+1]
SelfEnergyL2g0020071020 = dataL2g0020071020[:,][:,5*0+2]
EigenValReL2g0020071020 = dataL2g0020071020[:,][:,5*0+3]
EigenValImL2g0020071020 = dataL2g0020071020[:,][:,5*0+4]

dataL2g0020071030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK007/N030/HamVals.txt')

MomentumAxL2g0020071030 = dataL2g0020071030[:,][:,5*0+0]
KineticEneL2g0020071030 = dataL2g0020071030[:,][:,5*0+1]
SelfEnergyL2g0020071030 = dataL2g0020071030[:,][:,5*0+2]
EigenValReL2g0020071030 = dataL2g0020071030[:,][:,5*0+3]
EigenValImL2g0020071030 = dataL2g0020071030[:,][:,5*0+4]

dataL2g0020071040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK007/N040/HamVals.txt')

MomentumAxL2g0020071040 = dataL2g0020071040[:,][:,5*0+0]
KineticEneL2g0020071040 = dataL2g0020071040[:,][:,5*0+1]
SelfEnergyL2g0020071040 = dataL2g0020071040[:,][:,5*0+2]
EigenValReL2g0020071040 = dataL2g0020071040[:,][:,5*0+3]
EigenValImL2g0020071040 = dataL2g0020071040[:,][:,5*0+4]

dataL2g0020071050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK007/N050/HamVals.txt')

MomentumAxL2g0020071050 = dataL2g0020071050[:,][:,5*0+0]
KineticEneL2g0020071050 = dataL2g0020071050[:,][:,5*0+1]
SelfEnergyL2g0020071050 = dataL2g0020071050[:,][:,5*0+2]
EigenValReL2g0020071050 = dataL2g0020071050[:,][:,5*0+3]
EigenValImL2g0020071050 = dataL2g0020071050[:,][:,5*0+4]

dataL2g0020101010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK010/N010/HamVals.txt')

MomentumAxL2g0020101010 = dataL2g0020101010[:,][:,5*0+0]
KineticEneL2g0020101010 = dataL2g0020101010[:,][:,5*0+1]
SelfEnergyL2g0020101010 = dataL2g0020101010[:,][:,5*0+2]
EigenValReL2g0020101010 = dataL2g0020101010[:,][:,5*0+3]
EigenValImL2g0020101010 = dataL2g0020101010[:,][:,5*0+4]

dataL2g0020101020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK010/N020/HamVals.txt')

MomentumAxL2g0020101020 = dataL2g0020101020[:,][:,5*0+0]
KineticEneL2g0020101020 = dataL2g0020101020[:,][:,5*0+1]
SelfEnergyL2g0020101020 = dataL2g0020101020[:,][:,5*0+2]
EigenValReL2g0020101020 = dataL2g0020101020[:,][:,5*0+3]
EigenValImL2g0020101020 = dataL2g0020101020[:,][:,5*0+4]

dataL2g0020101030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK010/N030/HamVals.txt')

MomentumAxL2g0020101030 = dataL2g0020101030[:,][:,5*0+0]
KineticEneL2g0020101030 = dataL2g0020101030[:,][:,5*0+1]
SelfEnergyL2g0020101030 = dataL2g0020101030[:,][:,5*0+2]
EigenValReL2g0020101030 = dataL2g0020101030[:,][:,5*0+3]
EigenValImL2g0020101030 = dataL2g0020101030[:,][:,5*0+4]

dataL2g0020101040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK010/N040/HamVals.txt')

MomentumAxL2g0020101040 = dataL2g0020101040[:,][:,5*0+0]
KineticEneL2g0020101040 = dataL2g0020101040[:,][:,5*0+1]
SelfEnergyL2g0020101040 = dataL2g0020101040[:,][:,5*0+2]
EigenValReL2g0020101040 = dataL2g0020101040[:,][:,5*0+3]
EigenValImL2g0020101040 = dataL2g0020101040[:,][:,5*0+4]

dataL2g0020101050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK010/N050/HamVals.txt')

MomentumAxL2g0020101050 = dataL2g0020101050[:,][:,5*0+0]
KineticEneL2g0020101050 = dataL2g0020101050[:,][:,5*0+1]
SelfEnergyL2g0020101050 = dataL2g0020101050[:,][:,5*0+2]
EigenValReL2g0020101050 = dataL2g0020101050[:,][:,5*0+3]
EigenValImL2g0020101050 = dataL2g0020101050[:,][:,5*0+4]

MaxEigenValImL2g0021Inf = np.zeros((6))

MaxEigenValImL2g0021Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0020011010),np.max(EigenValImL2g0020011020),np.max(EigenValImL2g0020011030),np.max(EigenValImL2g0020011040),np.max(EigenValImL2g0020011050)], 1)[[1]]
MaxEigenValImL2g0021Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0020021010),np.max(EigenValImL2g0020021020),np.max(EigenValImL2g0020021030),np.max(EigenValImL2g0020021040),np.max(EigenValImL2g0020021050)], 1)[[1]]
MaxEigenValImL2g0021Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0020031010),np.max(EigenValImL2g0020031020),np.max(EigenValImL2g0020031030),np.max(EigenValImL2g0020031040),np.max(EigenValImL2g0020031050)], 1)[[1]]
MaxEigenValImL2g0021Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0020051010),np.max(EigenValImL2g0020051020),np.max(EigenValImL2g0020051030),np.max(EigenValImL2g0020051040),np.max(EigenValImL2g0020051050)], 1)[[1]]
MaxEigenValImL2g0021Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0020071010),np.max(EigenValImL2g0020071020),np.max(EigenValImL2g0020071030),np.max(EigenValImL2g0020071040),np.max(EigenValImL2g0020071050)], 1)[[1]]
MaxEigenValImL2g0021Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0020101010),np.max(EigenValImL2g0020101020),np.max(EigenValImL2g0020101030),np.max(EigenValImL2g0020101040),np.max(EigenValImL2g0020101050)], 1)[[1]]

########################################################################

dataL2g0050011010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK001/N010/HamVals.txt')

MomentumAxL2g0050011010 = dataL2g0050011010[:,][:,5*0+0]
KineticEneL2g0050011010 = dataL2g0050011010[:,][:,5*0+1]
SelfEnergyL2g0050011010 = dataL2g0050011010[:,][:,5*0+2]
EigenValReL2g0050011010 = dataL2g0050011010[:,][:,5*0+3]
EigenValImL2g0050011010 = dataL2g0050011010[:,][:,5*0+4]

dataL2g0050011020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK001/N020/HamVals.txt')

MomentumAxL2g0050011020 = dataL2g0050011020[:,][:,5*0+0]
KineticEneL2g0050011020 = dataL2g0050011020[:,][:,5*0+1]
SelfEnergyL2g0050011020 = dataL2g0050011020[:,][:,5*0+2]
EigenValReL2g0050011020 = dataL2g0050011020[:,][:,5*0+3]
EigenValImL2g0050011020 = dataL2g0050011020[:,][:,5*0+4]

dataL2g0050011030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK001/N030/HamVals.txt')

MomentumAxL2g0050011030 = dataL2g0050011030[:,][:,5*0+0]
KineticEneL2g0050011030 = dataL2g0050011030[:,][:,5*0+1]
SelfEnergyL2g0050011030 = dataL2g0050011030[:,][:,5*0+2]
EigenValReL2g0050011030 = dataL2g0050011030[:,][:,5*0+3]
EigenValImL2g0050011030 = dataL2g0050011030[:,][:,5*0+4]

dataL2g0050011040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK001/N040/HamVals.txt')

MomentumAxL2g0050011040 = dataL2g0050011040[:,][:,5*0+0]
KineticEneL2g0050011040 = dataL2g0050011040[:,][:,5*0+1]
SelfEnergyL2g0050011040 = dataL2g0050011040[:,][:,5*0+2]
EigenValReL2g0050011040 = dataL2g0050011040[:,][:,5*0+3]
EigenValImL2g0050011040 = dataL2g0050011040[:,][:,5*0+4]

dataL2g0050011050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK001/N050/HamVals.txt')

MomentumAxL2g0050011050 = dataL2g0050011050[:,][:,5*0+0]
KineticEneL2g0050011050 = dataL2g0050011050[:,][:,5*0+1]
SelfEnergyL2g0050011050 = dataL2g0050011050[:,][:,5*0+2]
EigenValReL2g0050011050 = dataL2g0050011050[:,][:,5*0+3]
EigenValImL2g0050011050 = dataL2g0050011050[:,][:,5*0+4]

dataL2g0050021010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK002/N010/HamVals.txt')

MomentumAxL2g0050021010 = dataL2g0050021010[:,][:,5*0+0]
KineticEneL2g0050021010 = dataL2g0050021010[:,][:,5*0+1]
SelfEnergyL2g0050021010 = dataL2g0050021010[:,][:,5*0+2]
EigenValReL2g0050021010 = dataL2g0050021010[:,][:,5*0+3]
EigenValImL2g0050021010 = dataL2g0050021010[:,][:,5*0+4]

dataL2g0050021020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK002/N020/HamVals.txt')

MomentumAxL2g0050021020 = dataL2g0050021020[:,][:,5*0+0]
KineticEneL2g0050021020 = dataL2g0050021020[:,][:,5*0+1]
SelfEnergyL2g0050021020 = dataL2g0050021020[:,][:,5*0+2]
EigenValReL2g0050021020 = dataL2g0050021020[:,][:,5*0+3]
EigenValImL2g0050021020 = dataL2g0050021020[:,][:,5*0+4]

dataL2g0050021030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK002/N030/HamVals.txt')

MomentumAxL2g0050021030 = dataL2g0050021030[:,][:,5*0+0]
KineticEneL2g0050021030 = dataL2g0050021030[:,][:,5*0+1]
SelfEnergyL2g0050021030 = dataL2g0050021030[:,][:,5*0+2]
EigenValReL2g0050021030 = dataL2g0050021030[:,][:,5*0+3]
EigenValImL2g0050021030 = dataL2g0050021030[:,][:,5*0+4]

dataL2g0050021040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK002/N040/HamVals.txt')

MomentumAxL2g0050021040 = dataL2g0050021040[:,][:,5*0+0]
KineticEneL2g0050021040 = dataL2g0050021040[:,][:,5*0+1]
SelfEnergyL2g0050021040 = dataL2g0050021040[:,][:,5*0+2]
EigenValReL2g0050021040 = dataL2g0050021040[:,][:,5*0+3]
EigenValImL2g0050021040 = dataL2g0050021040[:,][:,5*0+4]

dataL2g0050021050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK002/N050/HamVals.txt')

MomentumAxL2g0050021050 = dataL2g0050021050[:,][:,5*0+0]
KineticEneL2g0050021050 = dataL2g0050021050[:,][:,5*0+1]
SelfEnergyL2g0050021050 = dataL2g0050021050[:,][:,5*0+2]
EigenValReL2g0050021050 = dataL2g0050021050[:,][:,5*0+3]
EigenValImL2g0050021050 = dataL2g0050021050[:,][:,5*0+4]

dataL2g0050031010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK003/N010/HamVals.txt')

MomentumAxL2g0050031010 = dataL2g0050031010[:,][:,5*0+0]
KineticEneL2g0050031010 = dataL2g0050031010[:,][:,5*0+1]
SelfEnergyL2g0050031010 = dataL2g0050031010[:,][:,5*0+2]
EigenValReL2g0050031010 = dataL2g0050031010[:,][:,5*0+3]
EigenValImL2g0050031010 = dataL2g0050031010[:,][:,5*0+4]

dataL2g0050031020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK003/N020/HamVals.txt')

MomentumAxL2g0050031020 = dataL2g0050031020[:,][:,5*0+0]
KineticEneL2g0050031020 = dataL2g0050031020[:,][:,5*0+1]
SelfEnergyL2g0050031020 = dataL2g0050031020[:,][:,5*0+2]
EigenValReL2g0050031020 = dataL2g0050031020[:,][:,5*0+3]
EigenValImL2g0050031020 = dataL2g0050031020[:,][:,5*0+4]

dataL2g0050031030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK003/N030/HamVals.txt')

MomentumAxL2g0050031030 = dataL2g0050031030[:,][:,5*0+0]
KineticEneL2g0050031030 = dataL2g0050031030[:,][:,5*0+1]
SelfEnergyL2g0050031030 = dataL2g0050031030[:,][:,5*0+2]
EigenValReL2g0050031030 = dataL2g0050031030[:,][:,5*0+3]
EigenValImL2g0050031030 = dataL2g0050031030[:,][:,5*0+4]

dataL2g0050031040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK003/N040/HamVals.txt')

MomentumAxL2g0050031040 = dataL2g0050031040[:,][:,5*0+0]
KineticEneL2g0050031040 = dataL2g0050031040[:,][:,5*0+1]
SelfEnergyL2g0050031040 = dataL2g0050031040[:,][:,5*0+2]
EigenValReL2g0050031040 = dataL2g0050031040[:,][:,5*0+3]
EigenValImL2g0050031040 = dataL2g0050031040[:,][:,5*0+4]

dataL2g0050031050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK003/N050/HamVals.txt')

MomentumAxL2g0050031050 = dataL2g0050031050[:,][:,5*0+0]
KineticEneL2g0050031050 = dataL2g0050031050[:,][:,5*0+1]
SelfEnergyL2g0050031050 = dataL2g0050031050[:,][:,5*0+2]
EigenValReL2g0050031050 = dataL2g0050031050[:,][:,5*0+3]
EigenValImL2g0050031050 = dataL2g0050031050[:,][:,5*0+4]

dataL2g0050051010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK005/N010/HamVals.txt')

MomentumAxL2g0050051010 = dataL2g0050051010[:,][:,5*0+0]
KineticEneL2g0050051010 = dataL2g0050051010[:,][:,5*0+1]
SelfEnergyL2g0050051010 = dataL2g0050051010[:,][:,5*0+2]
EigenValReL2g0050051010 = dataL2g0050051010[:,][:,5*0+3]
EigenValImL2g0050051010 = dataL2g0050051010[:,][:,5*0+4]

dataL2g0050051020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK005/N020/HamVals.txt')

MomentumAxL2g0050051020 = dataL2g0050051020[:,][:,5*0+0]
KineticEneL2g0050051020 = dataL2g0050051020[:,][:,5*0+1]
SelfEnergyL2g0050051020 = dataL2g0050051020[:,][:,5*0+2]
EigenValReL2g0050051020 = dataL2g0050051020[:,][:,5*0+3]
EigenValImL2g0050051020 = dataL2g0050051020[:,][:,5*0+4]

dataL2g0050051030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK005/N030/HamVals.txt')

MomentumAxL2g0050051030 = dataL2g0050051030[:,][:,5*0+0]
KineticEneL2g0050051030 = dataL2g0050051030[:,][:,5*0+1]
SelfEnergyL2g0050051030 = dataL2g0050051030[:,][:,5*0+2]
EigenValReL2g0050051030 = dataL2g0050051030[:,][:,5*0+3]
EigenValImL2g0050051030 = dataL2g0050051030[:,][:,5*0+4]

dataL2g0050051040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK005/N040/HamVals.txt')

MomentumAxL2g0050051040 = dataL2g0050051040[:,][:,5*0+0]
KineticEneL2g0050051040 = dataL2g0050051040[:,][:,5*0+1]
SelfEnergyL2g0050051040 = dataL2g0050051040[:,][:,5*0+2]
EigenValReL2g0050051040 = dataL2g0050051040[:,][:,5*0+3]
EigenValImL2g0050051040 = dataL2g0050051040[:,][:,5*0+4]

dataL2g0050051050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK005/N050/HamVals.txt')

MomentumAxL2g0050051050 = dataL2g0050051050[:,][:,5*0+0]
KineticEneL2g0050051050 = dataL2g0050051050[:,][:,5*0+1]
SelfEnergyL2g0050051050 = dataL2g0050051050[:,][:,5*0+2]
EigenValReL2g0050051050 = dataL2g0050051050[:,][:,5*0+3]
EigenValImL2g0050051050 = dataL2g0050051050[:,][:,5*0+4]

dataL2g0050071010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK007/N010/HamVals.txt')

MomentumAxL2g0050071010 = dataL2g0050071010[:,][:,5*0+0]
KineticEneL2g0050071010 = dataL2g0050071010[:,][:,5*0+1]
SelfEnergyL2g0050071010 = dataL2g0050071010[:,][:,5*0+2]
EigenValReL2g0050071010 = dataL2g0050071010[:,][:,5*0+3]
EigenValImL2g0050071010 = dataL2g0050071010[:,][:,5*0+4]

dataL2g0050071020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK007/N020/HamVals.txt')

MomentumAxL2g0050071020 = dataL2g0050071020[:,][:,5*0+0]
KineticEneL2g0050071020 = dataL2g0050071020[:,][:,5*0+1]
SelfEnergyL2g0050071020 = dataL2g0050071020[:,][:,5*0+2]
EigenValReL2g0050071020 = dataL2g0050071020[:,][:,5*0+3]
EigenValImL2g0050071020 = dataL2g0050071020[:,][:,5*0+4]

dataL2g0050071030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK007/N030/HamVals.txt')

MomentumAxL2g0050071030 = dataL2g0050071030[:,][:,5*0+0]
KineticEneL2g0050071030 = dataL2g0050071030[:,][:,5*0+1]
SelfEnergyL2g0050071030 = dataL2g0050071030[:,][:,5*0+2]
EigenValReL2g0050071030 = dataL2g0050071030[:,][:,5*0+3]
EigenValImL2g0050071030 = dataL2g0050071030[:,][:,5*0+4]

dataL2g0050071040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK007/N040/HamVals.txt')

MomentumAxL2g0050071040 = dataL2g0050071040[:,][:,5*0+0]
KineticEneL2g0050071040 = dataL2g0050071040[:,][:,5*0+1]
SelfEnergyL2g0050071040 = dataL2g0050071040[:,][:,5*0+2]
EigenValReL2g0050071040 = dataL2g0050071040[:,][:,5*0+3]
EigenValImL2g0050071040 = dataL2g0050071040[:,][:,5*0+4]

dataL2g0050071050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK007/N050/HamVals.txt')

MomentumAxL2g0050071050 = dataL2g0050071050[:,][:,5*0+0]
KineticEneL2g0050071050 = dataL2g0050071050[:,][:,5*0+1]
SelfEnergyL2g0050071050 = dataL2g0050071050[:,][:,5*0+2]
EigenValReL2g0050071050 = dataL2g0050071050[:,][:,5*0+3]
EigenValImL2g0050071050 = dataL2g0050071050[:,][:,5*0+4]

dataL2g0050101010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK010/N010/HamVals.txt')

MomentumAxL2g0050101010 = dataL2g0050101010[:,][:,5*0+0]
KineticEneL2g0050101010 = dataL2g0050101010[:,][:,5*0+1]
SelfEnergyL2g0050101010 = dataL2g0050101010[:,][:,5*0+2]
EigenValReL2g0050101010 = dataL2g0050101010[:,][:,5*0+3]
EigenValImL2g0050101010 = dataL2g0050101010[:,][:,5*0+4]

dataL2g0050101020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK010/N020/HamVals.txt')

MomentumAxL2g0050101020 = dataL2g0050101020[:,][:,5*0+0]
KineticEneL2g0050101020 = dataL2g0050101020[:,][:,5*0+1]
SelfEnergyL2g0050101020 = dataL2g0050101020[:,][:,5*0+2]
EigenValReL2g0050101020 = dataL2g0050101020[:,][:,5*0+3]
EigenValImL2g0050101020 = dataL2g0050101020[:,][:,5*0+4]

dataL2g0050101030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK010/N030/HamVals.txt')

MomentumAxL2g0050101030 = dataL2g0050101030[:,][:,5*0+0]
KineticEneL2g0050101030 = dataL2g0050101030[:,][:,5*0+1]
SelfEnergyL2g0050101030 = dataL2g0050101030[:,][:,5*0+2]
EigenValReL2g0050101030 = dataL2g0050101030[:,][:,5*0+3]
EigenValImL2g0050101030 = dataL2g0050101030[:,][:,5*0+4]

dataL2g0050101040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK010/N040/HamVals.txt')

MomentumAxL2g0050101040 = dataL2g0050101040[:,][:,5*0+0]
KineticEneL2g0050101040 = dataL2g0050101040[:,][:,5*0+1]
SelfEnergyL2g0050101040 = dataL2g0050101040[:,][:,5*0+2]
EigenValReL2g0050101040 = dataL2g0050101040[:,][:,5*0+3]
EigenValImL2g0050101040 = dataL2g0050101040[:,][:,5*0+4]

dataL2g0050101050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK010/N050/HamVals.txt')

MomentumAxL2g0050101050 = dataL2g0050101050[:,][:,5*0+0]
KineticEneL2g0050101050 = dataL2g0050101050[:,][:,5*0+1]
SelfEnergyL2g0050101050 = dataL2g0050101050[:,][:,5*0+2]
EigenValReL2g0050101050 = dataL2g0050101050[:,][:,5*0+3]
EigenValImL2g0050101050 = dataL2g0050101050[:,][:,5*0+4]

MaxEigenValImL2g0051Inf = np.zeros((6))

MaxEigenValImL2g0051Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0050011010),np.max(EigenValImL2g0050011020),np.max(EigenValImL2g0050011030),np.max(EigenValImL2g0050011040),np.max(EigenValImL2g0050011050)], 1)[[1]]
MaxEigenValImL2g0051Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0050021010),np.max(EigenValImL2g0050021020),np.max(EigenValImL2g0050021030),np.max(EigenValImL2g0050021040),np.max(EigenValImL2g0050021050)], 1)[[1]]
MaxEigenValImL2g0051Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0050031010),np.max(EigenValImL2g0050031020),np.max(EigenValImL2g0050031030),np.max(EigenValImL2g0050031040),np.max(EigenValImL2g0050031050)], 1)[[1]]
MaxEigenValImL2g0051Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0050051010),np.max(EigenValImL2g0050051020),np.max(EigenValImL2g0050051030),np.max(EigenValImL2g0050051040),np.max(EigenValImL2g0050051050)], 1)[[1]]
MaxEigenValImL2g0051Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0050071010),np.max(EigenValImL2g0050071020),np.max(EigenValImL2g0050071030),np.max(EigenValImL2g0050071040),np.max(EigenValImL2g0050071050)], 1)[[1]]
MaxEigenValImL2g0051Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0050101010),np.max(EigenValImL2g0050101020),np.max(EigenValImL2g0050101030),np.max(EigenValImL2g0050101040),np.max(EigenValImL2g0050101050)], 1)[[1]]

########################################################################

dataL2g0100011010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK001/N010/HamVals.txt')

MomentumAxL2g0100011010 = dataL2g0100011010[:,][:,5*0+0]
KineticEneL2g0100011010 = dataL2g0100011010[:,][:,5*0+1]
SelfEnergyL2g0100011010 = dataL2g0100011010[:,][:,5*0+2]
EigenValReL2g0100011010 = dataL2g0100011010[:,][:,5*0+3]
EigenValImL2g0100011010 = dataL2g0100011010[:,][:,5*0+4]

dataL2g0100011020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK001/N020/HamVals.txt')

MomentumAxL2g0100011020 = dataL2g0100011020[:,][:,5*0+0]
KineticEneL2g0100011020 = dataL2g0100011020[:,][:,5*0+1]
SelfEnergyL2g0100011020 = dataL2g0100011020[:,][:,5*0+2]
EigenValReL2g0100011020 = dataL2g0100011020[:,][:,5*0+3]
EigenValImL2g0100011020 = dataL2g0100011020[:,][:,5*0+4]

dataL2g0100011030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK001/N030/HamVals.txt')

MomentumAxL2g0100011030 = dataL2g0100011030[:,][:,5*0+0]
KineticEneL2g0100011030 = dataL2g0100011030[:,][:,5*0+1]
SelfEnergyL2g0100011030 = dataL2g0100011030[:,][:,5*0+2]
EigenValReL2g0100011030 = dataL2g0100011030[:,][:,5*0+3]
EigenValImL2g0100011030 = dataL2g0100011030[:,][:,5*0+4]

dataL2g0100011040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK001/N040/HamVals.txt')

MomentumAxL2g0100011040 = dataL2g0100011040[:,][:,5*0+0]
KineticEneL2g0100011040 = dataL2g0100011040[:,][:,5*0+1]
SelfEnergyL2g0100011040 = dataL2g0100011040[:,][:,5*0+2]
EigenValReL2g0100011040 = dataL2g0100011040[:,][:,5*0+3]
EigenValImL2g0100011040 = dataL2g0100011040[:,][:,5*0+4]

dataL2g0100011050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK001/N050/HamVals.txt')

MomentumAxL2g0100011050 = dataL2g0100011050[:,][:,5*0+0]
KineticEneL2g0100011050 = dataL2g0100011050[:,][:,5*0+1]
SelfEnergyL2g0100011050 = dataL2g0100011050[:,][:,5*0+2]
EigenValReL2g0100011050 = dataL2g0100011050[:,][:,5*0+3]
EigenValImL2g0100011050 = dataL2g0100011050[:,][:,5*0+4]

dataL2g0100021010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK002/N010/HamVals.txt')

MomentumAxL2g0100021010 = dataL2g0100021010[:,][:,5*0+0]
KineticEneL2g0100021010 = dataL2g0100021010[:,][:,5*0+1]
SelfEnergyL2g0100021010 = dataL2g0100021010[:,][:,5*0+2]
EigenValReL2g0100021010 = dataL2g0100021010[:,][:,5*0+3]
EigenValImL2g0100021010 = dataL2g0100021010[:,][:,5*0+4]

dataL2g0100021020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK002/N020/HamVals.txt')

MomentumAxL2g0100021020 = dataL2g0100021020[:,][:,5*0+0]
KineticEneL2g0100021020 = dataL2g0100021020[:,][:,5*0+1]
SelfEnergyL2g0100021020 = dataL2g0100021020[:,][:,5*0+2]
EigenValReL2g0100021020 = dataL2g0100021020[:,][:,5*0+3]
EigenValImL2g0100021020 = dataL2g0100021020[:,][:,5*0+4]

dataL2g0100021030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK002/N030/HamVals.txt')

MomentumAxL2g0100021030 = dataL2g0100021030[:,][:,5*0+0]
KineticEneL2g0100021030 = dataL2g0100021030[:,][:,5*0+1]
SelfEnergyL2g0100021030 = dataL2g0100021030[:,][:,5*0+2]
EigenValReL2g0100021030 = dataL2g0100021030[:,][:,5*0+3]
EigenValImL2g0100021030 = dataL2g0100021030[:,][:,5*0+4]

dataL2g0100021040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK002/N040/HamVals.txt')

MomentumAxL2g0100021040 = dataL2g0100021040[:,][:,5*0+0]
KineticEneL2g0100021040 = dataL2g0100021040[:,][:,5*0+1]
SelfEnergyL2g0100021040 = dataL2g0100021040[:,][:,5*0+2]
EigenValReL2g0100021040 = dataL2g0100021040[:,][:,5*0+3]
EigenValImL2g0100021040 = dataL2g0100021040[:,][:,5*0+4]

dataL2g0100021050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK002/N050/HamVals.txt')

MomentumAxL2g0100021050 = dataL2g0100021050[:,][:,5*0+0]
KineticEneL2g0100021050 = dataL2g0100021050[:,][:,5*0+1]
SelfEnergyL2g0100021050 = dataL2g0100021050[:,][:,5*0+2]
EigenValReL2g0100021050 = dataL2g0100021050[:,][:,5*0+3]
EigenValImL2g0100021050 = dataL2g0100021050[:,][:,5*0+4]

dataL2g0100031010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK003/N010/HamVals.txt')

MomentumAxL2g0100031010 = dataL2g0100031010[:,][:,5*0+0]
KineticEneL2g0100031010 = dataL2g0100031010[:,][:,5*0+1]
SelfEnergyL2g0100031010 = dataL2g0100031010[:,][:,5*0+2]
EigenValReL2g0100031010 = dataL2g0100031010[:,][:,5*0+3]
EigenValImL2g0100031010 = dataL2g0100031010[:,][:,5*0+4]

dataL2g0100031020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK003/N020/HamVals.txt')

MomentumAxL2g0100031020 = dataL2g0100031020[:,][:,5*0+0]
KineticEneL2g0100031020 = dataL2g0100031020[:,][:,5*0+1]
SelfEnergyL2g0100031020 = dataL2g0100031020[:,][:,5*0+2]
EigenValReL2g0100031020 = dataL2g0100031020[:,][:,5*0+3]
EigenValImL2g0100031020 = dataL2g0100031020[:,][:,5*0+4]

dataL2g0100031030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK003/N030/HamVals.txt')

MomentumAxL2g0100031030 = dataL2g0100031030[:,][:,5*0+0]
KineticEneL2g0100031030 = dataL2g0100031030[:,][:,5*0+1]
SelfEnergyL2g0100031030 = dataL2g0100031030[:,][:,5*0+2]
EigenValReL2g0100031030 = dataL2g0100031030[:,][:,5*0+3]
EigenValImL2g0100031030 = dataL2g0100031030[:,][:,5*0+4]

dataL2g0100031040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK003/N040/HamVals.txt')

MomentumAxL2g0100031040 = dataL2g0100031040[:,][:,5*0+0]
KineticEneL2g0100031040 = dataL2g0100031040[:,][:,5*0+1]
SelfEnergyL2g0100031040 = dataL2g0100031040[:,][:,5*0+2]
EigenValReL2g0100031040 = dataL2g0100031040[:,][:,5*0+3]
EigenValImL2g0100031040 = dataL2g0100031040[:,][:,5*0+4]

dataL2g0100031050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK003/N050/HamVals.txt')

MomentumAxL2g0100031050 = dataL2g0100031050[:,][:,5*0+0]
KineticEneL2g0100031050 = dataL2g0100031050[:,][:,5*0+1]
SelfEnergyL2g0100031050 = dataL2g0100031050[:,][:,5*0+2]
EigenValReL2g0100031050 = dataL2g0100031050[:,][:,5*0+3]
EigenValImL2g0100031050 = dataL2g0100031050[:,][:,5*0+4]

dataL2g0100051010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK005/N010/HamVals.txt')

MomentumAxL2g0100051010 = dataL2g0100051010[:,][:,5*0+0]
KineticEneL2g0100051010 = dataL2g0100051010[:,][:,5*0+1]
SelfEnergyL2g0100051010 = dataL2g0100051010[:,][:,5*0+2]
EigenValReL2g0100051010 = dataL2g0100051010[:,][:,5*0+3]
EigenValImL2g0100051010 = dataL2g0100051010[:,][:,5*0+4]

dataL2g0100051020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK005/N020/HamVals.txt')

MomentumAxL2g0100051020 = dataL2g0100051020[:,][:,5*0+0]
KineticEneL2g0100051020 = dataL2g0100051020[:,][:,5*0+1]
SelfEnergyL2g0100051020 = dataL2g0100051020[:,][:,5*0+2]
EigenValReL2g0100051020 = dataL2g0100051020[:,][:,5*0+3]
EigenValImL2g0100051020 = dataL2g0100051020[:,][:,5*0+4]

dataL2g0100051030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK005/N030/HamVals.txt')

MomentumAxL2g0100051030 = dataL2g0100051030[:,][:,5*0+0]
KineticEneL2g0100051030 = dataL2g0100051030[:,][:,5*0+1]
SelfEnergyL2g0100051030 = dataL2g0100051030[:,][:,5*0+2]
EigenValReL2g0100051030 = dataL2g0100051030[:,][:,5*0+3]
EigenValImL2g0100051030 = dataL2g0100051030[:,][:,5*0+4]

dataL2g0100051040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK005/N040/HamVals.txt')

MomentumAxL2g0100051040 = dataL2g0100051040[:,][:,5*0+0]
KineticEneL2g0100051040 = dataL2g0100051040[:,][:,5*0+1]
SelfEnergyL2g0100051040 = dataL2g0100051040[:,][:,5*0+2]
EigenValReL2g0100051040 = dataL2g0100051040[:,][:,5*0+3]
EigenValImL2g0100051040 = dataL2g0100051040[:,][:,5*0+4]

dataL2g0100051050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK005/N050/HamVals.txt')

MomentumAxL2g0100051050 = dataL2g0100051050[:,][:,5*0+0]
KineticEneL2g0100051050 = dataL2g0100051050[:,][:,5*0+1]
SelfEnergyL2g0100051050 = dataL2g0100051050[:,][:,5*0+2]
EigenValReL2g0100051050 = dataL2g0100051050[:,][:,5*0+3]
EigenValImL2g0100051050 = dataL2g0100051050[:,][:,5*0+4]

dataL2g0100071010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK007/N010/HamVals.txt')

MomentumAxL2g0100071010 = dataL2g0100071010[:,][:,5*0+0]
KineticEneL2g0100071010 = dataL2g0100071010[:,][:,5*0+1]
SelfEnergyL2g0100071010 = dataL2g0100071010[:,][:,5*0+2]
EigenValReL2g0100071010 = dataL2g0100071010[:,][:,5*0+3]
EigenValImL2g0100071010 = dataL2g0100071010[:,][:,5*0+4]

dataL2g0100071020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK007/N020/HamVals.txt')

MomentumAxL2g0100071020 = dataL2g0100071020[:,][:,5*0+0]
KineticEneL2g0100071020 = dataL2g0100071020[:,][:,5*0+1]
SelfEnergyL2g0100071020 = dataL2g0100071020[:,][:,5*0+2]
EigenValReL2g0100071020 = dataL2g0100071020[:,][:,5*0+3]
EigenValImL2g0100071020 = dataL2g0100071020[:,][:,5*0+4]

dataL2g0100071030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK007/N030/HamVals.txt')

MomentumAxL2g0100071030 = dataL2g0100071030[:,][:,5*0+0]
KineticEneL2g0100071030 = dataL2g0100071030[:,][:,5*0+1]
SelfEnergyL2g0100071030 = dataL2g0100071030[:,][:,5*0+2]
EigenValReL2g0100071030 = dataL2g0100071030[:,][:,5*0+3]
EigenValImL2g0100071030 = dataL2g0100071030[:,][:,5*0+4]

dataL2g0100071040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK007/N040/HamVals.txt')

MomentumAxL2g0100071040 = dataL2g0100071040[:,][:,5*0+0]
KineticEneL2g0100071040 = dataL2g0100071040[:,][:,5*0+1]
SelfEnergyL2g0100071040 = dataL2g0100071040[:,][:,5*0+2]
EigenValReL2g0100071040 = dataL2g0100071040[:,][:,5*0+3]
EigenValImL2g0100071040 = dataL2g0100071040[:,][:,5*0+4]

dataL2g0100071050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK007/N050/HamVals.txt')

MomentumAxL2g0100071050 = dataL2g0100071050[:,][:,5*0+0]
KineticEneL2g0100071050 = dataL2g0100071050[:,][:,5*0+1]
SelfEnergyL2g0100071050 = dataL2g0100071050[:,][:,5*0+2]
EigenValReL2g0100071050 = dataL2g0100071050[:,][:,5*0+3]
EigenValImL2g0100071050 = dataL2g0100071050[:,][:,5*0+4]

dataL2g0100101010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK010/N010/HamVals.txt')

MomentumAxL2g0100101010 = dataL2g0100101010[:,][:,5*0+0]
KineticEneL2g0100101010 = dataL2g0100101010[:,][:,5*0+1]
SelfEnergyL2g0100101010 = dataL2g0100101010[:,][:,5*0+2]
EigenValReL2g0100101010 = dataL2g0100101010[:,][:,5*0+3]
EigenValImL2g0100101010 = dataL2g0100101010[:,][:,5*0+4]

dataL2g0100101020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK010/N020/HamVals.txt')

MomentumAxL2g0100101020 = dataL2g0100101020[:,][:,5*0+0]
KineticEneL2g0100101020 = dataL2g0100101020[:,][:,5*0+1]
SelfEnergyL2g0100101020 = dataL2g0100101020[:,][:,5*0+2]
EigenValReL2g0100101020 = dataL2g0100101020[:,][:,5*0+3]
EigenValImL2g0100101020 = dataL2g0100101020[:,][:,5*0+4]

dataL2g0100101030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK010/N030/HamVals.txt')

MomentumAxL2g0100101030 = dataL2g0100101030[:,][:,5*0+0]
KineticEneL2g0100101030 = dataL2g0100101030[:,][:,5*0+1]
SelfEnergyL2g0100101030 = dataL2g0100101030[:,][:,5*0+2]
EigenValReL2g0100101030 = dataL2g0100101030[:,][:,5*0+3]
EigenValImL2g0100101030 = dataL2g0100101030[:,][:,5*0+4]

dataL2g0100101040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK010/N040/HamVals.txt')

MomentumAxL2g0100101040 = dataL2g0100101040[:,][:,5*0+0]
KineticEneL2g0100101040 = dataL2g0100101040[:,][:,5*0+1]
SelfEnergyL2g0100101040 = dataL2g0100101040[:,][:,5*0+2]
EigenValReL2g0100101040 = dataL2g0100101040[:,][:,5*0+3]
EigenValImL2g0100101040 = dataL2g0100101040[:,][:,5*0+4]

dataL2g0100101050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK010/N050/HamVals.txt')

MomentumAxL2g0100101050 = dataL2g0100101050[:,][:,5*0+0]
KineticEneL2g0100101050 = dataL2g0100101050[:,][:,5*0+1]
SelfEnergyL2g0100101050 = dataL2g0100101050[:,][:,5*0+2]
EigenValReL2g0100101050 = dataL2g0100101050[:,][:,5*0+3]
EigenValImL2g0100101050 = dataL2g0100101050[:,][:,5*0+4]

MaxEigenValImL2g0101Inf = np.zeros((6))

MaxEigenValImL2g0101Inf[0] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0100011010),np.max(EigenValImL2g0100011020),np.max(EigenValImL2g0100011030),np.max(EigenValImL2g0100011040),np.max(EigenValImL2g0100011050)], 1)[[1]]
MaxEigenValImL2g0101Inf[1] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0100021010),np.max(EigenValImL2g0100021020),np.max(EigenValImL2g0100021030),np.max(EigenValImL2g0100021040),np.max(EigenValImL2g0100021050)], 1)[[1]]
MaxEigenValImL2g0101Inf[2] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0100031010),np.max(EigenValImL2g0100031020),np.max(EigenValImL2g0100031030),np.max(EigenValImL2g0100031040),np.max(EigenValImL2g0100031050)], 1)[[1]]
MaxEigenValImL2g0101Inf[3] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0100051010),np.max(EigenValImL2g0100051020),np.max(EigenValImL2g0100051030),np.max(EigenValImL2g0100051040),np.max(EigenValImL2g0100051050)], 1)[[1]]
MaxEigenValImL2g0101Inf[4] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0100071010),np.max(EigenValImL2g0100071020),np.max(EigenValImL2g0100071030),np.max(EigenValImL2g0100071040),np.max(EigenValImL2g0100071050)], 1)[[1]]
MaxEigenValImL2g0101Inf[5] = np.polyfit(fiveSizes, [np.max(EigenValImL2g0100101010),np.max(EigenValImL2g0100101020),np.max(EigenValImL2g0100101030),np.max(EigenValImL2g0100101040),np.max(EigenValImL2g0100101050)], 1)[[1]]





































































































########################################################################
########################################################################

Spreading = np.zeros((4))
Spreading[0] = 1
Spreading[1] = 2
Spreading[2] = 5
Spreading[3] = 10

CouplingA = np.zeros((10))
CouplingA[0] = 1/0.25
CouplingA[1] = 1/0.30
CouplingA[2] = 1/0.35
CouplingA[3] = 1/0.40
CouplingA[4] = 1/0.45
CouplingA[5] = 1/0.50
CouplingA[6] = 1/1.0
CouplingA[7] = 1/2.0
CouplingA[8] = 1/5.0
CouplingA[9] = 1/10.0

CouplingB = np.zeros((6))
CouplingB[0] = 1/0.25
CouplingB[1] = 1/0.30
CouplingB[2] = 1/0.35
CouplingB[3] = 1/0.40
CouplingB[4] = 1/0.45
CouplingB[5] = 1/0.50

CouplingAxis = np.linspace(0,4.0,51,endpoint=True)
CouplingAxisA= np.linspace(0,2.0,51,endpoint=True)

########################################################################
########################################################################

def func(x,E0,GK):
    return E0 * np.exp(-GK*x**1)

plt.clf()
fig, axs = plt.subplots(1, 2, figsize=(6, 3), sharey=True)
plt.subplots_adjust(left=0.25,bottom=0.15,right=0.8,top=0.7,wspace=0.15,hspace=0.4)

MaxEigenValImL0aK001Total = np.zeros(( len(CouplingA) ))
MaxEigenValImL0aK002Total = np.zeros(( len(CouplingA) ))
MaxEigenValImL0aK003Total = np.zeros(( len(CouplingA) ))
MaxEigenValImL0aK005Total = np.zeros(( len(CouplingA) ))
MaxEigenValImL0aK007Total = np.zeros(( len(CouplingA) ))
MaxEigenValImL0aK010Total = np.zeros(( len(CouplingA) ))

MaxEigenValImL0aK001Total = [MaxEigenValImL0g000_251Inf[0],MaxEigenValImL0g000_31Inf[0],MaxEigenValImL0g000_351Inf[0],MaxEigenValImL0g000_41Inf[0],MaxEigenValImL0g000_451Inf[0],MaxEigenValImL0g000_51Inf[0],MaxEigenValImL0g0011Inf[0],MaxEigenValImL0g0021Inf[0],MaxEigenValImL0g0051Inf[0],MaxEigenValImL0g0101Inf[0]]
MaxEigenValImL0aK002Total = [MaxEigenValImL0g000_251Inf[1],MaxEigenValImL0g000_31Inf[1],MaxEigenValImL0g000_351Inf[1],MaxEigenValImL0g000_41Inf[1],MaxEigenValImL0g000_451Inf[1],MaxEigenValImL0g000_51Inf[1],MaxEigenValImL0g0011Inf[1],MaxEigenValImL0g0021Inf[1],MaxEigenValImL0g0051Inf[1],MaxEigenValImL0g0101Inf[1]]
MaxEigenValImL0aK003Total = [MaxEigenValImL0g000_251Inf[2],MaxEigenValImL0g000_31Inf[2],MaxEigenValImL0g000_351Inf[2],MaxEigenValImL0g000_41Inf[2],MaxEigenValImL0g000_451Inf[2],MaxEigenValImL0g000_51Inf[2],MaxEigenValImL0g0011Inf[2],MaxEigenValImL0g0021Inf[2],MaxEigenValImL0g0051Inf[2],MaxEigenValImL0g0101Inf[2]]
MaxEigenValImL0aK005Total = [MaxEigenValImL0g000_251Inf[3],MaxEigenValImL0g000_31Inf[3],MaxEigenValImL0g000_351Inf[3],MaxEigenValImL0g000_41Inf[3],MaxEigenValImL0g000_451Inf[3],MaxEigenValImL0g000_51Inf[3],MaxEigenValImL0g0011Inf[3],MaxEigenValImL0g0021Inf[3],MaxEigenValImL0g0051Inf[3],MaxEigenValImL0g0101Inf[3]]
MaxEigenValImL0aK007Total = [MaxEigenValImL0g000_251Inf[4],MaxEigenValImL0g000_31Inf[4],MaxEigenValImL0g000_351Inf[4],MaxEigenValImL0g000_41Inf[4],MaxEigenValImL0g000_451Inf[4],MaxEigenValImL0g000_51Inf[4],MaxEigenValImL0g0011Inf[4],MaxEigenValImL0g0021Inf[4],MaxEigenValImL0g0051Inf[4],MaxEigenValImL0g0101Inf[4]]
MaxEigenValImL0aK010Total = [MaxEigenValImL0g000_251Inf[5],MaxEigenValImL0g000_31Inf[5],MaxEigenValImL0g000_351Inf[5],MaxEigenValImL0g000_41Inf[5],MaxEigenValImL0g000_451Inf[5],MaxEigenValImL0g000_51Inf[5],MaxEigenValImL0g0011Inf[5],MaxEigenValImL0g0021Inf[5],MaxEigenValImL0g0051Inf[5],MaxEigenValImL0g0101Inf[5]]

MaxEigenValImL0aK001 = np.zeros(( len(CouplingB) ))
MaxEigenValImL0aK002 = np.zeros(( len(CouplingB) ))
MaxEigenValImL0aK003 = np.zeros(( len(CouplingB) ))
MaxEigenValImL0aK005 = np.zeros(( len(CouplingB) ))
MaxEigenValImL0aK007 = np.zeros(( len(CouplingB) ))
MaxEigenValImL0aK010 = np.zeros(( len(CouplingB) ))

MaxEigenValImL0aK001 = [MaxEigenValImL0g000_251Inf[0],MaxEigenValImL0g000_31Inf[0],MaxEigenValImL0g000_351Inf[0],MaxEigenValImL0g000_41Inf[0],MaxEigenValImL0g000_451Inf[0],MaxEigenValImL0g000_51Inf[0]]
MaxEigenValImL0aK002 = [MaxEigenValImL0g000_251Inf[1],MaxEigenValImL0g000_31Inf[1],MaxEigenValImL0g000_351Inf[1],MaxEigenValImL0g000_41Inf[1],MaxEigenValImL0g000_451Inf[1],MaxEigenValImL0g000_51Inf[1]]
MaxEigenValImL0aK003 = [MaxEigenValImL0g000_251Inf[2],MaxEigenValImL0g000_31Inf[2],MaxEigenValImL0g000_351Inf[2],MaxEigenValImL0g000_41Inf[2],MaxEigenValImL0g000_451Inf[2],MaxEigenValImL0g000_51Inf[2]]
MaxEigenValImL0aK005 = [MaxEigenValImL0g000_251Inf[3],MaxEigenValImL0g000_31Inf[3],MaxEigenValImL0g000_351Inf[3],MaxEigenValImL0g000_41Inf[3],MaxEigenValImL0g000_451Inf[3],MaxEigenValImL0g000_51Inf[3]]
MaxEigenValImL0aK007 = [MaxEigenValImL0g000_251Inf[4],MaxEigenValImL0g000_31Inf[4],MaxEigenValImL0g000_351Inf[4],MaxEigenValImL0g000_41Inf[4],MaxEigenValImL0g000_451Inf[4],MaxEigenValImL0g000_51Inf[4]]
MaxEigenValImL0aK010 = [MaxEigenValImL0g000_251Inf[5],MaxEigenValImL0g000_31Inf[5],MaxEigenValImL0g000_351Inf[5],MaxEigenValImL0g000_41Inf[5],MaxEigenValImL0g000_451Inf[5],MaxEigenValImL0g000_51Inf[5]]

#MaxEigenValImL0aK001 = [MaxEigenValImL0g000_41Inf[0],MaxEigenValImL0g000_51Inf[0],MaxEigenValImL0g000_61Inf[0],MaxEigenValImL0g000_71Inf[0],MaxEigenValImL0g000_81Inf[0],MaxEigenValImL0g0011Inf[0],MaxEigenValImL0g0021Inf[0],MaxEigenValImL0g0051Inf[0],MaxEigenValImL0g0101Inf[0]]
#MaxEigenValImL0aK002 = [MaxEigenValImL0g000_41Inf[1],MaxEigenValImL0g000_51Inf[1],MaxEigenValImL0g000_61Inf[1],MaxEigenValImL0g000_71Inf[1],MaxEigenValImL0g000_81Inf[1],MaxEigenValImL0g0011Inf[1],MaxEigenValImL0g0021Inf[1],MaxEigenValImL0g0051Inf[1],MaxEigenValImL0g0101Inf[1]]
#MaxEigenValImL0aK003 = [MaxEigenValImL0g000_41Inf[2],MaxEigenValImL0g000_51Inf[2],MaxEigenValImL0g000_61Inf[2],MaxEigenValImL0g000_71Inf[2],MaxEigenValImL0g000_81Inf[2],MaxEigenValImL0g0011Inf[1],MaxEigenValImL0g0021Inf[1],MaxEigenValImL0g0051Inf[1],MaxEigenValImL0g0101Inf[1]]
#MaxEigenValImL0aK005 = [MaxEigenValImL0g000_41Inf[3],MaxEigenValImL0g000_51Inf[3],MaxEigenValImL0g000_61Inf[3],MaxEigenValImL0g000_71Inf[3],MaxEigenValImL0g000_81Inf[3],MaxEigenValImL0g0011Inf[2],MaxEigenValImL0g0021Inf[2],MaxEigenValImL0g0051Inf[2],MaxEigenValImL0g0101Inf[2]]
#MaxEigenValImL0aK007 = [MaxEigenValImL0g000_41Inf[4],MaxEigenValImL0g000_51Inf[4],MaxEigenValImL0g000_61Inf[4],MaxEigenValImL0g000_71Inf[4],MaxEigenValImL0g000_81Inf[4],MaxEigenValImL0g0011Inf[2],MaxEigenValImL0g0021Inf[2],MaxEigenValImL0g0051Inf[2],MaxEigenValImL0g0101Inf[2]]
#MaxEigenValImL0aK010 = [MaxEigenValImL0g000_41Inf[5],MaxEigenValImL0g000_51Inf[5],MaxEigenValImL0g000_61Inf[5],MaxEigenValImL0g000_71Inf[5],MaxEigenValImL0g000_81Inf[5],MaxEigenValImL0g0011Inf[3],MaxEigenValImL0g0021Inf[3],MaxEigenValImL0g0051Inf[3],MaxEigenValImL0g0101Inf[3]]

axs[0].semilogy(
            CouplingA,MaxEigenValImL0aK001Total, marker='o',c=[0.0, 1.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 1$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[0].plot(CouplingA,MaxEigenValImL0aK002Total, marker='o',c=[0.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 2$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[0].plot(CouplingA,MaxEigenValImL0aK003Total, marker='o',c=[0.5, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 3$', markersize=5, linewidth=1,markeredgecolor=[0.5*0.8, 0.0*0.8, 1.0*0.8])
axs[0].plot(CouplingA,MaxEigenValImL0aK005Total, marker='o',c=[1.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 5$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 1.0*0.8])
axs[0].plot(CouplingA,MaxEigenValImL0aK007Total, marker='o',c=[1.0, 0.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 7$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[0].plot(CouplingA,MaxEigenValImL0aK010Total, marker='o',c=[1.0, 0.5, 0.0],ls='None',label='$a_{\\mathcal{K}}=10$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])

FitaK001L0, CovaK001L0 = curve_fit(func, CouplingB, MaxEigenValImL0aK001)
FitaK002L0, CovaK002L0 = curve_fit(func, CouplingB, MaxEigenValImL0aK002)
FitaK003L0, CovaK003L0 = curve_fit(func, CouplingB, MaxEigenValImL0aK003)
FitaK005L0, CovaK005L0 = curve_fit(func, CouplingB, MaxEigenValImL0aK005)
FitaK007L0, CovaK007L0 = curve_fit(func, CouplingB, MaxEigenValImL0aK007)
FitaK010L0, CovaK010L0 = curve_fit(func, CouplingB, MaxEigenValImL0aK010)

print "     L0"
print FitaK001L0
#print CovaK001L0
print np.sqrt(np.diag(CovaK001L0))
print FitaK002L0
#print CovaK002L0
print np.sqrt(np.diag(CovaK002L0))
print FitaK003L0
#print CovaK002L0
print np.sqrt(np.diag(CovaK003L0))
print FitaK005L0
#print CovaK005L0
print np.sqrt(np.diag(CovaK005L0))
print FitaK007L0
#print CovaK002L0
print np.sqrt(np.diag(CovaK007L0))
print FitaK010L0
#print CovaK010L0
print np.sqrt(np.diag(CovaK010L0))

axs[0].plot(CouplingAxis, func(CouplingAxis, *FitaK001L0), marker='.',c=[0.0/1.5, 1.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, *FitaK002L0), marker='.',c=[0.0/1.5, 0.0/1.5, 1.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, *FitaK003L0), marker='.',c=[0.5/1.5, 0.0/1.5, 1.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, *FitaK005L0), marker='.',c=[1.0/1.5, 0.0/1.5, 1.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, *FitaK007L0), marker='.',c=[1.0/1.5, 0.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, *FitaK010L0), marker='.',c=[1.0/1.5, 0.5/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))

axs[0].plot(CouplingB,MaxEigenValImL0aK001, marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[1.0*1.0, 0.0*1.0, 0.0*1.0])#,label='100')
axs[0].plot(CouplingB,MaxEigenValImL0aK002, marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[1.0*1.0, 0.5*1.0, 0.0*1.0])#,label='100')
axs[0].plot(CouplingB,MaxEigenValImL0aK003, marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[0.0*1.0, 1.0*1.0, 0.0*1.0])#,label='100')
axs[0].plot(CouplingB,MaxEigenValImL0aK005, marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[0.0*1.0, 1.0*1.0, 0.0*1.0])#,label='100')
axs[0].plot(CouplingB,MaxEigenValImL0aK007, marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[0.0*1.0, 1.0*1.0, 0.0*1.0])#,label='100')
axs[0].plot(CouplingB,MaxEigenValImL0aK010, marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[0.0*1.0, 0.4*1.0, 1.0*1.0])#,label='100')

#axs[1].plot(CouplingC,[MaxEigenValImL0g000_41Inf[0],MaxEigenValImL0g000_51Inf[0],MaxEigenValImL0g000_61Inf[0],MaxEigenValImL0g000_71Inf[0],MaxEigenValImL0g000_81Inf[0]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[1.0*1.0, 0.0*1.0, 0.0*1.0])#,label='100')
#axs[1].plot(CouplingC,[MaxEigenValImL0g000_41Inf[1],MaxEigenValImL0g000_51Inf[1],MaxEigenValImL0g000_61Inf[1],MaxEigenValImL0g000_71Inf[1],MaxEigenValImL0g000_81Inf[1]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[1.0*1.0, 0.5*1.0, 0.0*1.0])#,label='100')
#axs[1].plot(CouplingC,[MaxEigenValImL0g000_41Inf[2],MaxEigenValImL0g000_51Inf[2],MaxEigenValImL0g000_61Inf[2],MaxEigenValImL0g000_71Inf[2],MaxEigenValImL0g000_81Inf[2]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[0.0*1.0, 1.0*1.0, 0.0*1.0])#,label='100')
#axs[1].plot(CouplingC,[MaxEigenValImL0g000_41Inf[3],MaxEigenValImL0g000_51Inf[3],MaxEigenValImL0g000_61Inf[3],MaxEigenValImL0g000_71Inf[3],MaxEigenValImL0g000_81Inf[3]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[0.0*1.0, 0.4*1.0, 1.0*1.0])#,label='100')
"""
axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.276892/1**2, 4.09233), marker='.',c=[1.0/1.5, 0.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.276892/2**2, 4.09233), marker='.',c=[1.0/1.5, 0.5/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.276892/3**2, 4.09233), marker='.',c=[1.0/1.5, 0.5/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.276892/5**2, 4.09233), marker='.',c=[0.0/1.5, 1.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.276892/7**2, 4.09233), marker='.',c=[0.0/1.5, 1.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.276892/10**2,4.09233), marker='.',c=[0.0/1.5, 0.0/1.5, 1.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
"""
#axs[0].plot(CouplingAxis, func(CouplingAxis, 0.276892/1**2, 4.02233), marker='.',c=[1.0/1.5, 0.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
#axs[0].plot(CouplingAxis, func(CouplingAxis, 0.276892/2**2, 4.02233), marker='.',c=[1.0/1.5, 0.5/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
#axs[0].plot(CouplingAxis, func(CouplingAxis, 0.276892/3**2, 4.02233), marker='.',c=[1.0/1.5, 0.5/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
#axs[0].plot(CouplingAxis, func(CouplingAxis, 0.276892/5**2, 4.02233), marker='.',c=[0.0/1.5, 1.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
#axs[0].plot(CouplingAxis, func(CouplingAxis, 0.276892/7**2, 4.02233), marker='.',c=[0.0/1.5, 1.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
#axs[0].plot(CouplingAxis, func(CouplingAxis, 0.276892/10**2,4.02233), marker='.',c=[0.0/1.5, 0.0/1.5, 1.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))

#"""

#axs[1].semilogy(100*Coupling,MaxEigenValImL0g0011Inf, marker='o',c=[1.0, 0.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.01$', markersize=4, linewidth=1)#,label='100')
#axs[1].semilogy(100*Coupling,MaxEigenValImL0g0021Inf, marker='o',c=[1.0, 0.5, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.02$', markersize=4, linewidth=1)#,label='100')
#axs[1].semilogy(100*Coupling,MaxEigenValImL0g0051Inf, marker='o',c=[0.0, 1.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.05$', markersize=4, linewidth=1)#,label='100')
#axs[1].semilogy(100*Coupling,MaxEigenValImL0g0101Inf, marker='o',c=[0.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 0.10$', markersize=4, linewidth=1)#,label='100')

axs[0].set_title("$\\ell=0$" ,fontsize=12, fontname='Times New Roman')

axs[0].grid(True)
axs[0].set_xlim(-0.e+0,+4.10e+0)
axs[0].set_xticks(np.arange(-0.0e+1,+4.01e+0, step=1.e-0))
axs[0].set_ylim(+1e-10,+1e+0)
#axs[0].set_ylim(+1e0,+1.01e+16)
axs[0].set_yticks([1e0,1e-2,1e-4,1e-6,1e-8,1e-10])

#axs[0].legend(bbox_to_anchor=(0.2, +1.40), loc=2, borderaxespad=0., ncol=3, labelspacing=.1,handleheight=.5, columnspacing=.5, handletextpad=.5)
axs[0].legend(bbox_to_anchor=(-0.6, +1.30), loc=2, borderaxespad=0., ncol=6, labelspacing=.05,handleheight=.05, columnspacing=.05, handletextpad=.05)
#plt.suptitle('$\\ell=0XXX, g_{\\mathcal{K}}=0.1$', fontsize=20, fontname='Times New Roman')
axs[0].set_xlabel('$1/g_{\\mathcal{K}}$', fontsize=12, fontname='Times New Roman')
axs[0].set_ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}(a_{\\mathcal{K}},g_{\\mathcal{K}})$', fontsize=12, fontname='Times New Roman')
"""
Coupling = np.zeros((6))
Coupling[0] = 1/0.4
Coupling[1] = 1/0.5
Coupling[2] = 1/1.0
Coupling[3] = 1/2.0
Coupling[4] = 1/5.0
Coupling[5] = 1/10.

axs[1].semilogy(Coupling,[MaxEigenValImL2g000_41Inf[0],MaxEigenValImL2g000_51Inf[0],MaxEigenValImL2g0011Inf[0],MaxEigenValImL2g0021Inf[0],MaxEigenValImL2g0051Inf[0],MaxEigenValImL2g0101Inf[0]], marker='o',c=[1.0, 0.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.01$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[1].plot(Coupling,[MaxEigenValImL2g000_41Inf[1],MaxEigenValImL2g000_51Inf[1],MaxEigenValImL2g0011Inf[1],MaxEigenValImL2g0021Inf[1],MaxEigenValImL2g0051Inf[1],MaxEigenValImL2g0101Inf[1]], marker='o',c=[1.0, 0.5, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.02$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[1].plot(Coupling,[MaxEigenValImL2g000_41Inf[2],MaxEigenValImL2g000_51Inf[2],MaxEigenValImL2g0011Inf[2],MaxEigenValImL2g0021Inf[2],MaxEigenValImL2g0051Inf[2],MaxEigenValImL2g0101Inf[2]], marker='o',c=[0.0, 1.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.05$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[1].plot(Coupling,[MaxEigenValImL2g000_41Inf[3],MaxEigenValImL2g000_51Inf[3],MaxEigenValImL2g0011Inf[3],MaxEigenValImL2g0021Inf[3],MaxEigenValImL2g0051Inf[3],MaxEigenValImL2g0101Inf[3]], marker='o',c=[0.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 0.10$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
"""
#"""
Coupling = np.zeros((9))
Coupling[0] = 1/0.5
Coupling[1] = 1/0.6
Coupling[2] = 1/0.7
Coupling[3] = 1/0.8
Coupling[4] = 1/0.9
Coupling[5] = 1/1.0
Coupling[6] = 1/2.0
Coupling[7] = 1/5.0
Coupling[8] = 1/10.0

CouplingC = np.zeros((5))
CouplingC[0] = 1/0.5
CouplingC[1] = 1/0.6
CouplingC[2] = 1/0.7
CouplingC[3] = 1/0.8
CouplingC[4] = 1/0.9

CouplingD = np.zeros((5))
CouplingD[0] = 1/0.4
CouplingD[1] = 1/0.5
CouplingD[2] = 1/0.6
CouplingD[3] = 1/0.7
CouplingD[4] = 1/0.8

#CouplingC = np.zeros((5))
#CouplingC[0] = 1/0.4
#CouplingC[1] = 1/0.5
#CouplingC[2] = 1/0.6
#CouplingC[3] = 1/0.7
#CouplingC[4] = 1/0.8

MaxEigenValImL2aK001Total = np.zeros(( len(CouplingC) ))
MaxEigenValImL2aK002Total = np.zeros(( len(CouplingC) ))
MaxEigenValImL2aK003Total = np.zeros(( len(CouplingC) ))
MaxEigenValImL2aK005Total = np.zeros(( len(CouplingC) ))
MaxEigenValImL2aK007Total = np.zeros(( len(CouplingC) ))
MaxEigenValImL2aK010Total = np.zeros(( len(CouplingC) ))

MaxEigenValImL2aK001Total = [MaxEigenValImL2g000_51Inf[0],MaxEigenValImL2g000_61Inf[0],MaxEigenValImL2g000_71Inf[0],MaxEigenValImL2g000_81Inf[0],MaxEigenValImL2g000_91Inf[0],MaxEigenValImL2g0011Inf[0],MaxEigenValImL2g0021Inf[0],MaxEigenValImL2g0051Inf[0],MaxEigenValImL2g0101Inf[0]]
MaxEigenValImL2aK002Total = [MaxEigenValImL2g000_51Inf[1],MaxEigenValImL2g000_61Inf[1],MaxEigenValImL2g000_71Inf[1],MaxEigenValImL2g000_81Inf[1],MaxEigenValImL2g000_91Inf[1],MaxEigenValImL2g0011Inf[1],MaxEigenValImL2g0021Inf[1],MaxEigenValImL2g0051Inf[1],MaxEigenValImL2g0101Inf[1]]
MaxEigenValImL2aK003Total = [MaxEigenValImL2g000_51Inf[2],MaxEigenValImL2g000_61Inf[2],MaxEigenValImL2g000_71Inf[2],MaxEigenValImL2g000_81Inf[2],MaxEigenValImL2g000_91Inf[2],MaxEigenValImL2g0011Inf[2],MaxEigenValImL2g0021Inf[2],MaxEigenValImL2g0051Inf[2],MaxEigenValImL2g0101Inf[2]]
MaxEigenValImL2aK005Total = [MaxEigenValImL2g000_51Inf[3],MaxEigenValImL2g000_61Inf[3],MaxEigenValImL2g000_71Inf[3],MaxEigenValImL2g000_81Inf[3],MaxEigenValImL2g000_91Inf[3],MaxEigenValImL2g0011Inf[3],MaxEigenValImL2g0021Inf[3],MaxEigenValImL2g0051Inf[3],MaxEigenValImL2g0101Inf[3]]
MaxEigenValImL2aK007Total = [MaxEigenValImL2g000_51Inf[4],MaxEigenValImL2g000_61Inf[4],MaxEigenValImL2g000_71Inf[4],MaxEigenValImL2g000_81Inf[4],MaxEigenValImL2g000_91Inf[4],MaxEigenValImL2g0011Inf[4],MaxEigenValImL2g0021Inf[4],MaxEigenValImL2g0051Inf[4],MaxEigenValImL2g0101Inf[4]]
MaxEigenValImL2aK010Total = [MaxEigenValImL2g000_51Inf[5],MaxEigenValImL2g000_61Inf[5],MaxEigenValImL2g000_71Inf[5],MaxEigenValImL2g000_81Inf[5],MaxEigenValImL2g000_91Inf[5],MaxEigenValImL2g0011Inf[5],MaxEigenValImL2g0021Inf[5],MaxEigenValImL2g0051Inf[5],MaxEigenValImL2g0101Inf[5]]

MaxEigenValImL2aK001 = np.zeros(( len(CouplingC) ))
MaxEigenValImL2aK002 = np.zeros(( len(CouplingC) ))
MaxEigenValImL2aK003 = np.zeros(( len(CouplingC) ))
MaxEigenValImL2aK005 = np.zeros(( len(CouplingC) ))
MaxEigenValImL2aK007 = np.zeros(( len(CouplingC) ))
MaxEigenValImL2aK010 = np.zeros(( len(CouplingC) ))

MaxEigenValImL2aK001 = [MaxEigenValImL2g000_51Inf[0],MaxEigenValImL2g000_61Inf[0],MaxEigenValImL2g000_71Inf[0],MaxEigenValImL2g000_81Inf[0],MaxEigenValImL2g000_91Inf[0]]
MaxEigenValImL2aK002 = [MaxEigenValImL2g000_51Inf[1],MaxEigenValImL2g000_61Inf[1],MaxEigenValImL2g000_71Inf[1],MaxEigenValImL2g000_81Inf[1],MaxEigenValImL2g000_91Inf[1]]
MaxEigenValImL2aK003 = [MaxEigenValImL2g000_51Inf[2],MaxEigenValImL2g000_61Inf[2],MaxEigenValImL2g000_71Inf[2],MaxEigenValImL2g000_81Inf[2],MaxEigenValImL2g000_91Inf[2]]
MaxEigenValImL2aK005 = [MaxEigenValImL2g000_51Inf[3],MaxEigenValImL2g000_61Inf[3],MaxEigenValImL2g000_71Inf[3],MaxEigenValImL2g000_81Inf[3],MaxEigenValImL2g000_91Inf[3]]
MaxEigenValImL2aK007 = [MaxEigenValImL2g000_51Inf[4],MaxEigenValImL2g000_61Inf[4],MaxEigenValImL2g000_71Inf[4],MaxEigenValImL2g000_81Inf[4],MaxEigenValImL2g000_91Inf[4]]
MaxEigenValImL2aK010 = [MaxEigenValImL2g000_51Inf[5],MaxEigenValImL2g000_61Inf[5],MaxEigenValImL2g000_71Inf[5],MaxEigenValImL2g000_81Inf[5],MaxEigenValImL2g000_91Inf[5]]

#MaxEigenValImL2aK001 = [MaxEigenValImL2g000_41Inf[0],MaxEigenValImL2g000_51Inf[0],MaxEigenValImL2g000_61Inf[0],MaxEigenValImL2g000_71Inf[0],MaxEigenValImL2g000_81Inf[0],MaxEigenValImL2g0011Inf[0],MaxEigenValImL2g0021Inf[0],MaxEigenValImL2g0051Inf[0],MaxEigenValImL2g0101Inf[0]]
#MaxEigenValImL2aK002 = [MaxEigenValImL2g000_41Inf[1],MaxEigenValImL2g000_51Inf[1],MaxEigenValImL2g000_61Inf[1],MaxEigenValImL2g000_71Inf[1],MaxEigenValImL2g000_81Inf[1],MaxEigenValImL2g0011Inf[1],MaxEigenValImL2g0021Inf[1],MaxEigenValImL2g0051Inf[1],MaxEigenValImL2g0101Inf[1]]
#MaxEigenValImL2aK003 = [MaxEigenValImL2g000_41Inf[2],MaxEigenValImL2g000_51Inf[2],MaxEigenValImL2g000_61Inf[2],MaxEigenValImL2g000_71Inf[2],MaxEigenValImL2g000_81Inf[2],MaxEigenValImL2g0011Inf[1],MaxEigenValImL2g0021Inf[1],MaxEigenValImL2g0051Inf[1],MaxEigenValImL2g0101Inf[1]]
#MaxEigenValImL2aK005 = [MaxEigenValImL2g000_41Inf[3],MaxEigenValImL2g000_51Inf[3],MaxEigenValImL2g000_61Inf[3],MaxEigenValImL2g000_71Inf[3],MaxEigenValImL2g000_81Inf[3],MaxEigenValImL2g0011Inf[2],MaxEigenValImL2g0021Inf[2],MaxEigenValImL2g0051Inf[2],MaxEigenValImL2g0101Inf[2]]
#MaxEigenValImL2aK007 = [MaxEigenValImL2g000_41Inf[4],MaxEigenValImL2g000_51Inf[4],MaxEigenValImL2g000_61Inf[4],MaxEigenValImL2g000_71Inf[4],MaxEigenValImL2g000_81Inf[4],MaxEigenValImL2g0011Inf[2],MaxEigenValImL2g0021Inf[2],MaxEigenValImL2g0051Inf[2],MaxEigenValImL2g0101Inf[2]]
#MaxEigenValImL2aK010 = [MaxEigenValImL2g000_41Inf[5],MaxEigenValImL2g000_51Inf[5],MaxEigenValImL2g000_61Inf[5],MaxEigenValImL2g000_71Inf[5],MaxEigenValImL2g000_81Inf[5],MaxEigenValImL2g0011Inf[3],MaxEigenValImL2g0021Inf[3],MaxEigenValImL2g0051Inf[3],MaxEigenValImL2g0101Inf[3]]

axs[1].semilogy(
            Coupling,MaxEigenValImL2aK001Total, marker='o',c=[0.0, 1.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 1$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[1].plot(Coupling,MaxEigenValImL2aK002Total, marker='o',c=[0.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 2$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[1].plot(Coupling,MaxEigenValImL2aK003Total, marker='o',c=[0.5, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 3$', markersize=5, linewidth=1,markeredgecolor=[0.5*0.8, 0.0*0.8, 1.0*0.8])
axs[1].plot(Coupling,MaxEigenValImL2aK005Total, marker='o',c=[1.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 5$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 1.0*0.8])
axs[1].plot(Coupling,MaxEigenValImL2aK007Total, marker='o',c=[1.0, 0.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 7$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[1].plot(Coupling,MaxEigenValImL2aK010Total, marker='o',c=[1.0, 0.5, 0.0],ls='None',label='$a_{\\mathcal{K}}=10$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])

FitaK001L2, CovaK001L2 = curve_fit(func, CouplingC, MaxEigenValImL2aK001)
FitaK002L2, CovaK002L2 = curve_fit(func, CouplingC, MaxEigenValImL2aK002)
FitaK003L2, CovaK003L2 = curve_fit(func, CouplingC, MaxEigenValImL2aK003)
FitaK005L2, CovaK005L2 = curve_fit(func, CouplingC, MaxEigenValImL2aK005)
FitaK007L2, CovaK007L2 = curve_fit(func, CouplingC, MaxEigenValImL2aK007)
FitaK010L2, CovaK010L2 = curve_fit(func, CouplingC, MaxEigenValImL2aK010)

#FitaK001L2, CovaK001L2 = curve_fit(func, CouplingC, [MaxEigenValImL2g000_41Inf[0],MaxEigenValImL2g000_51Inf[0],MaxEigenValImL2g000_61Inf[0],MaxEigenValImL2g000_71Inf[0],MaxEigenValImL2g000_81Inf[0]])
#FitaK002L2, CovaK002L2 = curve_fit(func, CouplingC, [MaxEigenValImL2g000_41Inf[1],MaxEigenValImL2g000_51Inf[1],MaxEigenValImL2g000_61Inf[1],MaxEigenValImL2g000_71Inf[1],MaxEigenValImL2g000_81Inf[1]])
#FitaK005L2, CovaK005L2 = curve_fit(func, CouplingC, [MaxEigenValImL2g000_41Inf[2],MaxEigenValImL2g000_51Inf[2],MaxEigenValImL2g000_61Inf[2],MaxEigenValImL2g000_71Inf[2],MaxEigenValImL2g000_81Inf[2]])
#FitaK010L2, CovaK010L2 = curve_fit(func, CouplingC, [MaxEigenValImL2g000_41Inf[3],MaxEigenValImL2g000_51Inf[3],MaxEigenValImL2g000_61Inf[3],MaxEigenValImL2g000_71Inf[3],MaxEigenValImL2g000_81Inf[3]])

print "     L2"
print FitaK001L2
#print CovaK001L2
print np.sqrt(np.diag(CovaK001L2))
print FitaK002L2
#print CovaK002L2
print np.sqrt(np.diag(CovaK002L2))
print FitaK003L2
#print CovaK002L2
print np.sqrt(np.diag(CovaK003L2))
print FitaK005L2
#print CovaK005L2
print np.sqrt(np.diag(CovaK005L2))
print FitaK007L2
#print CovaK002L2
print np.sqrt(np.diag(CovaK007L2))
print FitaK010L2
#print CovaK010L2
print np.sqrt(np.diag(CovaK010L2))

axs[1].plot(CouplingAxisA, func(CouplingAxisA, *FitaK001L2), marker='.',c=[0.0/1.5, 1.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, *FitaK002L2), marker='.',c=[0.0/1.5, 0.0/1.5, 1.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, *FitaK003L2), marker='.',c=[0.5/1.5, 0.0/1.5, 1.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, *FitaK005L2), marker='.',c=[1.0/1.5, 0.0/1.5, 1.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, *FitaK007L2), marker='.',c=[1.0/1.5, 0.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, *FitaK010L2), marker='.',c=[1.0/1.5, 0.5/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))

axs[1].plot(CouplingC,MaxEigenValImL2aK001, marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[1.0*1.0, 0.0*1.0, 0.0*1.0])#,label='100')
axs[1].plot(CouplingC,MaxEigenValImL2aK002, marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[1.0*1.0, 0.5*1.0, 0.0*1.0])#,label='100')
axs[1].plot(CouplingC,MaxEigenValImL2aK003, marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[0.0*1.0, 1.0*1.0, 0.0*1.0])#,label='100')
axs[1].plot(CouplingC,MaxEigenValImL2aK005, marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[0.0*1.0, 1.0*1.0, 0.0*1.0])#,label='100')
axs[1].plot(CouplingC,MaxEigenValImL2aK007, marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[0.0*1.0, 1.0*1.0, 0.0*1.0])#,label='100')
axs[1].plot(CouplingC,MaxEigenValImL2aK010, marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[0.0*1.0, 0.4*1.0, 1.0*1.0])#,label='100')

#axs[1].plot(CouplingC,[MaxEigenValImL2g000_41Inf[0],MaxEigenValImL2g000_51Inf[0],MaxEigenValImL2g000_61Inf[0],MaxEigenValImL2g000_71Inf[0],MaxEigenValImL2g000_81Inf[0]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[1.0*1.0, 0.0*1.0, 0.0*1.0])#,label='100')
#axs[1].plot(CouplingC,[MaxEigenValImL2g000_41Inf[1],MaxEigenValImL2g000_51Inf[1],MaxEigenValImL2g000_61Inf[1],MaxEigenValImL2g000_71Inf[1],MaxEigenValImL2g000_81Inf[1]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[1.0*1.0, 0.5*1.0, 0.0*1.0])#,label='100')
#axs[1].plot(CouplingC,[MaxEigenValImL2g000_41Inf[2],MaxEigenValImL2g000_51Inf[2],MaxEigenValImL2g000_61Inf[2],MaxEigenValImL2g000_71Inf[2],MaxEigenValImL2g000_81Inf[2]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[0.0*1.0, 1.0*1.0, 0.0*1.0])#,label='100')
#axs[1].plot(CouplingC,[MaxEigenValImL2g000_41Inf[3],MaxEigenValImL2g000_51Inf[3],MaxEigenValImL2g000_61Inf[3],MaxEigenValImL2g000_71Inf[3],MaxEigenValImL2g000_81Inf[3]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[0.0*1.0, 0.4*1.0, 1.0*1.0])#,label='100')
"""
axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.2676/1**2, 8.06042), marker='.',c=[1.0/1.5, 0.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.2676/2**2, 8.06042), marker='.',c=[1.0/1.5, 0.5/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.2676/3**2, 8.06042), marker='.',c=[1.0/1.5, 0.5/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.2676/5**2, 8.06042), marker='.',c=[0.0/1.5, 1.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.2676/7**2, 8.06042), marker='.',c=[0.0/1.5, 1.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.2676/10**2,8.06042), marker='.',c=[0.0/1.5, 0.0/1.5, 1.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))

axs[0].plot(CouplingAxis, func(CouplingAxis, 0.2676/1**2, 8.06042), marker='.',c=[1.0/1.5, 0.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, 0.2676/2**2, 8.06042), marker='.',c=[1.0/1.5, 0.5/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, 0.2676/3**2, 8.06042), marker='.',c=[1.0/1.5, 0.5/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, 0.2676/5**2, 8.06042), marker='.',c=[0.0/1.5, 1.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, 0.2676/7**2, 8.06042), marker='.',c=[0.0/1.5, 1.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, 0.2676/10**2,8.06042), marker='.',c=[0.0/1.5, 0.0/1.5, 1.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
"""
#"""

#axs[1].semilogy(100*Coupling,MaxEigenValImL2g0011Inf, marker='o',c=[1.0, 0.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.01$', markersize=4, linewidth=1)#,label='100')
#axs[1].semilogy(100*Coupling,MaxEigenValImL2g0021Inf, marker='o',c=[1.0, 0.5, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.02$', markersize=4, linewidth=1)#,label='100')
#axs[1].semilogy(100*Coupling,MaxEigenValImL2g0051Inf, marker='o',c=[0.0, 1.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.05$', markersize=4, linewidth=1)#,label='100')
#axs[1].semilogy(100*Coupling,MaxEigenValImL2g0101Inf, marker='o',c=[0.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 0.10$', markersize=4, linewidth=1)#,label='100')

axs[1].set_title("$\\ell=2$" ,fontsize=12, fontname='Times New Roman')

axs[1].grid(True)
axs[1].set_xlim(-0.e+0,+2.05e+0)
axs[1].set_xticks(np.arange(-0.0e+1,+2.01e+0, step=5.e-1))
axs[1].set_ylim(+1e-10,+1e+0)
axs[1].set_yticks([1e0,1e-2,1e-4,1e-6,1e-8,1e-10])

axs[0].text(-0.28, .4e-12, '(a)', fontsize=12)
axs[1].text(-0.14, .4e-12, '(b)', fontsize=12)

#axs[1,0].legend(bbox_to_anchor=(0.4, +1.2), loc=2, borderaxespad=0., ncol=4, labelspacing=1,handleheight=1, columnspacing=0.1, handletextpad=0.1)
#plt.suptitle('$\\ell=0XXX, g_{\\mathcal{K}}=0.1$', fontsize=20, fontname='Times New Roman')
axs[1].set_xlabel('$1/g_{\\mathcal{K}}$', fontsize=12, fontname='Times New Roman')
#axs[1].set_ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}\\times 10e{+7}$', fontsize=12, fontname='Times New Roman')


#plt.show()
fig.savefig('PlotReportTotal.pdf')

########################################################################
########################################################################

CouplingZ = np.zeros((4))
CouplingZ[0] = 1.
CouplingZ[1] = 2.
CouplingZ[2] = 5.
CouplingZ[3] = 10.

plt.clf()
fig, axs = plt.subplots(1, 2, figsize=(6, 3), sharey=True)
plt.subplots_adjust(left=0.25,bottom=0.15,right=0.8,top=0.7,wspace=0.15,hspace=0.4)

MaxEigenValImL0aK001Z = np.zeros(( len(CouplingZ) ))
MaxEigenValImL0aK002Z = np.zeros(( len(CouplingZ) ))
MaxEigenValImL0aK003Z = np.zeros(( len(CouplingZ) ))
MaxEigenValImL0aK005Z = np.zeros(( len(CouplingZ) ))
MaxEigenValImL0aK007Z = np.zeros(( len(CouplingZ) ))
MaxEigenValImL0aK010Z = np.zeros(( len(CouplingZ) ))

MaxEigenValImL0aK001Z = [MaxEigenValImL0g0011Inf[0],MaxEigenValImL0g0021Inf[0],MaxEigenValImL0g0051Inf[0],MaxEigenValImL0g0101Inf[0]]
MaxEigenValImL0aK002Z = [MaxEigenValImL0g0011Inf[1],MaxEigenValImL0g0021Inf[1],MaxEigenValImL0g0051Inf[1],MaxEigenValImL0g0101Inf[1]]
MaxEigenValImL0aK003Z = [MaxEigenValImL0g0011Inf[2],MaxEigenValImL0g0021Inf[2],MaxEigenValImL0g0051Inf[2],MaxEigenValImL0g0101Inf[2]]
MaxEigenValImL0aK005Z = [MaxEigenValImL0g0011Inf[3],MaxEigenValImL0g0021Inf[3],MaxEigenValImL0g0051Inf[3],MaxEigenValImL0g0101Inf[3]]
MaxEigenValImL0aK007Z = [MaxEigenValImL0g0011Inf[4],MaxEigenValImL0g0021Inf[4],MaxEigenValImL0g0051Inf[4],MaxEigenValImL0g0101Inf[4]]
MaxEigenValImL0aK010Z = [MaxEigenValImL0g0011Inf[5],MaxEigenValImL0g0021Inf[5],MaxEigenValImL0g0051Inf[5],MaxEigenValImL0g0101Inf[5]]

axs[0].semilogy(
            CouplingZ,MaxEigenValImL0aK001Z, marker='o',c=[0.0, 1.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 1$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[0].plot(CouplingZ,MaxEigenValImL0aK002Z, marker='o',c=[0.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 2$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[0].plot(CouplingZ,MaxEigenValImL0aK003Z, marker='o',c=[0.5, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 3$', markersize=5, linewidth=1,markeredgecolor=[0.5*0.8, 0.0*0.8, 1.0*0.8])
axs[0].plot(CouplingZ,MaxEigenValImL0aK005Z, marker='o',c=[1.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 5$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 1.0*0.8])
axs[0].plot(CouplingZ,MaxEigenValImL0aK007Z, marker='o',c=[1.0, 0.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 7$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[0].plot(CouplingZ,MaxEigenValImL0aK010Z, marker='o',c=[1.0, 0.5, 0.0],ls='None',label='$a_{\\mathcal{K}}=10$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])

axs[0].set_title("$\\ell=0$" ,fontsize=12, fontname='Times New Roman')

axs[0].grid(True)
axs[0].set_xlim(-0.e+0,+12.0e+0)
axs[0].set_xticks(np.arange(-0.0e+1,+12.01e+0, step=2.e-0))
axs[0].set_ylim(+1e-7,+1e+0)
#axs[0].set_ylim(+1e0,+1.01e+16)
axs[0].set_yticks([1e0,1e-1,1e-2,1e-3,1e-4,1e-5,1e-6,1e-7])

axs[0].legend(bbox_to_anchor=(-0.6, +1.30), loc=2, borderaxespad=0., ncol=6, labelspacing=.05,handleheight=.05, columnspacing=.05, handletextpad=.05)
#plt.suptitle('$\\ell=0XXX, g_{\\mathcal{K}}=0.1$', fontsize=20, fontname='Times New Roman')
axs[0].set_xlabel('$g_{\\mathcal{K}}$', fontsize=12, fontname='Times New Roman')
axs[0].set_ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}(a_{\\mathcal{K}},g_{\\mathcal{K}})$', fontsize=12, fontname='Times New Roman')

MaxEigenValImL2aK001Z = np.zeros(( len(CouplingZ) ))
MaxEigenValImL2aK002Z = np.zeros(( len(CouplingZ) ))
MaxEigenValImL2aK003Z = np.zeros(( len(CouplingZ) ))
MaxEigenValImL2aK005Z = np.zeros(( len(CouplingZ) ))
MaxEigenValImL2aK007Z = np.zeros(( len(CouplingZ) ))
MaxEigenValImL2aK010Z = np.zeros(( len(CouplingZ) ))

MaxEigenValImL2aK001Z = [MaxEigenValImL2g0011Inf[0],MaxEigenValImL2g0021Inf[0],MaxEigenValImL2g0051Inf[0],MaxEigenValImL2g0101Inf[0]]
MaxEigenValImL2aK002Z = [MaxEigenValImL2g0011Inf[1],MaxEigenValImL2g0021Inf[1],MaxEigenValImL2g0051Inf[1],MaxEigenValImL2g0101Inf[1]]
MaxEigenValImL2aK003Z = [MaxEigenValImL2g0011Inf[2],MaxEigenValImL2g0021Inf[2],MaxEigenValImL2g0051Inf[2],MaxEigenValImL2g0101Inf[2]]
MaxEigenValImL2aK005Z = [MaxEigenValImL2g0011Inf[3],MaxEigenValImL2g0021Inf[3],MaxEigenValImL2g0051Inf[3],MaxEigenValImL2g0101Inf[3]]
MaxEigenValImL2aK007Z = [MaxEigenValImL2g0011Inf[4],MaxEigenValImL2g0021Inf[4],MaxEigenValImL2g0051Inf[4],MaxEigenValImL2g0101Inf[4]]
MaxEigenValImL2aK010Z = [MaxEigenValImL2g0011Inf[5],MaxEigenValImL2g0021Inf[5],MaxEigenValImL2g0051Inf[5],MaxEigenValImL2g0101Inf[5]]

axs[1].semilogy(
            CouplingZ,MaxEigenValImL2aK001Z, marker='o',c=[0.0, 1.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 1$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[1].plot(CouplingZ,MaxEigenValImL2aK002Z, marker='o',c=[0.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 2$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
axs[1].plot(CouplingZ,MaxEigenValImL2aK003Z, marker='o',c=[0.5, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 3$', markersize=5, linewidth=1,markeredgecolor=[0.5*0.8, 0.0*0.8, 1.0*0.8])
axs[1].plot(CouplingZ,MaxEigenValImL2aK005Z, marker='o',c=[1.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 5$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 1.0*0.8])
axs[1].plot(CouplingZ,MaxEigenValImL2aK007Z, marker='o',c=[1.0, 0.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 7$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[1].plot(CouplingZ,MaxEigenValImL2aK010Z, marker='o',c=[1.0, 0.5, 0.0],ls='None',label='$a_{\\mathcal{K}}=10$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])

axs[1].set_title("$\\ell=2$" ,fontsize=12, fontname='Times New Roman')

axs[1].grid(True)
axs[1].set_xlim(-0.e+0,+12.0e+0)
axs[1].set_xticks(np.arange(-0.0e+1,+12.01e+0, step=2.e-0))
axs[1].set_ylim(+1e-7,+1e+0)
axs[1].set_yticks([1e0,1e-1,1e-2,1e-3,1e-4,1e-5,1e-6,1e-7])

axs[0].text(-0.28, .4e-12, '(a)', fontsize=12)
axs[1].text(-0.14, .4e-12, '(b)', fontsize=12)

#axs[1,0].legend(bbox_to_anchor=(0.4, +1.2), loc=2, borderaxespad=0., ncol=4, labelspacing=1,handleheight=1, columnspacing=0.1, handletextpad=0.1)
#plt.suptitle('$\\ell=0XXX, g_{\\mathcal{K}}=0.1$', fontsize=20, fontname='Times New Roman')
axs[1].set_xlabel('$g_{\\mathcal{K}}$', fontsize=12, fontname='Times New Roman')
#axs[1].set_ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}\\times 10e{+7}$', fontsize=12, fontname='Times New Roman')


#plt.show()
fig.savefig('PlotReportBiggK.pdf')

########################################################################
########################################################################


fileL0 = open("fileL0.txt","w") 

for m1 in range(0,len(CouplingB)):
    fileL0.write("%s" % ( 1 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( CouplingB[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( (MaxEigenValImL0aK001[m1]) ))
    fileL0.write('\n'),
for m1 in range(0,len(CouplingB)):
    fileL0.write("%s" % ( 2 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( CouplingB[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( (MaxEigenValImL0aK002[m1]) ))
    fileL0.write('\n'),
for m1 in range(0,len(CouplingB)):
    fileL0.write("%s" % ( 3 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( CouplingB[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( (MaxEigenValImL0aK003[m1]) ))
    fileL0.write('\n'),
for m1 in range(0,len(CouplingB)):
    fileL0.write("%s" % ( 5 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( CouplingB[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( (MaxEigenValImL0aK005[m1]) ))
    fileL0.write('\n'),
for m1 in range(0,len(CouplingB)):
    fileL0.write("%s" % ( 7 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( CouplingB[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( (MaxEigenValImL0aK007[m1]) ))
    fileL0.write('\n'),
for m1 in range(0,len(CouplingB)):
    fileL0.write("%s" % ( 10 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( CouplingB[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( (MaxEigenValImL0aK010[m1]) ))
    fileL0.write('\n'),
fileL0.close() 

########################################################################

fileL2 = open("fileL2.txt","w") 

for m1 in range(0,len(CouplingC)):
    fileL2.write("%s" % ( 1 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( CouplingC[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( (MaxEigenValImL2aK001[m1]) ))
    fileL2.write('\n'),
for m1 in range(0,len(CouplingC)):
    fileL2.write("%s" % ( 2 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( CouplingC[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( (MaxEigenValImL2aK002[m1]) ))
    fileL2.write('\n'),
for m1 in range(0,len(CouplingC)):
    fileL2.write("%s" % ( 3 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( CouplingC[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( (MaxEigenValImL2aK003[m1]) ))
    fileL2.write('\n'),
for m1 in range(0,len(CouplingC)):
    fileL2.write("%s" % ( 5 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( CouplingC[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( (MaxEigenValImL2aK005[m1]) ))
    fileL2.write('\n'),
for m1 in range(0,len(CouplingC)):
    fileL2.write("%s" % ( 7 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( CouplingC[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( (MaxEigenValImL2aK007[m1]) ))
    fileL2.write('\n'),
for m1 in range(0,len(CouplingC)):
    fileL2.write("%s" % ( 10 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( CouplingC[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( (MaxEigenValImL2aK010[m1]) ))
    fileL2.write('\n'),
fileL2.close() 

########################################################################
########################################################################

fileL0 = open("fileL0log10.txt","w") 

for m1 in range(0,len(CouplingA)):
    fileL0.write("%s" % ( 1 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( CouplingA[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( np.log10(MaxEigenValImL0aK001Total[m1]) ))
    fileL0.write('\n'),
for m1 in range(0,len(CouplingA)):
    fileL0.write("%s" % ( 2 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( CouplingA[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( np.log10(MaxEigenValImL0aK002Total[m1]) ))
    fileL0.write('\n'),
for m1 in range(0,len(CouplingA)):
    fileL0.write("%s" % ( 3 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( CouplingA[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( np.log10(MaxEigenValImL0aK003Total[m1]) ))
    fileL0.write('\n'),
for m1 in range(0,len(CouplingA)):
    fileL0.write("%s" % ( 5 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( CouplingA[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( np.log10(MaxEigenValImL0aK005Total[m1]) ))
    fileL0.write('\n'),
for m1 in range(0,len(CouplingA)):
    fileL0.write("%s" % ( 7 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( CouplingA[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( np.log10(MaxEigenValImL0aK007Total[m1]) ))
    fileL0.write('\n'),
for m1 in range(0,len(CouplingA)):
    fileL0.write("%s" % ( 10 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( CouplingA[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( np.log10(MaxEigenValImL0aK010Total[m1]) ))
    fileL0.write('\n'),
fileL0.close() 

########################################################################

fileL2 = open("fileL2log10.txt","w") 

for m1 in range(0,len(Coupling)):
    fileL2.write("%s" % ( 1 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( Coupling[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( np.log10(MaxEigenValImL2aK001Total[m1]) ))
    fileL2.write('\n'),
for m1 in range(0,len(Coupling)):
    fileL2.write("%s" % ( 2 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( Coupling[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( np.log10(MaxEigenValImL2aK002Total[m1]) ))
    fileL2.write('\n'),
for m1 in range(0,len(Coupling)):
    fileL2.write("%s" % ( 3 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( Coupling[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( np.log10(MaxEigenValImL2aK003Total[m1]) ))
    fileL2.write('\n'),
for m1 in range(0,len(Coupling)):
    fileL2.write("%s" % ( 5 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( Coupling[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( np.log10(MaxEigenValImL2aK005Total[m1]) ))
    fileL2.write('\n'),
for m1 in range(0,len(Coupling)):
    fileL2.write("%s" % ( 7 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( Coupling[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( np.log10(MaxEigenValImL2aK007Total[m1]) ))
    fileL2.write('\n'),
for m1 in range(0,len(Coupling)):
    fileL2.write("%s" % ( 10 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( Coupling[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( np.log10(MaxEigenValImL2aK010Total[m1]) ))
    fileL2.write('\n'),
fileL2.close() 

########################################################################
########################################################################

fileL0 = open("C0L0.txt","w") 

for m1 in range(0,1):
    fileL0.write("%s" % ( 1 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( FitaK001L0[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( np.sqrt(np.diag(CovaK001L0))[m1] ))
    fileL0.write('\n'),
for m1 in range(0,1):
    fileL0.write("%s" % ( 2 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( FitaK002L0[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( np.sqrt(np.diag(CovaK002L0))[m1] ))
    fileL0.write('\n'),
for m1 in range(0,1):
    fileL0.write("%s" % ( 3 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( FitaK003L0[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( np.sqrt(np.diag(CovaK003L0))[m1] ))
    fileL0.write('\n'),
for m1 in range(0,1):
    fileL0.write("%s" % ( 5 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( FitaK005L0[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( np.sqrt(np.diag(CovaK005L0))[m1] ))
    fileL0.write('\n'),
for m1 in range(0,1):
    fileL0.write("%s" % ( 7 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( FitaK007L0[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( np.sqrt(np.diag(CovaK007L0))[m1] ))
    fileL0.write('\n'),
for m1 in range(0,1):
    fileL0.write("%s" % ( 10 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( FitaK010L0[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( np.sqrt(np.diag(CovaK010L0))[m1] ))
    fileL0.write('\n'),
fileL0.close() 

########################################################################

fileL2 = open("C0L2.txt","w") 

for m1 in range(0,1):
    fileL2.write("%s" % ( 1 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( FitaK001L2[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( np.sqrt(np.diag(CovaK001L2))[m1] ))
    fileL2.write('\n'),
for m1 in range(0,1):
    fileL2.write("%s" % ( 2 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( FitaK002L2[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( np.sqrt(np.diag(CovaK002L2))[m1] ))
    fileL2.write('\n'),
for m1 in range(0,1):
    fileL2.write("%s" % ( 3 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( FitaK003L2[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( np.sqrt(np.diag(CovaK003L2))[m1] ))
    fileL2.write('\n'),
for m1 in range(0,1):
    fileL2.write("%s" % ( 5 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( FitaK005L2[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( np.sqrt(np.diag(CovaK005L2))[m1] ))
    fileL2.write('\n'),
for m1 in range(0,1):
    fileL2.write("%s" % ( 7 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( FitaK007L2[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( np.sqrt(np.diag(CovaK007L2))[m1] ))
    fileL2.write('\n'),
for m1 in range(0,1):
    fileL2.write("%s" % ( 10 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( FitaK010L2[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( np.sqrt(np.diag(CovaK010L2))[m1] ))
    fileL2.write('\n'),
fileL2.close()

########################################################################
########################################################################

fileL0 = open("G0L0.txt","w") 

for m1 in range(1,2):
    fileL0.write("%s" % ( 1 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( FitaK001L0[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( np.sqrt(np.diag(CovaK001L0))[m1] ))
    fileL0.write('\n'),
for m1 in range(1,2):
    fileL0.write("%s" % ( 2 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( FitaK002L0[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( np.sqrt(np.diag(CovaK002L0))[m1] ))
    fileL0.write('\n'),
for m1 in range(1,2):
    fileL0.write("%s" % ( 3 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( FitaK003L0[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( np.sqrt(np.diag(CovaK003L0))[m1] ))
    fileL0.write('\n'),
for m1 in range(1,2):
    fileL0.write("%s" % ( 5 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( FitaK005L0[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( np.sqrt(np.diag(CovaK005L0))[m1] ))
    fileL0.write('\n'),
for m1 in range(1,2):
    fileL0.write("%s" % ( 7 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( FitaK007L0[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( np.sqrt(np.diag(CovaK007L0))[m1] ))
    fileL0.write('\n'),
for m1 in range(1,2):
    fileL0.write("%s" % ( 10 )),
    fileL0.write("\t"),
    fileL0.write("%s" % ( FitaK010L0[m1] ))
    fileL0.write("\t"),
    fileL0.write("%s" % ( np.sqrt(np.diag(CovaK010L0))[m1] ))
    fileL0.write('\n'),
fileL0.close() 

########################################################################

fileL2 = open("G0L2.txt","w") 

for m1 in range(1,2):
    fileL2.write("%s" % ( 1 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( FitaK001L2[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( np.sqrt(np.diag(CovaK001L2))[m1] ))
    fileL2.write('\n'),
for m1 in range(1,2):
    fileL2.write("%s" % ( 2 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( FitaK002L2[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( np.sqrt(np.diag(CovaK002L2))[m1] ))
    fileL2.write('\n'),
for m1 in range(1,2):
    fileL2.write("%s" % ( 3 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( FitaK003L2[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( np.sqrt(np.diag(CovaK003L2))[m1] ))
    fileL2.write('\n'),
for m1 in range(1,2):
    fileL2.write("%s" % ( 5 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( FitaK005L2[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( np.sqrt(np.diag(CovaK005L2))[m1] ))
    fileL2.write('\n'),
for m1 in range(1,2):
    fileL2.write("%s" % ( 7 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( FitaK007L2[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( np.sqrt(np.diag(CovaK007L2))[m1] ))
    fileL2.write('\n'),
for m1 in range(1,2):
    fileL2.write("%s" % ( 10 )),
    fileL2.write("\t"),
    fileL2.write("%s" % ( FitaK010L2[m1] ))
    fileL2.write("\t"),
    fileL2.write("%s" % ( np.sqrt(np.diag(CovaK010L2))[m1] ))
    fileL2.write('\n'),
fileL2.close() 
