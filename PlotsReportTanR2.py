import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from matplotlib.ticker import (MultipleLocator, NullFormatter,
                                   ScalarFormatter)

fiveSizes = [1./10,1./20,1./30,1./40,1./50]

dataL0g0010011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK001/N010/HamVals.txt')

MomentumAxL0g0010011010 = dataL0g0010011010[:,][:,5*0+0]
KineticEneL0g0010011010 = dataL0g0010011010[:,][:,5*0+1]
SelfEnergyL0g0010011010 = dataL0g0010011010[:,][:,5*0+2]
EigenValReL0g0010011010 = dataL0g0010011010[:,][:,5*0+3]
EigenValImL0g0010011010 = dataL0g0010011010[:,][:,5*0+4]

dataL0g0010011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK001/N020/HamVals.txt')

MomentumAxL0g0010011020 = dataL0g0010011020[:,][:,5*0+0]
KineticEneL0g0010011020 = dataL0g0010011020[:,][:,5*0+1]
SelfEnergyL0g0010011020 = dataL0g0010011020[:,][:,5*0+2]
EigenValReL0g0010011020 = dataL0g0010011020[:,][:,5*0+3]
EigenValImL0g0010011020 = dataL0g0010011020[:,][:,5*0+4]

dataL0g0010011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK001/N030/HamVals.txt')

MomentumAxL0g0010011030 = dataL0g0010011030[:,][:,5*0+0]
KineticEneL0g0010011030 = dataL0g0010011030[:,][:,5*0+1]
SelfEnergyL0g0010011030 = dataL0g0010011030[:,][:,5*0+2]
EigenValReL0g0010011030 = dataL0g0010011030[:,][:,5*0+3]
EigenValImL0g0010011030 = dataL0g0010011030[:,][:,5*0+4]

dataL0g0010011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK001/N040/HamVals.txt')

MomentumAxL0g0010011040 = dataL0g0010011040[:,][:,5*0+0]
KineticEneL0g0010011040 = dataL0g0010011040[:,][:,5*0+1]
SelfEnergyL0g0010011040 = dataL0g0010011040[:,][:,5*0+2]
EigenValReL0g0010011040 = dataL0g0010011040[:,][:,5*0+3]
EigenValImL0g0010011040 = dataL0g0010011040[:,][:,5*0+4]

dataL0g0010011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK001/N050/HamVals.txt')

MomentumAxL0g0010011050 = dataL0g0010011050[:,][:,5*0+0]
KineticEneL0g0010011050 = dataL0g0010011050[:,][:,5*0+1]
SelfEnergyL0g0010011050 = dataL0g0010011050[:,][:,5*0+2]
EigenValReL0g0010011050 = dataL0g0010011050[:,][:,5*0+3]
EigenValImL0g0010011050 = dataL0g0010011050[:,][:,5*0+4]

dataL0g0010021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK002/N010/HamVals.txt')

MomentumAxL0g0010021010 = dataL0g0010021010[:,][:,5*0+0]
KineticEneL0g0010021010 = dataL0g0010021010[:,][:,5*0+1]
SelfEnergyL0g0010021010 = dataL0g0010021010[:,][:,5*0+2]
EigenValReL0g0010021010 = dataL0g0010021010[:,][:,5*0+3]
EigenValImL0g0010021010 = dataL0g0010021010[:,][:,5*0+4]

dataL0g0010021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK002/N020/HamVals.txt')

MomentumAxL0g0010021020 = dataL0g0010021020[:,][:,5*0+0]
KineticEneL0g0010021020 = dataL0g0010021020[:,][:,5*0+1]
SelfEnergyL0g0010021020 = dataL0g0010021020[:,][:,5*0+2]
EigenValReL0g0010021020 = dataL0g0010021020[:,][:,5*0+3]
EigenValImL0g0010021020 = dataL0g0010021020[:,][:,5*0+4]

dataL0g0010021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK002/N030/HamVals.txt')

MomentumAxL0g0010021030 = dataL0g0010021030[:,][:,5*0+0]
KineticEneL0g0010021030 = dataL0g0010021030[:,][:,5*0+1]
SelfEnergyL0g0010021030 = dataL0g0010021030[:,][:,5*0+2]
EigenValReL0g0010021030 = dataL0g0010021030[:,][:,5*0+3]
EigenValImL0g0010021030 = dataL0g0010021030[:,][:,5*0+4]

dataL0g0010021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK002/N040/HamVals.txt')

MomentumAxL0g0010021040 = dataL0g0010021040[:,][:,5*0+0]
KineticEneL0g0010021040 = dataL0g0010021040[:,][:,5*0+1]
SelfEnergyL0g0010021040 = dataL0g0010021040[:,][:,5*0+2]
EigenValReL0g0010021040 = dataL0g0010021040[:,][:,5*0+3]
EigenValImL0g0010021040 = dataL0g0010021040[:,][:,5*0+4]

dataL0g0010021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK002/N050/HamVals.txt')

MomentumAxL0g0010021050 = dataL0g0010021050[:,][:,5*0+0]
KineticEneL0g0010021050 = dataL0g0010021050[:,][:,5*0+1]
SelfEnergyL0g0010021050 = dataL0g0010021050[:,][:,5*0+2]
EigenValReL0g0010021050 = dataL0g0010021050[:,][:,5*0+3]
EigenValImL0g0010021050 = dataL0g0010021050[:,][:,5*0+4]

dataL0g0010051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK005/N010/HamVals.txt')

MomentumAxL0g0010051010 = dataL0g0010051010[:,][:,5*0+0]
KineticEneL0g0010051010 = dataL0g0010051010[:,][:,5*0+1]
SelfEnergyL0g0010051010 = dataL0g0010051010[:,][:,5*0+2]
EigenValReL0g0010051010 = dataL0g0010051010[:,][:,5*0+3]
EigenValImL0g0010051010 = dataL0g0010051010[:,][:,5*0+4]

dataL0g0010051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK005/N020/HamVals.txt')

MomentumAxL0g0010051020 = dataL0g0010051020[:,][:,5*0+0]
KineticEneL0g0010051020 = dataL0g0010051020[:,][:,5*0+1]
SelfEnergyL0g0010051020 = dataL0g0010051020[:,][:,5*0+2]
EigenValReL0g0010051020 = dataL0g0010051020[:,][:,5*0+3]
EigenValImL0g0010051020 = dataL0g0010051020[:,][:,5*0+4]

dataL0g0010051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK005/N030/HamVals.txt')

MomentumAxL0g0010051030 = dataL0g0010051030[:,][:,5*0+0]
KineticEneL0g0010051030 = dataL0g0010051030[:,][:,5*0+1]
SelfEnergyL0g0010051030 = dataL0g0010051030[:,][:,5*0+2]
EigenValReL0g0010051030 = dataL0g0010051030[:,][:,5*0+3]
EigenValImL0g0010051030 = dataL0g0010051030[:,][:,5*0+4]

dataL0g0010051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK005/N040/HamVals.txt')

MomentumAxL0g0010051040 = dataL0g0010051040[:,][:,5*0+0]
KineticEneL0g0010051040 = dataL0g0010051040[:,][:,5*0+1]
SelfEnergyL0g0010051040 = dataL0g0010051040[:,][:,5*0+2]
EigenValReL0g0010051040 = dataL0g0010051040[:,][:,5*0+3]
EigenValImL0g0010051040 = dataL0g0010051040[:,][:,5*0+4]

dataL0g0010051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK005/N050/HamVals.txt')

MomentumAxL0g0010051050 = dataL0g0010051050[:,][:,5*0+0]
KineticEneL0g0010051050 = dataL0g0010051050[:,][:,5*0+1]
SelfEnergyL0g0010051050 = dataL0g0010051050[:,][:,5*0+2]
EigenValReL0g0010051050 = dataL0g0010051050[:,][:,5*0+3]
EigenValImL0g0010051050 = dataL0g0010051050[:,][:,5*0+4]

dataL0g0010101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK010/N010/HamVals.txt')

MomentumAxL0g0010101010 = dataL0g0010101010[:,][:,5*0+0]
KineticEneL0g0010101010 = dataL0g0010101010[:,][:,5*0+1]
SelfEnergyL0g0010101010 = dataL0g0010101010[:,][:,5*0+2]
EigenValReL0g0010101010 = dataL0g0010101010[:,][:,5*0+3]
EigenValImL0g0010101010 = dataL0g0010101010[:,][:,5*0+4]

dataL0g0010101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK010/N020/HamVals.txt')

MomentumAxL0g0010101020 = dataL0g0010101020[:,][:,5*0+0]
KineticEneL0g0010101020 = dataL0g0010101020[:,][:,5*0+1]
SelfEnergyL0g0010101020 = dataL0g0010101020[:,][:,5*0+2]
EigenValReL0g0010101020 = dataL0g0010101020[:,][:,5*0+3]
EigenValImL0g0010101020 = dataL0g0010101020[:,][:,5*0+4]

dataL0g0010101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK010/N030/HamVals.txt')

MomentumAxL0g0010101030 = dataL0g0010101030[:,][:,5*0+0]
KineticEneL0g0010101030 = dataL0g0010101030[:,][:,5*0+1]
SelfEnergyL0g0010101030 = dataL0g0010101030[:,][:,5*0+2]
EigenValReL0g0010101030 = dataL0g0010101030[:,][:,5*0+3]
EigenValImL0g0010101030 = dataL0g0010101030[:,][:,5*0+4]

dataL0g0010101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK010/N040/HamVals.txt')

MomentumAxL0g0010101040 = dataL0g0010101040[:,][:,5*0+0]
KineticEneL0g0010101040 = dataL0g0010101040[:,][:,5*0+1]
SelfEnergyL0g0010101040 = dataL0g0010101040[:,][:,5*0+2]
EigenValReL0g0010101040 = dataL0g0010101040[:,][:,5*0+3]
EigenValImL0g0010101040 = dataL0g0010101040[:,][:,5*0+4]

dataL0g0010101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK010/N050/HamVals.txt')

MomentumAxL0g0010101050 = dataL0g0010101050[:,][:,5*0+0]
KineticEneL0g0010101050 = dataL0g0010101050[:,][:,5*0+1]
SelfEnergyL0g0010101050 = dataL0g0010101050[:,][:,5*0+2]
EigenValReL0g0010101050 = dataL0g0010101050[:,][:,5*0+3]
EigenValImL0g0010101050 = dataL0g0010101050[:,][:,5*0+4]
"""
dataL0g0010201010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK020/N010/HamVals.txt')

MomentumAxL0g0010201010 = dataL0g0010201010[:,][:,5*0+0]
KineticEneL0g0010201010 = dataL0g0010201010[:,][:,5*0+1]
SelfEnergyL0g0010201010 = dataL0g0010201010[:,][:,5*0+2]
EigenValReL0g0010201010 = dataL0g0010201010[:,][:,5*0+3]
EigenValImL0g0010201010 = dataL0g0010201010[:,][:,5*0+4]

dataL0g0010201020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK020/N020/HamVals.txt')

MomentumAxL0g0010201020 = dataL0g0010201020[:,][:,5*0+0]
KineticEneL0g0010201020 = dataL0g0010201020[:,][:,5*0+1]
SelfEnergyL0g0010201020 = dataL0g0010201020[:,][:,5*0+2]
EigenValReL0g0010201020 = dataL0g0010201020[:,][:,5*0+3]
EigenValImL0g0010201020 = dataL0g0010201020[:,][:,5*0+4]

dataL0g0010201030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK020/N030/HamVals.txt')

MomentumAxL0g0010201030 = dataL0g0010201030[:,][:,5*0+0]
KineticEneL0g0010201030 = dataL0g0010201030[:,][:,5*0+1]
SelfEnergyL0g0010201030 = dataL0g0010201030[:,][:,5*0+2]
EigenValReL0g0010201030 = dataL0g0010201030[:,][:,5*0+3]
EigenValImL0g0010201030 = dataL0g0010201030[:,][:,5*0+4]

dataL0g0010201040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK020/N040/HamVals.txt')

MomentumAxL0g0010201040 = dataL0g0010201040[:,][:,5*0+0]
KineticEneL0g0010201040 = dataL0g0010201040[:,][:,5*0+1]
SelfEnergyL0g0010201040 = dataL0g0010201040[:,][:,5*0+2]
EigenValReL0g0010201040 = dataL0g0010201040[:,][:,5*0+3]
EigenValImL0g0010201040 = dataL0g0010201040[:,][:,5*0+4]

dataL0g0010201050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK00-01/aK020/N050/HamVals.txt')

MomentumAxL0g0010201050 = dataL0g0010201050[:,][:,5*0+0]
KineticEneL0g0010201050 = dataL0g0010201050[:,][:,5*0+1]
SelfEnergyL0g0010201050 = dataL0g0010201050[:,][:,5*0+2]
EigenValReL0g0010201050 = dataL0g0010201050[:,][:,5*0+3]
EigenValImL0g0010201050 = dataL0g0010201050[:,][:,5*0+4]
"""
MaxEigenValImL0g000_011010 = np.zeros((4))
MaxEigenValImL0g000_011020 = np.zeros((4))
MaxEigenValImL0g000_011030 = np.zeros((4))
MaxEigenValImL0g000_011040 = np.zeros((4))
MaxEigenValImL0g000_011050 = np.zeros((4))
MaxEigenValImL0g000_011Inf = np.zeros((4))

MaxEigenValImL0g000_011010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g000_011010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g000_011010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g000_011010[3] = np.max(EigenValImL0g0010101010)
#MaxEigenValImL0g000_011010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g000_011020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g000_011020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g000_011020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g000_011020[3] = np.max(EigenValImL0g0010101020)
#MaxEigenValImL0g000_011020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g000_011030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g000_011030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g000_011030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g000_011030[3] = np.max(EigenValImL0g0010101030)
#MaxEigenValImL0g000_011030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g000_011040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g000_011040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g000_011040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g000_011040[3] = np.max(EigenValImL0g0010101040)
#MaxEigenValImL0g000_011040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g000_011050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g000_011050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g000_011050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g000_011050[3] = np.max(EigenValImL0g0010101050)
#MaxEigenValImL0g000_011050[4] = np.max(EigenValImL0g0010201050)

MaxEigenValImL0g000_011Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_011010[0],MaxEigenValImL0g000_011020[0],MaxEigenValImL0g000_011030[0],MaxEigenValImL0g000_011040[0],MaxEigenValImL0g000_011050[0]], 1)[[1]]
MaxEigenValImL0g000_011Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_011010[1],MaxEigenValImL0g000_011020[1],MaxEigenValImL0g000_011030[1],MaxEigenValImL0g000_011040[1],MaxEigenValImL0g000_011050[1]], 1)[[1]]
MaxEigenValImL0g000_011Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_011010[2],MaxEigenValImL0g000_011020[2],MaxEigenValImL0g000_011030[2],MaxEigenValImL0g000_011040[2],MaxEigenValImL0g000_011050[2]], 1)[[1]]
MaxEigenValImL0g000_011Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_011010[3],MaxEigenValImL0g000_011020[3],MaxEigenValImL0g000_011030[3],MaxEigenValImL0g000_011040[3],MaxEigenValImL0g000_011050[3]], 1)[[1]]
#MaxEigenValImL0g000_011Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_011010[4],MaxEigenValImL0g000_011020[4],MaxEigenValImL0g000_011030[4],MaxEigenValImL0g000_011040[4],MaxEigenValImL0g000_011050[4]], 1)[[1]]

########################################################################

dataL0g0010011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK001/N010/HamVals.txt')

MomentumAxL0g0010011010 = dataL0g0010011010[:,][:,5*0+0]
KineticEneL0g0010011010 = dataL0g0010011010[:,][:,5*0+1]
SelfEnergyL0g0010011010 = dataL0g0010011010[:,][:,5*0+2]
EigenValReL0g0010011010 = dataL0g0010011010[:,][:,5*0+3]
EigenValImL0g0010011010 = dataL0g0010011010[:,][:,5*0+4]

dataL0g0010011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK001/N020/HamVals.txt')

MomentumAxL0g0010011020 = dataL0g0010011020[:,][:,5*0+0]
KineticEneL0g0010011020 = dataL0g0010011020[:,][:,5*0+1]
SelfEnergyL0g0010011020 = dataL0g0010011020[:,][:,5*0+2]
EigenValReL0g0010011020 = dataL0g0010011020[:,][:,5*0+3]
EigenValImL0g0010011020 = dataL0g0010011020[:,][:,5*0+4]

dataL0g0010011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK001/N030/HamVals.txt')

MomentumAxL0g0010011030 = dataL0g0010011030[:,][:,5*0+0]
KineticEneL0g0010011030 = dataL0g0010011030[:,][:,5*0+1]
SelfEnergyL0g0010011030 = dataL0g0010011030[:,][:,5*0+2]
EigenValReL0g0010011030 = dataL0g0010011030[:,][:,5*0+3]
EigenValImL0g0010011030 = dataL0g0010011030[:,][:,5*0+4]

dataL0g0010011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK001/N040/HamVals.txt')

MomentumAxL0g0010011040 = dataL0g0010011040[:,][:,5*0+0]
KineticEneL0g0010011040 = dataL0g0010011040[:,][:,5*0+1]
SelfEnergyL0g0010011040 = dataL0g0010011040[:,][:,5*0+2]
EigenValReL0g0010011040 = dataL0g0010011040[:,][:,5*0+3]
EigenValImL0g0010011040 = dataL0g0010011040[:,][:,5*0+4]

dataL0g0010011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK001/N050/HamVals.txt')

MomentumAxL0g0010011050 = dataL0g0010011050[:,][:,5*0+0]
KineticEneL0g0010011050 = dataL0g0010011050[:,][:,5*0+1]
SelfEnergyL0g0010011050 = dataL0g0010011050[:,][:,5*0+2]
EigenValReL0g0010011050 = dataL0g0010011050[:,][:,5*0+3]
EigenValImL0g0010011050 = dataL0g0010011050[:,][:,5*0+4]

dataL0g0010021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK002/N010/HamVals.txt')

MomentumAxL0g0010021010 = dataL0g0010021010[:,][:,5*0+0]
KineticEneL0g0010021010 = dataL0g0010021010[:,][:,5*0+1]
SelfEnergyL0g0010021010 = dataL0g0010021010[:,][:,5*0+2]
EigenValReL0g0010021010 = dataL0g0010021010[:,][:,5*0+3]
EigenValImL0g0010021010 = dataL0g0010021010[:,][:,5*0+4]

dataL0g0010021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK002/N020/HamVals.txt')

MomentumAxL0g0010021020 = dataL0g0010021020[:,][:,5*0+0]
KineticEneL0g0010021020 = dataL0g0010021020[:,][:,5*0+1]
SelfEnergyL0g0010021020 = dataL0g0010021020[:,][:,5*0+2]
EigenValReL0g0010021020 = dataL0g0010021020[:,][:,5*0+3]
EigenValImL0g0010021020 = dataL0g0010021020[:,][:,5*0+4]

dataL0g0010021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK002/N030/HamVals.txt')

MomentumAxL0g0010021030 = dataL0g0010021030[:,][:,5*0+0]
KineticEneL0g0010021030 = dataL0g0010021030[:,][:,5*0+1]
SelfEnergyL0g0010021030 = dataL0g0010021030[:,][:,5*0+2]
EigenValReL0g0010021030 = dataL0g0010021030[:,][:,5*0+3]
EigenValImL0g0010021030 = dataL0g0010021030[:,][:,5*0+4]

dataL0g0010021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK002/N040/HamVals.txt')

MomentumAxL0g0010021040 = dataL0g0010021040[:,][:,5*0+0]
KineticEneL0g0010021040 = dataL0g0010021040[:,][:,5*0+1]
SelfEnergyL0g0010021040 = dataL0g0010021040[:,][:,5*0+2]
EigenValReL0g0010021040 = dataL0g0010021040[:,][:,5*0+3]
EigenValImL0g0010021040 = dataL0g0010021040[:,][:,5*0+4]

dataL0g0010021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK002/N050/HamVals.txt')

MomentumAxL0g0010021050 = dataL0g0010021050[:,][:,5*0+0]
KineticEneL0g0010021050 = dataL0g0010021050[:,][:,5*0+1]
SelfEnergyL0g0010021050 = dataL0g0010021050[:,][:,5*0+2]
EigenValReL0g0010021050 = dataL0g0010021050[:,][:,5*0+3]
EigenValImL0g0010021050 = dataL0g0010021050[:,][:,5*0+4]

dataL0g0010051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK005/N010/HamVals.txt')

MomentumAxL0g0010051010 = dataL0g0010051010[:,][:,5*0+0]
KineticEneL0g0010051010 = dataL0g0010051010[:,][:,5*0+1]
SelfEnergyL0g0010051010 = dataL0g0010051010[:,][:,5*0+2]
EigenValReL0g0010051010 = dataL0g0010051010[:,][:,5*0+3]
EigenValImL0g0010051010 = dataL0g0010051010[:,][:,5*0+4]

dataL0g0010051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK005/N020/HamVals.txt')

MomentumAxL0g0010051020 = dataL0g0010051020[:,][:,5*0+0]
KineticEneL0g0010051020 = dataL0g0010051020[:,][:,5*0+1]
SelfEnergyL0g0010051020 = dataL0g0010051020[:,][:,5*0+2]
EigenValReL0g0010051020 = dataL0g0010051020[:,][:,5*0+3]
EigenValImL0g0010051020 = dataL0g0010051020[:,][:,5*0+4]

dataL0g0010051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK005/N030/HamVals.txt')

MomentumAxL0g0010051030 = dataL0g0010051030[:,][:,5*0+0]
KineticEneL0g0010051030 = dataL0g0010051030[:,][:,5*0+1]
SelfEnergyL0g0010051030 = dataL0g0010051030[:,][:,5*0+2]
EigenValReL0g0010051030 = dataL0g0010051030[:,][:,5*0+3]
EigenValImL0g0010051030 = dataL0g0010051030[:,][:,5*0+4]

dataL0g0010051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK005/N040/HamVals.txt')

MomentumAxL0g0010051040 = dataL0g0010051040[:,][:,5*0+0]
KineticEneL0g0010051040 = dataL0g0010051040[:,][:,5*0+1]
SelfEnergyL0g0010051040 = dataL0g0010051040[:,][:,5*0+2]
EigenValReL0g0010051040 = dataL0g0010051040[:,][:,5*0+3]
EigenValImL0g0010051040 = dataL0g0010051040[:,][:,5*0+4]

dataL0g0010051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK005/N050/HamVals.txt')

MomentumAxL0g0010051050 = dataL0g0010051050[:,][:,5*0+0]
KineticEneL0g0010051050 = dataL0g0010051050[:,][:,5*0+1]
SelfEnergyL0g0010051050 = dataL0g0010051050[:,][:,5*0+2]
EigenValReL0g0010051050 = dataL0g0010051050[:,][:,5*0+3]
EigenValImL0g0010051050 = dataL0g0010051050[:,][:,5*0+4]

dataL0g0010101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK010/N010/HamVals.txt')

MomentumAxL0g0010101010 = dataL0g0010101010[:,][:,5*0+0]
KineticEneL0g0010101010 = dataL0g0010101010[:,][:,5*0+1]
SelfEnergyL0g0010101010 = dataL0g0010101010[:,][:,5*0+2]
EigenValReL0g0010101010 = dataL0g0010101010[:,][:,5*0+3]
EigenValImL0g0010101010 = dataL0g0010101010[:,][:,5*0+4]

dataL0g0010101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK010/N020/HamVals.txt')

MomentumAxL0g0010101020 = dataL0g0010101020[:,][:,5*0+0]
KineticEneL0g0010101020 = dataL0g0010101020[:,][:,5*0+1]
SelfEnergyL0g0010101020 = dataL0g0010101020[:,][:,5*0+2]
EigenValReL0g0010101020 = dataL0g0010101020[:,][:,5*0+3]
EigenValImL0g0010101020 = dataL0g0010101020[:,][:,5*0+4]

dataL0g0010101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK010/N030/HamVals.txt')

MomentumAxL0g0010101030 = dataL0g0010101030[:,][:,5*0+0]
KineticEneL0g0010101030 = dataL0g0010101030[:,][:,5*0+1]
SelfEnergyL0g0010101030 = dataL0g0010101030[:,][:,5*0+2]
EigenValReL0g0010101030 = dataL0g0010101030[:,][:,5*0+3]
EigenValImL0g0010101030 = dataL0g0010101030[:,][:,5*0+4]

dataL0g0010101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK010/N040/HamVals.txt')

MomentumAxL0g0010101040 = dataL0g0010101040[:,][:,5*0+0]
KineticEneL0g0010101040 = dataL0g0010101040[:,][:,5*0+1]
SelfEnergyL0g0010101040 = dataL0g0010101040[:,][:,5*0+2]
EigenValReL0g0010101040 = dataL0g0010101040[:,][:,5*0+3]
EigenValImL0g0010101040 = dataL0g0010101040[:,][:,5*0+4]

dataL0g0010101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK010/N050/HamVals.txt')

MomentumAxL0g0010101050 = dataL0g0010101050[:,][:,5*0+0]
KineticEneL0g0010101050 = dataL0g0010101050[:,][:,5*0+1]
SelfEnergyL0g0010101050 = dataL0g0010101050[:,][:,5*0+2]
EigenValReL0g0010101050 = dataL0g0010101050[:,][:,5*0+3]
EigenValImL0g0010101050 = dataL0g0010101050[:,][:,5*0+4]
"""
dataL0g0010201010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK020/N010/HamVals.txt')

MomentumAxL0g0010201010 = dataL0g0010201010[:,][:,5*0+0]
KineticEneL0g0010201010 = dataL0g0010201010[:,][:,5*0+1]
SelfEnergyL0g0010201010 = dataL0g0010201010[:,][:,5*0+2]
EigenValReL0g0010201010 = dataL0g0010201010[:,][:,5*0+3]
EigenValImL0g0010201010 = dataL0g0010201010[:,][:,5*0+4]

dataL0g0010201020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK020/N020/HamVals.txt')

MomentumAxL0g0010201020 = dataL0g0010201020[:,][:,5*0+0]
KineticEneL0g0010201020 = dataL0g0010201020[:,][:,5*0+1]
SelfEnergyL0g0010201020 = dataL0g0010201020[:,][:,5*0+2]
EigenValReL0g0010201020 = dataL0g0010201020[:,][:,5*0+3]
EigenValImL0g0010201020 = dataL0g0010201020[:,][:,5*0+4]

dataL0g0010201030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK020/N030/HamVals.txt')

MomentumAxL0g0010201030 = dataL0g0010201030[:,][:,5*0+0]
KineticEneL0g0010201030 = dataL0g0010201030[:,][:,5*0+1]
SelfEnergyL0g0010201030 = dataL0g0010201030[:,][:,5*0+2]
EigenValReL0g0010201030 = dataL0g0010201030[:,][:,5*0+3]
EigenValImL0g0010201030 = dataL0g0010201030[:,][:,5*0+4]

dataL0g0010201040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK020/N040/HamVals.txt')

MomentumAxL0g0010201040 = dataL0g0010201040[:,][:,5*0+0]
KineticEneL0g0010201040 = dataL0g0010201040[:,][:,5*0+1]
SelfEnergyL0g0010201040 = dataL0g0010201040[:,][:,5*0+2]
EigenValReL0g0010201040 = dataL0g0010201040[:,][:,5*0+3]
EigenValImL0g0010201040 = dataL0g0010201040[:,][:,5*0+4]

dataL0g0010201050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-10/aK020/N050/HamVals.txt')

MomentumAxL0g0010201050 = dataL0g0010201050[:,][:,5*0+0]
KineticEneL0g0010201050 = dataL0g0010201050[:,][:,5*0+1]
SelfEnergyL0g0010201050 = dataL0g0010201050[:,][:,5*0+2]
EigenValReL0g0010201050 = dataL0g0010201050[:,][:,5*0+3]
EigenValImL0g0010201050 = dataL0g0010201050[:,][:,5*0+4]
"""
MaxEigenValImL0g000_11010 = np.zeros((4))
MaxEigenValImL0g000_11020 = np.zeros((4))
MaxEigenValImL0g000_11030 = np.zeros((4))
MaxEigenValImL0g000_11040 = np.zeros((4))
MaxEigenValImL0g000_11050 = np.zeros((4))
MaxEigenValImL0g000_11Inf = np.zeros((4))

MaxEigenValImL0g000_11010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g000_11010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g000_11010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g000_11010[3] = np.max(EigenValImL0g0010101010)
#MaxEigenValImL0g000_11010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g000_11020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g000_11020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g000_11020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g000_11020[3] = np.max(EigenValImL0g0010101020)
#MaxEigenValImL0g000_11020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g000_11030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g000_11030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g000_11030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g000_11030[3] = np.max(EigenValImL0g0010101030)
#MaxEigenValImL0g000_11030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g000_11040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g000_11040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g000_11040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g000_11040[3] = np.max(EigenValImL0g0010101040)
#MaxEigenValImL0g000_11040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g000_11050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g000_11050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g000_11050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g000_11050[3] = np.max(EigenValImL0g0010101050)
#MaxEigenValImL0g000_11050[4] = np.max(EigenValImL0g0010201050)

MaxEigenValImL0g000_11Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_11010[0],MaxEigenValImL0g000_11020[0],MaxEigenValImL0g000_11030[0],MaxEigenValImL0g000_11040[0],MaxEigenValImL0g000_11050[0]], 1)[[1]]
MaxEigenValImL0g000_11Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_11010[1],MaxEigenValImL0g000_11020[1],MaxEigenValImL0g000_11030[1],MaxEigenValImL0g000_11040[1],MaxEigenValImL0g000_11050[1]], 1)[[1]]
MaxEigenValImL0g000_11Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_11010[2],MaxEigenValImL0g000_11020[2],MaxEigenValImL0g000_11030[2],MaxEigenValImL0g000_11040[2],MaxEigenValImL0g000_11050[2]], 1)[[1]]
MaxEigenValImL0g000_11Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_11010[3],MaxEigenValImL0g000_11020[3],MaxEigenValImL0g000_11030[3],MaxEigenValImL0g000_11040[3],MaxEigenValImL0g000_11050[3]], 1)[[1]]
#MaxEigenValImL0g000_11Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_11010[4],MaxEigenValImL0g000_11020[4],MaxEigenValImL0g000_11030[4],MaxEigenValImL0g000_11040[4],MaxEigenValImL0g000_11050[4]], 1)[[1]]

########################################################################

dataL0g0010011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK001/N040/HamVals.txt')

MomentumAxL0g0010011010 = dataL0g0010011010[:,][:,5*0+0]
KineticEneL0g0010011010 = dataL0g0010011010[:,][:,5*0+1]
SelfEnergyL0g0010011010 = dataL0g0010011010[:,][:,5*0+2]
EigenValReL0g0010011010 = dataL0g0010011010[:,][:,5*0+3]
EigenValImL0g0010011010 = dataL0g0010011010[:,][:,5*0+4]

dataL0g0010011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK001/N050/HamVals.txt')

MomentumAxL0g0010011020 = dataL0g0010011020[:,][:,5*0+0]
KineticEneL0g0010011020 = dataL0g0010011020[:,][:,5*0+1]
SelfEnergyL0g0010011020 = dataL0g0010011020[:,][:,5*0+2]
EigenValReL0g0010011020 = dataL0g0010011020[:,][:,5*0+3]
EigenValImL0g0010011020 = dataL0g0010011020[:,][:,5*0+4]

dataL0g0010011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK001/N060/HamVals.txt')

MomentumAxL0g0010011030 = dataL0g0010011030[:,][:,5*0+0]
KineticEneL0g0010011030 = dataL0g0010011030[:,][:,5*0+1]
SelfEnergyL0g0010011030 = dataL0g0010011030[:,][:,5*0+2]
EigenValReL0g0010011030 = dataL0g0010011030[:,][:,5*0+3]
EigenValImL0g0010011030 = dataL0g0010011030[:,][:,5*0+4]

dataL0g0010011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK001/N070/HamVals.txt')

MomentumAxL0g0010011040 = dataL0g0010011040[:,][:,5*0+0]
KineticEneL0g0010011040 = dataL0g0010011040[:,][:,5*0+1]
SelfEnergyL0g0010011040 = dataL0g0010011040[:,][:,5*0+2]
EigenValReL0g0010011040 = dataL0g0010011040[:,][:,5*0+3]
EigenValImL0g0010011040 = dataL0g0010011040[:,][:,5*0+4]

dataL0g0010011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK001/N080/HamVals.txt')

MomentumAxL0g0010011050 = dataL0g0010011050[:,][:,5*0+0]
KineticEneL0g0010011050 = dataL0g0010011050[:,][:,5*0+1]
SelfEnergyL0g0010011050 = dataL0g0010011050[:,][:,5*0+2]
EigenValReL0g0010011050 = dataL0g0010011050[:,][:,5*0+3]
EigenValImL0g0010011050 = dataL0g0010011050[:,][:,5*0+4]

dataL0g0010021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK002/N040/HamVals.txt')

MomentumAxL0g0010021010 = dataL0g0010021010[:,][:,5*0+0]
KineticEneL0g0010021010 = dataL0g0010021010[:,][:,5*0+1]
SelfEnergyL0g0010021010 = dataL0g0010021010[:,][:,5*0+2]
EigenValReL0g0010021010 = dataL0g0010021010[:,][:,5*0+3]
EigenValImL0g0010021010 = dataL0g0010021010[:,][:,5*0+4]

dataL0g0010021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK002/N050/HamVals.txt')

MomentumAxL0g0010021020 = dataL0g0010021020[:,][:,5*0+0]
KineticEneL0g0010021020 = dataL0g0010021020[:,][:,5*0+1]
SelfEnergyL0g0010021020 = dataL0g0010021020[:,][:,5*0+2]
EigenValReL0g0010021020 = dataL0g0010021020[:,][:,5*0+3]
EigenValImL0g0010021020 = dataL0g0010021020[:,][:,5*0+4]

dataL0g0010021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK002/N060/HamVals.txt')

MomentumAxL0g0010021030 = dataL0g0010021030[:,][:,5*0+0]
KineticEneL0g0010021030 = dataL0g0010021030[:,][:,5*0+1]
SelfEnergyL0g0010021030 = dataL0g0010021030[:,][:,5*0+2]
EigenValReL0g0010021030 = dataL0g0010021030[:,][:,5*0+3]
EigenValImL0g0010021030 = dataL0g0010021030[:,][:,5*0+4]

dataL0g0010021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK002/N070/HamVals.txt')

MomentumAxL0g0010021040 = dataL0g0010021040[:,][:,5*0+0]
KineticEneL0g0010021040 = dataL0g0010021040[:,][:,5*0+1]
SelfEnergyL0g0010021040 = dataL0g0010021040[:,][:,5*0+2]
EigenValReL0g0010021040 = dataL0g0010021040[:,][:,5*0+3]
EigenValImL0g0010021040 = dataL0g0010021040[:,][:,5*0+4]

dataL0g0010021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK002/N080/HamVals.txt')

MomentumAxL0g0010021050 = dataL0g0010021050[:,][:,5*0+0]
KineticEneL0g0010021050 = dataL0g0010021050[:,][:,5*0+1]
SelfEnergyL0g0010021050 = dataL0g0010021050[:,][:,5*0+2]
EigenValReL0g0010021050 = dataL0g0010021050[:,][:,5*0+3]
EigenValImL0g0010021050 = dataL0g0010021050[:,][:,5*0+4]

dataL0g0010051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK005/N040/HamVals.txt')

MomentumAxL0g0010051010 = dataL0g0010051010[:,][:,5*0+0]
KineticEneL0g0010051010 = dataL0g0010051010[:,][:,5*0+1]
SelfEnergyL0g0010051010 = dataL0g0010051010[:,][:,5*0+2]
EigenValReL0g0010051010 = dataL0g0010051010[:,][:,5*0+3]
EigenValImL0g0010051010 = dataL0g0010051010[:,][:,5*0+4]

dataL0g0010051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK005/N050/HamVals.txt')

MomentumAxL0g0010051020 = dataL0g0010051020[:,][:,5*0+0]
KineticEneL0g0010051020 = dataL0g0010051020[:,][:,5*0+1]
SelfEnergyL0g0010051020 = dataL0g0010051020[:,][:,5*0+2]
EigenValReL0g0010051020 = dataL0g0010051020[:,][:,5*0+3]
EigenValImL0g0010051020 = dataL0g0010051020[:,][:,5*0+4]

dataL0g0010051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK005/N060/HamVals.txt')

MomentumAxL0g0010051030 = dataL0g0010051030[:,][:,5*0+0]
KineticEneL0g0010051030 = dataL0g0010051030[:,][:,5*0+1]
SelfEnergyL0g0010051030 = dataL0g0010051030[:,][:,5*0+2]
EigenValReL0g0010051030 = dataL0g0010051030[:,][:,5*0+3]
EigenValImL0g0010051030 = dataL0g0010051030[:,][:,5*0+4]

dataL0g0010051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK005/N070/HamVals.txt')

MomentumAxL0g0010051040 = dataL0g0010051040[:,][:,5*0+0]
KineticEneL0g0010051040 = dataL0g0010051040[:,][:,5*0+1]
SelfEnergyL0g0010051040 = dataL0g0010051040[:,][:,5*0+2]
EigenValReL0g0010051040 = dataL0g0010051040[:,][:,5*0+3]
EigenValImL0g0010051040 = dataL0g0010051040[:,][:,5*0+4]

dataL0g0010051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK005/N080/HamVals.txt')

MomentumAxL0g0010051050 = dataL0g0010051050[:,][:,5*0+0]
KineticEneL0g0010051050 = dataL0g0010051050[:,][:,5*0+1]
SelfEnergyL0g0010051050 = dataL0g0010051050[:,][:,5*0+2]
EigenValReL0g0010051050 = dataL0g0010051050[:,][:,5*0+3]
EigenValImL0g0010051050 = dataL0g0010051050[:,][:,5*0+4]

dataL0g0010101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK010/N040/HamVals.txt')

MomentumAxL0g0010101010 = dataL0g0010101010[:,][:,5*0+0]
KineticEneL0g0010101010 = dataL0g0010101010[:,][:,5*0+1]
SelfEnergyL0g0010101010 = dataL0g0010101010[:,][:,5*0+2]
EigenValReL0g0010101010 = dataL0g0010101010[:,][:,5*0+3]
EigenValImL0g0010101010 = dataL0g0010101010[:,][:,5*0+4]

dataL0g0010101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK010/N050/HamVals.txt')

MomentumAxL0g0010101020 = dataL0g0010101020[:,][:,5*0+0]
KineticEneL0g0010101020 = dataL0g0010101020[:,][:,5*0+1]
SelfEnergyL0g0010101020 = dataL0g0010101020[:,][:,5*0+2]
EigenValReL0g0010101020 = dataL0g0010101020[:,][:,5*0+3]
EigenValImL0g0010101020 = dataL0g0010101020[:,][:,5*0+4]

dataL0g0010101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK010/N060/HamVals.txt')

MomentumAxL0g0010101030 = dataL0g0010101030[:,][:,5*0+0]
KineticEneL0g0010101030 = dataL0g0010101030[:,][:,5*0+1]
SelfEnergyL0g0010101030 = dataL0g0010101030[:,][:,5*0+2]
EigenValReL0g0010101030 = dataL0g0010101030[:,][:,5*0+3]
EigenValImL0g0010101030 = dataL0g0010101030[:,][:,5*0+4]

dataL0g0010101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK010/N070/HamVals.txt')

MomentumAxL0g0010101040 = dataL0g0010101040[:,][:,5*0+0]
KineticEneL0g0010101040 = dataL0g0010101040[:,][:,5*0+1]
SelfEnergyL0g0010101040 = dataL0g0010101040[:,][:,5*0+2]
EigenValReL0g0010101040 = dataL0g0010101040[:,][:,5*0+3]
EigenValImL0g0010101040 = dataL0g0010101040[:,][:,5*0+4]

dataL0g0010101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK010/N080/HamVals.txt')

MomentumAxL0g0010101050 = dataL0g0010101050[:,][:,5*0+0]
KineticEneL0g0010101050 = dataL0g0010101050[:,][:,5*0+1]
SelfEnergyL0g0010101050 = dataL0g0010101050[:,][:,5*0+2]
EigenValReL0g0010101050 = dataL0g0010101050[:,][:,5*0+3]
EigenValImL0g0010101050 = dataL0g0010101050[:,][:,5*0+4]
"""
dataL0g0010201010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK020/N010/HamVals.txt')

MomentumAxL0g0010201010 = dataL0g0010201010[:,][:,5*0+0]
KineticEneL0g0010201010 = dataL0g0010201010[:,][:,5*0+1]
SelfEnergyL0g0010201010 = dataL0g0010201010[:,][:,5*0+2]
EigenValReL0g0010201010 = dataL0g0010201010[:,][:,5*0+3]
EigenValImL0g0010201010 = dataL0g0010201010[:,][:,5*0+4]

dataL0g0010201020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK020/N020/HamVals.txt')

MomentumAxL0g0010201020 = dataL0g0010201020[:,][:,5*0+0]
KineticEneL0g0010201020 = dataL0g0010201020[:,][:,5*0+1]
SelfEnergyL0g0010201020 = dataL0g0010201020[:,][:,5*0+2]
EigenValReL0g0010201020 = dataL0g0010201020[:,][:,5*0+3]
EigenValImL0g0010201020 = dataL0g0010201020[:,][:,5*0+4]

dataL0g0010201030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK020/N030/HamVals.txt')

MomentumAxL0g0010201030 = dataL0g0010201030[:,][:,5*0+0]
KineticEneL0g0010201030 = dataL0g0010201030[:,][:,5*0+1]
SelfEnergyL0g0010201030 = dataL0g0010201030[:,][:,5*0+2]
EigenValReL0g0010201030 = dataL0g0010201030[:,][:,5*0+3]
EigenValImL0g0010201030 = dataL0g0010201030[:,][:,5*0+4]

dataL0g0010201040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK020/N040/HamVals.txt')

MomentumAxL0g0010201040 = dataL0g0010201040[:,][:,5*0+0]
KineticEneL0g0010201040 = dataL0g0010201040[:,][:,5*0+1]
SelfEnergyL0g0010201040 = dataL0g0010201040[:,][:,5*0+2]
EigenValReL0g0010201040 = dataL0g0010201040[:,][:,5*0+3]
EigenValImL0g0010201040 = dataL0g0010201040[:,][:,5*0+4]

dataL0g0010201050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-20/aK020/N050/HamVals.txt')

MomentumAxL0g0010201050 = dataL0g0010201050[:,][:,5*0+0]
KineticEneL0g0010201050 = dataL0g0010201050[:,][:,5*0+1]
SelfEnergyL0g0010201050 = dataL0g0010201050[:,][:,5*0+2]
EigenValReL0g0010201050 = dataL0g0010201050[:,][:,5*0+3]
EigenValImL0g0010201050 = dataL0g0010201050[:,][:,5*0+4]
"""
MaxEigenValImL0g000_21010 = np.zeros((4))
MaxEigenValImL0g000_21020 = np.zeros((4))
MaxEigenValImL0g000_21030 = np.zeros((4))
MaxEigenValImL0g000_21040 = np.zeros((4))
MaxEigenValImL0g000_21050 = np.zeros((4))
MaxEigenValImL0g000_21Inf = np.zeros((4))

MaxEigenValImL0g000_21010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g000_21010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g000_21010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g000_21010[3] = np.max(EigenValImL0g0010101010)
#MaxEigenValImL0g000_21010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g000_21020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g000_21020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g000_21020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g000_21020[3] = np.max(EigenValImL0g0010101020)
#MaxEigenValImL0g000_21020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g000_21030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g000_21030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g000_21030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g000_21030[3] = np.max(EigenValImL0g0010101030)
#MaxEigenValImL0g000_21030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g000_21040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g000_21040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g000_21040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g000_21040[3] = np.max(EigenValImL0g0010101040)
#MaxEigenValImL0g000_21040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g000_21050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g000_21050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g000_21050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g000_21050[3] = np.max(EigenValImL0g0010101050)
#MaxEigenValImL0g000_21050[4] = np.max(EigenValImL0g0010201050)

fiveSizesA = [1./40,1./50,1./60,1./70,1./80]

MaxEigenValImL0g000_21Inf[0] = np.polyfit(fiveSizesA, [MaxEigenValImL0g000_21010[0],MaxEigenValImL0g000_21020[0],MaxEigenValImL0g000_21030[0],MaxEigenValImL0g000_21040[0],MaxEigenValImL0g000_21050[0]], 1)[[1]]
MaxEigenValImL0g000_21Inf[1] = np.polyfit(fiveSizesA, [MaxEigenValImL0g000_21010[1],MaxEigenValImL0g000_21020[1],MaxEigenValImL0g000_21030[1],MaxEigenValImL0g000_21040[1],MaxEigenValImL0g000_21050[1]], 1)[[1]]
MaxEigenValImL0g000_21Inf[2] = np.polyfit(fiveSizesA, [MaxEigenValImL0g000_21010[2],MaxEigenValImL0g000_21020[2],MaxEigenValImL0g000_21030[2],MaxEigenValImL0g000_21040[2],MaxEigenValImL0g000_21050[2]], 1)[[1]]
MaxEigenValImL0g000_21Inf[3] = np.polyfit(fiveSizesA, [MaxEigenValImL0g000_21010[3],MaxEigenValImL0g000_21020[3],MaxEigenValImL0g000_21030[3],MaxEigenValImL0g000_21040[3],MaxEigenValImL0g000_21050[3]], 1)[[1]]
#MaxEigenValImL0g000_21Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_21010[4],MaxEigenValImL0g000_21020[4],MaxEigenValImL0g000_21030[4],MaxEigenValImL0g000_21040[4],MaxEigenValImL0g000_21050[4]], 1)[[1]]

########################################################################

dataL0g0010011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK001/N010/HamVals.txt')

MomentumAxL0g0010011010 = dataL0g0010011010[:,][:,5*0+0]
KineticEneL0g0010011010 = dataL0g0010011010[:,][:,5*0+1]
SelfEnergyL0g0010011010 = dataL0g0010011010[:,][:,5*0+2]
EigenValReL0g0010011010 = dataL0g0010011010[:,][:,5*0+3]
EigenValImL0g0010011010 = dataL0g0010011010[:,][:,5*0+4]

dataL0g0010011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK001/N020/HamVals.txt')

MomentumAxL0g0010011020 = dataL0g0010011020[:,][:,5*0+0]
KineticEneL0g0010011020 = dataL0g0010011020[:,][:,5*0+1]
SelfEnergyL0g0010011020 = dataL0g0010011020[:,][:,5*0+2]
EigenValReL0g0010011020 = dataL0g0010011020[:,][:,5*0+3]
EigenValImL0g0010011020 = dataL0g0010011020[:,][:,5*0+4]

dataL0g0010011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK001/N030/HamVals.txt')

MomentumAxL0g0010011030 = dataL0g0010011030[:,][:,5*0+0]
KineticEneL0g0010011030 = dataL0g0010011030[:,][:,5*0+1]
SelfEnergyL0g0010011030 = dataL0g0010011030[:,][:,5*0+2]
EigenValReL0g0010011030 = dataL0g0010011030[:,][:,5*0+3]
EigenValImL0g0010011030 = dataL0g0010011030[:,][:,5*0+4]

dataL0g0010011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK001/N040/HamVals.txt')

MomentumAxL0g0010011040 = dataL0g0010011040[:,][:,5*0+0]
KineticEneL0g0010011040 = dataL0g0010011040[:,][:,5*0+1]
SelfEnergyL0g0010011040 = dataL0g0010011040[:,][:,5*0+2]
EigenValReL0g0010011040 = dataL0g0010011040[:,][:,5*0+3]
EigenValImL0g0010011040 = dataL0g0010011040[:,][:,5*0+4]

dataL0g0010011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK001/N050/HamVals.txt')

MomentumAxL0g0010011050 = dataL0g0010011050[:,][:,5*0+0]
KineticEneL0g0010011050 = dataL0g0010011050[:,][:,5*0+1]
SelfEnergyL0g0010011050 = dataL0g0010011050[:,][:,5*0+2]
EigenValReL0g0010011050 = dataL0g0010011050[:,][:,5*0+3]
EigenValImL0g0010011050 = dataL0g0010011050[:,][:,5*0+4]

dataL0g0010021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK002/N010/HamVals.txt')

MomentumAxL0g0010021010 = dataL0g0010021010[:,][:,5*0+0]
KineticEneL0g0010021010 = dataL0g0010021010[:,][:,5*0+1]
SelfEnergyL0g0010021010 = dataL0g0010021010[:,][:,5*0+2]
EigenValReL0g0010021010 = dataL0g0010021010[:,][:,5*0+3]
EigenValImL0g0010021010 = dataL0g0010021010[:,][:,5*0+4]

dataL0g0010021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK002/N020/HamVals.txt')

MomentumAxL0g0010021020 = dataL0g0010021020[:,][:,5*0+0]
KineticEneL0g0010021020 = dataL0g0010021020[:,][:,5*0+1]
SelfEnergyL0g0010021020 = dataL0g0010021020[:,][:,5*0+2]
EigenValReL0g0010021020 = dataL0g0010021020[:,][:,5*0+3]
EigenValImL0g0010021020 = dataL0g0010021020[:,][:,5*0+4]

dataL0g0010021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK002/N030/HamVals.txt')

MomentumAxL0g0010021030 = dataL0g0010021030[:,][:,5*0+0]
KineticEneL0g0010021030 = dataL0g0010021030[:,][:,5*0+1]
SelfEnergyL0g0010021030 = dataL0g0010021030[:,][:,5*0+2]
EigenValReL0g0010021030 = dataL0g0010021030[:,][:,5*0+3]
EigenValImL0g0010021030 = dataL0g0010021030[:,][:,5*0+4]

dataL0g0010021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK002/N040/HamVals.txt')

MomentumAxL0g0010021040 = dataL0g0010021040[:,][:,5*0+0]
KineticEneL0g0010021040 = dataL0g0010021040[:,][:,5*0+1]
SelfEnergyL0g0010021040 = dataL0g0010021040[:,][:,5*0+2]
EigenValReL0g0010021040 = dataL0g0010021040[:,][:,5*0+3]
EigenValImL0g0010021040 = dataL0g0010021040[:,][:,5*0+4]

dataL0g0010021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK002/N050/HamVals.txt')

MomentumAxL0g0010021050 = dataL0g0010021050[:,][:,5*0+0]
KineticEneL0g0010021050 = dataL0g0010021050[:,][:,5*0+1]
SelfEnergyL0g0010021050 = dataL0g0010021050[:,][:,5*0+2]
EigenValReL0g0010021050 = dataL0g0010021050[:,][:,5*0+3]
EigenValImL0g0010021050 = dataL0g0010021050[:,][:,5*0+4]

dataL0g0010051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK005/N010/HamVals.txt')

MomentumAxL0g0010051010 = dataL0g0010051010[:,][:,5*0+0]
KineticEneL0g0010051010 = dataL0g0010051010[:,][:,5*0+1]
SelfEnergyL0g0010051010 = dataL0g0010051010[:,][:,5*0+2]
EigenValReL0g0010051010 = dataL0g0010051010[:,][:,5*0+3]
EigenValImL0g0010051010 = dataL0g0010051010[:,][:,5*0+4]

dataL0g0010051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK005/N020/HamVals.txt')

MomentumAxL0g0010051020 = dataL0g0010051020[:,][:,5*0+0]
KineticEneL0g0010051020 = dataL0g0010051020[:,][:,5*0+1]
SelfEnergyL0g0010051020 = dataL0g0010051020[:,][:,5*0+2]
EigenValReL0g0010051020 = dataL0g0010051020[:,][:,5*0+3]
EigenValImL0g0010051020 = dataL0g0010051020[:,][:,5*0+4]

dataL0g0010051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK005/N030/HamVals.txt')

MomentumAxL0g0010051030 = dataL0g0010051030[:,][:,5*0+0]
KineticEneL0g0010051030 = dataL0g0010051030[:,][:,5*0+1]
SelfEnergyL0g0010051030 = dataL0g0010051030[:,][:,5*0+2]
EigenValReL0g0010051030 = dataL0g0010051030[:,][:,5*0+3]
EigenValImL0g0010051030 = dataL0g0010051030[:,][:,5*0+4]

dataL0g0010051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK005/N040/HamVals.txt')

MomentumAxL0g0010051040 = dataL0g0010051040[:,][:,5*0+0]
KineticEneL0g0010051040 = dataL0g0010051040[:,][:,5*0+1]
SelfEnergyL0g0010051040 = dataL0g0010051040[:,][:,5*0+2]
EigenValReL0g0010051040 = dataL0g0010051040[:,][:,5*0+3]
EigenValImL0g0010051040 = dataL0g0010051040[:,][:,5*0+4]

dataL0g0010051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK005/N050/HamVals.txt')

MomentumAxL0g0010051050 = dataL0g0010051050[:,][:,5*0+0]
KineticEneL0g0010051050 = dataL0g0010051050[:,][:,5*0+1]
SelfEnergyL0g0010051050 = dataL0g0010051050[:,][:,5*0+2]
EigenValReL0g0010051050 = dataL0g0010051050[:,][:,5*0+3]
EigenValImL0g0010051050 = dataL0g0010051050[:,][:,5*0+4]

dataL0g0010101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK010/N010/HamVals.txt')

MomentumAxL0g0010101010 = dataL0g0010101010[:,][:,5*0+0]
KineticEneL0g0010101010 = dataL0g0010101010[:,][:,5*0+1]
SelfEnergyL0g0010101010 = dataL0g0010101010[:,][:,5*0+2]
EigenValReL0g0010101010 = dataL0g0010101010[:,][:,5*0+3]
EigenValImL0g0010101010 = dataL0g0010101010[:,][:,5*0+4]

dataL0g0010101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK010/N020/HamVals.txt')

MomentumAxL0g0010101020 = dataL0g0010101020[:,][:,5*0+0]
KineticEneL0g0010101020 = dataL0g0010101020[:,][:,5*0+1]
SelfEnergyL0g0010101020 = dataL0g0010101020[:,][:,5*0+2]
EigenValReL0g0010101020 = dataL0g0010101020[:,][:,5*0+3]
EigenValImL0g0010101020 = dataL0g0010101020[:,][:,5*0+4]

dataL0g0010101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK010/N030/HamVals.txt')

MomentumAxL0g0010101030 = dataL0g0010101030[:,][:,5*0+0]
KineticEneL0g0010101030 = dataL0g0010101030[:,][:,5*0+1]
SelfEnergyL0g0010101030 = dataL0g0010101030[:,][:,5*0+2]
EigenValReL0g0010101030 = dataL0g0010101030[:,][:,5*0+3]
EigenValImL0g0010101030 = dataL0g0010101030[:,][:,5*0+4]

dataL0g0010101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK010/N040/HamVals.txt')

MomentumAxL0g0010101040 = dataL0g0010101040[:,][:,5*0+0]
KineticEneL0g0010101040 = dataL0g0010101040[:,][:,5*0+1]
SelfEnergyL0g0010101040 = dataL0g0010101040[:,][:,5*0+2]
EigenValReL0g0010101040 = dataL0g0010101040[:,][:,5*0+3]
EigenValImL0g0010101040 = dataL0g0010101040[:,][:,5*0+4]

dataL0g0010101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK010/N050/HamVals.txt')

MomentumAxL0g0010101050 = dataL0g0010101050[:,][:,5*0+0]
KineticEneL0g0010101050 = dataL0g0010101050[:,][:,5*0+1]
SelfEnergyL0g0010101050 = dataL0g0010101050[:,][:,5*0+2]
EigenValReL0g0010101050 = dataL0g0010101050[:,][:,5*0+3]
EigenValImL0g0010101050 = dataL0g0010101050[:,][:,5*0+4]
"""
dataL0g0010201010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK020/N010/HamVals.txt')

MomentumAxL0g0010201010 = dataL0g0010201010[:,][:,5*0+0]
KineticEneL0g0010201010 = dataL0g0010201010[:,][:,5*0+1]
SelfEnergyL0g0010201010 = dataL0g0010201010[:,][:,5*0+2]
EigenValReL0g0010201010 = dataL0g0010201010[:,][:,5*0+3]
EigenValImL0g0010201010 = dataL0g0010201010[:,][:,5*0+4]

dataL0g0010201020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK020/N020/HamVals.txt')

MomentumAxL0g0010201020 = dataL0g0010201020[:,][:,5*0+0]
KineticEneL0g0010201020 = dataL0g0010201020[:,][:,5*0+1]
SelfEnergyL0g0010201020 = dataL0g0010201020[:,][:,5*0+2]
EigenValReL0g0010201020 = dataL0g0010201020[:,][:,5*0+3]
EigenValImL0g0010201020 = dataL0g0010201020[:,][:,5*0+4]

dataL0g0010201030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK020/N030/HamVals.txt')

MomentumAxL0g0010201030 = dataL0g0010201030[:,][:,5*0+0]
KineticEneL0g0010201030 = dataL0g0010201030[:,][:,5*0+1]
SelfEnergyL0g0010201030 = dataL0g0010201030[:,][:,5*0+2]
EigenValReL0g0010201030 = dataL0g0010201030[:,][:,5*0+3]
EigenValImL0g0010201030 = dataL0g0010201030[:,][:,5*0+4]

dataL0g0010201040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK020/N040/HamVals.txt')

MomentumAxL0g0010201040 = dataL0g0010201040[:,][:,5*0+0]
KineticEneL0g0010201040 = dataL0g0010201040[:,][:,5*0+1]
SelfEnergyL0g0010201040 = dataL0g0010201040[:,][:,5*0+2]
EigenValReL0g0010201040 = dataL0g0010201040[:,][:,5*0+3]
EigenValImL0g0010201040 = dataL0g0010201040[:,][:,5*0+4]

dataL0g0010201050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-25/aK020/N050/HamVals.txt')

MomentumAxL0g0010201050 = dataL0g0010201050[:,][:,5*0+0]
KineticEneL0g0010201050 = dataL0g0010201050[:,][:,5*0+1]
SelfEnergyL0g0010201050 = dataL0g0010201050[:,][:,5*0+2]
EigenValReL0g0010201050 = dataL0g0010201050[:,][:,5*0+3]
EigenValImL0g0010201050 = dataL0g0010201050[:,][:,5*0+4]
"""
MaxEigenValImL0g000_251010 = np.zeros((4))
MaxEigenValImL0g000_251020 = np.zeros((4))
MaxEigenValImL0g000_251030 = np.zeros((4))
MaxEigenValImL0g000_251040 = np.zeros((4))
MaxEigenValImL0g000_251050 = np.zeros((4))
MaxEigenValImL0g000_251Inf = np.zeros((4))

MaxEigenValImL0g000_251010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g000_251010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g000_251010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g000_251010[3] = np.max(EigenValImL0g0010101010)
#MaxEigenValImL0g000_251010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g000_251020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g000_251020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g000_251020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g000_251020[3] = np.max(EigenValImL0g0010101020)
#MaxEigenValImL0g000_251020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g000_251030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g000_251030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g000_251030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g000_251030[3] = np.max(EigenValImL0g0010101030)
#MaxEigenValImL0g000_251030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g000_251040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g000_251040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g000_251040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g000_251040[3] = np.max(EigenValImL0g0010101040)
#MaxEigenValImL0g000_251040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g000_251050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g000_251050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g000_251050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g000_251050[3] = np.max(EigenValImL0g0010101050)
#MaxEigenValImL0g000_251050[4] = np.max(EigenValImL0g0010201050)

MaxEigenValImL0g000_251Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_251010[0],MaxEigenValImL0g000_251020[0],MaxEigenValImL0g000_251030[0],MaxEigenValImL0g000_251040[0],MaxEigenValImL0g000_251050[0]], 1)[[1]]
MaxEigenValImL0g000_251Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_251010[1],MaxEigenValImL0g000_251020[1],MaxEigenValImL0g000_251030[1],MaxEigenValImL0g000_251040[1],MaxEigenValImL0g000_251050[1]], 1)[[1]]
MaxEigenValImL0g000_251Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_251010[2],MaxEigenValImL0g000_251020[2],MaxEigenValImL0g000_251030[2],MaxEigenValImL0g000_251040[2],MaxEigenValImL0g000_251050[2]], 1)[[1]]
MaxEigenValImL0g000_251Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_251010[3],MaxEigenValImL0g000_251020[3],MaxEigenValImL0g000_251030[3],MaxEigenValImL0g000_251040[3],MaxEigenValImL0g000_251050[3]], 1)[[1]]
#MaxEigenValImL0g000_251Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_251010[4],MaxEigenValImL0g000_251020[4],MaxEigenValImL0g000_251030[4],MaxEigenValImL0g000_251040[4],MaxEigenValImL0g000_251050[4]], 1)[[1]]

########################################################################

dataL0g0010011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK001/N010/HamVals.txt')

MomentumAxL0g0010011010 = dataL0g0010011010[:,][:,5*0+0]
KineticEneL0g0010011010 = dataL0g0010011010[:,][:,5*0+1]
SelfEnergyL0g0010011010 = dataL0g0010011010[:,][:,5*0+2]
EigenValReL0g0010011010 = dataL0g0010011010[:,][:,5*0+3]
EigenValImL0g0010011010 = dataL0g0010011010[:,][:,5*0+4]

dataL0g0010011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK001/N020/HamVals.txt')

MomentumAxL0g0010011020 = dataL0g0010011020[:,][:,5*0+0]
KineticEneL0g0010011020 = dataL0g0010011020[:,][:,5*0+1]
SelfEnergyL0g0010011020 = dataL0g0010011020[:,][:,5*0+2]
EigenValReL0g0010011020 = dataL0g0010011020[:,][:,5*0+3]
EigenValImL0g0010011020 = dataL0g0010011020[:,][:,5*0+4]

dataL0g0010011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK001/N030/HamVals.txt')

MomentumAxL0g0010011030 = dataL0g0010011030[:,][:,5*0+0]
KineticEneL0g0010011030 = dataL0g0010011030[:,][:,5*0+1]
SelfEnergyL0g0010011030 = dataL0g0010011030[:,][:,5*0+2]
EigenValReL0g0010011030 = dataL0g0010011030[:,][:,5*0+3]
EigenValImL0g0010011030 = dataL0g0010011030[:,][:,5*0+4]

dataL0g0010011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK001/N040/HamVals.txt')

MomentumAxL0g0010011040 = dataL0g0010011040[:,][:,5*0+0]
KineticEneL0g0010011040 = dataL0g0010011040[:,][:,5*0+1]
SelfEnergyL0g0010011040 = dataL0g0010011040[:,][:,5*0+2]
EigenValReL0g0010011040 = dataL0g0010011040[:,][:,5*0+3]
EigenValImL0g0010011040 = dataL0g0010011040[:,][:,5*0+4]

dataL0g0010011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK001/N050/HamVals.txt')

MomentumAxL0g0010011050 = dataL0g0010011050[:,][:,5*0+0]
KineticEneL0g0010011050 = dataL0g0010011050[:,][:,5*0+1]
SelfEnergyL0g0010011050 = dataL0g0010011050[:,][:,5*0+2]
EigenValReL0g0010011050 = dataL0g0010011050[:,][:,5*0+3]
EigenValImL0g0010011050 = dataL0g0010011050[:,][:,5*0+4]

dataL0g0010021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK002/N010/HamVals.txt')

MomentumAxL0g0010021010 = dataL0g0010021010[:,][:,5*0+0]
KineticEneL0g0010021010 = dataL0g0010021010[:,][:,5*0+1]
SelfEnergyL0g0010021010 = dataL0g0010021010[:,][:,5*0+2]
EigenValReL0g0010021010 = dataL0g0010021010[:,][:,5*0+3]
EigenValImL0g0010021010 = dataL0g0010021010[:,][:,5*0+4]

dataL0g0010021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK002/N020/HamVals.txt')

MomentumAxL0g0010021020 = dataL0g0010021020[:,][:,5*0+0]
KineticEneL0g0010021020 = dataL0g0010021020[:,][:,5*0+1]
SelfEnergyL0g0010021020 = dataL0g0010021020[:,][:,5*0+2]
EigenValReL0g0010021020 = dataL0g0010021020[:,][:,5*0+3]
EigenValImL0g0010021020 = dataL0g0010021020[:,][:,5*0+4]

dataL0g0010021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK002/N030/HamVals.txt')

MomentumAxL0g0010021030 = dataL0g0010021030[:,][:,5*0+0]
KineticEneL0g0010021030 = dataL0g0010021030[:,][:,5*0+1]
SelfEnergyL0g0010021030 = dataL0g0010021030[:,][:,5*0+2]
EigenValReL0g0010021030 = dataL0g0010021030[:,][:,5*0+3]
EigenValImL0g0010021030 = dataL0g0010021030[:,][:,5*0+4]

dataL0g0010021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK002/N040/HamVals.txt')

MomentumAxL0g0010021040 = dataL0g0010021040[:,][:,5*0+0]
KineticEneL0g0010021040 = dataL0g0010021040[:,][:,5*0+1]
SelfEnergyL0g0010021040 = dataL0g0010021040[:,][:,5*0+2]
EigenValReL0g0010021040 = dataL0g0010021040[:,][:,5*0+3]
EigenValImL0g0010021040 = dataL0g0010021040[:,][:,5*0+4]

dataL0g0010021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK002/N050/HamVals.txt')

MomentumAxL0g0010021050 = dataL0g0010021050[:,][:,5*0+0]
KineticEneL0g0010021050 = dataL0g0010021050[:,][:,5*0+1]
SelfEnergyL0g0010021050 = dataL0g0010021050[:,][:,5*0+2]
EigenValReL0g0010021050 = dataL0g0010021050[:,][:,5*0+3]
EigenValImL0g0010021050 = dataL0g0010021050[:,][:,5*0+4]

dataL0g0010051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK005/N010/HamVals.txt')

MomentumAxL0g0010051010 = dataL0g0010051010[:,][:,5*0+0]
KineticEneL0g0010051010 = dataL0g0010051010[:,][:,5*0+1]
SelfEnergyL0g0010051010 = dataL0g0010051010[:,][:,5*0+2]
EigenValReL0g0010051010 = dataL0g0010051010[:,][:,5*0+3]
EigenValImL0g0010051010 = dataL0g0010051010[:,][:,5*0+4]

dataL0g0010051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK005/N020/HamVals.txt')

MomentumAxL0g0010051020 = dataL0g0010051020[:,][:,5*0+0]
KineticEneL0g0010051020 = dataL0g0010051020[:,][:,5*0+1]
SelfEnergyL0g0010051020 = dataL0g0010051020[:,][:,5*0+2]
EigenValReL0g0010051020 = dataL0g0010051020[:,][:,5*0+3]
EigenValImL0g0010051020 = dataL0g0010051020[:,][:,5*0+4]

dataL0g0010051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK005/N030/HamVals.txt')

MomentumAxL0g0010051030 = dataL0g0010051030[:,][:,5*0+0]
KineticEneL0g0010051030 = dataL0g0010051030[:,][:,5*0+1]
SelfEnergyL0g0010051030 = dataL0g0010051030[:,][:,5*0+2]
EigenValReL0g0010051030 = dataL0g0010051030[:,][:,5*0+3]
EigenValImL0g0010051030 = dataL0g0010051030[:,][:,5*0+4]

dataL0g0010051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK005/N040/HamVals.txt')

MomentumAxL0g0010051040 = dataL0g0010051040[:,][:,5*0+0]
KineticEneL0g0010051040 = dataL0g0010051040[:,][:,5*0+1]
SelfEnergyL0g0010051040 = dataL0g0010051040[:,][:,5*0+2]
EigenValReL0g0010051040 = dataL0g0010051040[:,][:,5*0+3]
EigenValImL0g0010051040 = dataL0g0010051040[:,][:,5*0+4]

dataL0g0010051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK005/N050/HamVals.txt')

MomentumAxL0g0010051050 = dataL0g0010051050[:,][:,5*0+0]
KineticEneL0g0010051050 = dataL0g0010051050[:,][:,5*0+1]
SelfEnergyL0g0010051050 = dataL0g0010051050[:,][:,5*0+2]
EigenValReL0g0010051050 = dataL0g0010051050[:,][:,5*0+3]
EigenValImL0g0010051050 = dataL0g0010051050[:,][:,5*0+4]

dataL0g0010101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK010/N010/HamVals.txt')

MomentumAxL0g0010101010 = dataL0g0010101010[:,][:,5*0+0]
KineticEneL0g0010101010 = dataL0g0010101010[:,][:,5*0+1]
SelfEnergyL0g0010101010 = dataL0g0010101010[:,][:,5*0+2]
EigenValReL0g0010101010 = dataL0g0010101010[:,][:,5*0+3]
EigenValImL0g0010101010 = dataL0g0010101010[:,][:,5*0+4]

dataL0g0010101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK010/N020/HamVals.txt')

MomentumAxL0g0010101020 = dataL0g0010101020[:,][:,5*0+0]
KineticEneL0g0010101020 = dataL0g0010101020[:,][:,5*0+1]
SelfEnergyL0g0010101020 = dataL0g0010101020[:,][:,5*0+2]
EigenValReL0g0010101020 = dataL0g0010101020[:,][:,5*0+3]
EigenValImL0g0010101020 = dataL0g0010101020[:,][:,5*0+4]

dataL0g0010101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK010/N030/HamVals.txt')

MomentumAxL0g0010101030 = dataL0g0010101030[:,][:,5*0+0]
KineticEneL0g0010101030 = dataL0g0010101030[:,][:,5*0+1]
SelfEnergyL0g0010101030 = dataL0g0010101030[:,][:,5*0+2]
EigenValReL0g0010101030 = dataL0g0010101030[:,][:,5*0+3]
EigenValImL0g0010101030 = dataL0g0010101030[:,][:,5*0+4]

dataL0g0010101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK010/N040/HamVals.txt')

MomentumAxL0g0010101040 = dataL0g0010101040[:,][:,5*0+0]
KineticEneL0g0010101040 = dataL0g0010101040[:,][:,5*0+1]
SelfEnergyL0g0010101040 = dataL0g0010101040[:,][:,5*0+2]
EigenValReL0g0010101040 = dataL0g0010101040[:,][:,5*0+3]
EigenValImL0g0010101040 = dataL0g0010101040[:,][:,5*0+4]

dataL0g0010101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK010/N050/HamVals.txt')

MomentumAxL0g0010101050 = dataL0g0010101050[:,][:,5*0+0]
KineticEneL0g0010101050 = dataL0g0010101050[:,][:,5*0+1]
SelfEnergyL0g0010101050 = dataL0g0010101050[:,][:,5*0+2]
EigenValReL0g0010101050 = dataL0g0010101050[:,][:,5*0+3]
EigenValImL0g0010101050 = dataL0g0010101050[:,][:,5*0+4]
"""
dataL0g0010201010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK020/N010/HamVals.txt')

MomentumAxL0g0010201010 = dataL0g0010201010[:,][:,5*0+0]
KineticEneL0g0010201010 = dataL0g0010201010[:,][:,5*0+1]
SelfEnergyL0g0010201010 = dataL0g0010201010[:,][:,5*0+2]
EigenValReL0g0010201010 = dataL0g0010201010[:,][:,5*0+3]
EigenValImL0g0010201010 = dataL0g0010201010[:,][:,5*0+4]

dataL0g0010201020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK020/N020/HamVals.txt')

MomentumAxL0g0010201020 = dataL0g0010201020[:,][:,5*0+0]
KineticEneL0g0010201020 = dataL0g0010201020[:,][:,5*0+1]
SelfEnergyL0g0010201020 = dataL0g0010201020[:,][:,5*0+2]
EigenValReL0g0010201020 = dataL0g0010201020[:,][:,5*0+3]
EigenValImL0g0010201020 = dataL0g0010201020[:,][:,5*0+4]

dataL0g0010201030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK020/N030/HamVals.txt')

MomentumAxL0g0010201030 = dataL0g0010201030[:,][:,5*0+0]
KineticEneL0g0010201030 = dataL0g0010201030[:,][:,5*0+1]
SelfEnergyL0g0010201030 = dataL0g0010201030[:,][:,5*0+2]
EigenValReL0g0010201030 = dataL0g0010201030[:,][:,5*0+3]
EigenValImL0g0010201030 = dataL0g0010201030[:,][:,5*0+4]

dataL0g0010201040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK020/N040/HamVals.txt')

MomentumAxL0g0010201040 = dataL0g0010201040[:,][:,5*0+0]
KineticEneL0g0010201040 = dataL0g0010201040[:,][:,5*0+1]
SelfEnergyL0g0010201040 = dataL0g0010201040[:,][:,5*0+2]
EigenValReL0g0010201040 = dataL0g0010201040[:,][:,5*0+3]
EigenValImL0g0010201040 = dataL0g0010201040[:,][:,5*0+4]

dataL0g0010201050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-30/aK020/N050/HamVals.txt')

MomentumAxL0g0010201050 = dataL0g0010201050[:,][:,5*0+0]
KineticEneL0g0010201050 = dataL0g0010201050[:,][:,5*0+1]
SelfEnergyL0g0010201050 = dataL0g0010201050[:,][:,5*0+2]
EigenValReL0g0010201050 = dataL0g0010201050[:,][:,5*0+3]
EigenValImL0g0010201050 = dataL0g0010201050[:,][:,5*0+4]
"""
MaxEigenValImL0g000_31010 = np.zeros((4))
MaxEigenValImL0g000_31020 = np.zeros((4))
MaxEigenValImL0g000_31030 = np.zeros((4))
MaxEigenValImL0g000_31040 = np.zeros((4))
MaxEigenValImL0g000_31050 = np.zeros((4))
MaxEigenValImL0g000_31Inf = np.zeros((4))

MaxEigenValImL0g000_31010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g000_31010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g000_31010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g000_31010[3] = np.max(EigenValImL0g0010101010)
#MaxEigenValImL0g000_31010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g000_31020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g000_31020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g000_31020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g000_31020[3] = np.max(EigenValImL0g0010101020)
#MaxEigenValImL0g000_31020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g000_31030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g000_31030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g000_31030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g000_31030[3] = np.max(EigenValImL0g0010101030)
#MaxEigenValImL0g000_31030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g000_31040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g000_31040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g000_31040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g000_31040[3] = np.max(EigenValImL0g0010101040)
#MaxEigenValImL0g000_31040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g000_31050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g000_31050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g000_31050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g000_31050[3] = np.max(EigenValImL0g0010101050)
#MaxEigenValImL0g000_31050[4] = np.max(EigenValImL0g0010201050)

MaxEigenValImL0g000_31Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_31010[0],MaxEigenValImL0g000_31020[0],MaxEigenValImL0g000_31030[0],MaxEigenValImL0g000_31040[0],MaxEigenValImL0g000_31050[0]], 1)[[1]]
MaxEigenValImL0g000_31Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_31010[1],MaxEigenValImL0g000_31020[1],MaxEigenValImL0g000_31030[1],MaxEigenValImL0g000_31040[1],MaxEigenValImL0g000_31050[1]], 1)[[1]]
MaxEigenValImL0g000_31Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_31010[2],MaxEigenValImL0g000_31020[2],MaxEigenValImL0g000_31030[2],MaxEigenValImL0g000_31040[2],MaxEigenValImL0g000_31050[2]], 1)[[1]]
MaxEigenValImL0g000_31Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_31010[3],MaxEigenValImL0g000_31020[3],MaxEigenValImL0g000_31030[3],MaxEigenValImL0g000_31040[3],MaxEigenValImL0g000_31050[3]], 1)[[1]]
#MaxEigenValImL0g000_31Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_31010[4],MaxEigenValImL0g000_31020[4],MaxEigenValImL0g000_31030[4],MaxEigenValImL0g000_31040[4],MaxEigenValImL0g000_31050[4]], 1)[[1]]

########################################################################

dataL0g0010011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK001/N010/HamVals.txt')

MomentumAxL0g0010011010 = dataL0g0010011010[:,][:,5*0+0]
KineticEneL0g0010011010 = dataL0g0010011010[:,][:,5*0+1]
SelfEnergyL0g0010011010 = dataL0g0010011010[:,][:,5*0+2]
EigenValReL0g0010011010 = dataL0g0010011010[:,][:,5*0+3]
EigenValImL0g0010011010 = dataL0g0010011010[:,][:,5*0+4]

dataL0g0010011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK001/N020/HamVals.txt')

MomentumAxL0g0010011020 = dataL0g0010011020[:,][:,5*0+0]
KineticEneL0g0010011020 = dataL0g0010011020[:,][:,5*0+1]
SelfEnergyL0g0010011020 = dataL0g0010011020[:,][:,5*0+2]
EigenValReL0g0010011020 = dataL0g0010011020[:,][:,5*0+3]
EigenValImL0g0010011020 = dataL0g0010011020[:,][:,5*0+4]

dataL0g0010011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK001/N030/HamVals.txt')

MomentumAxL0g0010011030 = dataL0g0010011030[:,][:,5*0+0]
KineticEneL0g0010011030 = dataL0g0010011030[:,][:,5*0+1]
SelfEnergyL0g0010011030 = dataL0g0010011030[:,][:,5*0+2]
EigenValReL0g0010011030 = dataL0g0010011030[:,][:,5*0+3]
EigenValImL0g0010011030 = dataL0g0010011030[:,][:,5*0+4]

dataL0g0010011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK001/N040/HamVals.txt')

MomentumAxL0g0010011040 = dataL0g0010011040[:,][:,5*0+0]
KineticEneL0g0010011040 = dataL0g0010011040[:,][:,5*0+1]
SelfEnergyL0g0010011040 = dataL0g0010011040[:,][:,5*0+2]
EigenValReL0g0010011040 = dataL0g0010011040[:,][:,5*0+3]
EigenValImL0g0010011040 = dataL0g0010011040[:,][:,5*0+4]

dataL0g0010011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK001/N050/HamVals.txt')

MomentumAxL0g0010011050 = dataL0g0010011050[:,][:,5*0+0]
KineticEneL0g0010011050 = dataL0g0010011050[:,][:,5*0+1]
SelfEnergyL0g0010011050 = dataL0g0010011050[:,][:,5*0+2]
EigenValReL0g0010011050 = dataL0g0010011050[:,][:,5*0+3]
EigenValImL0g0010011050 = dataL0g0010011050[:,][:,5*0+4]

dataL0g0010021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK002/N010/HamVals.txt')

MomentumAxL0g0010021010 = dataL0g0010021010[:,][:,5*0+0]
KineticEneL0g0010021010 = dataL0g0010021010[:,][:,5*0+1]
SelfEnergyL0g0010021010 = dataL0g0010021010[:,][:,5*0+2]
EigenValReL0g0010021010 = dataL0g0010021010[:,][:,5*0+3]
EigenValImL0g0010021010 = dataL0g0010021010[:,][:,5*0+4]

dataL0g0010021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK002/N020/HamVals.txt')

MomentumAxL0g0010021020 = dataL0g0010021020[:,][:,5*0+0]
KineticEneL0g0010021020 = dataL0g0010021020[:,][:,5*0+1]
SelfEnergyL0g0010021020 = dataL0g0010021020[:,][:,5*0+2]
EigenValReL0g0010021020 = dataL0g0010021020[:,][:,5*0+3]
EigenValImL0g0010021020 = dataL0g0010021020[:,][:,5*0+4]

dataL0g0010021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK002/N030/HamVals.txt')

MomentumAxL0g0010021030 = dataL0g0010021030[:,][:,5*0+0]
KineticEneL0g0010021030 = dataL0g0010021030[:,][:,5*0+1]
SelfEnergyL0g0010021030 = dataL0g0010021030[:,][:,5*0+2]
EigenValReL0g0010021030 = dataL0g0010021030[:,][:,5*0+3]
EigenValImL0g0010021030 = dataL0g0010021030[:,][:,5*0+4]

dataL0g0010021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK002/N040/HamVals.txt')

MomentumAxL0g0010021040 = dataL0g0010021040[:,][:,5*0+0]
KineticEneL0g0010021040 = dataL0g0010021040[:,][:,5*0+1]
SelfEnergyL0g0010021040 = dataL0g0010021040[:,][:,5*0+2]
EigenValReL0g0010021040 = dataL0g0010021040[:,][:,5*0+3]
EigenValImL0g0010021040 = dataL0g0010021040[:,][:,5*0+4]

dataL0g0010021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK002/N050/HamVals.txt')

MomentumAxL0g0010021050 = dataL0g0010021050[:,][:,5*0+0]
KineticEneL0g0010021050 = dataL0g0010021050[:,][:,5*0+1]
SelfEnergyL0g0010021050 = dataL0g0010021050[:,][:,5*0+2]
EigenValReL0g0010021050 = dataL0g0010021050[:,][:,5*0+3]
EigenValImL0g0010021050 = dataL0g0010021050[:,][:,5*0+4]

dataL0g0010051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK005/N010/HamVals.txt')

MomentumAxL0g0010051010 = dataL0g0010051010[:,][:,5*0+0]
KineticEneL0g0010051010 = dataL0g0010051010[:,][:,5*0+1]
SelfEnergyL0g0010051010 = dataL0g0010051010[:,][:,5*0+2]
EigenValReL0g0010051010 = dataL0g0010051010[:,][:,5*0+3]
EigenValImL0g0010051010 = dataL0g0010051010[:,][:,5*0+4]

dataL0g0010051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK005/N020/HamVals.txt')

MomentumAxL0g0010051020 = dataL0g0010051020[:,][:,5*0+0]
KineticEneL0g0010051020 = dataL0g0010051020[:,][:,5*0+1]
SelfEnergyL0g0010051020 = dataL0g0010051020[:,][:,5*0+2]
EigenValReL0g0010051020 = dataL0g0010051020[:,][:,5*0+3]
EigenValImL0g0010051020 = dataL0g0010051020[:,][:,5*0+4]

dataL0g0010051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK005/N030/HamVals.txt')

MomentumAxL0g0010051030 = dataL0g0010051030[:,][:,5*0+0]
KineticEneL0g0010051030 = dataL0g0010051030[:,][:,5*0+1]
SelfEnergyL0g0010051030 = dataL0g0010051030[:,][:,5*0+2]
EigenValReL0g0010051030 = dataL0g0010051030[:,][:,5*0+3]
EigenValImL0g0010051030 = dataL0g0010051030[:,][:,5*0+4]

dataL0g0010051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK005/N040/HamVals.txt')

MomentumAxL0g0010051040 = dataL0g0010051040[:,][:,5*0+0]
KineticEneL0g0010051040 = dataL0g0010051040[:,][:,5*0+1]
SelfEnergyL0g0010051040 = dataL0g0010051040[:,][:,5*0+2]
EigenValReL0g0010051040 = dataL0g0010051040[:,][:,5*0+3]
EigenValImL0g0010051040 = dataL0g0010051040[:,][:,5*0+4]

dataL0g0010051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK005/N050/HamVals.txt')

MomentumAxL0g0010051050 = dataL0g0010051050[:,][:,5*0+0]
KineticEneL0g0010051050 = dataL0g0010051050[:,][:,5*0+1]
SelfEnergyL0g0010051050 = dataL0g0010051050[:,][:,5*0+2]
EigenValReL0g0010051050 = dataL0g0010051050[:,][:,5*0+3]
EigenValImL0g0010051050 = dataL0g0010051050[:,][:,5*0+4]

dataL0g0010101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK010/N010/HamVals.txt')

MomentumAxL0g0010101010 = dataL0g0010101010[:,][:,5*0+0]
KineticEneL0g0010101010 = dataL0g0010101010[:,][:,5*0+1]
SelfEnergyL0g0010101010 = dataL0g0010101010[:,][:,5*0+2]
EigenValReL0g0010101010 = dataL0g0010101010[:,][:,5*0+3]
EigenValImL0g0010101010 = dataL0g0010101010[:,][:,5*0+4]

dataL0g0010101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK010/N020/HamVals.txt')

MomentumAxL0g0010101020 = dataL0g0010101020[:,][:,5*0+0]
KineticEneL0g0010101020 = dataL0g0010101020[:,][:,5*0+1]
SelfEnergyL0g0010101020 = dataL0g0010101020[:,][:,5*0+2]
EigenValReL0g0010101020 = dataL0g0010101020[:,][:,5*0+3]
EigenValImL0g0010101020 = dataL0g0010101020[:,][:,5*0+4]

dataL0g0010101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK010/N030/HamVals.txt')

MomentumAxL0g0010101030 = dataL0g0010101030[:,][:,5*0+0]
KineticEneL0g0010101030 = dataL0g0010101030[:,][:,5*0+1]
SelfEnergyL0g0010101030 = dataL0g0010101030[:,][:,5*0+2]
EigenValReL0g0010101030 = dataL0g0010101030[:,][:,5*0+3]
EigenValImL0g0010101030 = dataL0g0010101030[:,][:,5*0+4]

dataL0g0010101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK010/N040/HamVals.txt')

MomentumAxL0g0010101040 = dataL0g0010101040[:,][:,5*0+0]
KineticEneL0g0010101040 = dataL0g0010101040[:,][:,5*0+1]
SelfEnergyL0g0010101040 = dataL0g0010101040[:,][:,5*0+2]
EigenValReL0g0010101040 = dataL0g0010101040[:,][:,5*0+3]
EigenValImL0g0010101040 = dataL0g0010101040[:,][:,5*0+4]

dataL0g0010101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK010/N050/HamVals.txt')

MomentumAxL0g0010101050 = dataL0g0010101050[:,][:,5*0+0]
KineticEneL0g0010101050 = dataL0g0010101050[:,][:,5*0+1]
SelfEnergyL0g0010101050 = dataL0g0010101050[:,][:,5*0+2]
EigenValReL0g0010101050 = dataL0g0010101050[:,][:,5*0+3]
EigenValImL0g0010101050 = dataL0g0010101050[:,][:,5*0+4]
"""
dataL0g0010201010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK020/N010/HamVals.txt')

MomentumAxL0g0010201010 = dataL0g0010201010[:,][:,5*0+0]
KineticEneL0g0010201010 = dataL0g0010201010[:,][:,5*0+1]
SelfEnergyL0g0010201010 = dataL0g0010201010[:,][:,5*0+2]
EigenValReL0g0010201010 = dataL0g0010201010[:,][:,5*0+3]
EigenValImL0g0010201010 = dataL0g0010201010[:,][:,5*0+4]

dataL0g0010201020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK020/N020/HamVals.txt')

MomentumAxL0g0010201020 = dataL0g0010201020[:,][:,5*0+0]
KineticEneL0g0010201020 = dataL0g0010201020[:,][:,5*0+1]
SelfEnergyL0g0010201020 = dataL0g0010201020[:,][:,5*0+2]
EigenValReL0g0010201020 = dataL0g0010201020[:,][:,5*0+3]
EigenValImL0g0010201020 = dataL0g0010201020[:,][:,5*0+4]

dataL0g0010201030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK020/N030/HamVals.txt')

MomentumAxL0g0010201030 = dataL0g0010201030[:,][:,5*0+0]
KineticEneL0g0010201030 = dataL0g0010201030[:,][:,5*0+1]
SelfEnergyL0g0010201030 = dataL0g0010201030[:,][:,5*0+2]
EigenValReL0g0010201030 = dataL0g0010201030[:,][:,5*0+3]
EigenValImL0g0010201030 = dataL0g0010201030[:,][:,5*0+4]

dataL0g0010201040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK020/N040/HamVals.txt')

MomentumAxL0g0010201040 = dataL0g0010201040[:,][:,5*0+0]
KineticEneL0g0010201040 = dataL0g0010201040[:,][:,5*0+1]
SelfEnergyL0g0010201040 = dataL0g0010201040[:,][:,5*0+2]
EigenValReL0g0010201040 = dataL0g0010201040[:,][:,5*0+3]
EigenValImL0g0010201040 = dataL0g0010201040[:,][:,5*0+4]

dataL0g0010201050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-40/aK020/N050/HamVals.txt')

MomentumAxL0g0010201050 = dataL0g0010201050[:,][:,5*0+0]
KineticEneL0g0010201050 = dataL0g0010201050[:,][:,5*0+1]
SelfEnergyL0g0010201050 = dataL0g0010201050[:,][:,5*0+2]
EigenValReL0g0010201050 = dataL0g0010201050[:,][:,5*0+3]
EigenValImL0g0010201050 = dataL0g0010201050[:,][:,5*0+4]
"""
MaxEigenValImL0g000_41010 = np.zeros((4))
MaxEigenValImL0g000_41020 = np.zeros((4))
MaxEigenValImL0g000_41030 = np.zeros((4))
MaxEigenValImL0g000_41040 = np.zeros((4))
MaxEigenValImL0g000_41050 = np.zeros((4))
MaxEigenValImL0g000_41Inf = np.zeros((4))

MaxEigenValImL0g000_41010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g000_41010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g000_41010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g000_41010[3] = np.max(EigenValImL0g0010101010)
#MaxEigenValImL0g000_41010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g000_41020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g000_41020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g000_41020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g000_41020[3] = np.max(EigenValImL0g0010101020)
#MaxEigenValImL0g000_41020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g000_41030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g000_41030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g000_41030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g000_41030[3] = np.max(EigenValImL0g0010101030)
#MaxEigenValImL0g000_41030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g000_41040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g000_41040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g000_41040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g000_41040[3] = np.max(EigenValImL0g0010101040)
#MaxEigenValImL0g000_41040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g000_41050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g000_41050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g000_41050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g000_41050[3] = np.max(EigenValImL0g0010101050)
#MaxEigenValImL0g000_41050[4] = np.max(EigenValImL0g0010201050)

MaxEigenValImL0g000_41Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_41010[0],MaxEigenValImL0g000_41020[0],MaxEigenValImL0g000_41030[0],MaxEigenValImL0g000_41040[0],MaxEigenValImL0g000_41050[0]], 1)[[1]]
MaxEigenValImL0g000_41Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_41010[1],MaxEigenValImL0g000_41020[1],MaxEigenValImL0g000_41030[1],MaxEigenValImL0g000_41040[1],MaxEigenValImL0g000_41050[1]], 1)[[1]]
MaxEigenValImL0g000_41Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_41010[2],MaxEigenValImL0g000_41020[2],MaxEigenValImL0g000_41030[2],MaxEigenValImL0g000_41040[2],MaxEigenValImL0g000_41050[2]], 1)[[1]]
MaxEigenValImL0g000_41Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_41010[3],MaxEigenValImL0g000_41020[3],MaxEigenValImL0g000_41030[3],MaxEigenValImL0g000_41040[3],MaxEigenValImL0g000_41050[3]], 1)[[1]]
#MaxEigenValImL0g000_41Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_41010[4],MaxEigenValImL0g000_41020[4],MaxEigenValImL0g000_41030[4],MaxEigenValImL0g000_41040[4],MaxEigenValImL0g000_41050[4]], 1)[[1]]

########################################################################

dataL0g0010011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK001/N010/HamVals.txt')

MomentumAxL0g0010011010 = dataL0g0010011010[:,][:,5*0+0]
KineticEneL0g0010011010 = dataL0g0010011010[:,][:,5*0+1]
SelfEnergyL0g0010011010 = dataL0g0010011010[:,][:,5*0+2]
EigenValReL0g0010011010 = dataL0g0010011010[:,][:,5*0+3]
EigenValImL0g0010011010 = dataL0g0010011010[:,][:,5*0+4]

dataL0g0010011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK001/N020/HamVals.txt')

MomentumAxL0g0010011020 = dataL0g0010011020[:,][:,5*0+0]
KineticEneL0g0010011020 = dataL0g0010011020[:,][:,5*0+1]
SelfEnergyL0g0010011020 = dataL0g0010011020[:,][:,5*0+2]
EigenValReL0g0010011020 = dataL0g0010011020[:,][:,5*0+3]
EigenValImL0g0010011020 = dataL0g0010011020[:,][:,5*0+4]

dataL0g0010011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK001/N030/HamVals.txt')

MomentumAxL0g0010011030 = dataL0g0010011030[:,][:,5*0+0]
KineticEneL0g0010011030 = dataL0g0010011030[:,][:,5*0+1]
SelfEnergyL0g0010011030 = dataL0g0010011030[:,][:,5*0+2]
EigenValReL0g0010011030 = dataL0g0010011030[:,][:,5*0+3]
EigenValImL0g0010011030 = dataL0g0010011030[:,][:,5*0+4]

dataL0g0010011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK001/N040/HamVals.txt')

MomentumAxL0g0010011040 = dataL0g0010011040[:,][:,5*0+0]
KineticEneL0g0010011040 = dataL0g0010011040[:,][:,5*0+1]
SelfEnergyL0g0010011040 = dataL0g0010011040[:,][:,5*0+2]
EigenValReL0g0010011040 = dataL0g0010011040[:,][:,5*0+3]
EigenValImL0g0010011040 = dataL0g0010011040[:,][:,5*0+4]

dataL0g0010011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK001/N050/HamVals.txt')

MomentumAxL0g0010011050 = dataL0g0010011050[:,][:,5*0+0]
KineticEneL0g0010011050 = dataL0g0010011050[:,][:,5*0+1]
SelfEnergyL0g0010011050 = dataL0g0010011050[:,][:,5*0+2]
EigenValReL0g0010011050 = dataL0g0010011050[:,][:,5*0+3]
EigenValImL0g0010011050 = dataL0g0010011050[:,][:,5*0+4]

dataL0g0010021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK002/N010/HamVals.txt')

MomentumAxL0g0010021010 = dataL0g0010021010[:,][:,5*0+0]
KineticEneL0g0010021010 = dataL0g0010021010[:,][:,5*0+1]
SelfEnergyL0g0010021010 = dataL0g0010021010[:,][:,5*0+2]
EigenValReL0g0010021010 = dataL0g0010021010[:,][:,5*0+3]
EigenValImL0g0010021010 = dataL0g0010021010[:,][:,5*0+4]

dataL0g0010021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK002/N020/HamVals.txt')

MomentumAxL0g0010021020 = dataL0g0010021020[:,][:,5*0+0]
KineticEneL0g0010021020 = dataL0g0010021020[:,][:,5*0+1]
SelfEnergyL0g0010021020 = dataL0g0010021020[:,][:,5*0+2]
EigenValReL0g0010021020 = dataL0g0010021020[:,][:,5*0+3]
EigenValImL0g0010021020 = dataL0g0010021020[:,][:,5*0+4]

dataL0g0010021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK002/N030/HamVals.txt')

MomentumAxL0g0010021030 = dataL0g0010021030[:,][:,5*0+0]
KineticEneL0g0010021030 = dataL0g0010021030[:,][:,5*0+1]
SelfEnergyL0g0010021030 = dataL0g0010021030[:,][:,5*0+2]
EigenValReL0g0010021030 = dataL0g0010021030[:,][:,5*0+3]
EigenValImL0g0010021030 = dataL0g0010021030[:,][:,5*0+4]

dataL0g0010021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK002/N040/HamVals.txt')

MomentumAxL0g0010021040 = dataL0g0010021040[:,][:,5*0+0]
KineticEneL0g0010021040 = dataL0g0010021040[:,][:,5*0+1]
SelfEnergyL0g0010021040 = dataL0g0010021040[:,][:,5*0+2]
EigenValReL0g0010021040 = dataL0g0010021040[:,][:,5*0+3]
EigenValImL0g0010021040 = dataL0g0010021040[:,][:,5*0+4]

dataL0g0010021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK002/N050/HamVals.txt')

MomentumAxL0g0010021050 = dataL0g0010021050[:,][:,5*0+0]
KineticEneL0g0010021050 = dataL0g0010021050[:,][:,5*0+1]
SelfEnergyL0g0010021050 = dataL0g0010021050[:,][:,5*0+2]
EigenValReL0g0010021050 = dataL0g0010021050[:,][:,5*0+3]
EigenValImL0g0010021050 = dataL0g0010021050[:,][:,5*0+4]

dataL0g0010051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK005/N010/HamVals.txt')

MomentumAxL0g0010051010 = dataL0g0010051010[:,][:,5*0+0]
KineticEneL0g0010051010 = dataL0g0010051010[:,][:,5*0+1]
SelfEnergyL0g0010051010 = dataL0g0010051010[:,][:,5*0+2]
EigenValReL0g0010051010 = dataL0g0010051010[:,][:,5*0+3]
EigenValImL0g0010051010 = dataL0g0010051010[:,][:,5*0+4]

dataL0g0010051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK005/N020/HamVals.txt')

MomentumAxL0g0010051020 = dataL0g0010051020[:,][:,5*0+0]
KineticEneL0g0010051020 = dataL0g0010051020[:,][:,5*0+1]
SelfEnergyL0g0010051020 = dataL0g0010051020[:,][:,5*0+2]
EigenValReL0g0010051020 = dataL0g0010051020[:,][:,5*0+3]
EigenValImL0g0010051020 = dataL0g0010051020[:,][:,5*0+4]

dataL0g0010051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK005/N030/HamVals.txt')

MomentumAxL0g0010051030 = dataL0g0010051030[:,][:,5*0+0]
KineticEneL0g0010051030 = dataL0g0010051030[:,][:,5*0+1]
SelfEnergyL0g0010051030 = dataL0g0010051030[:,][:,5*0+2]
EigenValReL0g0010051030 = dataL0g0010051030[:,][:,5*0+3]
EigenValImL0g0010051030 = dataL0g0010051030[:,][:,5*0+4]

dataL0g0010051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK005/N040/HamVals.txt')

MomentumAxL0g0010051040 = dataL0g0010051040[:,][:,5*0+0]
KineticEneL0g0010051040 = dataL0g0010051040[:,][:,5*0+1]
SelfEnergyL0g0010051040 = dataL0g0010051040[:,][:,5*0+2]
EigenValReL0g0010051040 = dataL0g0010051040[:,][:,5*0+3]
EigenValImL0g0010051040 = dataL0g0010051040[:,][:,5*0+4]

dataL0g0010051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK005/N050/HamVals.txt')

MomentumAxL0g0010051050 = dataL0g0010051050[:,][:,5*0+0]
KineticEneL0g0010051050 = dataL0g0010051050[:,][:,5*0+1]
SelfEnergyL0g0010051050 = dataL0g0010051050[:,][:,5*0+2]
EigenValReL0g0010051050 = dataL0g0010051050[:,][:,5*0+3]
EigenValImL0g0010051050 = dataL0g0010051050[:,][:,5*0+4]

dataL0g0010101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK010/N010/HamVals.txt')

MomentumAxL0g0010101010 = dataL0g0010101010[:,][:,5*0+0]
KineticEneL0g0010101010 = dataL0g0010101010[:,][:,5*0+1]
SelfEnergyL0g0010101010 = dataL0g0010101010[:,][:,5*0+2]
EigenValReL0g0010101010 = dataL0g0010101010[:,][:,5*0+3]
EigenValImL0g0010101010 = dataL0g0010101010[:,][:,5*0+4]

dataL0g0010101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK010/N020/HamVals.txt')

MomentumAxL0g0010101020 = dataL0g0010101020[:,][:,5*0+0]
KineticEneL0g0010101020 = dataL0g0010101020[:,][:,5*0+1]
SelfEnergyL0g0010101020 = dataL0g0010101020[:,][:,5*0+2]
EigenValReL0g0010101020 = dataL0g0010101020[:,][:,5*0+3]
EigenValImL0g0010101020 = dataL0g0010101020[:,][:,5*0+4]

dataL0g0010101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK010/N030/HamVals.txt')

MomentumAxL0g0010101030 = dataL0g0010101030[:,][:,5*0+0]
KineticEneL0g0010101030 = dataL0g0010101030[:,][:,5*0+1]
SelfEnergyL0g0010101030 = dataL0g0010101030[:,][:,5*0+2]
EigenValReL0g0010101030 = dataL0g0010101030[:,][:,5*0+3]
EigenValImL0g0010101030 = dataL0g0010101030[:,][:,5*0+4]

dataL0g0010101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK010/N040/HamVals.txt')

MomentumAxL0g0010101040 = dataL0g0010101040[:,][:,5*0+0]
KineticEneL0g0010101040 = dataL0g0010101040[:,][:,5*0+1]
SelfEnergyL0g0010101040 = dataL0g0010101040[:,][:,5*0+2]
EigenValReL0g0010101040 = dataL0g0010101040[:,][:,5*0+3]
EigenValImL0g0010101040 = dataL0g0010101040[:,][:,5*0+4]

dataL0g0010101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK010/N050/HamVals.txt')

MomentumAxL0g0010101050 = dataL0g0010101050[:,][:,5*0+0]
KineticEneL0g0010101050 = dataL0g0010101050[:,][:,5*0+1]
SelfEnergyL0g0010101050 = dataL0g0010101050[:,][:,5*0+2]
EigenValReL0g0010101050 = dataL0g0010101050[:,][:,5*0+3]
EigenValImL0g0010101050 = dataL0g0010101050[:,][:,5*0+4]
"""
dataL0g0010201010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK020/N010/HamVals.txt')

MomentumAxL0g0010201010 = dataL0g0010201010[:,][:,5*0+0]
KineticEneL0g0010201010 = dataL0g0010201010[:,][:,5*0+1]
SelfEnergyL0g0010201010 = dataL0g0010201010[:,][:,5*0+2]
EigenValReL0g0010201010 = dataL0g0010201010[:,][:,5*0+3]
EigenValImL0g0010201010 = dataL0g0010201010[:,][:,5*0+4]

dataL0g0010201020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK020/N020/HamVals.txt')

MomentumAxL0g0010201020 = dataL0g0010201020[:,][:,5*0+0]
KineticEneL0g0010201020 = dataL0g0010201020[:,][:,5*0+1]
SelfEnergyL0g0010201020 = dataL0g0010201020[:,][:,5*0+2]
EigenValReL0g0010201020 = dataL0g0010201020[:,][:,5*0+3]
EigenValImL0g0010201020 = dataL0g0010201020[:,][:,5*0+4]

dataL0g0010201030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK020/N030/HamVals.txt')

MomentumAxL0g0010201030 = dataL0g0010201030[:,][:,5*0+0]
KineticEneL0g0010201030 = dataL0g0010201030[:,][:,5*0+1]
SelfEnergyL0g0010201030 = dataL0g0010201030[:,][:,5*0+2]
EigenValReL0g0010201030 = dataL0g0010201030[:,][:,5*0+3]
EigenValImL0g0010201030 = dataL0g0010201030[:,][:,5*0+4]

dataL0g0010201040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK020/N040/HamVals.txt')

MomentumAxL0g0010201040 = dataL0g0010201040[:,][:,5*0+0]
KineticEneL0g0010201040 = dataL0g0010201040[:,][:,5*0+1]
SelfEnergyL0g0010201040 = dataL0g0010201040[:,][:,5*0+2]
EigenValReL0g0010201040 = dataL0g0010201040[:,][:,5*0+3]
EigenValImL0g0010201040 = dataL0g0010201040[:,][:,5*0+4]

dataL0g0010201050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK000-50/aK020/N050/HamVals.txt')

MomentumAxL0g0010201050 = dataL0g0010201050[:,][:,5*0+0]
KineticEneL0g0010201050 = dataL0g0010201050[:,][:,5*0+1]
SelfEnergyL0g0010201050 = dataL0g0010201050[:,][:,5*0+2]
EigenValReL0g0010201050 = dataL0g0010201050[:,][:,5*0+3]
EigenValImL0g0010201050 = dataL0g0010201050[:,][:,5*0+4]
"""
MaxEigenValImL0g000_51010 = np.zeros((4))
MaxEigenValImL0g000_51020 = np.zeros((4))
MaxEigenValImL0g000_51030 = np.zeros((4))
MaxEigenValImL0g000_51040 = np.zeros((4))
MaxEigenValImL0g000_51050 = np.zeros((4))
MaxEigenValImL0g000_51Inf = np.zeros((4))

MaxEigenValImL0g000_51010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g000_51010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g000_51010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g000_51010[3] = np.max(EigenValImL0g0010101010)
#MaxEigenValImL0g000_51010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g000_51020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g000_51020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g000_51020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g000_51020[3] = np.max(EigenValImL0g0010101020)
#MaxEigenValImL0g000_51020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g000_51030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g000_51030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g000_51030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g000_51030[3] = np.max(EigenValImL0g0010101030)
#MaxEigenValImL0g000_51030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g000_51040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g000_51040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g000_51040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g000_51040[3] = np.max(EigenValImL0g0010101040)
#MaxEigenValImL0g000_51040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g000_51050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g000_51050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g000_51050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g000_51050[3] = np.max(EigenValImL0g0010101050)
#MaxEigenValImL0g000_51050[4] = np.max(EigenValImL0g0010201050)

MaxEigenValImL0g000_51Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_51010[0],MaxEigenValImL0g000_51020[0],MaxEigenValImL0g000_51030[0],MaxEigenValImL0g000_51040[0],MaxEigenValImL0g000_51050[0]], 1)[[1]]
MaxEigenValImL0g000_51Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_51010[1],MaxEigenValImL0g000_51020[1],MaxEigenValImL0g000_51030[1],MaxEigenValImL0g000_51040[1],MaxEigenValImL0g000_51050[1]], 1)[[1]]
MaxEigenValImL0g000_51Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_51010[2],MaxEigenValImL0g000_51020[2],MaxEigenValImL0g000_51030[2],MaxEigenValImL0g000_51040[2],MaxEigenValImL0g000_51050[2]], 1)[[1]]
MaxEigenValImL0g000_51Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_51010[3],MaxEigenValImL0g000_51020[3],MaxEigenValImL0g000_51030[3],MaxEigenValImL0g000_51040[3],MaxEigenValImL0g000_51050[3]], 1)[[1]]
#MaxEigenValImL0g000_51Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g000_51010[4],MaxEigenValImL0g000_51020[4],MaxEigenValImL0g000_51030[4],MaxEigenValImL0g000_51040[4],MaxEigenValImL0g000_51050[4]], 1)[[1]]

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
"""
dataL0g0010201010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK020/N010/HamVals.txt')

MomentumAxL0g0010201010 = dataL0g0010201010[:,][:,5*0+0]
KineticEneL0g0010201010 = dataL0g0010201010[:,][:,5*0+1]
SelfEnergyL0g0010201010 = dataL0g0010201010[:,][:,5*0+2]
EigenValReL0g0010201010 = dataL0g0010201010[:,][:,5*0+3]
EigenValImL0g0010201010 = dataL0g0010201010[:,][:,5*0+4]

dataL0g0010201020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK020/N020/HamVals.txt')

MomentumAxL0g0010201020 = dataL0g0010201020[:,][:,5*0+0]
KineticEneL0g0010201020 = dataL0g0010201020[:,][:,5*0+1]
SelfEnergyL0g0010201020 = dataL0g0010201020[:,][:,5*0+2]
EigenValReL0g0010201020 = dataL0g0010201020[:,][:,5*0+3]
EigenValImL0g0010201020 = dataL0g0010201020[:,][:,5*0+4]

dataL0g0010201030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK020/N030/HamVals.txt')

MomentumAxL0g0010201030 = dataL0g0010201030[:,][:,5*0+0]
KineticEneL0g0010201030 = dataL0g0010201030[:,][:,5*0+1]
SelfEnergyL0g0010201030 = dataL0g0010201030[:,][:,5*0+2]
EigenValReL0g0010201030 = dataL0g0010201030[:,][:,5*0+3]
EigenValImL0g0010201030 = dataL0g0010201030[:,][:,5*0+4]

dataL0g0010201040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK020/N040/HamVals.txt')

MomentumAxL0g0010201040 = dataL0g0010201040[:,][:,5*0+0]
KineticEneL0g0010201040 = dataL0g0010201040[:,][:,5*0+1]
SelfEnergyL0g0010201040 = dataL0g0010201040[:,][:,5*0+2]
EigenValReL0g0010201040 = dataL0g0010201040[:,][:,5*0+3]
EigenValImL0g0010201040 = dataL0g0010201040[:,][:,5*0+4]

dataL0g0010201050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK001/aK020/N050/HamVals.txt')

MomentumAxL0g0010201050 = dataL0g0010201050[:,][:,5*0+0]
KineticEneL0g0010201050 = dataL0g0010201050[:,][:,5*0+1]
SelfEnergyL0g0010201050 = dataL0g0010201050[:,][:,5*0+2]
EigenValReL0g0010201050 = dataL0g0010201050[:,][:,5*0+3]
EigenValImL0g0010201050 = dataL0g0010201050[:,][:,5*0+4]
"""
MaxEigenValImL0g0011010 = np.zeros((4))
MaxEigenValImL0g0011020 = np.zeros((4))
MaxEigenValImL0g0011030 = np.zeros((4))
MaxEigenValImL0g0011040 = np.zeros((4))
MaxEigenValImL0g0011050 = np.zeros((4))
MaxEigenValImL0g0011Inf = np.zeros((4))

MaxEigenValImL0g0011010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g0011010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g0011010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g0011010[3] = np.max(EigenValImL0g0010101010)
#MaxEigenValImL0g0011010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g0011020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g0011020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g0011020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g0011020[3] = np.max(EigenValImL0g0010101020)
#MaxEigenValImL0g0011020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g0011030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g0011030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g0011030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g0011030[3] = np.max(EigenValImL0g0010101030)
#MaxEigenValImL0g0011030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g0011040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g0011040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g0011040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g0011040[3] = np.max(EigenValImL0g0010101040)
#MaxEigenValImL0g0011040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g0011050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g0011050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g0011050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g0011050[3] = np.max(EigenValImL0g0010101050)
#MaxEigenValImL0g0011050[4] = np.max(EigenValImL0g0010201050)

MaxEigenValImL0g0011Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL0g0011010[0],MaxEigenValImL0g0011020[0],MaxEigenValImL0g0011030[0],MaxEigenValImL0g0011040[0],MaxEigenValImL0g0011050[0]], 1)[[1]]
MaxEigenValImL0g0011Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL0g0011010[1],MaxEigenValImL0g0011020[1],MaxEigenValImL0g0011030[1],MaxEigenValImL0g0011040[1],MaxEigenValImL0g0011050[1]], 1)[[1]]
MaxEigenValImL0g0011Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL0g0011010[2],MaxEigenValImL0g0011020[2],MaxEigenValImL0g0011030[2],MaxEigenValImL0g0011040[2],MaxEigenValImL0g0011050[2]], 1)[[1]]
MaxEigenValImL0g0011Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL0g0011010[3],MaxEigenValImL0g0011020[3],MaxEigenValImL0g0011030[3],MaxEigenValImL0g0011040[3],MaxEigenValImL0g0011050[3]], 1)[[1]]
#MaxEigenValImL0g0011Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g0011010[4],MaxEigenValImL0g0011020[4],MaxEigenValImL0g0011030[4],MaxEigenValImL0g0011040[4],MaxEigenValImL0g0011050[4]], 1)[[1]]

########################################################################

dataL0g0010011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK001/N010/HamVals.txt')

MomentumAxL0g0010011010 = dataL0g0010011010[:,][:,5*0+0]
KineticEneL0g0010011010 = dataL0g0010011010[:,][:,5*0+1]
SelfEnergyL0g0010011010 = dataL0g0010011010[:,][:,5*0+2]
EigenValReL0g0010011010 = dataL0g0010011010[:,][:,5*0+3]
EigenValImL0g0010011010 = dataL0g0010011010[:,][:,5*0+4]

dataL0g0010011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK001/N020/HamVals.txt')

MomentumAxL0g0010011020 = dataL0g0010011020[:,][:,5*0+0]
KineticEneL0g0010011020 = dataL0g0010011020[:,][:,5*0+1]
SelfEnergyL0g0010011020 = dataL0g0010011020[:,][:,5*0+2]
EigenValReL0g0010011020 = dataL0g0010011020[:,][:,5*0+3]
EigenValImL0g0010011020 = dataL0g0010011020[:,][:,5*0+4]

dataL0g0010011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK001/N030/HamVals.txt')

MomentumAxL0g0010011030 = dataL0g0010011030[:,][:,5*0+0]
KineticEneL0g0010011030 = dataL0g0010011030[:,][:,5*0+1]
SelfEnergyL0g0010011030 = dataL0g0010011030[:,][:,5*0+2]
EigenValReL0g0010011030 = dataL0g0010011030[:,][:,5*0+3]
EigenValImL0g0010011030 = dataL0g0010011030[:,][:,5*0+4]

dataL0g0010011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK001/N040/HamVals.txt')

MomentumAxL0g0010011040 = dataL0g0010011040[:,][:,5*0+0]
KineticEneL0g0010011040 = dataL0g0010011040[:,][:,5*0+1]
SelfEnergyL0g0010011040 = dataL0g0010011040[:,][:,5*0+2]
EigenValReL0g0010011040 = dataL0g0010011040[:,][:,5*0+3]
EigenValImL0g0010011040 = dataL0g0010011040[:,][:,5*0+4]

dataL0g0010011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK001/N050/HamVals.txt')

MomentumAxL0g0010011050 = dataL0g0010011050[:,][:,5*0+0]
KineticEneL0g0010011050 = dataL0g0010011050[:,][:,5*0+1]
SelfEnergyL0g0010011050 = dataL0g0010011050[:,][:,5*0+2]
EigenValReL0g0010011050 = dataL0g0010011050[:,][:,5*0+3]
EigenValImL0g0010011050 = dataL0g0010011050[:,][:,5*0+4]

dataL0g0010021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK002/N010/HamVals.txt')

MomentumAxL0g0010021010 = dataL0g0010021010[:,][:,5*0+0]
KineticEneL0g0010021010 = dataL0g0010021010[:,][:,5*0+1]
SelfEnergyL0g0010021010 = dataL0g0010021010[:,][:,5*0+2]
EigenValReL0g0010021010 = dataL0g0010021010[:,][:,5*0+3]
EigenValImL0g0010021010 = dataL0g0010021010[:,][:,5*0+4]

dataL0g0010021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK002/N020/HamVals.txt')

MomentumAxL0g0010021020 = dataL0g0010021020[:,][:,5*0+0]
KineticEneL0g0010021020 = dataL0g0010021020[:,][:,5*0+1]
SelfEnergyL0g0010021020 = dataL0g0010021020[:,][:,5*0+2]
EigenValReL0g0010021020 = dataL0g0010021020[:,][:,5*0+3]
EigenValImL0g0010021020 = dataL0g0010021020[:,][:,5*0+4]

dataL0g0010021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK002/N030/HamVals.txt')

MomentumAxL0g0010021030 = dataL0g0010021030[:,][:,5*0+0]
KineticEneL0g0010021030 = dataL0g0010021030[:,][:,5*0+1]
SelfEnergyL0g0010021030 = dataL0g0010021030[:,][:,5*0+2]
EigenValReL0g0010021030 = dataL0g0010021030[:,][:,5*0+3]
EigenValImL0g0010021030 = dataL0g0010021030[:,][:,5*0+4]

dataL0g0010021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK002/N040/HamVals.txt')

MomentumAxL0g0010021040 = dataL0g0010021040[:,][:,5*0+0]
KineticEneL0g0010021040 = dataL0g0010021040[:,][:,5*0+1]
SelfEnergyL0g0010021040 = dataL0g0010021040[:,][:,5*0+2]
EigenValReL0g0010021040 = dataL0g0010021040[:,][:,5*0+3]
EigenValImL0g0010021040 = dataL0g0010021040[:,][:,5*0+4]

dataL0g0010021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK002/N050/HamVals.txt')

MomentumAxL0g0010021050 = dataL0g0010021050[:,][:,5*0+0]
KineticEneL0g0010021050 = dataL0g0010021050[:,][:,5*0+1]
SelfEnergyL0g0010021050 = dataL0g0010021050[:,][:,5*0+2]
EigenValReL0g0010021050 = dataL0g0010021050[:,][:,5*0+3]
EigenValImL0g0010021050 = dataL0g0010021050[:,][:,5*0+4]

dataL0g0010051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK005/N010/HamVals.txt')

MomentumAxL0g0010051010 = dataL0g0010051010[:,][:,5*0+0]
KineticEneL0g0010051010 = dataL0g0010051010[:,][:,5*0+1]
SelfEnergyL0g0010051010 = dataL0g0010051010[:,][:,5*0+2]
EigenValReL0g0010051010 = dataL0g0010051010[:,][:,5*0+3]
EigenValImL0g0010051010 = dataL0g0010051010[:,][:,5*0+4]

dataL0g0010051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK005/N020/HamVals.txt')

MomentumAxL0g0010051020 = dataL0g0010051020[:,][:,5*0+0]
KineticEneL0g0010051020 = dataL0g0010051020[:,][:,5*0+1]
SelfEnergyL0g0010051020 = dataL0g0010051020[:,][:,5*0+2]
EigenValReL0g0010051020 = dataL0g0010051020[:,][:,5*0+3]
EigenValImL0g0010051020 = dataL0g0010051020[:,][:,5*0+4]

dataL0g0010051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK005/N030/HamVals.txt')

MomentumAxL0g0010051030 = dataL0g0010051030[:,][:,5*0+0]
KineticEneL0g0010051030 = dataL0g0010051030[:,][:,5*0+1]
SelfEnergyL0g0010051030 = dataL0g0010051030[:,][:,5*0+2]
EigenValReL0g0010051030 = dataL0g0010051030[:,][:,5*0+3]
EigenValImL0g0010051030 = dataL0g0010051030[:,][:,5*0+4]

dataL0g0010051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK005/N040/HamVals.txt')

MomentumAxL0g0010051040 = dataL0g0010051040[:,][:,5*0+0]
KineticEneL0g0010051040 = dataL0g0010051040[:,][:,5*0+1]
SelfEnergyL0g0010051040 = dataL0g0010051040[:,][:,5*0+2]
EigenValReL0g0010051040 = dataL0g0010051040[:,][:,5*0+3]
EigenValImL0g0010051040 = dataL0g0010051040[:,][:,5*0+4]

dataL0g0010051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK005/N050/HamVals.txt')

MomentumAxL0g0010051050 = dataL0g0010051050[:,][:,5*0+0]
KineticEneL0g0010051050 = dataL0g0010051050[:,][:,5*0+1]
SelfEnergyL0g0010051050 = dataL0g0010051050[:,][:,5*0+2]
EigenValReL0g0010051050 = dataL0g0010051050[:,][:,5*0+3]
EigenValImL0g0010051050 = dataL0g0010051050[:,][:,5*0+4]

dataL0g0010101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK010/N010/HamVals.txt')

MomentumAxL0g0010101010 = dataL0g0010101010[:,][:,5*0+0]
KineticEneL0g0010101010 = dataL0g0010101010[:,][:,5*0+1]
SelfEnergyL0g0010101010 = dataL0g0010101010[:,][:,5*0+2]
EigenValReL0g0010101010 = dataL0g0010101010[:,][:,5*0+3]
EigenValImL0g0010101010 = dataL0g0010101010[:,][:,5*0+4]

dataL0g0010101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK010/N020/HamVals.txt')

MomentumAxL0g0010101020 = dataL0g0010101020[:,][:,5*0+0]
KineticEneL0g0010101020 = dataL0g0010101020[:,][:,5*0+1]
SelfEnergyL0g0010101020 = dataL0g0010101020[:,][:,5*0+2]
EigenValReL0g0010101020 = dataL0g0010101020[:,][:,5*0+3]
EigenValImL0g0010101020 = dataL0g0010101020[:,][:,5*0+4]

dataL0g0010101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK010/N030/HamVals.txt')

MomentumAxL0g0010101030 = dataL0g0010101030[:,][:,5*0+0]
KineticEneL0g0010101030 = dataL0g0010101030[:,][:,5*0+1]
SelfEnergyL0g0010101030 = dataL0g0010101030[:,][:,5*0+2]
EigenValReL0g0010101030 = dataL0g0010101030[:,][:,5*0+3]
EigenValImL0g0010101030 = dataL0g0010101030[:,][:,5*0+4]

dataL0g0010101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK010/N040/HamVals.txt')

MomentumAxL0g0010101040 = dataL0g0010101040[:,][:,5*0+0]
KineticEneL0g0010101040 = dataL0g0010101040[:,][:,5*0+1]
SelfEnergyL0g0010101040 = dataL0g0010101040[:,][:,5*0+2]
EigenValReL0g0010101040 = dataL0g0010101040[:,][:,5*0+3]
EigenValImL0g0010101040 = dataL0g0010101040[:,][:,5*0+4]

dataL0g0010101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK010/N050/HamVals.txt')

MomentumAxL0g0010101050 = dataL0g0010101050[:,][:,5*0+0]
KineticEneL0g0010101050 = dataL0g0010101050[:,][:,5*0+1]
SelfEnergyL0g0010101050 = dataL0g0010101050[:,][:,5*0+2]
EigenValReL0g0010101050 = dataL0g0010101050[:,][:,5*0+3]
EigenValImL0g0010101050 = dataL0g0010101050[:,][:,5*0+4]
"""
dataL0g0010201010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK020/N010/HamVals.txt')

MomentumAxL0g0010201010 = dataL0g0010201010[:,][:,5*0+0]
KineticEneL0g0010201010 = dataL0g0010201010[:,][:,5*0+1]
SelfEnergyL0g0010201010 = dataL0g0010201010[:,][:,5*0+2]
EigenValReL0g0010201010 = dataL0g0010201010[:,][:,5*0+3]
EigenValImL0g0010201010 = dataL0g0010201010[:,][:,5*0+4]

dataL0g0010201020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK020/N020/HamVals.txt')

MomentumAxL0g0010201020 = dataL0g0010201020[:,][:,5*0+0]
KineticEneL0g0010201020 = dataL0g0010201020[:,][:,5*0+1]
SelfEnergyL0g0010201020 = dataL0g0010201020[:,][:,5*0+2]
EigenValReL0g0010201020 = dataL0g0010201020[:,][:,5*0+3]
EigenValImL0g0010201020 = dataL0g0010201020[:,][:,5*0+4]

dataL0g0010201030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK020/N030/HamVals.txt')

MomentumAxL0g0010201030 = dataL0g0010201030[:,][:,5*0+0]
KineticEneL0g0010201030 = dataL0g0010201030[:,][:,5*0+1]
SelfEnergyL0g0010201030 = dataL0g0010201030[:,][:,5*0+2]
EigenValReL0g0010201030 = dataL0g0010201030[:,][:,5*0+3]
EigenValImL0g0010201030 = dataL0g0010201030[:,][:,5*0+4]

dataL0g0010201040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK020/N040/HamVals.txt')

MomentumAxL0g0010201040 = dataL0g0010201040[:,][:,5*0+0]
KineticEneL0g0010201040 = dataL0g0010201040[:,][:,5*0+1]
SelfEnergyL0g0010201040 = dataL0g0010201040[:,][:,5*0+2]
EigenValReL0g0010201040 = dataL0g0010201040[:,][:,5*0+3]
EigenValImL0g0010201040 = dataL0g0010201040[:,][:,5*0+4]

dataL0g0010201050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK002/aK020/N050/HamVals.txt')

MomentumAxL0g0010201050 = dataL0g0010201050[:,][:,5*0+0]
KineticEneL0g0010201050 = dataL0g0010201050[:,][:,5*0+1]
SelfEnergyL0g0010201050 = dataL0g0010201050[:,][:,5*0+2]
EigenValReL0g0010201050 = dataL0g0010201050[:,][:,5*0+3]
EigenValImL0g0010201050 = dataL0g0010201050[:,][:,5*0+4]
"""
MaxEigenValImL0g0021010 = np.zeros((4))
MaxEigenValImL0g0021020 = np.zeros((4))
MaxEigenValImL0g0021030 = np.zeros((4))
MaxEigenValImL0g0021040 = np.zeros((4))
MaxEigenValImL0g0021050 = np.zeros((4))
MaxEigenValImL0g0021Inf = np.zeros((4))

MaxEigenValImL0g0021010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g0021010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g0021010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g0021010[3] = np.max(EigenValImL0g0010101010)
#MaxEigenValImL0g0021010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g0021020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g0021020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g0021020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g0021020[3] = np.max(EigenValImL0g0010101020)
#MaxEigenValImL0g0021020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g0021030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g0021030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g0021030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g0021030[3] = np.max(EigenValImL0g0010101030)
#MaxEigenValImL0g0021030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g0021040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g0021040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g0021040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g0021040[3] = np.max(EigenValImL0g0010101040)
#MaxEigenValImL0g0021040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g0021050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g0021050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g0021050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g0021050[3] = np.max(EigenValImL0g0010101050)
#MaxEigenValImL0g0021050[4] = np.max(EigenValImL0g0010201050)

MaxEigenValImL0g0021Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL0g0021010[0],MaxEigenValImL0g0021020[0],MaxEigenValImL0g0021030[0],MaxEigenValImL0g0021040[0],MaxEigenValImL0g0021050[0]], 1)[[1]]
MaxEigenValImL0g0021Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL0g0021010[1],MaxEigenValImL0g0021020[1],MaxEigenValImL0g0021030[1],MaxEigenValImL0g0021040[1],MaxEigenValImL0g0021050[1]], 1)[[1]]
MaxEigenValImL0g0021Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL0g0021010[2],MaxEigenValImL0g0021020[2],MaxEigenValImL0g0021030[2],MaxEigenValImL0g0021040[2],MaxEigenValImL0g0021050[2]], 1)[[1]]
MaxEigenValImL0g0021Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL0g0021010[3],MaxEigenValImL0g0021020[3],MaxEigenValImL0g0021030[3],MaxEigenValImL0g0021040[3],MaxEigenValImL0g0021050[3]], 1)[[1]]
#MaxEigenValImL0g0021Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g0021010[4],MaxEigenValImL0g0021020[4],MaxEigenValImL0g0021030[4],MaxEigenValImL0g0021040[4],MaxEigenValImL0g0021050[4]], 1)[[1]]

########################################################################

dataL0g0010011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK001/N010/HamVals.txt')

MomentumAxL0g0010011010 = dataL0g0010011010[:,][:,5*0+0]
KineticEneL0g0010011010 = dataL0g0010011010[:,][:,5*0+1]
SelfEnergyL0g0010011010 = dataL0g0010011010[:,][:,5*0+2]
EigenValReL0g0010011010 = dataL0g0010011010[:,][:,5*0+3]
EigenValImL0g0010011010 = dataL0g0010011010[:,][:,5*0+4]

dataL0g0010011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK001/N020/HamVals.txt')

MomentumAxL0g0010011020 = dataL0g0010011020[:,][:,5*0+0]
KineticEneL0g0010011020 = dataL0g0010011020[:,][:,5*0+1]
SelfEnergyL0g0010011020 = dataL0g0010011020[:,][:,5*0+2]
EigenValReL0g0010011020 = dataL0g0010011020[:,][:,5*0+3]
EigenValImL0g0010011020 = dataL0g0010011020[:,][:,5*0+4]

dataL0g0010011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK001/N030/HamVals.txt')

MomentumAxL0g0010011030 = dataL0g0010011030[:,][:,5*0+0]
KineticEneL0g0010011030 = dataL0g0010011030[:,][:,5*0+1]
SelfEnergyL0g0010011030 = dataL0g0010011030[:,][:,5*0+2]
EigenValReL0g0010011030 = dataL0g0010011030[:,][:,5*0+3]
EigenValImL0g0010011030 = dataL0g0010011030[:,][:,5*0+4]

dataL0g0010011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK001/N040/HamVals.txt')

MomentumAxL0g0010011040 = dataL0g0010011040[:,][:,5*0+0]
KineticEneL0g0010011040 = dataL0g0010011040[:,][:,5*0+1]
SelfEnergyL0g0010011040 = dataL0g0010011040[:,][:,5*0+2]
EigenValReL0g0010011040 = dataL0g0010011040[:,][:,5*0+3]
EigenValImL0g0010011040 = dataL0g0010011040[:,][:,5*0+4]

dataL0g0010011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK001/N050/HamVals.txt')

MomentumAxL0g0010011050 = dataL0g0010011050[:,][:,5*0+0]
KineticEneL0g0010011050 = dataL0g0010011050[:,][:,5*0+1]
SelfEnergyL0g0010011050 = dataL0g0010011050[:,][:,5*0+2]
EigenValReL0g0010011050 = dataL0g0010011050[:,][:,5*0+3]
EigenValImL0g0010011050 = dataL0g0010011050[:,][:,5*0+4]

dataL0g0010021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK002/N010/HamVals.txt')

MomentumAxL0g0010021010 = dataL0g0010021010[:,][:,5*0+0]
KineticEneL0g0010021010 = dataL0g0010021010[:,][:,5*0+1]
SelfEnergyL0g0010021010 = dataL0g0010021010[:,][:,5*0+2]
EigenValReL0g0010021010 = dataL0g0010021010[:,][:,5*0+3]
EigenValImL0g0010021010 = dataL0g0010021010[:,][:,5*0+4]

dataL0g0010021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK002/N020/HamVals.txt')

MomentumAxL0g0010021020 = dataL0g0010021020[:,][:,5*0+0]
KineticEneL0g0010021020 = dataL0g0010021020[:,][:,5*0+1]
SelfEnergyL0g0010021020 = dataL0g0010021020[:,][:,5*0+2]
EigenValReL0g0010021020 = dataL0g0010021020[:,][:,5*0+3]
EigenValImL0g0010021020 = dataL0g0010021020[:,][:,5*0+4]

dataL0g0010021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK002/N030/HamVals.txt')

MomentumAxL0g0010021030 = dataL0g0010021030[:,][:,5*0+0]
KineticEneL0g0010021030 = dataL0g0010021030[:,][:,5*0+1]
SelfEnergyL0g0010021030 = dataL0g0010021030[:,][:,5*0+2]
EigenValReL0g0010021030 = dataL0g0010021030[:,][:,5*0+3]
EigenValImL0g0010021030 = dataL0g0010021030[:,][:,5*0+4]

dataL0g0010021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK002/N040/HamVals.txt')

MomentumAxL0g0010021040 = dataL0g0010021040[:,][:,5*0+0]
KineticEneL0g0010021040 = dataL0g0010021040[:,][:,5*0+1]
SelfEnergyL0g0010021040 = dataL0g0010021040[:,][:,5*0+2]
EigenValReL0g0010021040 = dataL0g0010021040[:,][:,5*0+3]
EigenValImL0g0010021040 = dataL0g0010021040[:,][:,5*0+4]

dataL0g0010021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK002/N050/HamVals.txt')

MomentumAxL0g0010021050 = dataL0g0010021050[:,][:,5*0+0]
KineticEneL0g0010021050 = dataL0g0010021050[:,][:,5*0+1]
SelfEnergyL0g0010021050 = dataL0g0010021050[:,][:,5*0+2]
EigenValReL0g0010021050 = dataL0g0010021050[:,][:,5*0+3]
EigenValImL0g0010021050 = dataL0g0010021050[:,][:,5*0+4]

dataL0g0010051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK005/N010/HamVals.txt')

MomentumAxL0g0010051010 = dataL0g0010051010[:,][:,5*0+0]
KineticEneL0g0010051010 = dataL0g0010051010[:,][:,5*0+1]
SelfEnergyL0g0010051010 = dataL0g0010051010[:,][:,5*0+2]
EigenValReL0g0010051010 = dataL0g0010051010[:,][:,5*0+3]
EigenValImL0g0010051010 = dataL0g0010051010[:,][:,5*0+4]

dataL0g0010051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK005/N020/HamVals.txt')

MomentumAxL0g0010051020 = dataL0g0010051020[:,][:,5*0+0]
KineticEneL0g0010051020 = dataL0g0010051020[:,][:,5*0+1]
SelfEnergyL0g0010051020 = dataL0g0010051020[:,][:,5*0+2]
EigenValReL0g0010051020 = dataL0g0010051020[:,][:,5*0+3]
EigenValImL0g0010051020 = dataL0g0010051020[:,][:,5*0+4]

dataL0g0010051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK005/N030/HamVals.txt')

MomentumAxL0g0010051030 = dataL0g0010051030[:,][:,5*0+0]
KineticEneL0g0010051030 = dataL0g0010051030[:,][:,5*0+1]
SelfEnergyL0g0010051030 = dataL0g0010051030[:,][:,5*0+2]
EigenValReL0g0010051030 = dataL0g0010051030[:,][:,5*0+3]
EigenValImL0g0010051030 = dataL0g0010051030[:,][:,5*0+4]

dataL0g0010051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK005/N040/HamVals.txt')

MomentumAxL0g0010051040 = dataL0g0010051040[:,][:,5*0+0]
KineticEneL0g0010051040 = dataL0g0010051040[:,][:,5*0+1]
SelfEnergyL0g0010051040 = dataL0g0010051040[:,][:,5*0+2]
EigenValReL0g0010051040 = dataL0g0010051040[:,][:,5*0+3]
EigenValImL0g0010051040 = dataL0g0010051040[:,][:,5*0+4]

dataL0g0010051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK005/N050/HamVals.txt')

MomentumAxL0g0010051050 = dataL0g0010051050[:,][:,5*0+0]
KineticEneL0g0010051050 = dataL0g0010051050[:,][:,5*0+1]
SelfEnergyL0g0010051050 = dataL0g0010051050[:,][:,5*0+2]
EigenValReL0g0010051050 = dataL0g0010051050[:,][:,5*0+3]
EigenValImL0g0010051050 = dataL0g0010051050[:,][:,5*0+4]

dataL0g0010101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK010/N010/HamVals.txt')

MomentumAxL0g0010101010 = dataL0g0010101010[:,][:,5*0+0]
KineticEneL0g0010101010 = dataL0g0010101010[:,][:,5*0+1]
SelfEnergyL0g0010101010 = dataL0g0010101010[:,][:,5*0+2]
EigenValReL0g0010101010 = dataL0g0010101010[:,][:,5*0+3]
EigenValImL0g0010101010 = dataL0g0010101010[:,][:,5*0+4]

dataL0g0010101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK010/N020/HamVals.txt')

MomentumAxL0g0010101020 = dataL0g0010101020[:,][:,5*0+0]
KineticEneL0g0010101020 = dataL0g0010101020[:,][:,5*0+1]
SelfEnergyL0g0010101020 = dataL0g0010101020[:,][:,5*0+2]
EigenValReL0g0010101020 = dataL0g0010101020[:,][:,5*0+3]
EigenValImL0g0010101020 = dataL0g0010101020[:,][:,5*0+4]

dataL0g0010101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK010/N030/HamVals.txt')

MomentumAxL0g0010101030 = dataL0g0010101030[:,][:,5*0+0]
KineticEneL0g0010101030 = dataL0g0010101030[:,][:,5*0+1]
SelfEnergyL0g0010101030 = dataL0g0010101030[:,][:,5*0+2]
EigenValReL0g0010101030 = dataL0g0010101030[:,][:,5*0+3]
EigenValImL0g0010101030 = dataL0g0010101030[:,][:,5*0+4]

dataL0g0010101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK010/N040/HamVals.txt')

MomentumAxL0g0010101040 = dataL0g0010101040[:,][:,5*0+0]
KineticEneL0g0010101040 = dataL0g0010101040[:,][:,5*0+1]
SelfEnergyL0g0010101040 = dataL0g0010101040[:,][:,5*0+2]
EigenValReL0g0010101040 = dataL0g0010101040[:,][:,5*0+3]
EigenValImL0g0010101040 = dataL0g0010101040[:,][:,5*0+4]

dataL0g0010101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK010/N050/HamVals.txt')

MomentumAxL0g0010101050 = dataL0g0010101050[:,][:,5*0+0]
KineticEneL0g0010101050 = dataL0g0010101050[:,][:,5*0+1]
SelfEnergyL0g0010101050 = dataL0g0010101050[:,][:,5*0+2]
EigenValReL0g0010101050 = dataL0g0010101050[:,][:,5*0+3]
EigenValImL0g0010101050 = dataL0g0010101050[:,][:,5*0+4]
"""
dataL0g0010201010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK020/N010/HamVals.txt')

MomentumAxL0g0010201010 = dataL0g0010201010[:,][:,5*0+0]
KineticEneL0g0010201010 = dataL0g0010201010[:,][:,5*0+1]
SelfEnergyL0g0010201010 = dataL0g0010201010[:,][:,5*0+2]
EigenValReL0g0010201010 = dataL0g0010201010[:,][:,5*0+3]
EigenValImL0g0010201010 = dataL0g0010201010[:,][:,5*0+4]

dataL0g0010201020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK020/N020/HamVals.txt')

MomentumAxL0g0010201020 = dataL0g0010201020[:,][:,5*0+0]
KineticEneL0g0010201020 = dataL0g0010201020[:,][:,5*0+1]
SelfEnergyL0g0010201020 = dataL0g0010201020[:,][:,5*0+2]
EigenValReL0g0010201020 = dataL0g0010201020[:,][:,5*0+3]
EigenValImL0g0010201020 = dataL0g0010201020[:,][:,5*0+4]

dataL0g0010201030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK020/N030/HamVals.txt')

MomentumAxL0g0010201030 = dataL0g0010201030[:,][:,5*0+0]
KineticEneL0g0010201030 = dataL0g0010201030[:,][:,5*0+1]
SelfEnergyL0g0010201030 = dataL0g0010201030[:,][:,5*0+2]
EigenValReL0g0010201030 = dataL0g0010201030[:,][:,5*0+3]
EigenValImL0g0010201030 = dataL0g0010201030[:,][:,5*0+4]

dataL0g0010201040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK020/N040/HamVals.txt')

MomentumAxL0g0010201040 = dataL0g0010201040[:,][:,5*0+0]
KineticEneL0g0010201040 = dataL0g0010201040[:,][:,5*0+1]
SelfEnergyL0g0010201040 = dataL0g0010201040[:,][:,5*0+2]
EigenValReL0g0010201040 = dataL0g0010201040[:,][:,5*0+3]
EigenValImL0g0010201040 = dataL0g0010201040[:,][:,5*0+4]

dataL0g0010201050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK005/aK020/N050/HamVals.txt')

MomentumAxL0g0010201050 = dataL0g0010201050[:,][:,5*0+0]
KineticEneL0g0010201050 = dataL0g0010201050[:,][:,5*0+1]
SelfEnergyL0g0010201050 = dataL0g0010201050[:,][:,5*0+2]
EigenValReL0g0010201050 = dataL0g0010201050[:,][:,5*0+3]
EigenValImL0g0010201050 = dataL0g0010201050[:,][:,5*0+4]
"""
MaxEigenValImL0g0051010 = np.zeros((4))
MaxEigenValImL0g0051020 = np.zeros((4))
MaxEigenValImL0g0051030 = np.zeros((4))
MaxEigenValImL0g0051040 = np.zeros((4))
MaxEigenValImL0g0051050 = np.zeros((4))
MaxEigenValImL0g0051Inf = np.zeros((4))

MaxEigenValImL0g0051010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g0051010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g0051010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g0051010[3] = np.max(EigenValImL0g0010101010)
#MaxEigenValImL0g0051010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g0051020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g0051020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g0051020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g0051020[3] = np.max(EigenValImL0g0010101020)
#MaxEigenValImL0g0051020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g0051030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g0051030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g0051030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g0051030[3] = np.max(EigenValImL0g0010101030)
#MaxEigenValImL0g0051030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g0051040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g0051040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g0051040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g0051040[3] = np.max(EigenValImL0g0010101040)
#MaxEigenValImL0g0051040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g0051050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g0051050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g0051050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g0051050[3] = np.max(EigenValImL0g0010101050)
#MaxEigenValImL0g0051050[4] = np.max(EigenValImL0g0010201050)

MaxEigenValImL0g0051Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL0g0051010[0],MaxEigenValImL0g0051020[0],MaxEigenValImL0g0051030[0],MaxEigenValImL0g0051040[0],MaxEigenValImL0g0051050[0]], 1)[[1]]
MaxEigenValImL0g0051Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL0g0051010[1],MaxEigenValImL0g0051020[1],MaxEigenValImL0g0051030[1],MaxEigenValImL0g0051040[1],MaxEigenValImL0g0051050[1]], 1)[[1]]
MaxEigenValImL0g0051Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL0g0051010[2],MaxEigenValImL0g0051020[2],MaxEigenValImL0g0051030[2],MaxEigenValImL0g0051040[2],MaxEigenValImL0g0051050[2]], 1)[[1]]
MaxEigenValImL0g0051Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL0g0051010[3],MaxEigenValImL0g0051020[3],MaxEigenValImL0g0051030[3],MaxEigenValImL0g0051040[3],MaxEigenValImL0g0051050[3]], 1)[[1]]
#MaxEigenValImL0g0051Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g0051010[4],MaxEigenValImL0g0051020[4],MaxEigenValImL0g0051030[4],MaxEigenValImL0g0051040[4],MaxEigenValImL0g0051050[4]], 1)[[1]]

########################################################################

dataL0g0010011010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK001/N010/HamVals.txt')

MomentumAxL0g0010011010 = dataL0g0010011010[:,][:,5*0+0]
KineticEneL0g0010011010 = dataL0g0010011010[:,][:,5*0+1]
SelfEnergyL0g0010011010 = dataL0g0010011010[:,][:,5*0+2]
EigenValReL0g0010011010 = dataL0g0010011010[:,][:,5*0+3]
EigenValImL0g0010011010 = dataL0g0010011010[:,][:,5*0+4]

dataL0g0010011020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK001/N020/HamVals.txt')

MomentumAxL0g0010011020 = dataL0g0010011020[:,][:,5*0+0]
KineticEneL0g0010011020 = dataL0g0010011020[:,][:,5*0+1]
SelfEnergyL0g0010011020 = dataL0g0010011020[:,][:,5*0+2]
EigenValReL0g0010011020 = dataL0g0010011020[:,][:,5*0+3]
EigenValImL0g0010011020 = dataL0g0010011020[:,][:,5*0+4]

dataL0g0010011030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK001/N030/HamVals.txt')

MomentumAxL0g0010011030 = dataL0g0010011030[:,][:,5*0+0]
KineticEneL0g0010011030 = dataL0g0010011030[:,][:,5*0+1]
SelfEnergyL0g0010011030 = dataL0g0010011030[:,][:,5*0+2]
EigenValReL0g0010011030 = dataL0g0010011030[:,][:,5*0+3]
EigenValImL0g0010011030 = dataL0g0010011030[:,][:,5*0+4]

dataL0g0010011040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK001/N040/HamVals.txt')

MomentumAxL0g0010011040 = dataL0g0010011040[:,][:,5*0+0]
KineticEneL0g0010011040 = dataL0g0010011040[:,][:,5*0+1]
SelfEnergyL0g0010011040 = dataL0g0010011040[:,][:,5*0+2]
EigenValReL0g0010011040 = dataL0g0010011040[:,][:,5*0+3]
EigenValImL0g0010011040 = dataL0g0010011040[:,][:,5*0+4]

dataL0g0010011050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK001/N050/HamVals.txt')

MomentumAxL0g0010011050 = dataL0g0010011050[:,][:,5*0+0]
KineticEneL0g0010011050 = dataL0g0010011050[:,][:,5*0+1]
SelfEnergyL0g0010011050 = dataL0g0010011050[:,][:,5*0+2]
EigenValReL0g0010011050 = dataL0g0010011050[:,][:,5*0+3]
EigenValImL0g0010011050 = dataL0g0010011050[:,][:,5*0+4]

dataL0g0010021010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK002/N010/HamVals.txt')

MomentumAxL0g0010021010 = dataL0g0010021010[:,][:,5*0+0]
KineticEneL0g0010021010 = dataL0g0010021010[:,][:,5*0+1]
SelfEnergyL0g0010021010 = dataL0g0010021010[:,][:,5*0+2]
EigenValReL0g0010021010 = dataL0g0010021010[:,][:,5*0+3]
EigenValImL0g0010021010 = dataL0g0010021010[:,][:,5*0+4]

dataL0g0010021020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK002/N020/HamVals.txt')

MomentumAxL0g0010021020 = dataL0g0010021020[:,][:,5*0+0]
KineticEneL0g0010021020 = dataL0g0010021020[:,][:,5*0+1]
SelfEnergyL0g0010021020 = dataL0g0010021020[:,][:,5*0+2]
EigenValReL0g0010021020 = dataL0g0010021020[:,][:,5*0+3]
EigenValImL0g0010021020 = dataL0g0010021020[:,][:,5*0+4]

dataL0g0010021030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK002/N030/HamVals.txt')

MomentumAxL0g0010021030 = dataL0g0010021030[:,][:,5*0+0]
KineticEneL0g0010021030 = dataL0g0010021030[:,][:,5*0+1]
SelfEnergyL0g0010021030 = dataL0g0010021030[:,][:,5*0+2]
EigenValReL0g0010021030 = dataL0g0010021030[:,][:,5*0+3]
EigenValImL0g0010021030 = dataL0g0010021030[:,][:,5*0+4]

dataL0g0010021040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK002/N040/HamVals.txt')

MomentumAxL0g0010021040 = dataL0g0010021040[:,][:,5*0+0]
KineticEneL0g0010021040 = dataL0g0010021040[:,][:,5*0+1]
SelfEnergyL0g0010021040 = dataL0g0010021040[:,][:,5*0+2]
EigenValReL0g0010021040 = dataL0g0010021040[:,][:,5*0+3]
EigenValImL0g0010021040 = dataL0g0010021040[:,][:,5*0+4]

dataL0g0010021050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK002/N050/HamVals.txt')

MomentumAxL0g0010021050 = dataL0g0010021050[:,][:,5*0+0]
KineticEneL0g0010021050 = dataL0g0010021050[:,][:,5*0+1]
SelfEnergyL0g0010021050 = dataL0g0010021050[:,][:,5*0+2]
EigenValReL0g0010021050 = dataL0g0010021050[:,][:,5*0+3]
EigenValImL0g0010021050 = dataL0g0010021050[:,][:,5*0+4]

dataL0g0010051010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK005/N010/HamVals.txt')

MomentumAxL0g0010051010 = dataL0g0010051010[:,][:,5*0+0]
KineticEneL0g0010051010 = dataL0g0010051010[:,][:,5*0+1]
SelfEnergyL0g0010051010 = dataL0g0010051010[:,][:,5*0+2]
EigenValReL0g0010051010 = dataL0g0010051010[:,][:,5*0+3]
EigenValImL0g0010051010 = dataL0g0010051010[:,][:,5*0+4]

dataL0g0010051020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK005/N020/HamVals.txt')

MomentumAxL0g0010051020 = dataL0g0010051020[:,][:,5*0+0]
KineticEneL0g0010051020 = dataL0g0010051020[:,][:,5*0+1]
SelfEnergyL0g0010051020 = dataL0g0010051020[:,][:,5*0+2]
EigenValReL0g0010051020 = dataL0g0010051020[:,][:,5*0+3]
EigenValImL0g0010051020 = dataL0g0010051020[:,][:,5*0+4]

dataL0g0010051030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK005/N030/HamVals.txt')

MomentumAxL0g0010051030 = dataL0g0010051030[:,][:,5*0+0]
KineticEneL0g0010051030 = dataL0g0010051030[:,][:,5*0+1]
SelfEnergyL0g0010051030 = dataL0g0010051030[:,][:,5*0+2]
EigenValReL0g0010051030 = dataL0g0010051030[:,][:,5*0+3]
EigenValImL0g0010051030 = dataL0g0010051030[:,][:,5*0+4]

dataL0g0010051040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK005/N040/HamVals.txt')

MomentumAxL0g0010051040 = dataL0g0010051040[:,][:,5*0+0]
KineticEneL0g0010051040 = dataL0g0010051040[:,][:,5*0+1]
SelfEnergyL0g0010051040 = dataL0g0010051040[:,][:,5*0+2]
EigenValReL0g0010051040 = dataL0g0010051040[:,][:,5*0+3]
EigenValImL0g0010051040 = dataL0g0010051040[:,][:,5*0+4]

dataL0g0010051050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK005/N050/HamVals.txt')

MomentumAxL0g0010051050 = dataL0g0010051050[:,][:,5*0+0]
KineticEneL0g0010051050 = dataL0g0010051050[:,][:,5*0+1]
SelfEnergyL0g0010051050 = dataL0g0010051050[:,][:,5*0+2]
EigenValReL0g0010051050 = dataL0g0010051050[:,][:,5*0+3]
EigenValImL0g0010051050 = dataL0g0010051050[:,][:,5*0+4]

dataL0g0010101010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK010/N010/HamVals.txt')

MomentumAxL0g0010101010 = dataL0g0010101010[:,][:,5*0+0]
KineticEneL0g0010101010 = dataL0g0010101010[:,][:,5*0+1]
SelfEnergyL0g0010101010 = dataL0g0010101010[:,][:,5*0+2]
EigenValReL0g0010101010 = dataL0g0010101010[:,][:,5*0+3]
EigenValImL0g0010101010 = dataL0g0010101010[:,][:,5*0+4]

dataL0g0010101020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK010/N020/HamVals.txt')

MomentumAxL0g0010101020 = dataL0g0010101020[:,][:,5*0+0]
KineticEneL0g0010101020 = dataL0g0010101020[:,][:,5*0+1]
SelfEnergyL0g0010101020 = dataL0g0010101020[:,][:,5*0+2]
EigenValReL0g0010101020 = dataL0g0010101020[:,][:,5*0+3]
EigenValImL0g0010101020 = dataL0g0010101020[:,][:,5*0+4]

dataL0g0010101030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK010/N030/HamVals.txt')

MomentumAxL0g0010101030 = dataL0g0010101030[:,][:,5*0+0]
KineticEneL0g0010101030 = dataL0g0010101030[:,][:,5*0+1]
SelfEnergyL0g0010101030 = dataL0g0010101030[:,][:,5*0+2]
EigenValReL0g0010101030 = dataL0g0010101030[:,][:,5*0+3]
EigenValImL0g0010101030 = dataL0g0010101030[:,][:,5*0+4]

dataL0g0010101040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK010/N040/HamVals.txt')

MomentumAxL0g0010101040 = dataL0g0010101040[:,][:,5*0+0]
KineticEneL0g0010101040 = dataL0g0010101040[:,][:,5*0+1]
SelfEnergyL0g0010101040 = dataL0g0010101040[:,][:,5*0+2]
EigenValReL0g0010101040 = dataL0g0010101040[:,][:,5*0+3]
EigenValImL0g0010101040 = dataL0g0010101040[:,][:,5*0+4]

dataL0g0010101050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK010/N050/HamVals.txt')

MomentumAxL0g0010101050 = dataL0g0010101050[:,][:,5*0+0]
KineticEneL0g0010101050 = dataL0g0010101050[:,][:,5*0+1]
SelfEnergyL0g0010101050 = dataL0g0010101050[:,][:,5*0+2]
EigenValReL0g0010101050 = dataL0g0010101050[:,][:,5*0+3]
EigenValImL0g0010101050 = dataL0g0010101050[:,][:,5*0+4]
"""
dataL0g0010201010 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK020/N010/HamVals.txt')

MomentumAxL0g0010201010 = dataL0g0010201010[:,][:,5*0+0]
KineticEneL0g0010201010 = dataL0g0010201010[:,][:,5*0+1]
SelfEnergyL0g0010201010 = dataL0g0010201010[:,][:,5*0+2]
EigenValReL0g0010201010 = dataL0g0010201010[:,][:,5*0+3]
EigenValImL0g0010201010 = dataL0g0010201010[:,][:,5*0+4]

dataL0g0010201020 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK020/N020/HamVals.txt')

MomentumAxL0g0010201020 = dataL0g0010201020[:,][:,5*0+0]
KineticEneL0g0010201020 = dataL0g0010201020[:,][:,5*0+1]
SelfEnergyL0g0010201020 = dataL0g0010201020[:,][:,5*0+2]
EigenValReL0g0010201020 = dataL0g0010201020[:,][:,5*0+3]
EigenValImL0g0010201020 = dataL0g0010201020[:,][:,5*0+4]

dataL0g0010201030 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK020/N030/HamVals.txt')

MomentumAxL0g0010201030 = dataL0g0010201030[:,][:,5*0+0]
KineticEneL0g0010201030 = dataL0g0010201030[:,][:,5*0+1]
SelfEnergyL0g0010201030 = dataL0g0010201030[:,][:,5*0+2]
EigenValReL0g0010201030 = dataL0g0010201030[:,][:,5*0+3]
EigenValImL0g0010201030 = dataL0g0010201030[:,][:,5*0+4]

dataL0g0010201040 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK020/N040/HamVals.txt')

MomentumAxL0g0010201040 = dataL0g0010201040[:,][:,5*0+0]
KineticEneL0g0010201040 = dataL0g0010201040[:,][:,5*0+1]
SelfEnergyL0g0010201040 = dataL0g0010201040[:,][:,5*0+2]
EigenValReL0g0010201040 = dataL0g0010201040[:,][:,5*0+3]
EigenValImL0g0010201040 = dataL0g0010201040[:,][:,5*0+4]

dataL0g0010201050 = np.genfromtxt('./TangentMomentum/R=2/L0/gK010/aK020/N050/HamVals.txt')

MomentumAxL0g0010201050 = dataL0g0010201050[:,][:,5*0+0]
KineticEneL0g0010201050 = dataL0g0010201050[:,][:,5*0+1]
SelfEnergyL0g0010201050 = dataL0g0010201050[:,][:,5*0+2]
EigenValReL0g0010201050 = dataL0g0010201050[:,][:,5*0+3]
EigenValImL0g0010201050 = dataL0g0010201050[:,][:,5*0+4]
"""
MaxEigenValImL0g0101010 = np.zeros((4))
MaxEigenValImL0g0101020 = np.zeros((4))
MaxEigenValImL0g0101030 = np.zeros((4))
MaxEigenValImL0g0101040 = np.zeros((4))
MaxEigenValImL0g0101050 = np.zeros((4))
MaxEigenValImL0g0101Inf = np.zeros((4))

MaxEigenValImL0g0101010[0] = np.max(EigenValImL0g0010011010)
MaxEigenValImL0g0101010[1] = np.max(EigenValImL0g0010021010)
MaxEigenValImL0g0101010[2] = np.max(EigenValImL0g0010051010)
MaxEigenValImL0g0101010[3] = np.max(EigenValImL0g0010101010)
#MaxEigenValImL0g0101010[4] = np.max(EigenValImL0g0010201010)

MaxEigenValImL0g0101020[0] = np.max(EigenValImL0g0010011020)
MaxEigenValImL0g0101020[1] = np.max(EigenValImL0g0010021020)
MaxEigenValImL0g0101020[2] = np.max(EigenValImL0g0010051020)
MaxEigenValImL0g0101020[3] = np.max(EigenValImL0g0010101020)
#MaxEigenValImL0g0101020[4] = np.max(EigenValImL0g0010201020)

MaxEigenValImL0g0101030[0] = np.max(EigenValImL0g0010011030)
MaxEigenValImL0g0101030[1] = np.max(EigenValImL0g0010021030)
MaxEigenValImL0g0101030[2] = np.max(EigenValImL0g0010051030)
MaxEigenValImL0g0101030[3] = np.max(EigenValImL0g0010101030)
#MaxEigenValImL0g0101030[4] = np.max(EigenValImL0g0010201030)

MaxEigenValImL0g0101040[0] = np.max(EigenValImL0g0010011040)
MaxEigenValImL0g0101040[1] = np.max(EigenValImL0g0010021040)
MaxEigenValImL0g0101040[2] = np.max(EigenValImL0g0010051040)
MaxEigenValImL0g0101040[3] = np.max(EigenValImL0g0010101040)
#MaxEigenValImL0g0101040[4] = np.max(EigenValImL0g0010201040)

MaxEigenValImL0g0101050[0] = np.max(EigenValImL0g0010011050)
MaxEigenValImL0g0101050[1] = np.max(EigenValImL0g0010021050)
MaxEigenValImL0g0101050[2] = np.max(EigenValImL0g0010051050)
MaxEigenValImL0g0101050[3] = np.max(EigenValImL0g0010101050)
#MaxEigenValImL0g0101050[4] = np.max(EigenValImL0g0010201050)

MaxEigenValImL0g0101Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL0g0101010[0],MaxEigenValImL0g0101020[0],MaxEigenValImL0g0101030[0],MaxEigenValImL0g0101040[0],MaxEigenValImL0g0101050[0]], 1)[[1]]
MaxEigenValImL0g0101Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL0g0101010[1],MaxEigenValImL0g0101020[1],MaxEigenValImL0g0101030[1],MaxEigenValImL0g0101040[1],MaxEigenValImL0g0101050[1]], 1)[[1]]
MaxEigenValImL0g0101Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL0g0101010[2],MaxEigenValImL0g0101020[2],MaxEigenValImL0g0101030[2],MaxEigenValImL0g0101040[2],MaxEigenValImL0g0101050[2]], 1)[[1]]
MaxEigenValImL0g0101Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL0g0101010[3],MaxEigenValImL0g0101020[3],MaxEigenValImL0g0101030[3],MaxEigenValImL0g0101040[3],MaxEigenValImL0g0101050[3]], 1)[[1]]
#MaxEigenValImL0g0101Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL0g0101010[4],MaxEigenValImL0g0101020[4],MaxEigenValImL0g0101030[4],MaxEigenValImL0g0101040[4],MaxEigenValImL0g0101050[4]], 1)[[1]]

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
MaxEigenValImL2g000_51010 = np.zeros((4))
MaxEigenValImL2g000_51020 = np.zeros((4))
MaxEigenValImL2g000_51030 = np.zeros((4))
MaxEigenValImL2g000_51040 = np.zeros((4))
MaxEigenValImL2g000_51050 = np.zeros((4))
MaxEigenValImL2g000_51Inf = np.zeros((4))

MaxEigenValImL2g000_51010[0] = np.max(EigenValImL2g000_50011010)
MaxEigenValImL2g000_51010[1] = np.max(EigenValImL2g000_50021010)
MaxEigenValImL2g000_51010[2] = np.max(EigenValImL2g000_50051010)
MaxEigenValImL2g000_51010[3] = np.max(EigenValImL2g000_50101010)
#MaxEigenValImL2g000_51010[4] = np.max(EigenValImL2g000_50201010)

MaxEigenValImL2g000_51020[0] = np.max(EigenValImL2g000_50011020)
MaxEigenValImL2g000_51020[1] = np.max(EigenValImL2g000_50021020)
MaxEigenValImL2g000_51020[2] = np.max(EigenValImL2g000_50051020)
MaxEigenValImL2g000_51020[3] = np.max(EigenValImL2g000_50101020)
#MaxEigenValImL2g000_51020[4] = np.max(EigenValImL2g000_50201020)

MaxEigenValImL2g000_51030[0] = np.max(EigenValImL2g000_50011030)
MaxEigenValImL2g000_51030[1] = np.max(EigenValImL2g000_50021030)
MaxEigenValImL2g000_51030[2] = np.max(EigenValImL2g000_50051030)
MaxEigenValImL2g000_51030[3] = np.max(EigenValImL2g000_50101030)
#MaxEigenValImL2g000_51030[4] = np.max(EigenValImL2g000_50201030)

MaxEigenValImL2g000_51040[0] = np.max(EigenValImL2g000_50011040)
MaxEigenValImL2g000_51040[1] = np.max(EigenValImL2g000_50021040)
MaxEigenValImL2g000_51040[2] = np.max(EigenValImL2g000_50051040)
MaxEigenValImL2g000_51040[3] = np.max(EigenValImL2g000_50101040)
#MaxEigenValImL2g000_51040[4] = np.max(EigenValImL2g000_50201040)

MaxEigenValImL2g000_51050[0] = np.max(EigenValImL2g000_50011050)
MaxEigenValImL2g000_51050[1] = np.max(EigenValImL2g000_50021050)
MaxEigenValImL2g000_51050[2] = np.max(EigenValImL2g000_50051050)
MaxEigenValImL2g000_51050[3] = np.max(EigenValImL2g000_50101050)
#MaxEigenValImL2g000_51050[4] = np.max(EigenValImL2g000_50201050)

MaxEigenValImL2g000_51Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_51010[0],MaxEigenValImL2g000_51020[0],MaxEigenValImL2g000_51030[0],MaxEigenValImL2g000_51040[0],MaxEigenValImL2g000_51050[0]], 1)[[1]]
MaxEigenValImL2g000_51Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_51010[1],MaxEigenValImL2g000_51020[1],MaxEigenValImL2g000_51030[1],MaxEigenValImL2g000_51040[1],MaxEigenValImL2g000_51050[1]], 1)[[1]]
MaxEigenValImL2g000_51Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_51010[2],MaxEigenValImL2g000_51020[2],MaxEigenValImL2g000_51030[2],MaxEigenValImL2g000_51040[2],MaxEigenValImL2g000_51050[2]], 1)[[1]]
MaxEigenValImL2g000_51Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_51010[3],MaxEigenValImL2g000_51020[3],MaxEigenValImL2g000_51030[3],MaxEigenValImL2g000_51040[3],MaxEigenValImL2g000_51050[3]], 1)[[1]]
#MaxEigenValImL2g000_51Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_51010[4],MaxEigenValImL2g000_51020[4],MaxEigenValImL2g000_51030[4],MaxEigenValImL2g000_51040[4],MaxEigenValImL2g000_51050[4]], 1)[[1]]

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
MaxEigenValImL2g000_61010 = np.zeros((4))
MaxEigenValImL2g000_61020 = np.zeros((4))
MaxEigenValImL2g000_61030 = np.zeros((4))
MaxEigenValImL2g000_61040 = np.zeros((4))
MaxEigenValImL2g000_61050 = np.zeros((4))
MaxEigenValImL2g000_61Inf = np.zeros((4))

MaxEigenValImL2g000_61010[0] = np.max(EigenValImL2g000_60011010)
MaxEigenValImL2g000_61010[1] = np.max(EigenValImL2g000_60021010)
MaxEigenValImL2g000_61010[2] = np.max(EigenValImL2g000_60051010)
MaxEigenValImL2g000_61010[3] = np.max(EigenValImL2g000_60101010)
#MaxEigenValImL2g000_61010[4] = np.max(EigenValImL2g000_60201010)

MaxEigenValImL2g000_61020[0] = np.max(EigenValImL2g000_60011020)
MaxEigenValImL2g000_61020[1] = np.max(EigenValImL2g000_60021020)
MaxEigenValImL2g000_61020[2] = np.max(EigenValImL2g000_60051020)
MaxEigenValImL2g000_61020[3] = np.max(EigenValImL2g000_60101020)
#MaxEigenValImL2g000_61020[4] = np.max(EigenValImL2g000_60201020)

MaxEigenValImL2g000_61030[0] = np.max(EigenValImL2g000_60011030)
MaxEigenValImL2g000_61030[1] = np.max(EigenValImL2g000_60021030)
MaxEigenValImL2g000_61030[2] = np.max(EigenValImL2g000_60051030)
MaxEigenValImL2g000_61030[3] = np.max(EigenValImL2g000_60101030)
#MaxEigenValImL2g000_61030[4] = np.max(EigenValImL2g000_60201030)

MaxEigenValImL2g000_61040[0] = np.max(EigenValImL2g000_60011040)
MaxEigenValImL2g000_61040[1] = np.max(EigenValImL2g000_60021040)
MaxEigenValImL2g000_61040[2] = np.max(EigenValImL2g000_60051040)
MaxEigenValImL2g000_61040[3] = np.max(EigenValImL2g000_60101040)
#MaxEigenValImL2g000_61040[4] = np.max(EigenValImL2g000_60201040)

MaxEigenValImL2g000_61050[0] = np.max(EigenValImL2g000_60011050)
MaxEigenValImL2g000_61050[1] = np.max(EigenValImL2g000_60021050)
MaxEigenValImL2g000_61050[2] = np.max(EigenValImL2g000_60051050)
MaxEigenValImL2g000_61050[3] = np.max(EigenValImL2g000_60101050)
#MaxEigenValImL2g000_61050[4] = np.max(EigenValImL2g000_60201050)

MaxEigenValImL2g000_61Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_61010[0],MaxEigenValImL2g000_61020[0],MaxEigenValImL2g000_61030[0],MaxEigenValImL2g000_61040[0],MaxEigenValImL2g000_61050[0]], 1)[[1]]
MaxEigenValImL2g000_61Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_61010[1],MaxEigenValImL2g000_61020[1],MaxEigenValImL2g000_61030[1],MaxEigenValImL2g000_61040[1],MaxEigenValImL2g000_61050[1]], 1)[[1]]
MaxEigenValImL2g000_61Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_61010[2],MaxEigenValImL2g000_61020[2],MaxEigenValImL2g000_61030[2],MaxEigenValImL2g000_61040[2],MaxEigenValImL2g000_61050[2]], 1)[[1]]
MaxEigenValImL2g000_61Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_61010[3],MaxEigenValImL2g000_61020[3],MaxEigenValImL2g000_61030[3],MaxEigenValImL2g000_61040[3],MaxEigenValImL2g000_61050[3]], 1)[[1]]
#MaxEigenValImL2g000_61Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_61010[4],MaxEigenValImL2g000_61020[4],MaxEigenValImL2g000_61030[4],MaxEigenValImL2g000_61040[4],MaxEigenValImL2g000_61050[4]], 1)[[1]]

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
MaxEigenValImL2g000_71010 = np.zeros((4))
MaxEigenValImL2g000_71020 = np.zeros((4))
MaxEigenValImL2g000_71030 = np.zeros((4))
MaxEigenValImL2g000_71040 = np.zeros((4))
MaxEigenValImL2g000_71050 = np.zeros((4))
MaxEigenValImL2g000_71Inf = np.zeros((4))

MaxEigenValImL2g000_71010[0] = np.max(EigenValImL2g000_70011010)
MaxEigenValImL2g000_71010[1] = np.max(EigenValImL2g000_70021010)
MaxEigenValImL2g000_71010[2] = np.max(EigenValImL2g000_70051010)
MaxEigenValImL2g000_71010[3] = np.max(EigenValImL2g000_70101010)
#MaxEigenValImL2g000_71010[4] = np.max(EigenValImL2g000_70201010)

MaxEigenValImL2g000_71020[0] = np.max(EigenValImL2g000_70011020)
MaxEigenValImL2g000_71020[1] = np.max(EigenValImL2g000_70021020)
MaxEigenValImL2g000_71020[2] = np.max(EigenValImL2g000_70051020)
MaxEigenValImL2g000_71020[3] = np.max(EigenValImL2g000_70101020)
#MaxEigenValImL2g000_71020[4] = np.max(EigenValImL2g000_70201020)

MaxEigenValImL2g000_71030[0] = np.max(EigenValImL2g000_70011030)
MaxEigenValImL2g000_71030[1] = np.max(EigenValImL2g000_70021030)
MaxEigenValImL2g000_71030[2] = np.max(EigenValImL2g000_70051030)
MaxEigenValImL2g000_71030[3] = np.max(EigenValImL2g000_70101030)
#MaxEigenValImL2g000_71030[4] = np.max(EigenValImL2g000_70201030)

MaxEigenValImL2g000_71040[0] = np.max(EigenValImL2g000_70011040)
MaxEigenValImL2g000_71040[1] = np.max(EigenValImL2g000_70021040)
MaxEigenValImL2g000_71040[2] = np.max(EigenValImL2g000_70051040)
MaxEigenValImL2g000_71040[3] = np.max(EigenValImL2g000_70101040)
#MaxEigenValImL2g000_71040[4] = np.max(EigenValImL2g000_70201040)

MaxEigenValImL2g000_71050[0] = np.max(EigenValImL2g000_70011050)
MaxEigenValImL2g000_71050[1] = np.max(EigenValImL2g000_70021050)
MaxEigenValImL2g000_71050[2] = np.max(EigenValImL2g000_70051050)
MaxEigenValImL2g000_71050[3] = np.max(EigenValImL2g000_70101050)
#MaxEigenValImL2g000_71050[4] = np.max(EigenValImL2g000_70201050)

MaxEigenValImL2g000_71Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_71010[0],MaxEigenValImL2g000_71020[0],MaxEigenValImL2g000_71030[0],MaxEigenValImL2g000_71040[0],MaxEigenValImL2g000_71050[0]], 1)[[1]]
MaxEigenValImL2g000_71Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_71010[1],MaxEigenValImL2g000_71020[1],MaxEigenValImL2g000_71030[1],MaxEigenValImL2g000_71040[1],MaxEigenValImL2g000_71050[1]], 1)[[1]]
MaxEigenValImL2g000_71Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_71010[2],MaxEigenValImL2g000_71020[2],MaxEigenValImL2g000_71030[2],MaxEigenValImL2g000_71040[2],MaxEigenValImL2g000_71050[2]], 1)[[1]]
MaxEigenValImL2g000_71Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_71010[3],MaxEigenValImL2g000_71020[3],MaxEigenValImL2g000_71030[3],MaxEigenValImL2g000_71040[3],MaxEigenValImL2g000_71050[3]], 1)[[1]]
#MaxEigenValImL2g000_71Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_71010[4],MaxEigenValImL2g000_71020[4],MaxEigenValImL2g000_71030[4],MaxEigenValImL2g000_71040[4],MaxEigenValImL2g000_71050[4]], 1)[[1]]

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
MaxEigenValImL2g000_81010 = np.zeros((4))
MaxEigenValImL2g000_81020 = np.zeros((4))
MaxEigenValImL2g000_81030 = np.zeros((4))
MaxEigenValImL2g000_81040 = np.zeros((4))
MaxEigenValImL2g000_81050 = np.zeros((4))
MaxEigenValImL2g000_81Inf = np.zeros((4))

MaxEigenValImL2g000_81010[0] = np.max(EigenValImL2g000_80011010)
MaxEigenValImL2g000_81010[1] = np.max(EigenValImL2g000_80021010)
MaxEigenValImL2g000_81010[2] = np.max(EigenValImL2g000_80051010)
MaxEigenValImL2g000_81010[3] = np.max(EigenValImL2g000_80101010)
#MaxEigenValImL2g000_81010[4] = np.max(EigenValImL2g000_80201010)

MaxEigenValImL2g000_81020[0] = np.max(EigenValImL2g000_80011020)
MaxEigenValImL2g000_81020[1] = np.max(EigenValImL2g000_80021020)
MaxEigenValImL2g000_81020[2] = np.max(EigenValImL2g000_80051020)
MaxEigenValImL2g000_81020[3] = np.max(EigenValImL2g000_80101020)
#MaxEigenValImL2g000_81020[4] = np.max(EigenValImL2g000_80201020)

MaxEigenValImL2g000_81030[0] = np.max(EigenValImL2g000_80011030)
MaxEigenValImL2g000_81030[1] = np.max(EigenValImL2g000_80021030)
MaxEigenValImL2g000_81030[2] = np.max(EigenValImL2g000_80051030)
MaxEigenValImL2g000_81030[3] = np.max(EigenValImL2g000_80101030)
#MaxEigenValImL2g000_81030[4] = np.max(EigenValImL2g000_80201030)

MaxEigenValImL2g000_81040[0] = np.max(EigenValImL2g000_80011040)
MaxEigenValImL2g000_81040[1] = np.max(EigenValImL2g000_80021040)
MaxEigenValImL2g000_81040[2] = np.max(EigenValImL2g000_80051040)
MaxEigenValImL2g000_81040[3] = np.max(EigenValImL2g000_80101040)
#MaxEigenValImL2g000_81040[4] = np.max(EigenValImL2g000_80201040)

MaxEigenValImL2g000_81050[0] = np.max(EigenValImL2g000_80011050)
MaxEigenValImL2g000_81050[1] = np.max(EigenValImL2g000_80021050)
MaxEigenValImL2g000_81050[2] = np.max(EigenValImL2g000_80051050)
MaxEigenValImL2g000_81050[3] = np.max(EigenValImL2g000_80101050)
#MaxEigenValImL2g000_81050[4] = np.max(EigenValImL2g000_80201050)

MaxEigenValImL2g000_81Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_81010[0],MaxEigenValImL2g000_81020[0],MaxEigenValImL2g000_81030[0],MaxEigenValImL2g000_81040[0],MaxEigenValImL2g000_81050[0]], 1)[[1]]
MaxEigenValImL2g000_81Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_81010[1],MaxEigenValImL2g000_81020[1],MaxEigenValImL2g000_81030[1],MaxEigenValImL2g000_81040[1],MaxEigenValImL2g000_81050[1]], 1)[[1]]
MaxEigenValImL2g000_81Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_81010[2],MaxEigenValImL2g000_81020[2],MaxEigenValImL2g000_81030[2],MaxEigenValImL2g000_81040[2],MaxEigenValImL2g000_81050[2]], 1)[[1]]
MaxEigenValImL2g000_81Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_81010[3],MaxEigenValImL2g000_81020[3],MaxEigenValImL2g000_81030[3],MaxEigenValImL2g000_81040[3],MaxEigenValImL2g000_81050[3]], 1)[[1]]
#MaxEigenValImL2g000_81Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL2g000_81010[4],MaxEigenValImL2g000_81020[4],MaxEigenValImL2g000_81030[4],MaxEigenValImL2g000_81040[4],MaxEigenValImL2g000_81050[4]], 1)[[1]]

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
"""
dataL2g0010201010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK020/N010/HamVals.txt')

MomentumAxL2g0010201010 = dataL2g0010201010[:,][:,5*0+0]
KineticEneL2g0010201010 = dataL2g0010201010[:,][:,5*0+1]
SelfEnergyL2g0010201010 = dataL2g0010201010[:,][:,5*0+2]
EigenValReL2g0010201010 = dataL2g0010201010[:,][:,5*0+3]
EigenValImL2g0010201010 = dataL2g0010201010[:,][:,5*0+4]

dataL2g0010201020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK020/N020/HamVals.txt')

MomentumAxL2g0010201020 = dataL2g0010201020[:,][:,5*0+0]
KineticEneL2g0010201020 = dataL2g0010201020[:,][:,5*0+1]
SelfEnergyL2g0010201020 = dataL2g0010201020[:,][:,5*0+2]
EigenValReL2g0010201020 = dataL2g0010201020[:,][:,5*0+3]
EigenValImL2g0010201020 = dataL2g0010201020[:,][:,5*0+4]

dataL2g0010201030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK020/N030/HamVals.txt')

MomentumAxL2g0010201030 = dataL2g0010201030[:,][:,5*0+0]
KineticEneL2g0010201030 = dataL2g0010201030[:,][:,5*0+1]
SelfEnergyL2g0010201030 = dataL2g0010201030[:,][:,5*0+2]
EigenValReL2g0010201030 = dataL2g0010201030[:,][:,5*0+3]
EigenValImL2g0010201030 = dataL2g0010201030[:,][:,5*0+4]

dataL2g0010201040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK020/N040/HamVals.txt')

MomentumAxL2g0010201040 = dataL2g0010201040[:,][:,5*0+0]
KineticEneL2g0010201040 = dataL2g0010201040[:,][:,5*0+1]
SelfEnergyL2g0010201040 = dataL2g0010201040[:,][:,5*0+2]
EigenValReL2g0010201040 = dataL2g0010201040[:,][:,5*0+3]
EigenValImL2g0010201040 = dataL2g0010201040[:,][:,5*0+4]

dataL2g0010201050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK001/aK020/N050/HamVals.txt')

MomentumAxL2g0010201050 = dataL2g0010201050[:,][:,5*0+0]
KineticEneL2g0010201050 = dataL2g0010201050[:,][:,5*0+1]
SelfEnergyL2g0010201050 = dataL2g0010201050[:,][:,5*0+2]
EigenValReL2g0010201050 = dataL2g0010201050[:,][:,5*0+3]
EigenValImL2g0010201050 = dataL2g0010201050[:,][:,5*0+4]
"""
MaxEigenValImL2g0011010 = np.zeros((4))
MaxEigenValImL2g0011020 = np.zeros((4))
MaxEigenValImL2g0011030 = np.zeros((4))
MaxEigenValImL2g0011040 = np.zeros((4))
MaxEigenValImL2g0011050 = np.zeros((4))
MaxEigenValImL2g0011Inf = np.zeros((4))

MaxEigenValImL2g0011010[0] = np.max(EigenValImL2g0010011010)
MaxEigenValImL2g0011010[1] = np.max(EigenValImL2g0010021010)
MaxEigenValImL2g0011010[2] = np.max(EigenValImL2g0010051010)
MaxEigenValImL2g0011010[3] = np.max(EigenValImL2g0010101010)
#MaxEigenValImL2g0011010[4] = np.max(EigenValImL2g0010201010)

MaxEigenValImL2g0011020[0] = np.max(EigenValImL2g0010011020)
MaxEigenValImL2g0011020[1] = np.max(EigenValImL2g0010021020)
MaxEigenValImL2g0011020[2] = np.max(EigenValImL2g0010051020)
MaxEigenValImL2g0011020[3] = np.max(EigenValImL2g0010101020)
#MaxEigenValImL2g0011020[4] = np.max(EigenValImL2g0010201020)

MaxEigenValImL2g0011030[0] = np.max(EigenValImL2g0010011030)
MaxEigenValImL2g0011030[1] = np.max(EigenValImL2g0010021030)
MaxEigenValImL2g0011030[2] = np.max(EigenValImL2g0010051030)
MaxEigenValImL2g0011030[3] = np.max(EigenValImL2g0010101030)
#MaxEigenValImL2g0011030[4] = np.max(EigenValImL2g0010201030)

MaxEigenValImL2g0011040[0] = np.max(EigenValImL2g0010011040)
MaxEigenValImL2g0011040[1] = np.max(EigenValImL2g0010021040)
MaxEigenValImL2g0011040[2] = np.max(EigenValImL2g0010051040)
MaxEigenValImL2g0011040[3] = np.max(EigenValImL2g0010101040)
#MaxEigenValImL2g0011040[4] = np.max(EigenValImL2g0010201040)

MaxEigenValImL2g0011050[0] = np.max(EigenValImL2g0010011050)
MaxEigenValImL2g0011050[1] = np.max(EigenValImL2g0010021050)
MaxEigenValImL2g0011050[2] = np.max(EigenValImL2g0010051050)
MaxEigenValImL2g0011050[3] = np.max(EigenValImL2g0010101050)
#MaxEigenValImL2g0011050[4] = np.max(EigenValImL2g0010201050)

MaxEigenValImL2g0011Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL2g0011010[0],MaxEigenValImL2g0011020[0],MaxEigenValImL2g0011030[0],MaxEigenValImL2g0011040[0],MaxEigenValImL2g0011050[0]], 1)[[1]]
MaxEigenValImL2g0011Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL2g0011010[1],MaxEigenValImL2g0011020[1],MaxEigenValImL2g0011030[1],MaxEigenValImL2g0011040[1],MaxEigenValImL2g0011050[1]], 1)[[1]]
MaxEigenValImL2g0011Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL2g0011010[2],MaxEigenValImL2g0011020[2],MaxEigenValImL2g0011030[2],MaxEigenValImL2g0011040[2],MaxEigenValImL2g0011050[2]], 1)[[1]]
MaxEigenValImL2g0011Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL2g0011010[3],MaxEigenValImL2g0011020[3],MaxEigenValImL2g0011030[3],MaxEigenValImL2g0011040[3],MaxEigenValImL2g0011050[3]], 1)[[1]]
#MaxEigenValImL2g0011Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL2g0011010[4],MaxEigenValImL2g0011020[4],MaxEigenValImL2g0011030[4],MaxEigenValImL2g0011040[4],MaxEigenValImL2g0011050[4]], 1)[[1]]

########################################################################

dataL2g0010011010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK001/N010/HamVals.txt')

MomentumAxL2g0010011010 = dataL2g0010011010[:,][:,5*0+0]
KineticEneL2g0010011010 = dataL2g0010011010[:,][:,5*0+1]
SelfEnergyL2g0010011010 = dataL2g0010011010[:,][:,5*0+2]
EigenValReL2g0010011010 = dataL2g0010011010[:,][:,5*0+3]
EigenValImL2g0010011010 = dataL2g0010011010[:,][:,5*0+4]

dataL2g0010011020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK001/N020/HamVals.txt')

MomentumAxL2g0010011020 = dataL2g0010011020[:,][:,5*0+0]
KineticEneL2g0010011020 = dataL2g0010011020[:,][:,5*0+1]
SelfEnergyL2g0010011020 = dataL2g0010011020[:,][:,5*0+2]
EigenValReL2g0010011020 = dataL2g0010011020[:,][:,5*0+3]
EigenValImL2g0010011020 = dataL2g0010011020[:,][:,5*0+4]

dataL2g0010011030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK001/N030/HamVals.txt')

MomentumAxL2g0010011030 = dataL2g0010011030[:,][:,5*0+0]
KineticEneL2g0010011030 = dataL2g0010011030[:,][:,5*0+1]
SelfEnergyL2g0010011030 = dataL2g0010011030[:,][:,5*0+2]
EigenValReL2g0010011030 = dataL2g0010011030[:,][:,5*0+3]
EigenValImL2g0010011030 = dataL2g0010011030[:,][:,5*0+4]

dataL2g0010011040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK001/N040/HamVals.txt')

MomentumAxL2g0010011040 = dataL2g0010011040[:,][:,5*0+0]
KineticEneL2g0010011040 = dataL2g0010011040[:,][:,5*0+1]
SelfEnergyL2g0010011040 = dataL2g0010011040[:,][:,5*0+2]
EigenValReL2g0010011040 = dataL2g0010011040[:,][:,5*0+3]
EigenValImL2g0010011040 = dataL2g0010011040[:,][:,5*0+4]

dataL2g0010011050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK001/N050/HamVals.txt')

MomentumAxL2g0010011050 = dataL2g0010011050[:,][:,5*0+0]
KineticEneL2g0010011050 = dataL2g0010011050[:,][:,5*0+1]
SelfEnergyL2g0010011050 = dataL2g0010011050[:,][:,5*0+2]
EigenValReL2g0010011050 = dataL2g0010011050[:,][:,5*0+3]
EigenValImL2g0010011050 = dataL2g0010011050[:,][:,5*0+4]

dataL2g0010021010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK002/N010/HamVals.txt')

MomentumAxL2g0010021010 = dataL2g0010021010[:,][:,5*0+0]
KineticEneL2g0010021010 = dataL2g0010021010[:,][:,5*0+1]
SelfEnergyL2g0010021010 = dataL2g0010021010[:,][:,5*0+2]
EigenValReL2g0010021010 = dataL2g0010021010[:,][:,5*0+3]
EigenValImL2g0010021010 = dataL2g0010021010[:,][:,5*0+4]

dataL2g0010021020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK002/N020/HamVals.txt')

MomentumAxL2g0010021020 = dataL2g0010021020[:,][:,5*0+0]
KineticEneL2g0010021020 = dataL2g0010021020[:,][:,5*0+1]
SelfEnergyL2g0010021020 = dataL2g0010021020[:,][:,5*0+2]
EigenValReL2g0010021020 = dataL2g0010021020[:,][:,5*0+3]
EigenValImL2g0010021020 = dataL2g0010021020[:,][:,5*0+4]

dataL2g0010021030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK002/N030/HamVals.txt')

MomentumAxL2g0010021030 = dataL2g0010021030[:,][:,5*0+0]
KineticEneL2g0010021030 = dataL2g0010021030[:,][:,5*0+1]
SelfEnergyL2g0010021030 = dataL2g0010021030[:,][:,5*0+2]
EigenValReL2g0010021030 = dataL2g0010021030[:,][:,5*0+3]
EigenValImL2g0010021030 = dataL2g0010021030[:,][:,5*0+4]

dataL2g0010021040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK002/N040/HamVals.txt')

MomentumAxL2g0010021040 = dataL2g0010021040[:,][:,5*0+0]
KineticEneL2g0010021040 = dataL2g0010021040[:,][:,5*0+1]
SelfEnergyL2g0010021040 = dataL2g0010021040[:,][:,5*0+2]
EigenValReL2g0010021040 = dataL2g0010021040[:,][:,5*0+3]
EigenValImL2g0010021040 = dataL2g0010021040[:,][:,5*0+4]

dataL2g0010021050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK002/N050/HamVals.txt')

MomentumAxL2g0010021050 = dataL2g0010021050[:,][:,5*0+0]
KineticEneL2g0010021050 = dataL2g0010021050[:,][:,5*0+1]
SelfEnergyL2g0010021050 = dataL2g0010021050[:,][:,5*0+2]
EigenValReL2g0010021050 = dataL2g0010021050[:,][:,5*0+3]
EigenValImL2g0010021050 = dataL2g0010021050[:,][:,5*0+4]

dataL2g0010051010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK005/N010/HamVals.txt')

MomentumAxL2g0010051010 = dataL2g0010051010[:,][:,5*0+0]
KineticEneL2g0010051010 = dataL2g0010051010[:,][:,5*0+1]
SelfEnergyL2g0010051010 = dataL2g0010051010[:,][:,5*0+2]
EigenValReL2g0010051010 = dataL2g0010051010[:,][:,5*0+3]
EigenValImL2g0010051010 = dataL2g0010051010[:,][:,5*0+4]

dataL2g0010051020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK005/N020/HamVals.txt')

MomentumAxL2g0010051020 = dataL2g0010051020[:,][:,5*0+0]
KineticEneL2g0010051020 = dataL2g0010051020[:,][:,5*0+1]
SelfEnergyL2g0010051020 = dataL2g0010051020[:,][:,5*0+2]
EigenValReL2g0010051020 = dataL2g0010051020[:,][:,5*0+3]
EigenValImL2g0010051020 = dataL2g0010051020[:,][:,5*0+4]

dataL2g0010051030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK005/N030/HamVals.txt')

MomentumAxL2g0010051030 = dataL2g0010051030[:,][:,5*0+0]
KineticEneL2g0010051030 = dataL2g0010051030[:,][:,5*0+1]
SelfEnergyL2g0010051030 = dataL2g0010051030[:,][:,5*0+2]
EigenValReL2g0010051030 = dataL2g0010051030[:,][:,5*0+3]
EigenValImL2g0010051030 = dataL2g0010051030[:,][:,5*0+4]

dataL2g0010051040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK005/N040/HamVals.txt')

MomentumAxL2g0010051040 = dataL2g0010051040[:,][:,5*0+0]
KineticEneL2g0010051040 = dataL2g0010051040[:,][:,5*0+1]
SelfEnergyL2g0010051040 = dataL2g0010051040[:,][:,5*0+2]
EigenValReL2g0010051040 = dataL2g0010051040[:,][:,5*0+3]
EigenValImL2g0010051040 = dataL2g0010051040[:,][:,5*0+4]

dataL2g0010051050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK005/N050/HamVals.txt')

MomentumAxL2g0010051050 = dataL2g0010051050[:,][:,5*0+0]
KineticEneL2g0010051050 = dataL2g0010051050[:,][:,5*0+1]
SelfEnergyL2g0010051050 = dataL2g0010051050[:,][:,5*0+2]
EigenValReL2g0010051050 = dataL2g0010051050[:,][:,5*0+3]
EigenValImL2g0010051050 = dataL2g0010051050[:,][:,5*0+4]

dataL2g0010101010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK010/N010/HamVals.txt')

MomentumAxL2g0010101010 = dataL2g0010101010[:,][:,5*0+0]
KineticEneL2g0010101010 = dataL2g0010101010[:,][:,5*0+1]
SelfEnergyL2g0010101010 = dataL2g0010101010[:,][:,5*0+2]
EigenValReL2g0010101010 = dataL2g0010101010[:,][:,5*0+3]
EigenValImL2g0010101010 = dataL2g0010101010[:,][:,5*0+4]

dataL2g0010101020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK010/N020/HamVals.txt')

MomentumAxL2g0010101020 = dataL2g0010101020[:,][:,5*0+0]
KineticEneL2g0010101020 = dataL2g0010101020[:,][:,5*0+1]
SelfEnergyL2g0010101020 = dataL2g0010101020[:,][:,5*0+2]
EigenValReL2g0010101020 = dataL2g0010101020[:,][:,5*0+3]
EigenValImL2g0010101020 = dataL2g0010101020[:,][:,5*0+4]

dataL2g0010101030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK010/N030/HamVals.txt')

MomentumAxL2g0010101030 = dataL2g0010101030[:,][:,5*0+0]
KineticEneL2g0010101030 = dataL2g0010101030[:,][:,5*0+1]
SelfEnergyL2g0010101030 = dataL2g0010101030[:,][:,5*0+2]
EigenValReL2g0010101030 = dataL2g0010101030[:,][:,5*0+3]
EigenValImL2g0010101030 = dataL2g0010101030[:,][:,5*0+4]

dataL2g0010101040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK010/N040/HamVals.txt')

MomentumAxL2g0010101040 = dataL2g0010101040[:,][:,5*0+0]
KineticEneL2g0010101040 = dataL2g0010101040[:,][:,5*0+1]
SelfEnergyL2g0010101040 = dataL2g0010101040[:,][:,5*0+2]
EigenValReL2g0010101040 = dataL2g0010101040[:,][:,5*0+3]
EigenValImL2g0010101040 = dataL2g0010101040[:,][:,5*0+4]

dataL2g0010101050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK010/N050/HamVals.txt')

MomentumAxL2g0010101050 = dataL2g0010101050[:,][:,5*0+0]
KineticEneL2g0010101050 = dataL2g0010101050[:,][:,5*0+1]
SelfEnergyL2g0010101050 = dataL2g0010101050[:,][:,5*0+2]
EigenValReL2g0010101050 = dataL2g0010101050[:,][:,5*0+3]
EigenValImL2g0010101050 = dataL2g0010101050[:,][:,5*0+4]
"""
dataL2g0010201010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK020/N010/HamVals.txt')

MomentumAxL2g0010201010 = dataL2g0010201010[:,][:,5*0+0]
KineticEneL2g0010201010 = dataL2g0010201010[:,][:,5*0+1]
SelfEnergyL2g0010201010 = dataL2g0010201010[:,][:,5*0+2]
EigenValReL2g0010201010 = dataL2g0010201010[:,][:,5*0+3]
EigenValImL2g0010201010 = dataL2g0010201010[:,][:,5*0+4]

dataL2g0010201020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK020/N020/HamVals.txt')

MomentumAxL2g0010201020 = dataL2g0010201020[:,][:,5*0+0]
KineticEneL2g0010201020 = dataL2g0010201020[:,][:,5*0+1]
SelfEnergyL2g0010201020 = dataL2g0010201020[:,][:,5*0+2]
EigenValReL2g0010201020 = dataL2g0010201020[:,][:,5*0+3]
EigenValImL2g0010201020 = dataL2g0010201020[:,][:,5*0+4]

dataL2g0010201030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK020/N030/HamVals.txt')

MomentumAxL2g0010201030 = dataL2g0010201030[:,][:,5*0+0]
KineticEneL2g0010201030 = dataL2g0010201030[:,][:,5*0+1]
SelfEnergyL2g0010201030 = dataL2g0010201030[:,][:,5*0+2]
EigenValReL2g0010201030 = dataL2g0010201030[:,][:,5*0+3]
EigenValImL2g0010201030 = dataL2g0010201030[:,][:,5*0+4]

dataL2g0010201040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK020/N040/HamVals.txt')

MomentumAxL2g0010201040 = dataL2g0010201040[:,][:,5*0+0]
KineticEneL2g0010201040 = dataL2g0010201040[:,][:,5*0+1]
SelfEnergyL2g0010201040 = dataL2g0010201040[:,][:,5*0+2]
EigenValReL2g0010201040 = dataL2g0010201040[:,][:,5*0+3]
EigenValImL2g0010201040 = dataL2g0010201040[:,][:,5*0+4]

dataL2g0010201050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK002/aK020/N050/HamVals.txt')

MomentumAxL2g0010201050 = dataL2g0010201050[:,][:,5*0+0]
KineticEneL2g0010201050 = dataL2g0010201050[:,][:,5*0+1]
SelfEnergyL2g0010201050 = dataL2g0010201050[:,][:,5*0+2]
EigenValReL2g0010201050 = dataL2g0010201050[:,][:,5*0+3]
EigenValImL2g0010201050 = dataL2g0010201050[:,][:,5*0+4]
"""
MaxEigenValImL2g0021010 = np.zeros((4))
MaxEigenValImL2g0021020 = np.zeros((4))
MaxEigenValImL2g0021030 = np.zeros((4))
MaxEigenValImL2g0021040 = np.zeros((4))
MaxEigenValImL2g0021050 = np.zeros((4))
MaxEigenValImL2g0021Inf = np.zeros((4))

MaxEigenValImL2g0021010[0] = np.max(EigenValImL2g0010011010)
MaxEigenValImL2g0021010[1] = np.max(EigenValImL2g0010021010)
MaxEigenValImL2g0021010[2] = np.max(EigenValImL2g0010051010)
MaxEigenValImL2g0021010[3] = np.max(EigenValImL2g0010101010)
#MaxEigenValImL2g0021010[4] = np.max(EigenValImL2g0010201010)

MaxEigenValImL2g0021020[0] = np.max(EigenValImL2g0010011020)
MaxEigenValImL2g0021020[1] = np.max(EigenValImL2g0010021020)
MaxEigenValImL2g0021020[2] = np.max(EigenValImL2g0010051020)
MaxEigenValImL2g0021020[3] = np.max(EigenValImL2g0010101020)
#MaxEigenValImL2g0021020[4] = np.max(EigenValImL2g0010201020)

MaxEigenValImL2g0021030[0] = np.max(EigenValImL2g0010011030)
MaxEigenValImL2g0021030[1] = np.max(EigenValImL2g0010021030)
MaxEigenValImL2g0021030[2] = np.max(EigenValImL2g0010051030)
MaxEigenValImL2g0021030[3] = np.max(EigenValImL2g0010101030)
#MaxEigenValImL2g0021030[4] = np.max(EigenValImL2g0010201030)

MaxEigenValImL2g0021040[0] = np.max(EigenValImL2g0010011040)
MaxEigenValImL2g0021040[1] = np.max(EigenValImL2g0010021040)
MaxEigenValImL2g0021040[2] = np.max(EigenValImL2g0010051040)
MaxEigenValImL2g0021040[3] = np.max(EigenValImL2g0010101040)
#MaxEigenValImL2g0021040[4] = np.max(EigenValImL2g0010201040)

MaxEigenValImL2g0021050[0] = np.max(EigenValImL2g0010011050)
MaxEigenValImL2g0021050[1] = np.max(EigenValImL2g0010021050)
MaxEigenValImL2g0021050[2] = np.max(EigenValImL2g0010051050)
MaxEigenValImL2g0021050[3] = np.max(EigenValImL2g0010101050)
#MaxEigenValImL2g0021050[4] = np.max(EigenValImL2g0010201050)

MaxEigenValImL2g0021Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL2g0021010[0],MaxEigenValImL2g0021020[0],MaxEigenValImL2g0021030[0],MaxEigenValImL2g0021040[0],MaxEigenValImL2g0021050[0]], 1)[[1]]
MaxEigenValImL2g0021Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL2g0021010[1],MaxEigenValImL2g0021020[1],MaxEigenValImL2g0021030[1],MaxEigenValImL2g0021040[1],MaxEigenValImL2g0021050[1]], 1)[[1]]
MaxEigenValImL2g0021Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL2g0021010[2],MaxEigenValImL2g0021020[2],MaxEigenValImL2g0021030[2],MaxEigenValImL2g0021040[2],MaxEigenValImL2g0021050[2]], 1)[[1]]
MaxEigenValImL2g0021Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL2g0021010[3],MaxEigenValImL2g0021020[3],MaxEigenValImL2g0021030[3],MaxEigenValImL2g0021040[3],MaxEigenValImL2g0021050[3]], 1)[[1]]
#MaxEigenValImL2g0021Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL2g0021010[4],MaxEigenValImL2g0021020[4],MaxEigenValImL2g0021030[4],MaxEigenValImL2g0021040[4],MaxEigenValImL2g0021050[4]], 1)[[1]]

########################################################################

dataL2g0010011010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK001/N010/HamVals.txt')

MomentumAxL2g0010011010 = dataL2g0010011010[:,][:,5*0+0]
KineticEneL2g0010011010 = dataL2g0010011010[:,][:,5*0+1]
SelfEnergyL2g0010011010 = dataL2g0010011010[:,][:,5*0+2]
EigenValReL2g0010011010 = dataL2g0010011010[:,][:,5*0+3]
EigenValImL2g0010011010 = dataL2g0010011010[:,][:,5*0+4]

dataL2g0010011020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK001/N020/HamVals.txt')

MomentumAxL2g0010011020 = dataL2g0010011020[:,][:,5*0+0]
KineticEneL2g0010011020 = dataL2g0010011020[:,][:,5*0+1]
SelfEnergyL2g0010011020 = dataL2g0010011020[:,][:,5*0+2]
EigenValReL2g0010011020 = dataL2g0010011020[:,][:,5*0+3]
EigenValImL2g0010011020 = dataL2g0010011020[:,][:,5*0+4]

dataL2g0010011030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK001/N030/HamVals.txt')

MomentumAxL2g0010011030 = dataL2g0010011030[:,][:,5*0+0]
KineticEneL2g0010011030 = dataL2g0010011030[:,][:,5*0+1]
SelfEnergyL2g0010011030 = dataL2g0010011030[:,][:,5*0+2]
EigenValReL2g0010011030 = dataL2g0010011030[:,][:,5*0+3]
EigenValImL2g0010011030 = dataL2g0010011030[:,][:,5*0+4]

dataL2g0010011040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK001/N040/HamVals.txt')

MomentumAxL2g0010011040 = dataL2g0010011040[:,][:,5*0+0]
KineticEneL2g0010011040 = dataL2g0010011040[:,][:,5*0+1]
SelfEnergyL2g0010011040 = dataL2g0010011040[:,][:,5*0+2]
EigenValReL2g0010011040 = dataL2g0010011040[:,][:,5*0+3]
EigenValImL2g0010011040 = dataL2g0010011040[:,][:,5*0+4]

dataL2g0010011050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK001/N050/HamVals.txt')

MomentumAxL2g0010011050 = dataL2g0010011050[:,][:,5*0+0]
KineticEneL2g0010011050 = dataL2g0010011050[:,][:,5*0+1]
SelfEnergyL2g0010011050 = dataL2g0010011050[:,][:,5*0+2]
EigenValReL2g0010011050 = dataL2g0010011050[:,][:,5*0+3]
EigenValImL2g0010011050 = dataL2g0010011050[:,][:,5*0+4]

dataL2g0010021010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK002/N010/HamVals.txt')

MomentumAxL2g0010021010 = dataL2g0010021010[:,][:,5*0+0]
KineticEneL2g0010021010 = dataL2g0010021010[:,][:,5*0+1]
SelfEnergyL2g0010021010 = dataL2g0010021010[:,][:,5*0+2]
EigenValReL2g0010021010 = dataL2g0010021010[:,][:,5*0+3]
EigenValImL2g0010021010 = dataL2g0010021010[:,][:,5*0+4]

dataL2g0010021020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK002/N020/HamVals.txt')

MomentumAxL2g0010021020 = dataL2g0010021020[:,][:,5*0+0]
KineticEneL2g0010021020 = dataL2g0010021020[:,][:,5*0+1]
SelfEnergyL2g0010021020 = dataL2g0010021020[:,][:,5*0+2]
EigenValReL2g0010021020 = dataL2g0010021020[:,][:,5*0+3]
EigenValImL2g0010021020 = dataL2g0010021020[:,][:,5*0+4]

dataL2g0010021030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK002/N030/HamVals.txt')

MomentumAxL2g0010021030 = dataL2g0010021030[:,][:,5*0+0]
KineticEneL2g0010021030 = dataL2g0010021030[:,][:,5*0+1]
SelfEnergyL2g0010021030 = dataL2g0010021030[:,][:,5*0+2]
EigenValReL2g0010021030 = dataL2g0010021030[:,][:,5*0+3]
EigenValImL2g0010021030 = dataL2g0010021030[:,][:,5*0+4]

dataL2g0010021040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK002/N040/HamVals.txt')

MomentumAxL2g0010021040 = dataL2g0010021040[:,][:,5*0+0]
KineticEneL2g0010021040 = dataL2g0010021040[:,][:,5*0+1]
SelfEnergyL2g0010021040 = dataL2g0010021040[:,][:,5*0+2]
EigenValReL2g0010021040 = dataL2g0010021040[:,][:,5*0+3]
EigenValImL2g0010021040 = dataL2g0010021040[:,][:,5*0+4]

dataL2g0010021050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK002/N050/HamVals.txt')

MomentumAxL2g0010021050 = dataL2g0010021050[:,][:,5*0+0]
KineticEneL2g0010021050 = dataL2g0010021050[:,][:,5*0+1]
SelfEnergyL2g0010021050 = dataL2g0010021050[:,][:,5*0+2]
EigenValReL2g0010021050 = dataL2g0010021050[:,][:,5*0+3]
EigenValImL2g0010021050 = dataL2g0010021050[:,][:,5*0+4]

dataL2g0010051010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK005/N010/HamVals.txt')

MomentumAxL2g0010051010 = dataL2g0010051010[:,][:,5*0+0]
KineticEneL2g0010051010 = dataL2g0010051010[:,][:,5*0+1]
SelfEnergyL2g0010051010 = dataL2g0010051010[:,][:,5*0+2]
EigenValReL2g0010051010 = dataL2g0010051010[:,][:,5*0+3]
EigenValImL2g0010051010 = dataL2g0010051010[:,][:,5*0+4]

dataL2g0010051020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK005/N020/HamVals.txt')

MomentumAxL2g0010051020 = dataL2g0010051020[:,][:,5*0+0]
KineticEneL2g0010051020 = dataL2g0010051020[:,][:,5*0+1]
SelfEnergyL2g0010051020 = dataL2g0010051020[:,][:,5*0+2]
EigenValReL2g0010051020 = dataL2g0010051020[:,][:,5*0+3]
EigenValImL2g0010051020 = dataL2g0010051020[:,][:,5*0+4]

dataL2g0010051030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK005/N030/HamVals.txt')

MomentumAxL2g0010051030 = dataL2g0010051030[:,][:,5*0+0]
KineticEneL2g0010051030 = dataL2g0010051030[:,][:,5*0+1]
SelfEnergyL2g0010051030 = dataL2g0010051030[:,][:,5*0+2]
EigenValReL2g0010051030 = dataL2g0010051030[:,][:,5*0+3]
EigenValImL2g0010051030 = dataL2g0010051030[:,][:,5*0+4]

dataL2g0010051040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK005/N040/HamVals.txt')

MomentumAxL2g0010051040 = dataL2g0010051040[:,][:,5*0+0]
KineticEneL2g0010051040 = dataL2g0010051040[:,][:,5*0+1]
SelfEnergyL2g0010051040 = dataL2g0010051040[:,][:,5*0+2]
EigenValReL2g0010051040 = dataL2g0010051040[:,][:,5*0+3]
EigenValImL2g0010051040 = dataL2g0010051040[:,][:,5*0+4]

dataL2g0010051050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK005/N050/HamVals.txt')

MomentumAxL2g0010051050 = dataL2g0010051050[:,][:,5*0+0]
KineticEneL2g0010051050 = dataL2g0010051050[:,][:,5*0+1]
SelfEnergyL2g0010051050 = dataL2g0010051050[:,][:,5*0+2]
EigenValReL2g0010051050 = dataL2g0010051050[:,][:,5*0+3]
EigenValImL2g0010051050 = dataL2g0010051050[:,][:,5*0+4]

dataL2g0010101010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK010/N010/HamVals.txt')

MomentumAxL2g0010101010 = dataL2g0010101010[:,][:,5*0+0]
KineticEneL2g0010101010 = dataL2g0010101010[:,][:,5*0+1]
SelfEnergyL2g0010101010 = dataL2g0010101010[:,][:,5*0+2]
EigenValReL2g0010101010 = dataL2g0010101010[:,][:,5*0+3]
EigenValImL2g0010101010 = dataL2g0010101010[:,][:,5*0+4]

dataL2g0010101020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK010/N020/HamVals.txt')

MomentumAxL2g0010101020 = dataL2g0010101020[:,][:,5*0+0]
KineticEneL2g0010101020 = dataL2g0010101020[:,][:,5*0+1]
SelfEnergyL2g0010101020 = dataL2g0010101020[:,][:,5*0+2]
EigenValReL2g0010101020 = dataL2g0010101020[:,][:,5*0+3]
EigenValImL2g0010101020 = dataL2g0010101020[:,][:,5*0+4]

dataL2g0010101030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK010/N030/HamVals.txt')

MomentumAxL2g0010101030 = dataL2g0010101030[:,][:,5*0+0]
KineticEneL2g0010101030 = dataL2g0010101030[:,][:,5*0+1]
SelfEnergyL2g0010101030 = dataL2g0010101030[:,][:,5*0+2]
EigenValReL2g0010101030 = dataL2g0010101030[:,][:,5*0+3]
EigenValImL2g0010101030 = dataL2g0010101030[:,][:,5*0+4]

dataL2g0010101040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK010/N040/HamVals.txt')

MomentumAxL2g0010101040 = dataL2g0010101040[:,][:,5*0+0]
KineticEneL2g0010101040 = dataL2g0010101040[:,][:,5*0+1]
SelfEnergyL2g0010101040 = dataL2g0010101040[:,][:,5*0+2]
EigenValReL2g0010101040 = dataL2g0010101040[:,][:,5*0+3]
EigenValImL2g0010101040 = dataL2g0010101040[:,][:,5*0+4]

dataL2g0010101050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK010/N050/HamVals.txt')

MomentumAxL2g0010101050 = dataL2g0010101050[:,][:,5*0+0]
KineticEneL2g0010101050 = dataL2g0010101050[:,][:,5*0+1]
SelfEnergyL2g0010101050 = dataL2g0010101050[:,][:,5*0+2]
EigenValReL2g0010101050 = dataL2g0010101050[:,][:,5*0+3]
EigenValImL2g0010101050 = dataL2g0010101050[:,][:,5*0+4]
"""
dataL2g0010201010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK020/N010/HamVals.txt')

MomentumAxL2g0010201010 = dataL2g0010201010[:,][:,5*0+0]
KineticEneL2g0010201010 = dataL2g0010201010[:,][:,5*0+1]
SelfEnergyL2g0010201010 = dataL2g0010201010[:,][:,5*0+2]
EigenValReL2g0010201010 = dataL2g0010201010[:,][:,5*0+3]
EigenValImL2g0010201010 = dataL2g0010201010[:,][:,5*0+4]

dataL2g0010201020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK020/N020/HamVals.txt')

MomentumAxL2g0010201020 = dataL2g0010201020[:,][:,5*0+0]
KineticEneL2g0010201020 = dataL2g0010201020[:,][:,5*0+1]
SelfEnergyL2g0010201020 = dataL2g0010201020[:,][:,5*0+2]
EigenValReL2g0010201020 = dataL2g0010201020[:,][:,5*0+3]
EigenValImL2g0010201020 = dataL2g0010201020[:,][:,5*0+4]

dataL2g0010201030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK020/N030/HamVals.txt')

MomentumAxL2g0010201030 = dataL2g0010201030[:,][:,5*0+0]
KineticEneL2g0010201030 = dataL2g0010201030[:,][:,5*0+1]
SelfEnergyL2g0010201030 = dataL2g0010201030[:,][:,5*0+2]
EigenValReL2g0010201030 = dataL2g0010201030[:,][:,5*0+3]
EigenValImL2g0010201030 = dataL2g0010201030[:,][:,5*0+4]

dataL2g0010201040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK020/N040/HamVals.txt')

MomentumAxL2g0010201040 = dataL2g0010201040[:,][:,5*0+0]
KineticEneL2g0010201040 = dataL2g0010201040[:,][:,5*0+1]
SelfEnergyL2g0010201040 = dataL2g0010201040[:,][:,5*0+2]
EigenValReL2g0010201040 = dataL2g0010201040[:,][:,5*0+3]
EigenValImL2g0010201040 = dataL2g0010201040[:,][:,5*0+4]

dataL2g0010201050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK005/aK020/N050/HamVals.txt')

MomentumAxL2g0010201050 = dataL2g0010201050[:,][:,5*0+0]
KineticEneL2g0010201050 = dataL2g0010201050[:,][:,5*0+1]
SelfEnergyL2g0010201050 = dataL2g0010201050[:,][:,5*0+2]
EigenValReL2g0010201050 = dataL2g0010201050[:,][:,5*0+3]
EigenValImL2g0010201050 = dataL2g0010201050[:,][:,5*0+4]
"""
MaxEigenValImL2g0051010 = np.zeros((4))
MaxEigenValImL2g0051020 = np.zeros((4))
MaxEigenValImL2g0051030 = np.zeros((4))
MaxEigenValImL2g0051040 = np.zeros((4))
MaxEigenValImL2g0051050 = np.zeros((4))
MaxEigenValImL2g0051Inf = np.zeros((4))

MaxEigenValImL2g0051010[0] = np.max(EigenValImL2g0010011010)
MaxEigenValImL2g0051010[1] = np.max(EigenValImL2g0010021010)
MaxEigenValImL2g0051010[2] = np.max(EigenValImL2g0010051010)
MaxEigenValImL2g0051010[3] = np.max(EigenValImL2g0010101010)
#MaxEigenValImL2g0051010[4] = np.max(EigenValImL2g0010201010)

MaxEigenValImL2g0051020[0] = np.max(EigenValImL2g0010011020)
MaxEigenValImL2g0051020[1] = np.max(EigenValImL2g0010021020)
MaxEigenValImL2g0051020[2] = np.max(EigenValImL2g0010051020)
MaxEigenValImL2g0051020[3] = np.max(EigenValImL2g0010101020)
#MaxEigenValImL2g0051020[4] = np.max(EigenValImL2g0010201020)

MaxEigenValImL2g0051030[0] = np.max(EigenValImL2g0010011030)
MaxEigenValImL2g0051030[1] = np.max(EigenValImL2g0010021030)
MaxEigenValImL2g0051030[2] = np.max(EigenValImL2g0010051030)
MaxEigenValImL2g0051030[3] = np.max(EigenValImL2g0010101030)
#MaxEigenValImL2g0051030[4] = np.max(EigenValImL2g0010201030)

MaxEigenValImL2g0051040[0] = np.max(EigenValImL2g0010011040)
MaxEigenValImL2g0051040[1] = np.max(EigenValImL2g0010021040)
MaxEigenValImL2g0051040[2] = np.max(EigenValImL2g0010051040)
MaxEigenValImL2g0051040[3] = np.max(EigenValImL2g0010101040)
#MaxEigenValImL2g0051040[4] = np.max(EigenValImL2g0010201040)

MaxEigenValImL2g0051050[0] = np.max(EigenValImL2g0010011050)
MaxEigenValImL2g0051050[1] = np.max(EigenValImL2g0010021050)
MaxEigenValImL2g0051050[2] = np.max(EigenValImL2g0010051050)
MaxEigenValImL2g0051050[3] = np.max(EigenValImL2g0010101050)
#MaxEigenValImL2g0051050[4] = np.max(EigenValImL2g0010201050)

MaxEigenValImL2g0051Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL2g0051010[0],MaxEigenValImL2g0051020[0],MaxEigenValImL2g0051030[0],MaxEigenValImL2g0051040[0],MaxEigenValImL2g0051050[0]], 1)[[1]]
MaxEigenValImL2g0051Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL2g0051010[1],MaxEigenValImL2g0051020[1],MaxEigenValImL2g0051030[1],MaxEigenValImL2g0051040[1],MaxEigenValImL2g0051050[1]], 1)[[1]]
MaxEigenValImL2g0051Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL2g0051010[2],MaxEigenValImL2g0051020[2],MaxEigenValImL2g0051030[2],MaxEigenValImL2g0051040[2],MaxEigenValImL2g0051050[2]], 1)[[1]]
MaxEigenValImL2g0051Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL2g0051010[3],MaxEigenValImL2g0051020[3],MaxEigenValImL2g0051030[3],MaxEigenValImL2g0051040[3],MaxEigenValImL2g0051050[3]], 1)[[1]]
#MaxEigenValImL2g0051Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL2g0051010[4],MaxEigenValImL2g0051020[4],MaxEigenValImL2g0051030[4],MaxEigenValImL2g0051040[4],MaxEigenValImL2g0051050[4]], 1)[[1]]

########################################################################

dataL2g0010011010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK001/N010/HamVals.txt')

MomentumAxL2g0010011010 = dataL2g0010011010[:,][:,5*0+0]
KineticEneL2g0010011010 = dataL2g0010011010[:,][:,5*0+1]
SelfEnergyL2g0010011010 = dataL2g0010011010[:,][:,5*0+2]
EigenValReL2g0010011010 = dataL2g0010011010[:,][:,5*0+3]
EigenValImL2g0010011010 = dataL2g0010011010[:,][:,5*0+4]

dataL2g0010011020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK001/N020/HamVals.txt')

MomentumAxL2g0010011020 = dataL2g0010011020[:,][:,5*0+0]
KineticEneL2g0010011020 = dataL2g0010011020[:,][:,5*0+1]
SelfEnergyL2g0010011020 = dataL2g0010011020[:,][:,5*0+2]
EigenValReL2g0010011020 = dataL2g0010011020[:,][:,5*0+3]
EigenValImL2g0010011020 = dataL2g0010011020[:,][:,5*0+4]

dataL2g0010011030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK001/N030/HamVals.txt')

MomentumAxL2g0010011030 = dataL2g0010011030[:,][:,5*0+0]
KineticEneL2g0010011030 = dataL2g0010011030[:,][:,5*0+1]
SelfEnergyL2g0010011030 = dataL2g0010011030[:,][:,5*0+2]
EigenValReL2g0010011030 = dataL2g0010011030[:,][:,5*0+3]
EigenValImL2g0010011030 = dataL2g0010011030[:,][:,5*0+4]

dataL2g0010011040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK001/N040/HamVals.txt')

MomentumAxL2g0010011040 = dataL2g0010011040[:,][:,5*0+0]
KineticEneL2g0010011040 = dataL2g0010011040[:,][:,5*0+1]
SelfEnergyL2g0010011040 = dataL2g0010011040[:,][:,5*0+2]
EigenValReL2g0010011040 = dataL2g0010011040[:,][:,5*0+3]
EigenValImL2g0010011040 = dataL2g0010011040[:,][:,5*0+4]

dataL2g0010011050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK001/N050/HamVals.txt')

MomentumAxL2g0010011050 = dataL2g0010011050[:,][:,5*0+0]
KineticEneL2g0010011050 = dataL2g0010011050[:,][:,5*0+1]
SelfEnergyL2g0010011050 = dataL2g0010011050[:,][:,5*0+2]
EigenValReL2g0010011050 = dataL2g0010011050[:,][:,5*0+3]
EigenValImL2g0010011050 = dataL2g0010011050[:,][:,5*0+4]

dataL2g0010021010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK002/N010/HamVals.txt')

MomentumAxL2g0010021010 = dataL2g0010021010[:,][:,5*0+0]
KineticEneL2g0010021010 = dataL2g0010021010[:,][:,5*0+1]
SelfEnergyL2g0010021010 = dataL2g0010021010[:,][:,5*0+2]
EigenValReL2g0010021010 = dataL2g0010021010[:,][:,5*0+3]
EigenValImL2g0010021010 = dataL2g0010021010[:,][:,5*0+4]

dataL2g0010021020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK002/N020/HamVals.txt')

MomentumAxL2g0010021020 = dataL2g0010021020[:,][:,5*0+0]
KineticEneL2g0010021020 = dataL2g0010021020[:,][:,5*0+1]
SelfEnergyL2g0010021020 = dataL2g0010021020[:,][:,5*0+2]
EigenValReL2g0010021020 = dataL2g0010021020[:,][:,5*0+3]
EigenValImL2g0010021020 = dataL2g0010021020[:,][:,5*0+4]

dataL2g0010021030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK002/N030/HamVals.txt')

MomentumAxL2g0010021030 = dataL2g0010021030[:,][:,5*0+0]
KineticEneL2g0010021030 = dataL2g0010021030[:,][:,5*0+1]
SelfEnergyL2g0010021030 = dataL2g0010021030[:,][:,5*0+2]
EigenValReL2g0010021030 = dataL2g0010021030[:,][:,5*0+3]
EigenValImL2g0010021030 = dataL2g0010021030[:,][:,5*0+4]

dataL2g0010021040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK002/N040/HamVals.txt')

MomentumAxL2g0010021040 = dataL2g0010021040[:,][:,5*0+0]
KineticEneL2g0010021040 = dataL2g0010021040[:,][:,5*0+1]
SelfEnergyL2g0010021040 = dataL2g0010021040[:,][:,5*0+2]
EigenValReL2g0010021040 = dataL2g0010021040[:,][:,5*0+3]
EigenValImL2g0010021040 = dataL2g0010021040[:,][:,5*0+4]

dataL2g0010021050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK002/N050/HamVals.txt')

MomentumAxL2g0010021050 = dataL2g0010021050[:,][:,5*0+0]
KineticEneL2g0010021050 = dataL2g0010021050[:,][:,5*0+1]
SelfEnergyL2g0010021050 = dataL2g0010021050[:,][:,5*0+2]
EigenValReL2g0010021050 = dataL2g0010021050[:,][:,5*0+3]
EigenValImL2g0010021050 = dataL2g0010021050[:,][:,5*0+4]

dataL2g0010051010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK005/N010/HamVals.txt')

MomentumAxL2g0010051010 = dataL2g0010051010[:,][:,5*0+0]
KineticEneL2g0010051010 = dataL2g0010051010[:,][:,5*0+1]
SelfEnergyL2g0010051010 = dataL2g0010051010[:,][:,5*0+2]
EigenValReL2g0010051010 = dataL2g0010051010[:,][:,5*0+3]
EigenValImL2g0010051010 = dataL2g0010051010[:,][:,5*0+4]

dataL2g0010051020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK005/N020/HamVals.txt')

MomentumAxL2g0010051020 = dataL2g0010051020[:,][:,5*0+0]
KineticEneL2g0010051020 = dataL2g0010051020[:,][:,5*0+1]
SelfEnergyL2g0010051020 = dataL2g0010051020[:,][:,5*0+2]
EigenValReL2g0010051020 = dataL2g0010051020[:,][:,5*0+3]
EigenValImL2g0010051020 = dataL2g0010051020[:,][:,5*0+4]

dataL2g0010051030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK005/N030/HamVals.txt')

MomentumAxL2g0010051030 = dataL2g0010051030[:,][:,5*0+0]
KineticEneL2g0010051030 = dataL2g0010051030[:,][:,5*0+1]
SelfEnergyL2g0010051030 = dataL2g0010051030[:,][:,5*0+2]
EigenValReL2g0010051030 = dataL2g0010051030[:,][:,5*0+3]
EigenValImL2g0010051030 = dataL2g0010051030[:,][:,5*0+4]

dataL2g0010051040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK005/N040/HamVals.txt')

MomentumAxL2g0010051040 = dataL2g0010051040[:,][:,5*0+0]
KineticEneL2g0010051040 = dataL2g0010051040[:,][:,5*0+1]
SelfEnergyL2g0010051040 = dataL2g0010051040[:,][:,5*0+2]
EigenValReL2g0010051040 = dataL2g0010051040[:,][:,5*0+3]
EigenValImL2g0010051040 = dataL2g0010051040[:,][:,5*0+4]

dataL2g0010051050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK005/N050/HamVals.txt')

MomentumAxL2g0010051050 = dataL2g0010051050[:,][:,5*0+0]
KineticEneL2g0010051050 = dataL2g0010051050[:,][:,5*0+1]
SelfEnergyL2g0010051050 = dataL2g0010051050[:,][:,5*0+2]
EigenValReL2g0010051050 = dataL2g0010051050[:,][:,5*0+3]
EigenValImL2g0010051050 = dataL2g0010051050[:,][:,5*0+4]

dataL2g0010101010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK010/N010/HamVals.txt')

MomentumAxL2g0010101010 = dataL2g0010101010[:,][:,5*0+0]
KineticEneL2g0010101010 = dataL2g0010101010[:,][:,5*0+1]
SelfEnergyL2g0010101010 = dataL2g0010101010[:,][:,5*0+2]
EigenValReL2g0010101010 = dataL2g0010101010[:,][:,5*0+3]
EigenValImL2g0010101010 = dataL2g0010101010[:,][:,5*0+4]

dataL2g0010101020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK010/N020/HamVals.txt')

MomentumAxL2g0010101020 = dataL2g0010101020[:,][:,5*0+0]
KineticEneL2g0010101020 = dataL2g0010101020[:,][:,5*0+1]
SelfEnergyL2g0010101020 = dataL2g0010101020[:,][:,5*0+2]
EigenValReL2g0010101020 = dataL2g0010101020[:,][:,5*0+3]
EigenValImL2g0010101020 = dataL2g0010101020[:,][:,5*0+4]

dataL2g0010101030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK010/N030/HamVals.txt')

MomentumAxL2g0010101030 = dataL2g0010101030[:,][:,5*0+0]
KineticEneL2g0010101030 = dataL2g0010101030[:,][:,5*0+1]
SelfEnergyL2g0010101030 = dataL2g0010101030[:,][:,5*0+2]
EigenValReL2g0010101030 = dataL2g0010101030[:,][:,5*0+3]
EigenValImL2g0010101030 = dataL2g0010101030[:,][:,5*0+4]

dataL2g0010101040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK010/N040/HamVals.txt')

MomentumAxL2g0010101040 = dataL2g0010101040[:,][:,5*0+0]
KineticEneL2g0010101040 = dataL2g0010101040[:,][:,5*0+1]
SelfEnergyL2g0010101040 = dataL2g0010101040[:,][:,5*0+2]
EigenValReL2g0010101040 = dataL2g0010101040[:,][:,5*0+3]
EigenValImL2g0010101040 = dataL2g0010101040[:,][:,5*0+4]

dataL2g0010101050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK010/N050/HamVals.txt')

MomentumAxL2g0010101050 = dataL2g0010101050[:,][:,5*0+0]
KineticEneL2g0010101050 = dataL2g0010101050[:,][:,5*0+1]
SelfEnergyL2g0010101050 = dataL2g0010101050[:,][:,5*0+2]
EigenValReL2g0010101050 = dataL2g0010101050[:,][:,5*0+3]
EigenValImL2g0010101050 = dataL2g0010101050[:,][:,5*0+4]
"""
dataL2g0010201010 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK020/N010/HamVals.txt')

MomentumAxL2g0010201010 = dataL2g0010201010[:,][:,5*0+0]
KineticEneL2g0010201010 = dataL2g0010201010[:,][:,5*0+1]
SelfEnergyL2g0010201010 = dataL2g0010201010[:,][:,5*0+2]
EigenValReL2g0010201010 = dataL2g0010201010[:,][:,5*0+3]
EigenValImL2g0010201010 = dataL2g0010201010[:,][:,5*0+4]

dataL2g0010201020 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK020/N020/HamVals.txt')

MomentumAxL2g0010201020 = dataL2g0010201020[:,][:,5*0+0]
KineticEneL2g0010201020 = dataL2g0010201020[:,][:,5*0+1]
SelfEnergyL2g0010201020 = dataL2g0010201020[:,][:,5*0+2]
EigenValReL2g0010201020 = dataL2g0010201020[:,][:,5*0+3]
EigenValImL2g0010201020 = dataL2g0010201020[:,][:,5*0+4]

dataL2g0010201030 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK020/N030/HamVals.txt')

MomentumAxL2g0010201030 = dataL2g0010201030[:,][:,5*0+0]
KineticEneL2g0010201030 = dataL2g0010201030[:,][:,5*0+1]
SelfEnergyL2g0010201030 = dataL2g0010201030[:,][:,5*0+2]
EigenValReL2g0010201030 = dataL2g0010201030[:,][:,5*0+3]
EigenValImL2g0010201030 = dataL2g0010201030[:,][:,5*0+4]

dataL2g0010201040 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK020/N040/HamVals.txt')

MomentumAxL2g0010201040 = dataL2g0010201040[:,][:,5*0+0]
KineticEneL2g0010201040 = dataL2g0010201040[:,][:,5*0+1]
SelfEnergyL2g0010201040 = dataL2g0010201040[:,][:,5*0+2]
EigenValReL2g0010201040 = dataL2g0010201040[:,][:,5*0+3]
EigenValImL2g0010201040 = dataL2g0010201040[:,][:,5*0+4]

dataL2g0010201050 = np.genfromtxt('./TangentMomentum/R=2/L2/gK010/aK020/N050/HamVals.txt')

MomentumAxL2g0010201050 = dataL2g0010201050[:,][:,5*0+0]
KineticEneL2g0010201050 = dataL2g0010201050[:,][:,5*0+1]
SelfEnergyL2g0010201050 = dataL2g0010201050[:,][:,5*0+2]
EigenValReL2g0010201050 = dataL2g0010201050[:,][:,5*0+3]
EigenValImL2g0010201050 = dataL2g0010201050[:,][:,5*0+4]
"""
MaxEigenValImL2g0101010 = np.zeros((4))
MaxEigenValImL2g0101020 = np.zeros((4))
MaxEigenValImL2g0101030 = np.zeros((4))
MaxEigenValImL2g0101040 = np.zeros((4))
MaxEigenValImL2g0101050 = np.zeros((4))
MaxEigenValImL2g0101Inf = np.zeros((4))

MaxEigenValImL2g0101010[0] = np.max(EigenValImL2g0010011010)
MaxEigenValImL2g0101010[1] = np.max(EigenValImL2g0010021010)
MaxEigenValImL2g0101010[2] = np.max(EigenValImL2g0010051010)
MaxEigenValImL2g0101010[3] = np.max(EigenValImL2g0010101010)
#MaxEigenValImL2g0101010[4] = np.max(EigenValImL2g0010201010)

MaxEigenValImL2g0101020[0] = np.max(EigenValImL2g0010011020)
MaxEigenValImL2g0101020[1] = np.max(EigenValImL2g0010021020)
MaxEigenValImL2g0101020[2] = np.max(EigenValImL2g0010051020)
MaxEigenValImL2g0101020[3] = np.max(EigenValImL2g0010101020)
#MaxEigenValImL2g0101020[4] = np.max(EigenValImL2g0010201020)

MaxEigenValImL2g0101030[0] = np.max(EigenValImL2g0010011030)
MaxEigenValImL2g0101030[1] = np.max(EigenValImL2g0010021030)
MaxEigenValImL2g0101030[2] = np.max(EigenValImL2g0010051030)
MaxEigenValImL2g0101030[3] = np.max(EigenValImL2g0010101030)
#MaxEigenValImL2g0101030[4] = np.max(EigenValImL2g0010201030)

MaxEigenValImL2g0101040[0] = np.max(EigenValImL2g0010011040)
MaxEigenValImL2g0101040[1] = np.max(EigenValImL2g0010021040)
MaxEigenValImL2g0101040[2] = np.max(EigenValImL2g0010051040)
MaxEigenValImL2g0101040[3] = np.max(EigenValImL2g0010101040)
#MaxEigenValImL2g0101040[4] = np.max(EigenValImL2g0010201040)

MaxEigenValImL2g0101050[0] = np.max(EigenValImL2g0010011050)
MaxEigenValImL2g0101050[1] = np.max(EigenValImL2g0010021050)
MaxEigenValImL2g0101050[2] = np.max(EigenValImL2g0010051050)
MaxEigenValImL2g0101050[3] = np.max(EigenValImL2g0010101050)
#MaxEigenValImL2g0101050[4] = np.max(EigenValImL2g0010201050)

MaxEigenValImL2g0101Inf[0] = np.polyfit(fiveSizes, [MaxEigenValImL2g0101010[0],MaxEigenValImL2g0101020[0],MaxEigenValImL2g0101030[0],MaxEigenValImL2g0101040[0],MaxEigenValImL2g0101050[0]], 1)[[1]]
MaxEigenValImL2g0101Inf[1] = np.polyfit(fiveSizes, [MaxEigenValImL2g0101010[1],MaxEigenValImL2g0101020[1],MaxEigenValImL2g0101030[1],MaxEigenValImL2g0101040[1],MaxEigenValImL2g0101050[1]], 1)[[1]]
MaxEigenValImL2g0101Inf[2] = np.polyfit(fiveSizes, [MaxEigenValImL2g0101010[2],MaxEigenValImL2g0101020[2],MaxEigenValImL2g0101030[2],MaxEigenValImL2g0101040[2],MaxEigenValImL2g0101050[2]], 1)[[1]]
MaxEigenValImL2g0101Inf[3] = np.polyfit(fiveSizes, [MaxEigenValImL2g0101010[3],MaxEigenValImL2g0101020[3],MaxEigenValImL2g0101030[3],MaxEigenValImL2g0101040[3],MaxEigenValImL2g0101050[3]], 1)[[1]]
#MaxEigenValImL2g0101Inf[4] = np.polyfit(fiveSizes, [MaxEigenValImL2g0101010[4],MaxEigenValImL2g0101020[4],MaxEigenValImL2g0101030[4],MaxEigenValImL2g0101040[4],MaxEigenValImL2g0101050[4]], 1)[[1]]

########################################################################
########################################################################

Spreading = np.zeros((4))
Spreading[0] = 1
Spreading[1] = 2
Spreading[2] = 5
Spreading[3] = 10

CouplingA = np.zeros((9))
CouplingA[0] = 1/0.2
CouplingA[1] = 1/0.25
CouplingA[2] = 1/0.3
CouplingA[3] = 1/0.4
CouplingA[4] = 1/0.5
CouplingA[5] = 1/1.0
CouplingA[6] = 1/2.0
CouplingA[7] = 1/5.0
CouplingA[8] = 1/10.0

CouplingB = np.zeros((4))
CouplingB[0] = 1/0.25
CouplingB[1] = 1/0.3
CouplingB[2] = 1/0.4
CouplingB[3] = 1/0.5

CouplingAxis = np.linspace(0,4.0,51,endpoint=True)
CouplingAxisA= np.linspace(0,2.0,51,endpoint=True)

########################################################################
########################################################################

def func(x,E0,GK):
    return E0 * np.exp(-GK*x**1)

plt.clf()
fig, axs = plt.subplots(1, 2, figsize=(6, 3), sharey=True)
plt.subplots_adjust(left=0.25,bottom=0.25,right=0.8,top=0.8,wspace=0.1,hspace=0.4)

#axs[0].loglog(CouplingA,[MaxEigenValImL0g000_21Inf[0],MaxEigenValImL0g000_31Inf[0],MaxEigenValImL0g000_41Inf[0],MaxEigenValImL0g000_51Inf[0],MaxEigenValImL0g0011Inf[0],MaxEigenValImL0g0021Inf[0],MaxEigenValImL0g0051Inf[0],MaxEigenValImL0g0101Inf[0]], marker='o',c=[1.0, 0.0, 0.0],ls='-',label='$a_{\\mathcal{K}}=  1$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])#,label='100')
axs[0].semilogy(CouplingA,[MaxEigenValImL0g000_21Inf[0],MaxEigenValImL0g000_251Inf[0],MaxEigenValImL0g000_31Inf[0],MaxEigenValImL0g000_41Inf[0],MaxEigenValImL0g000_51Inf[0],MaxEigenValImL0g0011Inf[0],MaxEigenValImL0g0021Inf[0],MaxEigenValImL0g0051Inf[0],MaxEigenValImL0g0101Inf[0]], marker='o',c=[1.0, 0.0, 0.0],ls='None',label='$a_{\\mathcal{K}}=  1$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])#,label='100')
axs[0].plot(CouplingA,[MaxEigenValImL0g000_21Inf[1],MaxEigenValImL0g000_251Inf[1],MaxEigenValImL0g000_31Inf[1],MaxEigenValImL0g000_41Inf[1],MaxEigenValImL0g000_51Inf[1],MaxEigenValImL0g0011Inf[1],MaxEigenValImL0g0021Inf[1],MaxEigenValImL0g0051Inf[1],MaxEigenValImL0g0101Inf[1]], marker='o',c=[1.0, 0.5, 0.0],ls='None',label='$a_{\\mathcal{K}}=  2$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])#,label='100')
axs[0].plot(CouplingA,[MaxEigenValImL0g000_21Inf[2],MaxEigenValImL0g000_251Inf[2],MaxEigenValImL0g000_31Inf[2],MaxEigenValImL0g000_41Inf[2],MaxEigenValImL0g000_51Inf[2],MaxEigenValImL0g0011Inf[2],MaxEigenValImL0g0021Inf[2],MaxEigenValImL0g0051Inf[2],MaxEigenValImL0g0101Inf[2]], marker='o',c=[0.0, 1.0, 0.0],ls='None',label='$a_{\\mathcal{K}}=  5$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])#,label='100')
axs[0].plot(CouplingA,[MaxEigenValImL0g000_21Inf[3],MaxEigenValImL0g000_251Inf[3],MaxEigenValImL0g000_31Inf[3],MaxEigenValImL0g000_41Inf[3],MaxEigenValImL0g000_51Inf[3],MaxEigenValImL0g0011Inf[3],MaxEigenValImL0g0021Inf[3],MaxEigenValImL0g0051Inf[3],MaxEigenValImL0g0101Inf[3]], marker='o',c=[0.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 10$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])#,label='100')

#FitaK001, CovaK001 = curve_fit(func, CouplingA, [MaxEigenValImL0g000_251Inf[0],MaxEigenValImL0g000_31Inf[0],MaxEigenValImL0g000_41Inf[0],MaxEigenValImL0g000_51Inf[0],MaxEigenValImL0g0011Inf[0],MaxEigenValImL0g0021Inf[0],MaxEigenValImL0g0051Inf[0],MaxEigenValImL0g0101Inf[0]])
#FitaK002, CovaK002 = curve_fit(func, CouplingA, [MaxEigenValImL0g000_251Inf[1],MaxEigenValImL0g000_31Inf[1],MaxEigenValImL0g000_41Inf[1],MaxEigenValImL0g000_51Inf[1],MaxEigenValImL0g0011Inf[1],MaxEigenValImL0g0021Inf[1],MaxEigenValImL0g0051Inf[1],MaxEigenValImL0g0101Inf[1]])
#FitaK005, CovaK005 = curve_fit(func, CouplingA, [MaxEigenValImL0g000_251Inf[2],MaxEigenValImL0g000_31Inf[2],MaxEigenValImL0g000_41Inf[2],MaxEigenValImL0g000_51Inf[2],MaxEigenValImL0g0011Inf[2],MaxEigenValImL0g0021Inf[2],MaxEigenValImL0g0051Inf[2],MaxEigenValImL0g0101Inf[2]])
#FitaK010, CovaK010 = curve_fit(func, CouplingA, [MaxEigenValImL0g000_251Inf[3],MaxEigenValImL0g000_31Inf[3],MaxEigenValImL0g000_41Inf[3],MaxEigenValImL0g000_51Inf[3],MaxEigenValImL0g0011Inf[3],MaxEigenValImL0g0021Inf[3],MaxEigenValImL0g0051Inf[3],MaxEigenValImL0g0101Inf[3]])

axs[0].plot(CouplingB,[MaxEigenValImL0g000_251Inf[0],MaxEigenValImL0g000_31Inf[0],MaxEigenValImL0g000_41Inf[0],MaxEigenValImL0g000_51Inf[0]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[1.0*1.0, 0.0*1.0, 0.0*1.0])#,label='100')
axs[0].plot(CouplingB,[MaxEigenValImL0g000_251Inf[1],MaxEigenValImL0g000_31Inf[1],MaxEigenValImL0g000_41Inf[1],MaxEigenValImL0g000_51Inf[1]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[1.0*1.0, 0.5*1.0, 0.0*1.0])#,label='100')
axs[0].plot(CouplingB,[MaxEigenValImL0g000_251Inf[2],MaxEigenValImL0g000_31Inf[2],MaxEigenValImL0g000_41Inf[2],MaxEigenValImL0g000_51Inf[2]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[0.0*1.0, 1.0*1.0, 0.0*1.0])#,label='100')
axs[0].plot(CouplingB,[MaxEigenValImL0g000_251Inf[3],MaxEigenValImL0g000_31Inf[3],MaxEigenValImL0g000_41Inf[3],MaxEigenValImL0g000_51Inf[3]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[0.0*1.0, 0.4*1.0, 1.0*1.0])#,label='100')

FitaK001, CovaK001 = curve_fit(func, CouplingB, [MaxEigenValImL0g000_251Inf[0],MaxEigenValImL0g000_31Inf[0],MaxEigenValImL0g000_41Inf[0],MaxEigenValImL0g000_51Inf[0]])
FitaK002, CovaK002 = curve_fit(func, CouplingB, [MaxEigenValImL0g000_251Inf[1],MaxEigenValImL0g000_31Inf[1],MaxEigenValImL0g000_41Inf[1],MaxEigenValImL0g000_51Inf[1]])
FitaK005, CovaK005 = curve_fit(func, CouplingB, [MaxEigenValImL0g000_251Inf[2],MaxEigenValImL0g000_31Inf[2],MaxEigenValImL0g000_41Inf[2],MaxEigenValImL0g000_51Inf[2]])
FitaK010, CovaK010 = curve_fit(func, CouplingB, [MaxEigenValImL0g000_251Inf[3],MaxEigenValImL0g000_31Inf[3],MaxEigenValImL0g000_41Inf[3],MaxEigenValImL0g000_51Inf[3]])

print "     L0"
print FitaK001
#print CovaK001
print np.sqrt(np.diag(CovaK001))
print FitaK002
#print CovaK002
print np.sqrt(np.diag(CovaK002))
print FitaK005
#print CovaK005
print np.sqrt(np.diag(CovaK005))
print FitaK010
#print CovaK010
print np.sqrt(np.diag(CovaK010))

axs[0].plot(CouplingAxis, func(CouplingAxis, *FitaK001), marker='.',c=[1.0, 0.0, 0.0],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, *FitaK002), marker='.',c=[1.0, 0.5, 0.0],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, *FitaK005), marker='.',c=[0.0, 1.0, 0.0],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, *FitaK010), marker='.',c=[0.0, 0.0, 1.0],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))

axs[0].plot(CouplingAxis, func(CouplingAxis, 0.28510649/1**2, 4.03), marker='.',c=[1.0/2, 0.0/2, 0.0/2],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, 0.28510649/2**2, 4.03), marker='.',c=[1.0/2, 0.5/2, 0.0/2],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, 0.28510649/5**2, 4.03), marker='.',c=[0.0/2, 1.0/2, 0.0/2],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, 0.28510649/10**2,4.03), marker='.',c=[0.0/2, 0.0/2, 1.0/2],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))

axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.28510649/1**2, 4.03), marker='.',c=[1.0/2, 0.0/2, 0.0/2],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.28510649/2**2, 4.03), marker='.',c=[1.0/2, 0.5/2, 0.0/2],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.28510649/5**2, 4.03), marker='.',c=[0.0/2, 1.0/2, 0.0/2],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.28510649/10**2,4.03), marker='.',c=[0.0/2, 0.0/2, 1.0/2],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))

#axs[0].plot(CouplingAxisA, func(CouplingAxisA, FitaK001[0]-0*np.sqrt(CovaK001[0,0]), FitaK001[1]-0*np.sqrt(CovaK001[1,1])), marker='None',c=[1.0/2, 0.0/2, 0.0/2],ls='-', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
#axs[0].plot(CouplingAxisA, func(CouplingAxisA, FitaK001[0]-np.sqrt(CovaK001[0,0]), FitaK001[1]-np.sqrt(CovaK001[1,1])), marker='None',c=[1.0/2, 0.0/2, 0.0/2],ls='-', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
#axs[0].plot(CouplingAxisA, func(CouplingAxisA, FitaK001[0]+np.sqrt(CovaK001[0,0]), FitaK001[1]+np.sqrt(CovaK001[1,1])), marker='None',c=[1.0/2, 0.0/2, 0.0/2],ls='-', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))

#axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.28510649/1**2, 4.07), marker='.',c=[1.0/1.5, 0.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
#axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.28510649/2**2, 4.07), marker='.',c=[1.0/1.5, 0.5/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
#axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.28510649/5**2, 4.07), marker='.',c=[0.0/1.5, 1.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
#axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.28510649/10**2,4.07), marker='.',c=[0.0/1.5, 0.0/1.5, 1.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))

#axs[0].semilogy(100*Spreading,MaxEigenValImL0g0011Inf, marker='o',c=[1.0, 0.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.01$', markersize=4, linewidth=1)#,label='100')
#axs[0].semilogy(100*Spreading,MaxEigenValImL0g0021Inf, marker='o',c=[1.0, 0.5, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.02$', markersize=4, linewidth=1)#,label='100')
#axs[0].semilogy(100*Spreading,MaxEigenValImL0g0051Inf, marker='o',c=[0.0, 1.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.05$', markersize=4, linewidth=1)#,label='100')
#axs[0].semilogy(100*Spreading,MaxEigenValImL0g0101Inf, marker='o',c=[0.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 0.10$', markersize=4, linewidth=1)#,label='100')

#plt.xlim(left  =0)
#plt.ylim(top=0.09,bottom=0)
#plt.xticks([0.01,0.02,0.05,0.10])
#plt.yticks(np.arange(0.984,+1.004, step=0.002))
#plt.show()

axs[0].set_title("$\\ell=0$" ,fontsize=12, fontname='Times New Roman')

axs[0].grid(True)
axs[0].set_xlim(-0.e+0,+4.1e+0)
axs[0].set_xticks(np.arange(-0.0e+1,+4.01e+0, step=1.e-0))
axs[0].set_ylim(+1e-12,+1e+0)
#axs[0].set_ylim(+1e0,+1.01e+16)
#axs[0].set_yticks([1e0,1e1,1e2,1e3,1e4,1e5,1e6,1e7])

axs[0].legend(bbox_to_anchor=(0.05, +1.3), loc=2, borderaxespad=0., ncol=4, labelspacing=1,handleheight=1, columnspacing=0.1, handletextpad=0.1)
#plt.suptitle('$\\ell=0XXX, g_{\\mathcal{K}}=0.1$', fontsize=20, fontname='Times New Roman')
axs[0].set_xlabel('$1/g_{\\mathcal{K}}$', fontsize=12, fontname='Times New Roman')
axs[0].set_ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}$', fontsize=12, fontname='Times New Roman')
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
Coupling[0] = 1/0.4
Coupling[1] = 1/0.5
Coupling[2] = 1/0.6
Coupling[3] = 1/0.7
Coupling[4] = 1/0.8
Coupling[5] = 1/1.0
Coupling[6] = 1/2.0
Coupling[7] = 1/5.0
Coupling[8] = 1/10.

CouplingC = np.zeros((4))
CouplingC[0] = 1/0.5
CouplingC[1] = 1/0.6
CouplingC[2] = 1/0.7
CouplingC[3] = 1/0.8

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

axs[1].semilogy(
            Coupling,[MaxEigenValImL2g000_41Inf[0],MaxEigenValImL2g000_51Inf[0],MaxEigenValImL2g000_61Inf[0],MaxEigenValImL2g000_71Inf[0],MaxEigenValImL2g000_81Inf[0],MaxEigenValImL2g0011Inf[0],MaxEigenValImL2g0021Inf[0],MaxEigenValImL2g0051Inf[0],MaxEigenValImL2g0101Inf[0]], marker='o',c=[1.0, 0.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.01$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
axs[1].plot(Coupling,[MaxEigenValImL2g000_41Inf[1],MaxEigenValImL2g000_51Inf[1],MaxEigenValImL2g000_61Inf[1],MaxEigenValImL2g000_71Inf[1],MaxEigenValImL2g000_81Inf[1],MaxEigenValImL2g0011Inf[1],MaxEigenValImL2g0021Inf[1],MaxEigenValImL2g0051Inf[1],MaxEigenValImL2g0101Inf[1]], marker='o',c=[1.0, 0.5, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.02$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
axs[1].plot(Coupling,[MaxEigenValImL2g000_41Inf[2],MaxEigenValImL2g000_51Inf[2],MaxEigenValImL2g000_61Inf[2],MaxEigenValImL2g000_71Inf[2],MaxEigenValImL2g000_81Inf[2],MaxEigenValImL2g0011Inf[2],MaxEigenValImL2g0021Inf[2],MaxEigenValImL2g0051Inf[2],MaxEigenValImL2g0101Inf[2]], marker='o',c=[0.0, 1.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.05$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
axs[1].plot(Coupling,[MaxEigenValImL2g000_41Inf[3],MaxEigenValImL2g000_51Inf[3],MaxEigenValImL2g000_61Inf[3],MaxEigenValImL2g000_71Inf[3],MaxEigenValImL2g000_81Inf[3],MaxEigenValImL2g0011Inf[3],MaxEigenValImL2g0021Inf[3],MaxEigenValImL2g0051Inf[3],MaxEigenValImL2g0101Inf[3]], marker='o',c=[0.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 0.10$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])

FitaK001L2, CovaK001L2 = curve_fit(func, CouplingD, [MaxEigenValImL2g000_41Inf[0],MaxEigenValImL2g000_51Inf[0],MaxEigenValImL2g000_61Inf[0],MaxEigenValImL2g000_71Inf[0],MaxEigenValImL2g000_81Inf[0]])
FitaK002L2, CovaK002L2 = curve_fit(func, CouplingC, [MaxEigenValImL2g000_51Inf[1],MaxEigenValImL2g000_61Inf[1],MaxEigenValImL2g000_71Inf[1],MaxEigenValImL2g000_81Inf[1]])
FitaK005L2, CovaK005L2 = curve_fit(func, CouplingC, [MaxEigenValImL2g000_51Inf[2],MaxEigenValImL2g000_61Inf[2],MaxEigenValImL2g000_71Inf[2],MaxEigenValImL2g000_81Inf[2]])
FitaK010L2, CovaK010L2 = curve_fit(func, CouplingC, [MaxEigenValImL2g000_51Inf[3],MaxEigenValImL2g000_61Inf[3],MaxEigenValImL2g000_71Inf[3],MaxEigenValImL2g000_81Inf[3]])

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
print FitaK005L2
#print CovaK005L2
print np.sqrt(np.diag(CovaK005L2))
print FitaK010L2
#print CovaK010L2
print np.sqrt(np.diag(CovaK010L2))

axs[1].plot(CouplingAxisA, func(CouplingAxisA, *FitaK001L2), marker='.',c=[1.0, 0.0, 0.0],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, *FitaK002L2), marker='.',c=[1.0, 0.5, 0.0],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, *FitaK005L2), marker='.',c=[0.0, 1.0, 0.0],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, *FitaK010L2), marker='.',c=[0.0, 0.0, 1.0],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))

axs[1].plot(CouplingD,[MaxEigenValImL2g000_41Inf[0],MaxEigenValImL2g000_51Inf[0],MaxEigenValImL2g000_61Inf[0],MaxEigenValImL2g000_71Inf[0],MaxEigenValImL2g000_81Inf[0]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[1.0*1.0, 0.0*1.0, 0.0*1.0])#,label='100')
axs[1].plot(CouplingC,[MaxEigenValImL2g000_51Inf[1],MaxEigenValImL2g000_61Inf[1],MaxEigenValImL2g000_71Inf[1],MaxEigenValImL2g000_81Inf[1]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[1.0*1.0, 0.5*1.0, 0.0*1.0])#,label='100')
axs[1].plot(CouplingC,[MaxEigenValImL2g000_51Inf[2],MaxEigenValImL2g000_61Inf[2],MaxEigenValImL2g000_71Inf[2],MaxEigenValImL2g000_81Inf[2]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[0.0*1.0, 1.0*1.0, 0.0*1.0])#,label='100')
axs[1].plot(CouplingC,[MaxEigenValImL2g000_51Inf[3],MaxEigenValImL2g000_61Inf[3],MaxEigenValImL2g000_71Inf[3],MaxEigenValImL2g000_81Inf[3]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[0.0*1.0, 0.4*1.0, 1.0*1.0])#,label='100')

#axs[1].plot(CouplingC,[MaxEigenValImL2g000_41Inf[0],MaxEigenValImL2g000_51Inf[0],MaxEigenValImL2g000_61Inf[0],MaxEigenValImL2g000_71Inf[0],MaxEigenValImL2g000_81Inf[0]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[1.0*1.0, 0.0*1.0, 0.0*1.0])#,label='100')
#axs[1].plot(CouplingC,[MaxEigenValImL2g000_41Inf[1],MaxEigenValImL2g000_51Inf[1],MaxEigenValImL2g000_61Inf[1],MaxEigenValImL2g000_71Inf[1],MaxEigenValImL2g000_81Inf[1]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[1.0*1.0, 0.5*1.0, 0.0*1.0])#,label='100')
#axs[1].plot(CouplingC,[MaxEigenValImL2g000_41Inf[2],MaxEigenValImL2g000_51Inf[2],MaxEigenValImL2g000_61Inf[2],MaxEigenValImL2g000_71Inf[2],MaxEigenValImL2g000_81Inf[2]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[0.0*1.0, 1.0*1.0, 0.0*1.0])#,label='100')
#axs[1].plot(CouplingC,[MaxEigenValImL2g000_41Inf[3],MaxEigenValImL2g000_51Inf[3],MaxEigenValImL2g000_61Inf[3],MaxEigenValImL2g000_71Inf[3],MaxEigenValImL2g000_81Inf[3]], marker='*',c=[0.0, 0.0, 0.0],ls='None',markersize=4, linewidth=1)#,markeredgecolor=[0.0*1.0, 0.4*1.0, 1.0*1.0])#,label='100')

axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.28510649/1**2, 8.06), marker='.',c=[1.0/1.5, 0.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.28510649/2**2, 8.06), marker='.',c=[1.0/1.5, 0.5/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.28510649/5**2, 8.06), marker='.',c=[0.0/1.5, 1.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[1].plot(CouplingAxisA, func(CouplingAxisA, 0.28510649/10**2,8.06), marker='.',c=[0.0/1.5, 0.0/1.5, 1.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))

axs[0].plot(CouplingAxis, func(CouplingAxis, 0.28510649/1**2, 8.06), marker='.',c=[1.0/1.5, 0.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, 0.28510649/2**2, 8.06), marker='.',c=[1.0/1.5, 0.5/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, 0.28510649/5**2, 8.06), marker='.',c=[0.0/1.5, 1.0/1.5, 0.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))
axs[0].plot(CouplingAxis, func(CouplingAxis, 0.28510649/10**2,8.06), marker='.',c=[0.0/1.5, 0.0/1.5, 1.0/1.5],ls='None', markersize=2)#, label='fit: E0=%5.3f, GK=%5.3f' % tuple(FitaK001))

#"""

#axs[1].semilogy(100*Coupling,MaxEigenValImL2g0011Inf, marker='o',c=[1.0, 0.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.01$', markersize=4, linewidth=1)#,label='100')
#axs[1].semilogy(100*Coupling,MaxEigenValImL2g0021Inf, marker='o',c=[1.0, 0.5, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.02$', markersize=4, linewidth=1)#,label='100')
#axs[1].semilogy(100*Coupling,MaxEigenValImL2g0051Inf, marker='o',c=[0.0, 1.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.05$', markersize=4, linewidth=1)#,label='100')
#axs[1].semilogy(100*Coupling,MaxEigenValImL2g0101Inf, marker='o',c=[0.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 0.10$', markersize=4, linewidth=1)#,label='100')

axs[1].set_title("$\\ell=2$" ,fontsize=12, fontname='Times New Roman')

axs[1].grid(True)
axs[1].set_xlim(-0.e+0,+2.1e+0)
axs[1].set_xticks(np.arange(-0.0e+1,+2.01e+0, step=5.e-1))
axs[1].set_ylim(+1e-12,+1e+0)
#axs[1].set_yticks([1e0,1e1,1e2,1e3,1e4,1e5,1e6,1e7])

axs[0].text(-0.40, 1e-15, '(a)', fontsize=12)
axs[1].text(-0.20, 1e-15, '(b)', fontsize=12)

#axs[1,0].legend(bbox_to_anchor=(0.4, +1.2), loc=2, borderaxespad=0., ncol=4, labelspacing=1,handleheight=1, columnspacing=0.1, handletextpad=0.1)
#plt.suptitle('$\\ell=0XXX, g_{\\mathcal{K}}=0.1$', fontsize=20, fontname='Times New Roman')
axs[1].set_xlabel('$g_{\\mathcal{K}}$', fontsize=12, fontname='Times New Roman')
#axs[1].set_ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}\\times 10e{+7}$', fontsize=12, fontname='Times New Roman')


#plt.show()
fig.savefig('PlotReportTotal.pdf')


########################################################################
########################################################################

plt.clf()
fig, axs = plt.subplots(1, 2, figsize=(6, 3), sharey=False)
plt.subplots_adjust(left=0.2,bottom=0.25,right=0.85,top=0.8,wspace=0.4,hspace=0.4)

#axs[0].loglog(CouplingA,[MaxEigenValImL0g000_11Inf[0],MaxEigenValImL0g000_21Inf[0],MaxEigenValImL0g000_31Inf[0],MaxEigenValImL0g000_41Inf[0],MaxEigenValImL0g000_51Inf[0],MaxEigenValImL0g0011Inf[0],MaxEigenValImL0g0021Inf[0],MaxEigenValImL0g0051Inf[0],MaxEigenValImL0g0101Inf[0]], marker='o',c=[1.0, 0.0, 0.0],ls='-',label='$a_{\\mathcal{K}}=  1$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])#,label='100')
###axs[0].semilogy(CouplingA,[MaxEigenValImL0g000_21Inf[0]-MaxEigenValImL0g000_21Inf[1],MaxEigenValImL0g000_31Inf[0]-MaxEigenValImL0g000_31Inf[1],MaxEigenValImL0g000_41Inf[0]-MaxEigenValImL0g000_41Inf[1],MaxEigenValImL0g000_51Inf[0]-MaxEigenValImL0g000_51Inf[1],MaxEigenValImL0g0011Inf[0]-MaxEigenValImL0g0011Inf[1],MaxEigenValImL0g0021Inf[0]-MaxEigenValImL0g0021Inf[1],MaxEigenValImL0g0051Inf[0]-MaxEigenValImL0g0051Inf[1],MaxEigenValImL0g0101Inf[0]-MaxEigenValImL0g0101Inf[1]], marker='o',c=[1.0, 0.0, 0.0],ls='-',label='$a_{\\mathcal{K}}=  1$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])#,label='100')
###axs[0].plot(CouplingA,  [MaxEigenValImL0g000_21Inf[1]-MaxEigenValImL0g000_21Inf[2],MaxEigenValImL0g000_31Inf[1]-MaxEigenValImL0g000_31Inf[2],MaxEigenValImL0g000_41Inf[1]-MaxEigenValImL0g000_41Inf[2],MaxEigenValImL0g000_51Inf[1]-MaxEigenValImL0g000_51Inf[2],MaxEigenValImL0g0011Inf[1]-MaxEigenValImL0g0011Inf[2],MaxEigenValImL0g0021Inf[1]-MaxEigenValImL0g0021Inf[2],MaxEigenValImL0g0051Inf[1]-MaxEigenValImL0g0051Inf[2],MaxEigenValImL0g0101Inf[1]-MaxEigenValImL0g0101Inf[2]], marker='o',c=[1.0, 0.5, 0.0],ls='-',label='$a_{\\mathcal{K}}=  2$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])#,label='100')
###axs[0].plot(CouplingA,  [MaxEigenValImL0g000_21Inf[2]-MaxEigenValImL0g000_21Inf[3],MaxEigenValImL0g000_31Inf[2]-MaxEigenValImL0g000_31Inf[3],MaxEigenValImL0g000_41Inf[2]-MaxEigenValImL0g000_41Inf[3],MaxEigenValImL0g000_51Inf[2]-MaxEigenValImL0g000_51Inf[3],MaxEigenValImL0g0011Inf[2]-MaxEigenValImL0g0011Inf[3],MaxEigenValImL0g0021Inf[2]-MaxEigenValImL0g0021Inf[3],MaxEigenValImL0g0051Inf[2]-MaxEigenValImL0g0051Inf[3],MaxEigenValImL0g0101Inf[2]-MaxEigenValImL0g0101Inf[3]], marker='o',c=[0.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}=  5$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])#,label='100')
#axs[0].plot(CouplingA,  [MaxEigenValImL0g000_21Inf[3],MaxEigenValImL0g000_31Inf[3],MaxEigenValImL0g000_41Inf[3],MaxEigenValImL0g000_51Inf[3],MaxEigenValImL0g0011Inf[3],MaxEigenValImL0g0021Inf[3],MaxEigenValImL0g0051Inf[3],MaxEigenValImL0g0101Inf[3]], marker='o',c=[0.0, 0.0, 1.0],ls='-',label='$a_{\\mathcal{K}}= 10$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])#,label='100')

#axs[0].semilogy(100*Spreading,MaxEigenValImL0g0011Inf, marker='o',c=[1.0, 0.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.01$', markersize=4, linewidth=1)#,label='100')
#axs[0].semilogy(100*Spreading,MaxEigenValImL0g0021Inf, marker='o',c=[1.0, 0.5, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.02$', markersize=4, linewidth=1)#,label='100')
#axs[0].semilogy(100*Spreading,MaxEigenValImL0g0051Inf, marker='o',c=[0.0, 1.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.05$', markersize=4, linewidth=1)#,label='100')
#axs[0].semilogy(100*Spreading,MaxEigenValImL0g0101Inf, marker='o',c=[0.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 0.10$', markersize=4, linewidth=1)#,label='100')

#plt.xlim(left  =0)
#plt.ylim(top=0.09,bottom=0)
#plt.xticks([0.01,0.02,0.05,0.10])
#plt.yticks(np.arange(0.984,+1.004, step=0.002))
#plt.show()

axs[0].set_title("$\\ell=0$" ,fontsize=12, fontname='Times New Roman')

axs[0].grid(True)
#axs[0].set_xlim(+0.0e+1,+1.2e+1)
#axs[0].set_xticks(np.arange(-0.0e+1,+1.21e+1, step=2.e-0))
#axs[0].set_ylim(+1e-15,+1.01e+7)
axs[0].set_ylim(+1e0,+1.01e+16)
#axs[0].set_yticks([1e0,1e1,1e2,1e3,1e4,1e5,1e6,1e7])

axs[0].legend(bbox_to_anchor=(0.2, +1.3), loc=2, borderaxespad=0., ncol=4, labelspacing=1,handleheight=1, columnspacing=0.1, handletextpad=0.1)
#plt.suptitle('$\\ell=0XXX, g_{\\mathcal{K}}=0.1$', fontsize=20, fontname='Times New Roman')
axs[0].set_xlabel('$g_{\\mathcal{K}}$', fontsize=12, fontname='Times New Roman')
axs[0].set_ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}\\times 10e{+7}$', fontsize=12, fontname='Times New Roman')

Coupling = np.zeros((4))
Coupling[0] = 0.01
Coupling[1] = 0.02
Coupling[2] = 0.05
Coupling[3] = 0.10

#axs[1].semilogy(100*Coupling,[MaxEigenValImL2g0011Inf[0],MaxEigenValImL2g0021Inf[0],MaxEigenValImL2g0051Inf[0],MaxEigenValImL2g0101Inf[0]], marker='o',c=[1.0, 0.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.01$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
#axs[1].semilogy(100*Coupling,[MaxEigenValImL2g0011Inf[1],MaxEigenValImL2g0021Inf[1],MaxEigenValImL2g0051Inf[1],MaxEigenValImL2g0101Inf[1]], marker='o',c=[1.0, 0.5, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.02$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
#axs[1].semilogy(100*Coupling,[MaxEigenValImL2g0011Inf[2],MaxEigenValImL2g0021Inf[2],MaxEigenValImL2g0051Inf[2],MaxEigenValImL2g0101Inf[2]], marker='o',c=[0.0, 1.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.05$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
#axs[1].semilogy(100*Coupling,[MaxEigenValImL2g0011Inf[3],MaxEigenValImL2g0021Inf[3],MaxEigenValImL2g0051Inf[3],MaxEigenValImL2g0101Inf[3]], marker='o',c=[0.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 0.10$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])

axs[1].semilogy(Spreading,MaxEigenValImL0g000_251Inf, marker='o',c=[1.0, 0.0, 0.0],ls='-',label='$a_{\\mathcal{K}}=  1$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])#,label='100')
axs[1].plot(Spreading,MaxEigenValImL0g000_31Inf, marker='o',c=[1.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}=  1$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 1.0*0.8, 0.0*0.8])#,label='100')
axs[1].plot(Spreading,MaxEigenValImL0g000_41Inf, marker='o',c=[0.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}=  1$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])#,label='100')
axs[1].plot(Spreading,MaxEigenValImL0g000_51Inf, marker='o',c=[0.0, 1.0, 1.0],ls='-',label='$a_{\\mathcal{K}}=  1$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 1.0*0.8, 1.0*0.8])#,label='100')
axs[1].plot(Spreading,MaxEigenValImL0g0011Inf,   marker='o',c=[0.0, 0.0, 1.0],ls='-',label='$a_{\\mathcal{K}}=  1$', markersize=5, linewidth=1,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])#,label='100')
axs[1].plot(Spreading,MaxEigenValImL0g0021Inf,   marker='o',c=[1.0, 0.0, 1.0],ls='-',label='$a_{\\mathcal{K}}=  1$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 1.0*0.8])#,label='100')
axs[1].plot(Spreading,MaxEigenValImL0g0051Inf,   marker='o',c=[1.0, 0.0, 0.0],ls='-',label='$a_{\\mathcal{K}}=  1$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])#,label='100')
axs[1].plot(Spreading,MaxEigenValImL0g0101Inf,   marker='o',c=[1.0, 1.0, 0.0],ls='-',label='$a_{\\mathcal{K}}=  1$', markersize=5, linewidth=1,markeredgecolor=[1.0*0.8, 1.0*0.8, 0.0*0.8])#,label='100')


#axs[1].semilogy(100*Coupling,MaxEigenValImL2g0011Inf, marker='o',c=[1.0, 0.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.01$', markersize=4, linewidth=1)#,label='100')
#axs[1].semilogy(100*Coupling,MaxEigenValImL2g0021Inf, marker='o',c=[1.0, 0.5, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.02$', markersize=4, linewidth=1)#,label='100')
#axs[1].semilogy(100*Coupling,MaxEigenValImL2g0051Inf, marker='o',c=[0.0, 1.0, 0.0],ls='None',label='$a_{\\mathcal{K}}= 0.05$', markersize=4, linewidth=1)#,label='100')
#axs[1].semilogy(100*Coupling,MaxEigenValImL2g0101Inf, marker='o',c=[0.0, 0.0, 1.0],ls='None',label='$a_{\\mathcal{K}}= 0.10$', markersize=4, linewidth=1)#,label='100')

axs[1].set_title("$\\ell=2$" ,fontsize=12, fontname='Times New Roman')

axs[1].grid(True)
#axs[1].set_xlim(+0.0e+1,+1.2e+1)
#axs[1].set_xticks(np.arange(-0.0e+1,+1.21e+1, step=2.e-0))
#axs[1].set_ylim(+1e0,+1.01e+7)
#axs[1].set_yticks([1e0,1e1,1e2,1e3,1e4,1e5,1e6,1e7])

axs[0].text(-2.5, 0.03, '(a)', fontsize=12)
axs[1].text(-2.5, 0.03, '(b)', fontsize=12)

#axs[1,0].legend(bbox_to_anchor=(0.4, +1.2), loc=2, borderaxespad=0., ncol=4, labelspacing=1,handleheight=1, columnspacing=0.1, handletextpad=0.1)
#plt.suptitle('$\\ell=0XXX, g_{\\mathcal{K}}=0.1$', fontsize=20, fontname='Times New Roman')
axs[1].set_xlabel('$g_{\\mathcal{K}}$', fontsize=12, fontname='Times New Roman')
axs[1].set_ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}\\times 10e{+7}$', fontsize=12, fontname='Times New Roman')


#plt.show()
fig.savefig('DiffPlotReportTotal.pdf')
