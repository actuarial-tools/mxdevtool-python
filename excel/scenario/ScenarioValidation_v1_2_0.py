# python script for ScenarioValidation_v1_0_0.xlsm file
# excel link : https://blog.naver.com/montrix/221359670804
# python link : https://blog.naver.com/montrix/***********

import mxdevtool as mx
import matplotlib
import matplotlib.pyplot as plt

# average test ---------

# load average
filename = 'd:/test_multiplemodels.npz'
results = mx.ScenarioResultReader(filename)

print(results.genInfo())

analytic_multiPath = results.analytic_multiPath()
average_multiPath = results.average_multiPath()

timeGrid = results.timeGrid()
t = timeGrid.times()

for i in range(results.assetNum()):
    # red dashes, blue squares and green triangles
    plt.plot(t, analytic_multiPath[i], 'r-', t, average_multiPath[i], 'b-')
    plt.show()

#print(results.analytic_multiPath()[0])

print(timeGrid.date_at(0))
print(timeGrid.closestIndex(2.2))
print(timeGrid.closestIndex_Date(mx.Date(2020, 10, 11)))

print(timeGrid.closestTime(2.2))
print(timeGrid.date_at(762))

# print(results.multiPathAllTPosInterpolateTime(1.2)[1])
# results.multiPathAllTPosInterpolateDate(mx.Date(2020, 10, 11))

# plot



