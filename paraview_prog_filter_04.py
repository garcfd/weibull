# paraview load vtk slice data
# cell data to point data
# calculate magU = mag(U)
# use programmable filter
# cut and paste this code into the programmable filter
# set legend to rainbow with range 0-5 and resolution 5 

import numpy as np

input0 = inputs[0]
numPoints = input0.GetNumberOfPoints()
magU = input0.PointData["magU"]

# weibull constants
Pdir = 12.4  # probability of this wind direction (say 12%)
wbk  = 2.92  # shape factor
wbc  = 4.94  # scale factor
loc  = 1.0   # location

corr = 0.58 # terrain correction factor
uref = 4.5  # ref velocity (u0) at ref height (zref)

# New array for output
pointArray = np.empty(numPoints,dtype=np.float64)

#
# loop through magU array and populate pointArray
#

#---NEN8100 standard
for i in range(numPoints):
    WAF = corr*(magU[i]/uref) # wind amplification factor
    prob5 = Pdir*math.exp( -((( (5.0/WAF)-loc)/wbc)**wbk) ) #5m/sec
    if   prob5 <   2.5:  pointArray[i] = 0.5 # blue
    elif prob5 <   5.0:  pointArray[i] = 1.5 # cyan
    elif prob5 <  10.0:  pointArray[i] = 2.5 # green
    elif prob5 <  20.0:  pointArray[i] = 3.5 # yellow
    elif prob5 >= 20.0:  pointArray[i] = 4.5 # red
    output.PointData.append(pointArray,"NEN 8100")

#---LAWSON(LDDC)
for i in range(numPoints):
    WAF = corr*(magU[i]/uref) # wind amplification factor
    prob4  = Pdir*math.exp( -((( (4.0/WAF)-loc)/wbc)**wbk) ) #4m/sec
    prob6  = Pdir*math.exp( -((( (6.0/WAF)-loc)/wbc)**wbk) ) #6m/sec
    prob8  = Pdir*math.exp( -((( (8.0/WAF)-loc)/wbc)**wbk) ) #8m/sec
    prob10 = Pdir*math.exp( -((((10.0/WAF)-loc)/wbc)**wbk) ) #10m/sec
    if   prob4  <  5.0:  pointArray[i] = 0.5 # blue (sitting)
    elif prob6  <  5.0:  pointArray[i] = 1.5 # cyan (standing)
    elif prob8  <  5.0:  pointArray[i] = 2.5 # green (walking)
    elif prob10 <  5.0:  pointArray[i] = 3.5 # yellow (business walking/cycling)
    elif prob10 >= 5.0:  pointArray[i] = 4.5 # red (uncomfortable)
    output.PointData.append(pointArray,"LawsonLDDC")

#---DAVENPORT
for i in range(numPoints):
    WAF = corr*(magU[i]/uref) # wind amplification factor
    prob3p6  = Pdir*math.exp( -((( (3.6/WAF)-loc)/wbc)**wbk) ) #4m/sec
    prob5p3  = Pdir*math.exp( -((( (5.3/WAF)-loc)/wbc)**wbk) ) #6m/sec
    prob7p6  = Pdir*math.exp( -((( (7.6/WAF)-loc)/wbc)**wbk) ) #8m/sec
    prob9p8  = Pdir*math.exp( -((( (9.8/WAF)-loc)/wbc)**wbk) ) #10m/sec
    prob15p1 = Pdir*math.exp( -((((15.1/WAF)-loc)/wbc)**wbk) ) #10m/sec


    if   prob3p6  <  1.5:  pointArray[i] = 0.5 # blue (sitting long)
    elif prob5p3  <  1.5:  pointArray[i] = 1.5 # cyan (standing short)
    elif prob7p6  <  1.5:  pointArray[i] = 2.5 # green (walking leisurely)
    elif prob9p8  <  1.5:  pointArray[i] = 3.5 # yellow (walking fast)
    elif prob9p8  >= 1.5:  pointArray[i] = 4.5 # red (uncomfortable)
    if prob15p1 >= 0.01: pointArray[i] = 5.5 # red (dangerous)
    output.PointData.append(pointArray,"Davenport")



