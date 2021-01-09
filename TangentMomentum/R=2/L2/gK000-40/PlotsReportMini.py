import numpy as np
import matplotlib.pyplot as plt

###############################################
###############################################
###############################################

data0010011010 = np.genfromtxt('./aK001/N070/HamVals.txt')

MomentumAx0010011010 = data0010011010[:,][:,5*0+0]
KineticEne0010011010 = data0010011010[:,][:,5*0+1]
SelfEnergy0010011010 = data0010011010[:,][:,5*0+2]
EigenValRe0010011010 = data0010011010[:,][:,5*0+3]
EigenValIm0010011010 = data0010011010[:,][:,5*0+4]

data0010011020 = np.genfromtxt('./aK001/N080/HamVals.txt')

MomentumAx0010011020 = data0010011020[:,][:,5*0+0]
KineticEne0010011020 = data0010011020[:,][:,5*0+1]
SelfEnergy0010011020 = data0010011020[:,][:,5*0+2]
EigenValRe0010011020 = data0010011020[:,][:,5*0+3]
EigenValIm0010011020 = data0010011020[:,][:,5*0+4]

data0010011030 = np.genfromtxt('./aK001/N090/HamVals.txt')

MomentumAx0010011030 = data0010011030[:,][:,5*0+0]
KineticEne0010011030 = data0010011030[:,][:,5*0+1]
SelfEnergy0010011030 = data0010011030[:,][:,5*0+2]
EigenValRe0010011030 = data0010011030[:,][:,5*0+3]
EigenValIm0010011030 = data0010011030[:,][:,5*0+4]

data0010011040 = np.genfromtxt('./aK001/N100/HamVals.txt')

MomentumAx0010011040 = data0010011040[:,][:,5*0+0]
KineticEne0010011040 = data0010011040[:,][:,5*0+1]
SelfEnergy0010011040 = data0010011040[:,][:,5*0+2]
EigenValRe0010011040 = data0010011040[:,][:,5*0+3]
EigenValIm0010011040 = data0010011040[:,][:,5*0+4]

data0010011050 = np.genfromtxt('./aK001/N110/HamVals.txt')

MomentumAx0010011050 = data0010011050[:,][:,5*0+0]
KineticEne0010011050 = data0010011050[:,][:,5*0+1]
SelfEnergy0010011050 = data0010011050[:,][:,5*0+2]
EigenValRe0010011050 = data0010011050[:,][:,5*0+3]
EigenValIm0010011050 = data0010011050[:,][:,5*0+4]
"""
data0010011060 = np.genfromtxt('./aK001/N060/HamVals.txt')

MomentumAx0010011060 = data0010011060[:,][:,5*0+0]
KineticEne0010011060 = data0010011060[:,][:,5*0+1]
SelfEnergy0010011060 = data0010011060[:,][:,5*0+2]
EigenValRe0010011060 = data0010011060[:,][:,5*0+3]
EigenValIm0010011060 = data0010011060[:,][:,5*0+4]

data0010011070 = np.genfromtxt('./aK001/N070/HamVals.txt')

MomentumAx0010011070 = data0010011070[:,][:,5*0+0]
KineticEne0010011070 = data0010011070[:,][:,5*0+1]
SelfEnergy0010011070 = data0010011070[:,][:,5*0+2]
EigenValRe0010011070 = data0010011070[:,][:,5*0+3]
EigenValIm0010011070 = data0010011070[:,][:,5*0+4]

data0010011080 = np.genfromtxt('./aK001/N080/HamVals.txt')

MomentumAx0010011080 = data0010011080[:,][:,5*0+0]
KineticEne0010011080 = data0010011080[:,][:,5*0+1]
SelfEnergy0010011080 = data0010011080[:,][:,5*0+2]
EigenValRe0010011080 = data0010011080[:,][:,5*0+3]
EigenValIm0010011080 = data0010011080[:,][:,5*0+4]

data0010011090 = np.genfromtxt('./aK001/N090/HamVals.txt')

MomentumAx0010011090 = data0010011090[:,][:,5*0+0]
KineticEne0010011090 = data0010011090[:,][:,5*0+1]
SelfEnergy0010011090 = data0010011090[:,][:,5*0+2]
EigenValRe0010011090 = data0010011090[:,][:,5*0+3]
EigenValIm0010011090 = data0010011090[:,][:,5*0+4]

data0010011100 = np.genfromtxt('./aK001/N100/HamVals.txt')

MomentumAx0010011100 = data0010011100[:,][:,5*0+0]
KineticEne0010011100 = data0010011100[:,][:,5*0+1]
SelfEnergy0010011100 = data0010011100[:,][:,5*0+2]
EigenValRe0010011100 = data0010011100[:,][:,5*0+3]
EigenValIm0010011100 = data0010011100[:,][:,5*0+4]
"""
data001A0011010 = np.genfromtxt('./aK001a/N010/HamVals.txt')

MomentumAx001A0011010 = data001A0011010[:,][:,5*0+0]
KineticEne001A0011010 = data001A0011010[:,][:,5*0+1]
SelfEnergy001A0011010 = data001A0011010[:,][:,5*0+2]
EigenValRe001A0011010 = data001A0011010[:,][:,5*0+3]
EigenValIm001A0011010 = data001A0011010[:,][:,5*0+4]

data001A0011020 = np.genfromtxt('./aK001a/N020/HamVals.txt')

MomentumAx001A0011020 = data001A0011020[:,][:,5*0+0]
KineticEne001A0011020 = data001A0011020[:,][:,5*0+1]
SelfEnergy001A0011020 = data001A0011020[:,][:,5*0+2]
EigenValRe001A0011020 = data001A0011020[:,][:,5*0+3]
EigenValIm001A0011020 = data001A0011020[:,][:,5*0+4]

data001A0011030 = np.genfromtxt('./aK001a/N030/HamVals.txt')

MomentumAx001A0011030 = data001A0011030[:,][:,5*0+0]
KineticEne001A0011030 = data001A0011030[:,][:,5*0+1]
SelfEnergy001A0011030 = data001A0011030[:,][:,5*0+2]
EigenValRe001A0011030 = data001A0011030[:,][:,5*0+3]
EigenValIm001A0011030 = data001A0011030[:,][:,5*0+4]

data001A0011040 = np.genfromtxt('./aK001a/N040/HamVals.txt')

MomentumAx001A0011040 = data001A0011040[:,][:,5*0+0]
KineticEne001A0011040 = data001A0011040[:,][:,5*0+1]
SelfEnergy001A0011040 = data001A0011040[:,][:,5*0+2]
EigenValRe001A0011040 = data001A0011040[:,][:,5*0+3]
EigenValIm001A0011040 = data001A0011040[:,][:,5*0+4]

data001A0011050 = np.genfromtxt('./aK001a/N050/HamVals.txt')

MomentumAx001A0011050 = data001A0011050[:,][:,5*0+0]
KineticEne001A0011050 = data001A0011050[:,][:,5*0+1]
SelfEnergy001A0011050 = data001A0011050[:,][:,5*0+2]
EigenValRe001A0011050 = data001A0011050[:,][:,5*0+3]
EigenValIm001A0011050 = data001A0011050[:,][:,5*0+4]





















data001B0011010 = np.genfromtxt('./aK001b/N070/HamVals.txt')

MomentumAx001B0011010 = data001B0011010[:,][:,5*0+0]
KineticEne001B0011010 = data001B0011010[:,][:,5*0+1]
SelfEnergy001B0011010 = data001B0011010[:,][:,5*0+2]
EigenValRe001B0011010 = data001B0011010[:,][:,5*0+3]
EigenValIm001B0011010 = data001B0011010[:,][:,5*0+4]

data001B0011020 = np.genfromtxt('./aK001b/N080/HamVals.txt')

MomentumAx001B0011020 = data001B0011020[:,][:,5*0+0]
KineticEne001B0011020 = data001B0011020[:,][:,5*0+1]
SelfEnergy001B0011020 = data001B0011020[:,][:,5*0+2]
EigenValRe001B0011020 = data001B0011020[:,][:,5*0+3]
EigenValIm001B0011020 = data001B0011020[:,][:,5*0+4]

data001B0011030 = np.genfromtxt('./aK001b/N090/HamVals.txt')

MomentumAx001B0011030 = data001B0011030[:,][:,5*0+0]
KineticEne001B0011030 = data001B0011030[:,][:,5*0+1]
SelfEnergy001B0011030 = data001B0011030[:,][:,5*0+2]
EigenValRe001B0011030 = data001B0011030[:,][:,5*0+3]
EigenValIm001B0011030 = data001B0011030[:,][:,5*0+4]

data001B0011040 = np.genfromtxt('./aK001b/N100/HamVals.txt')

MomentumAx001B0011040 = data001B0011040[:,][:,5*0+0]
KineticEne001B0011040 = data001B0011040[:,][:,5*0+1]
SelfEnergy001B0011040 = data001B0011040[:,][:,5*0+2]
EigenValRe001B0011040 = data001B0011040[:,][:,5*0+3]
EigenValIm001B0011040 = data001B0011040[:,][:,5*0+4]

data001B0011050 = np.genfromtxt('./aK001b/N110/HamVals.txt')

MomentumAx001B0011050 = data001B0011050[:,][:,5*0+0]
KineticEne001B0011050 = data001B0011050[:,][:,5*0+1]
SelfEnergy001B0011050 = data001B0011050[:,][:,5*0+2]
EigenValRe001B0011050 = data001B0011050[:,][:,5*0+3]
EigenValIm001B0011050 = data001B0011050[:,][:,5*0+4]

data001B0011060 = np.genfromtxt('./aK001b/N060/HamVals.txt')

MomentumAx001B0011060 = data001B0011060[:,][:,5*0+0]
KineticEne001B0011060 = data001B0011060[:,][:,5*0+1]
SelfEnergy001B0011060 = data001B0011060[:,][:,5*0+2]
EigenValRe001B0011060 = data001B0011060[:,][:,5*0+3]
EigenValIm001B0011060 = data001B0011060[:,][:,5*0+4]

data001B0011070 = np.genfromtxt('./aK001b/N070/HamVals.txt')

MomentumAx001B0011070 = data001B0011070[:,][:,5*0+0]
KineticEne001B0011070 = data001B0011070[:,][:,5*0+1]
SelfEnergy001B0011070 = data001B0011070[:,][:,5*0+2]
EigenValRe001B0011070 = data001B0011070[:,][:,5*0+3]
EigenValIm001B0011070 = data001B0011070[:,][:,5*0+4]

data001B0011080 = np.genfromtxt('./aK001b/N080/HamVals.txt')

MomentumAx001B0011080 = data001B0011080[:,][:,5*0+0]
KineticEne001B0011080 = data001B0011080[:,][:,5*0+1]
SelfEnergy001B0011080 = data001B0011080[:,][:,5*0+2]
EigenValRe001B0011080 = data001B0011080[:,][:,5*0+3]
EigenValIm001B0011080 = data001B0011080[:,][:,5*0+4]

data001B0011090 = np.genfromtxt('./aK001b/N090/HamVals.txt')

MomentumAx001B0011090 = data001B0011090[:,][:,5*0+0]
KineticEne001B0011090 = data001B0011090[:,][:,5*0+1]
SelfEnergy001B0011090 = data001B0011090[:,][:,5*0+2]
EigenValRe001B0011090 = data001B0011090[:,][:,5*0+3]
EigenValIm001B0011090 = data001B0011090[:,][:,5*0+4]

data001B0011100 = np.genfromtxt('./aK001b/N100/HamVals.txt')

MomentumAx001B0011100 = data001B0011100[:,][:,5*0+0]
KineticEne001B0011100 = data001B0011100[:,][:,5*0+1]
SelfEnergy001B0011100 = data001B0011100[:,][:,5*0+2]
EigenValRe001B0011100 = data001B0011100[:,][:,5*0+3]
EigenValIm001B0011100 = data001B0011100[:,][:,5*0+4]

data001B0011110 = np.genfromtxt('./aK001b/N110/HamVals.txt')

MomentumAx001B0011110 = data001B0011110[:,][:,5*0+0]
KineticEne001B0011110 = data001B0011110[:,][:,5*0+1]
SelfEnergy001B0011110 = data001B0011110[:,][:,5*0+2]
EigenValRe001B0011110 = data001B0011110[:,][:,5*0+3]
EigenValIm001B0011110 = data001B0011110[:,][:,5*0+4]





































data0010021010 = np.genfromtxt('./aK002/N010/HamVals.txt')

MomentumAx0010021010 = data0010021010[:,][:,5*0+0]
KineticEne0010021010 = data0010021010[:,][:,5*0+1]
SelfEnergy0010021010 = data0010021010[:,][:,5*0+2]
EigenValRe0010021010 = data0010021010[:,][:,5*0+3]
EigenValIm0010021010 = data0010021010[:,][:,5*0+4]

data0010021020 = np.genfromtxt('./aK002/N020/HamVals.txt')

MomentumAx0010021020 = data0010021020[:,][:,5*0+0]
KineticEne0010021020 = data0010021020[:,][:,5*0+1]
SelfEnergy0010021020 = data0010021020[:,][:,5*0+2]
EigenValRe0010021020 = data0010021020[:,][:,5*0+3]
EigenValIm0010021020 = data0010021020[:,][:,5*0+4]

data0010021030 = np.genfromtxt('./aK002/N030/HamVals.txt')

MomentumAx0010021030 = data0010021030[:,][:,5*0+0]
KineticEne0010021030 = data0010021030[:,][:,5*0+1]
SelfEnergy0010021030 = data0010021030[:,][:,5*0+2]
EigenValRe0010021030 = data0010021030[:,][:,5*0+3]
EigenValIm0010021030 = data0010021030[:,][:,5*0+4]

data0010021040 = np.genfromtxt('./aK002/N040/HamVals.txt')

MomentumAx0010021040 = data0010021040[:,][:,5*0+0]
KineticEne0010021040 = data0010021040[:,][:,5*0+1]
SelfEnergy0010021040 = data0010021040[:,][:,5*0+2]
EigenValRe0010021040 = data0010021040[:,][:,5*0+3]
EigenValIm0010021040 = data0010021040[:,][:,5*0+4]

data0010021050 = np.genfromtxt('./aK002/N050/HamVals.txt')

MomentumAx0010021050 = data0010021050[:,][:,5*0+0]
KineticEne0010021050 = data0010021050[:,][:,5*0+1]
SelfEnergy0010021050 = data0010021050[:,][:,5*0+2]
EigenValRe0010021050 = data0010021050[:,][:,5*0+3]
EigenValIm0010021050 = data0010021050[:,][:,5*0+4]




















data001B0021010 = np.genfromtxt('./aK002b/N070/HamVals.txt')

MomentumAx001B0021010 = data001B0021010[:,][:,5*0+0]
KineticEne001B0021010 = data001B0021010[:,][:,5*0+1]
SelfEnergy001B0021010 = data001B0021010[:,][:,5*0+2]
EigenValRe001B0021010 = data001B0021010[:,][:,5*0+3]
EigenValIm001B0021010 = data001B0021010[:,][:,5*0+4]

data001B0021020 = np.genfromtxt('./aK002b/N080/HamVals.txt')

MomentumAx001B0021020 = data001B0021020[:,][:,5*0+0]
KineticEne001B0021020 = data001B0021020[:,][:,5*0+1]
SelfEnergy001B0021020 = data001B0021020[:,][:,5*0+2]
EigenValRe001B0021020 = data001B0021020[:,][:,5*0+3]
EigenValIm001B0021020 = data001B0021020[:,][:,5*0+4]

data001B0021030 = np.genfromtxt('./aK002b/N090/HamVals.txt')

MomentumAx001B0021030 = data001B0021030[:,][:,5*0+0]
KineticEne001B0021030 = data001B0021030[:,][:,5*0+1]
SelfEnergy001B0021030 = data001B0021030[:,][:,5*0+2]
EigenValRe001B0021030 = data001B0021030[:,][:,5*0+3]
EigenValIm001B0021030 = data001B0021030[:,][:,5*0+4]

data001B0021040 = np.genfromtxt('./aK002b/N100/HamVals.txt')

MomentumAx001B0021040 = data001B0021040[:,][:,5*0+0]
KineticEne001B0021040 = data001B0021040[:,][:,5*0+1]
SelfEnergy001B0021040 = data001B0021040[:,][:,5*0+2]
EigenValRe001B0021040 = data001B0021040[:,][:,5*0+3]
EigenValIm001B0021040 = data001B0021040[:,][:,5*0+4]

data001B0021050 = np.genfromtxt('./aK002b/N110/HamVals.txt')

MomentumAx001B0021050 = data001B0021050[:,][:,5*0+0]
KineticEne001B0021050 = data001B0021050[:,][:,5*0+1]
SelfEnergy001B0021050 = data001B0021050[:,][:,5*0+2]
EigenValRe001B0021050 = data001B0021050[:,][:,5*0+3]
EigenValIm001B0021050 = data001B0021050[:,][:,5*0+4]

data001B0021060 = np.genfromtxt('./aK002b/N060/HamVals.txt')

MomentumAx001B0021060 = data001B0021060[:,][:,5*0+0]
KineticEne001B0021060 = data001B0021060[:,][:,5*0+1]
SelfEnergy001B0021060 = data001B0021060[:,][:,5*0+2]
EigenValRe001B0021060 = data001B0021060[:,][:,5*0+3]
EigenValIm001B0021060 = data001B0021060[:,][:,5*0+4]

data001B0021070 = np.genfromtxt('./aK002b/N070/HamVals.txt')

MomentumAx001B0021070 = data001B0021070[:,][:,5*0+0]
KineticEne001B0021070 = data001B0021070[:,][:,5*0+1]
SelfEnergy001B0021070 = data001B0021070[:,][:,5*0+2]
EigenValRe001B0021070 = data001B0021070[:,][:,5*0+3]
EigenValIm001B0021070 = data001B0021070[:,][:,5*0+4]

data001B0021080 = np.genfromtxt('./aK002b/N080/HamVals.txt')

MomentumAx001B0021080 = data001B0021080[:,][:,5*0+0]
KineticEne001B0021080 = data001B0021080[:,][:,5*0+1]
SelfEnergy001B0021080 = data001B0021080[:,][:,5*0+2]
EigenValRe001B0021080 = data001B0021080[:,][:,5*0+3]
EigenValIm001B0021080 = data001B0021080[:,][:,5*0+4]

data001B0021090 = np.genfromtxt('./aK002b/N090/HamVals.txt')

MomentumAx001B0021090 = data001B0021090[:,][:,5*0+0]
KineticEne001B0021090 = data001B0021090[:,][:,5*0+1]
SelfEnergy001B0021090 = data001B0021090[:,][:,5*0+2]
EigenValRe001B0021090 = data001B0021090[:,][:,5*0+3]
EigenValIm001B0021090 = data001B0021090[:,][:,5*0+4]

data001B0021100 = np.genfromtxt('./aK002b/N100/HamVals.txt')

MomentumAx001B0021100 = data001B0021100[:,][:,5*0+0]
KineticEne001B0021100 = data001B0021100[:,][:,5*0+1]
SelfEnergy001B0021100 = data001B0021100[:,][:,5*0+2]
EigenValRe001B0021100 = data001B0021100[:,][:,5*0+3]
EigenValIm001B0021100 = data001B0021100[:,][:,5*0+4]

data001B0021110 = np.genfromtxt('./aK002b/N110/HamVals.txt')

MomentumAx001B0021110 = data001B0021110[:,][:,5*0+0]
KineticEne001B0021110 = data001B0021110[:,][:,5*0+1]
SelfEnergy001B0021110 = data001B0021110[:,][:,5*0+2]
EigenValRe001B0021110 = data001B0021110[:,][:,5*0+3]
EigenValIm001B0021110 = data001B0021110[:,][:,5*0+4]























data0010051010 = np.genfromtxt('./aK005/N010/HamVals.txt')

MomentumAx0010051010 = data0010051010[:,][:,5*0+0]
KineticEne0010051010 = data0010051010[:,][:,5*0+1]
SelfEnergy0010051010 = data0010051010[:,][:,5*0+2]
EigenValRe0010051010 = data0010051010[:,][:,5*0+3]
EigenValIm0010051010 = data0010051010[:,][:,5*0+4]

data0010051020 = np.genfromtxt('./aK005/N020/HamVals.txt')

MomentumAx0010051020 = data0010051020[:,][:,5*0+0]
KineticEne0010051020 = data0010051020[:,][:,5*0+1]
SelfEnergy0010051020 = data0010051020[:,][:,5*0+2]
EigenValRe0010051020 = data0010051020[:,][:,5*0+3]
EigenValIm0010051020 = data0010051020[:,][:,5*0+4]

data0010051030 = np.genfromtxt('./aK005/N030/HamVals.txt')

MomentumAx0010051030 = data0010051030[:,][:,5*0+0]
KineticEne0010051030 = data0010051030[:,][:,5*0+1]
SelfEnergy0010051030 = data0010051030[:,][:,5*0+2]
EigenValRe0010051030 = data0010051030[:,][:,5*0+3]
EigenValIm0010051030 = data0010051030[:,][:,5*0+4]

data0010051040 = np.genfromtxt('./aK005/N040/HamVals.txt')

MomentumAx0010051040 = data0010051040[:,][:,5*0+0]
KineticEne0010051040 = data0010051040[:,][:,5*0+1]
SelfEnergy0010051040 = data0010051040[:,][:,5*0+2]
EigenValRe0010051040 = data0010051040[:,][:,5*0+3]
EigenValIm0010051040 = data0010051040[:,][:,5*0+4]

data0010051050 = np.genfromtxt('./aK005/N050/HamVals.txt')

MomentumAx0010051050 = data0010051050[:,][:,5*0+0]
KineticEne0010051050 = data0010051050[:,][:,5*0+1]
SelfEnergy0010051050 = data0010051050[:,][:,5*0+2]
EigenValRe0010051050 = data0010051050[:,][:,5*0+3]
EigenValIm0010051050 = data0010051050[:,][:,5*0+4]

data0010101010 = np.genfromtxt('./aK010/N010/HamVals.txt')

MomentumAx0010101010 = data0010101010[:,][:,5*0+0]
KineticEne0010101010 = data0010101010[:,][:,5*0+1]
SelfEnergy0010101010 = data0010101010[:,][:,5*0+2]
EigenValRe0010101010 = data0010101010[:,][:,5*0+3]
EigenValIm0010101010 = data0010101010[:,][:,5*0+4]

data0010101020 = np.genfromtxt('./aK010/N020/HamVals.txt')

MomentumAx0010101020 = data0010101020[:,][:,5*0+0]
KineticEne0010101020 = data0010101020[:,][:,5*0+1]
SelfEnergy0010101020 = data0010101020[:,][:,5*0+2]
EigenValRe0010101020 = data0010101020[:,][:,5*0+3]
EigenValIm0010101020 = data0010101020[:,][:,5*0+4]

data0010101030 = np.genfromtxt('./aK010/N030/HamVals.txt')

MomentumAx0010101030 = data0010101030[:,][:,5*0+0]
KineticEne0010101030 = data0010101030[:,][:,5*0+1]
SelfEnergy0010101030 = data0010101030[:,][:,5*0+2]
EigenValRe0010101030 = data0010101030[:,][:,5*0+3]
EigenValIm0010101030 = data0010101030[:,][:,5*0+4]

data0010101040 = np.genfromtxt('./aK010/N040/HamVals.txt')

MomentumAx0010101040 = data0010101040[:,][:,5*0+0]
KineticEne0010101040 = data0010101040[:,][:,5*0+1]
SelfEnergy0010101040 = data0010101040[:,][:,5*0+2]
EigenValRe0010101040 = data0010101040[:,][:,5*0+3]
EigenValIm0010101040 = data0010101040[:,][:,5*0+4]

data0010101050 = np.genfromtxt('./aK010/N050/HamVals.txt')

MomentumAx0010101050 = data0010101050[:,][:,5*0+0]
KineticEne0010101050 = data0010101050[:,][:,5*0+1]
SelfEnergy0010101050 = data0010101050[:,][:,5*0+2]
EigenValRe0010101050 = data0010101050[:,][:,5*0+3]
EigenValIm0010101050 = data0010101050[:,][:,5*0+4]
"""
data0010201010 = np.genfromtxt('./aK020/N010/HamVals.txt')

MomentumAx0010201010 = data0010201010[:,][:,5*0+0]
KineticEne0010201010 = data0010201010[:,][:,5*0+1]
SelfEnergy0010201010 = data0010201010[:,][:,5*0+2]
EigenValRe0010201010 = data0010201010[:,][:,5*0+3]
EigenValIm0010201010 = data0010201010[:,][:,5*0+4]

data0010201020 = np.genfromtxt('./aK020/N020/HamVals.txt')

MomentumAx0010201020 = data0010201020[:,][:,5*0+0]
KineticEne0010201020 = data0010201020[:,][:,5*0+1]
SelfEnergy0010201020 = data0010201020[:,][:,5*0+2]
EigenValRe0010201020 = data0010201020[:,][:,5*0+3]
EigenValIm0010201020 = data0010201020[:,][:,5*0+4]

data0010201030 = np.genfromtxt('./aK020/N030/HamVals.txt')

MomentumAx0010201030 = data0010201030[:,][:,5*0+0]
KineticEne0010201030 = data0010201030[:,][:,5*0+1]
SelfEnergy0010201030 = data0010201030[:,][:,5*0+2]
EigenValRe0010201030 = data0010201030[:,][:,5*0+3]
EigenValIm0010201030 = data0010201030[:,][:,5*0+4]

data0010201040 = np.genfromtxt('./aK020/N040/HamVals.txt')

MomentumAx0010201040 = data0010201040[:,][:,5*0+0]
KineticEne0010201040 = data0010201040[:,][:,5*0+1]
SelfEnergy0010201040 = data0010201040[:,][:,5*0+2]
EigenValRe0010201040 = data0010201040[:,][:,5*0+3]
EigenValIm0010201040 = data0010201040[:,][:,5*0+4]

data0010201050 = np.genfromtxt('./aK020/N050/HamVals.txt')

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

fiveSizes = [1./10,1./20,1./30,1./40,1./50]

SizesAxis = np.linspace(0,MomentumAx0010011010[len(MomentumAx0010011010)/2],11,endpoint=True)

fiveSizes2 = [1./70,1./80,1./90]
MaxEigenValIm0011Inf[0] = np.polyfit(fiveSizes2, [MaxEigenValIm0011010[0],MaxEigenValIm0011020[0],MaxEigenValIm0011030[0]], 1)[[1]]
MaxEigenValIm0011Inf[1] = np.polyfit(fiveSizes, [MaxEigenValIm0011010[1],MaxEigenValIm0011020[1],MaxEigenValIm0011030[1],MaxEigenValIm0011040[1],MaxEigenValIm0011050[1]], 1)[[1]]
MaxEigenValIm0011Inf[2] = np.polyfit(fiveSizes, [MaxEigenValIm0011010[2],MaxEigenValIm0011020[2],MaxEigenValIm0011030[2],MaxEigenValIm0011040[2],MaxEigenValIm0011050[2]], 1)[[1]]
MaxEigenValIm0011Inf[3] = np.polyfit(fiveSizes, [MaxEigenValIm0011010[3],MaxEigenValIm0011020[3],MaxEigenValIm0011030[3],MaxEigenValIm0011040[3],MaxEigenValIm0011050[3]], 1)[[1]]

fiveSizesA = [1./10,1./20,1./30,1./40,1./50, 1./60,1./70,1./80,1./90,1./100,1./110]
MaxEigenValIm0011Inf002A = np.polyfit(fiveSizesA, [np.max(EigenValIm001B0021010),np.max(EigenValIm001B0021020),np.max(EigenValIm001B0021030),np.max(EigenValIm001B0021040),np.max(EigenValIm001B0021050),np.max(EigenValIm001B0021060),np.max(EigenValIm001B0021070),np.max(EigenValIm001B0021080),np.max(EigenValIm001B0021090),np.max(EigenValIm001B0021100),np.max(EigenValIm001B0021110)], 1)[[1]]

fiveSizesB = [1./60,1./70,1./80,1./90,1./100,1./110]
MaxEigenValIm0011Inf002B = np.polyfit(fiveSizesB, [np.max(EigenValIm001B0021060),np.max(EigenValIm001B0021070),np.max(EigenValIm001B0021080),np.max(EigenValIm001B0021090),np.max(EigenValIm001B0021100),np.max(EigenValIm001B0021110)], 1)[[1]]


print MaxEigenValIm0011Inf
print np.polyfit(fiveSizes, [MaxEigenValIm0011010[0],MaxEigenValIm0011020[0],MaxEigenValIm0011030[0],MaxEigenValIm0011040[0],MaxEigenValIm0011050[0]], 1)









"""
plt.clf()
#fig, axs = plt.subplots(2, 2, figsize=(6, 6), sharey=False)
#plt.subplots_adjust(left=0.2,bottom=0.2,right=0.95,top=0.9,wspace=0.4,hspace=0.4)

plt.plot(1*MomentumAx0010011010[100],1*np.max(EigenValIm0010011010), marker='^',c=[1.0, 0.0, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1*MomentumAx0010011020[200],1*np.max(EigenValIm0010011020), marker='s',c=[1.0, 0.0, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1*MomentumAx0010011030[300],1*np.max(EigenValIm0010011030), marker='p',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1*MomentumAx0010011040[400],1*np.max(EigenValIm0010011040), marker='h',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1*MomentumAx0010011050[500],1*np.max(EigenValIm0010011050), marker='8',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
plt.semilogy(                           [0],[1*MaxEigenValIm0011Inf[0]], marker='o',c=[1.0, 0.0, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 1$', markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
plt.plot([MomentumAx0010011010[100],MomentumAx0010011020[200],MomentumAx0010011030[300],MomentumAx0010011040[400],MomentumAx0010011050[500],0],[MaxEigenValIm0011010[0],MaxEigenValIm0011020[0],MaxEigenValIm0011030[0],MaxEigenValIm0011040[0],MaxEigenValIm0011050[0],1*MaxEigenValIm0011Inf[0]], marker='.',c=[.0, 0.0, 0.0],ls='-', markersize=5,markeredgecolor=[0.0*0.8, 0.0*0.8, 0.0*0.8])

print [MomentumAx0010011010[100],MomentumAx0010011020[200],MomentumAx0010011030[300],MomentumAx0010011040[400],MomentumAx0010011050[500],0]
print [MaxEigenValIm0011010[0],MaxEigenValIm0011020[0],MaxEigenValIm0011030[0],MaxEigenValIm0011040[0],MaxEigenValIm0011050[0],1*MaxEigenValIm0011Inf[0]]

plt.plot(1*MomentumAx0010021010[100],1*np.max(EigenValIm0010021010), marker='^',c=[1.0, 0.5, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
plt.plot(1*MomentumAx0010021020[200],1*np.max(EigenValIm0010021020), marker='s',c=[1.0, 0.5, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
plt.plot(1*MomentumAx0010021030[300],1*np.max(EigenValIm0010021030), marker='p',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
plt.plot(1*MomentumAx0010021040[400],1*np.max(EigenValIm0010021040), marker='h',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
plt.plot(1*MomentumAx0010021050[500],1*np.max(EigenValIm0010021050), marker='8',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
plt.plot(                         [0],  [1*MaxEigenValIm0011Inf[1]], marker='o',c=[1.0, 0.5, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 2$', markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
plt.plot([MomentumAx0010021010[100],MomentumAx0010021020[200],MomentumAx0010021030[300],MomentumAx0010021040[400],MomentumAx0010021050[500],0],[1*np.max(EigenValIm0010021010),1*np.max(EigenValIm0010021020),1*np.max(EigenValIm0010021030),1*np.max(EigenValIm0010021040),1*np.max(EigenValIm0010021050),1*MaxEigenValIm0011Inf[1]], marker='None',c=[1.0, 0.5, 0.0],ls='-', markersize=5,label='$a_{\\mathcal{K}}= 2$', markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])

plt.plot(1*MomentumAx0010011010[100],1*np.max(EigenValIm0010051010), marker='^',c=[0.0, 1.0, 0.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
plt.plot(1*MomentumAx0010011020[200],1*np.max(EigenValIm0010051020), marker='s',c=[0.0, 1.0, 0.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
plt.plot(1*MomentumAx0010011030[300],1*np.max(EigenValIm0010051030), marker='p',c=[0.0, 1.0, 0.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
plt.plot(1*MomentumAx0010011040[400],1*np.max(EigenValIm0010051040), marker='h',c=[0.0, 1.0, 0.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
plt.plot(1*MomentumAx0010011050[500],1*np.max(EigenValIm0010051050), marker='8',c=[0.0, 1.0, 0.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
plt.plot(                      [0],  [1*MaxEigenValIm0011Inf[2]], marker='o',c=[0.0, 1.0, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 5$', markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
plt.plot([MomentumAx0010051010[100],MomentumAx0010051020[200],MomentumAx0010051030[300],MomentumAx0010051040[400],MomentumAx0010051050[500],0],[1*np.max(EigenValIm0010051010),1*np.max(EigenValIm0010051020),1*np.max(EigenValIm0010051030),1*np.max(EigenValIm0010051040),1*np.max(EigenValIm0010051050),1*MaxEigenValIm0011Inf[2]], marker='None',c=[0.0, 1.0, 0.0],ls='-', markersize=5,label='$a_{\\mathcal{K}}= 5$', markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])

plt.plot(1*MomentumAx0010101010[100],1*np.max(EigenValIm0010101010), marker='^',c=[0.0, 0.0, 1.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
plt.plot(1*MomentumAx0010101020[200],1*np.max(EigenValIm0010101020), marker='s',c=[0.0, 0.0, 1.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
plt.plot(1*MomentumAx0010101030[300],1*np.max(EigenValIm0010101030), marker='p',c=[0.0, 0.0, 1.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
plt.plot(1*MomentumAx0010101040[400],1*np.max(EigenValIm0010101040), marker='h',c=[0.0, 0.0, 1.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
plt.plot(1*MomentumAx0010101050[500],1*np.max(EigenValIm0010101050), marker='8',c=[0.0, 0.0, 1.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
plt.plot(                      [0],  [1*MaxEigenValIm0011Inf[3]], marker='o',c=[0.0, 0.0, 1.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 10$',markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
plt.plot([MomentumAx0010101010[100],MomentumAx0010101020[200],MomentumAx0010101030[300],MomentumAx0010101040[400],MomentumAx0010101050[500],0],[1*np.max(EigenValIm0010101010),1*np.max(EigenValIm0010101020),1*np.max(EigenValIm0010101030),1*np.max(EigenValIm0010101040),1*np.max(EigenValIm0010101050),1*MaxEigenValIm0011Inf[3]], marker='None',c=[0.0, 0.0, 1.0],ls='-', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])

plt.grid(True)
#plt.set_xlim(-0.0e+1,+2.0e+1)
#plt.set_xticks(np.arange(-0.0e+1,+2.01e+1, step=4.e-0))
#plt.set_ylim(1e-0,+1.0e+3)
#plt.set_yticks(np.arange(-0.e-2,+3.1e-0, step=0.5e-0))

plt.legend(bbox_to_anchor=(0.3, +1.3), loc=2, borderaxespad=0., ncol=4, labelspacing=1,handleheight=1, columnspacing=0.1, handletextpad=0.1)
#plt.suptitle('$\\ell=0XXX, g_{\\mathcal{K}}=0.1$', fontsize=20, fontname='Times New Roman')
plt.xlabel('$k/\\mathcal{K}\\times 10^{+5}$', fontsize=12, fontname='Times New Roman')
plt.ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}\\times 10^{+7}$', fontsize=12, fontname='Times New Roman')

#plt.show()
plt.savefig('PlotReportMini.pdf')
"""













plt.clf()
#fig, axs = plt.subplots(2, 2, figsize=(6, 6), sharey=False)
#plt.subplots_adjust(left=0.2,bottom=0.2,right=0.95,top=0.9,wspace=0.4,hspace=0.4)


plt.plot(1/70.,1*np.max(EigenValIm0010011010)/np.max(1), marker='^',c=[1.0, 0.0, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/80.,1*np.max(EigenValIm0010011020)/np.max(1), marker='s',c=[1.0, 0.0, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/90.,1*np.max(EigenValIm0010011030)/np.max(1), marker='p',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/100.,1*np.max(EigenValIm0010011040)/np.max(1), marker='h',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/100.,1*np.max(EigenValIm0010011050)/np.max(1), marker='8',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(                           [0],[1*MaxEigenValIm0011Inf[0]], marker='o',c=[1.0, 0.0, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 1$', markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot([1/70.,1/80.,1/90.,0],[MaxEigenValIm0011010[0],MaxEigenValIm0011020[0],MaxEigenValIm0011030[0],1*MaxEigenValIm0011Inf[0]], marker='.',c=[1.0, 0.0, 0.0],ls='-', markersize=5,markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])

"""
plt.plot(1/10.,1*np.max(EigenValIm001A0011010)/np.max(50)*np.max(1), marker='^',c=[.0, 0.0, 0.0],ls='None', markersize=5,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/20.,1*np.max(EigenValIm001A0011020)/np.max(50)*np.max(1), marker='s',c=[.0, 0.0, 0.0],ls='None', markersize=5,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/30.,1*np.max(EigenValIm001A0011030)/np.max(50)*np.max(1), marker='p',c=[.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/40.,1*np.max(EigenValIm001A0011040)/np.max(50)*np.max(1), marker='h',c=[.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/50.,1*np.max(EigenValIm001A0011050)/np.max(50)*np.max(1), marker='8',c=[.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(                           [0],[1*MaxEigenValIm0011Inf[0]], marker='o',c=[1.0, 0.0, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 1$', markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
#plt.plot([1/10.,1/20.,1/30.,1/40.,1/50.,0],[MaxEigenValIm0011010[0],MaxEigenValIm0011020[0],MaxEigenValIm0011030[0],MaxEigenValIm0011040[0],MaxEigenValIm0011050[0],1*MaxEigenValIm0011Inf[0]], marker='.',c=[.0, 0.0, 0.0],ls='-', markersize=5,markeredgecolor=[0.0*0.8, 0.0*0.8, 0.0*0.8])
"""


plt.plot(1/010.,1*np.max(EigenValIm001B0011010)/np.max(1)*np.max(1), marker='^',c=[1.0, 0.0, 0.0],ls='None', markersize=5,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/020.,1*np.max(EigenValIm001B0011020)/np.max(1)*np.max(1), marker='s',c=[1.0, 0.0, 0.0],ls='None', markersize=5,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/030.,1*np.max(EigenValIm001B0011030)/np.max(1)*np.max(1), marker='p',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/040.,1*np.max(EigenValIm001B0011040)/np.max(1)*np.max(1), marker='h',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/050.,1*np.max(EigenValIm001B0011050)/np.max(1)*np.max(1), marker='8',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/060.,1*np.max(EigenValIm001B0011060)/np.max(1)*np.max(1), marker='.',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/070.,1*np.max(EigenValIm001B0011070)/np.max(1)*np.max(1), marker='.',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/080.,1*np.max(EigenValIm001B0011080)/np.max(1)*np.max(1), marker='.',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/090.,1*np.max(EigenValIm001B0011090)/np.max(1)*np.max(1), marker='.',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/100.,1*np.max(EigenValIm001B0011100)/np.max(1)*np.max(1), marker='.',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/110.,1*np.max(EigenValIm001B0011110)/np.max(1)*np.max(1), marker='.',c=[1.0, 0.0, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(                           [0],[MaxEigenValIm0011Inf002A], marker='o',c=[1.0, 0.0, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 1$', markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])

#plt.plot([1./10,1./20,1./30,1./40,1./50, 1./60,1./70,1./80,1./90,1./100,1./110,0], [np.max(EigenValIm001B0011010),np.max(EigenValIm001B0011020),np.max(EigenValIm001B0011030),np.max(EigenValIm001B0011040),np.max(EigenValIm001B0011050),np.max(EigenValIm001B0011060),np.max(EigenValIm001B0011070),np.max(EigenValIm001B0011080),np.max(EigenValIm001B0011090),np.max(EigenValIm001B0011100),np.max(EigenValIm001B0011110),MaxEigenValIm0011Inf002A],ls='-', markersize=5,label='$a_{\\mathcal{K}}= 1$', markeredgecolor=[1.0*0.8, 0.0*0.8, 0.0*0.8])
#plt.plot([1/10.,1/20.,1/30.,1/40.,1/50.,0],[MaxEigenValIm0011010[0],MaxEigenValIm0011020[0],MaxEigenValIm0011030[0],MaxEigenValIm0011040[0],MaxEigenValIm0011050[0],1*MaxEigenValIm0011Inf[0]], marker='.',c=[.0, 0.0, 0.0],ls='-', markersize=5,markeredgecolor=[0.0*0.8, 0.0*0.8, 0.0*0.8])


plt.plot(1/010.,1*np.max(EigenValIm001B0021010)/np.max(1)*np.max(1), marker='^',c=[1.0, 0.5, 0.0],ls='None', markersize=5,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/020.,1*np.max(EigenValIm001B0021020)/np.max(1)*np.max(1), marker='s',c=[1.0, 0.5, 0.0],ls='None', markersize=5,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/030.,1*np.max(EigenValIm001B0021030)/np.max(1)*np.max(1), marker='p',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/040.,1*np.max(EigenValIm001B0021040)/np.max(1)*np.max(1), marker='h',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/050.,1*np.max(EigenValIm001B0021050)/np.max(1)*np.max(1), marker='8',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/060.,1*np.max(EigenValIm001B0021060)/np.max(1)*np.max(1), marker='^',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/070.,1*np.max(EigenValIm001B0021070)/np.max(1)*np.max(1), marker='s',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/080.,1*np.max(EigenValIm001B0021080)/np.max(1)*np.max(1), marker='p',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/090.,1*np.max(EigenValIm001B0021090)/np.max(1)*np.max(1), marker='h',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/100.,1*np.max(EigenValIm001B0021100)/np.max(1)*np.max(1), marker='8',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(1/110.,1*np.max(EigenValIm001B0021110)/np.max(1)*np.max(1), marker='^',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[.0*0.8, 0.0*0.8, 0.0*0.8])
plt.plot(                           [0],[1*MaxEigenValIm0011Inf[0]], marker='o',c=[1.0, 0.5, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 1$', markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
#plt.plot([1./10,1./20,1./30,1./40,1./50, 1./60,1./70,1./80,1./90,1./100,1./110,0], [np.max(EigenValIm001B0021010),np.max(EigenValIm001B0021020),np.max(EigenValIm001B0021030),np.max(EigenValIm001B0021040),np.max(EigenValIm001B0021050),np.max(EigenValIm001B0021060),np.max(EigenValIm001B0021070),np.max(EigenValIm001B0021080),np.max(EigenValIm001B0021090),np.max(EigenValIm001B0021100),np.max(EigenValIm001B0021110),MaxEigenValIm0011Inf002A],ls='-', markersize=5,label='$a_{\\mathcal{K}}= 1$', markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])

#plt.plot([1./10,1./20,1./30,1./40,1./50, 1./60,1./70,1./80,1./90,1./100,1./110,0], [np.max(EigenValIm001B0021010),np.max(EigenValIm001B0021020),np.max(EigenValIm001B0021030),np.max(EigenValIm001B0021040),np.max(EigenValIm001B0021050),np.max(EigenValIm001B0021060),np.max(EigenValIm001B0021070),np.max(EigenValIm001B0021080),np.max(EigenValIm001B0021090),np.max(EigenValIm001B0021100),np.max(EigenValIm001B0021110),MaxEigenValIm0011Inf002A],ls='-', markersize=5,label='$a_{\\mathcal{K}}= 1$', markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])


plt.semilogy([1./60,1./70,1./80,1./90,1./100.,1./110.,0], [np.max(EigenValIm001B0021060),np.max(EigenValIm001B0021070),np.max(EigenValIm001B0021080),np.max(EigenValIm001B0021090),np.max(EigenValIm001B0021100),np.max(EigenValIm001B0021110),MaxEigenValIm0011Inf002B],ls='-', markersize=5,label='$a_{\\mathcal{K}}= 1$', markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])

"""
plt.plot(1/10.,1*np.max(EigenValIm0010021010), marker='^',c=[1.0, 0.5, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
plt.plot(1/20.,1*np.max(EigenValIm0010021020), marker='s',c=[1.0, 0.5, 0.0],ls='None', markersize=5,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
plt.plot(1/30.,1*np.max(EigenValIm0010021030), marker='p',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
plt.plot(1/40.,1*np.max(EigenValIm0010021040), marker='h',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
plt.plot(1/50.,1*np.max(EigenValIm0010021050), marker='8',c=[1.0, 0.5, 0.0],ls='None', markersize=6,markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
plt.plot(                         [0],  [1*MaxEigenValIm0011Inf[1]], marker='o',c=[1.0, 0.5, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 2$', markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
plt.plot([1/10.,1/20.,1/30.,1/40.,1/50.,0],[1*np.max(EigenValIm0010021010),1*np.max(EigenValIm0010021020),1*np.max(EigenValIm0010021030),1*np.max(EigenValIm0010021040),1*np.max(EigenValIm0010021050),1*MaxEigenValIm0011Inf[1]], marker='None',c=[1.0, 0.5, 0.0],ls='-', markersize=5,label='$a_{\\mathcal{K}}= 2$', markeredgecolor=[1.0*0.8, 0.5*0.8, 0.0*0.8])
"""


plt.plot(1/10.,1*np.max(EigenValIm0010051010), marker='^',c=[0.0, 1.0, 0.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
plt.plot(1/20.,1*np.max(EigenValIm0010051020), marker='s',c=[0.0, 1.0, 0.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
plt.plot(1/30.,1*np.max(EigenValIm0010051030), marker='p',c=[0.0, 1.0, 0.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
plt.plot(1/40.,1*np.max(EigenValIm0010051040), marker='h',c=[0.0, 1.0, 0.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
plt.plot(1/50.,1*np.max(EigenValIm0010051050), marker='8',c=[0.0, 1.0, 0.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
plt.plot(                      [0],  [1*MaxEigenValIm0011Inf[2]], marker='o',c=[0.0, 1.0, 0.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 5$', markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])
plt.plot([1/10.,1/20.,1/30.,1/40.,1/50.,0],[1*np.max(EigenValIm0010051010),1*np.max(EigenValIm0010051020),1*np.max(EigenValIm0010051030),1*np.max(EigenValIm0010051040),1*np.max(EigenValIm0010051050),1*MaxEigenValIm0011Inf[2]], marker='None',c=[0.0, 1.0, 0.0],ls='-', markersize=5,label='$a_{\\mathcal{K}}= 5$', markeredgecolor=[0.0*0.8, 1.0*0.8, 0.0*0.8])

plt.plot(1/10.,1*np.max(EigenValIm0010101010), marker='^',c=[0.0, 0.0, 1.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
plt.plot(1/20.,1*np.max(EigenValIm0010101020), marker='s',c=[0.0, 0.0, 1.0],ls='None', markersize=5,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
plt.plot(1/30.,1*np.max(EigenValIm0010101030), marker='p',c=[0.0, 0.0, 1.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
plt.plot(1/40.,1*np.max(EigenValIm0010101040), marker='h',c=[0.0, 0.0, 1.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
plt.plot(1/50.,1*np.max(EigenValIm0010101050), marker='8',c=[0.0, 0.0, 1.0],ls='None', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
plt.plot(                      [0],  [1*MaxEigenValIm0011Inf[3]], marker='o',c=[0.0, 0.0, 1.0],ls='None', markersize=5,label='$a_{\\mathcal{K}}= 10$',markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])
plt.plot([1/10.,1/20.,1/30.,1/40.,1/50.,0],[1*np.max(EigenValIm0010101010),1*np.max(EigenValIm0010101020),1*np.max(EigenValIm0010101030),1*np.max(EigenValIm0010101040),1*np.max(EigenValIm0010101050),1*MaxEigenValIm0011Inf[3]], marker='None',c=[0.0, 0.0, 1.0],ls='-', markersize=6,markeredgecolor=[0.0*0.8, 0.0*0.8, 1.0*0.8])

plt.grid(True)
#plt.set_xlim(-0.0e+1,+2.0e+1)
#plt.set_xticks(np.arange(-0.0e+1,+2.01e+1, step=4.e-0))
plt.ylim(1e-12,+1.0e-9)
#plt.set_yticks(np.arange(-0.e-2,+3.1e-0, step=0.5e-0))

plt.legend(bbox_to_anchor=(0.3, +1.3), loc=2, borderaxespad=0., ncol=4, labelspacing=1,handleheight=1, columnspacing=0.1, handletextpad=0.1)
#plt.suptitle('$\\ell=0XXX, g_{\\mathcal{K}}=0.1$', fontsize=20, fontname='Times New Roman')
plt.xlabel('$k/\\mathcal{K}\\times 10^{+5}$', fontsize=12, fontname='Times New Roman')
plt.ylabel('Im[$E(k)$]$/E_{\\mathrm{UV}}\\times 10^{+7}$', fontsize=12, fontname='Times New Roman')

#plt.show()
plt.savefig('PlotReportMiniN.pdf')