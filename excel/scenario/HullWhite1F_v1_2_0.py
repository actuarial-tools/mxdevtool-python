# python script for HullWhite1F_v1_2_0.xlsm file
# excel link : https://blog.naver.com/montrix/221376083438
# python link : https://blog.naver.com/montrix/***********

import sys, os
import mxdevtool as mx
import numpy as np

filename = 'D:/mxdevtool_results/test_hw1f.npz'

def test():
    print('hw1f test...', filename)
    
    ref_date = mx.Date(2018, 9, 9)

    tenor_rates = [('3M', 0.0151),
                ('6M', 0.0152),
                ('9M', 0.0153),
                ('1Y', 0.0154),
                ('2Y', 0.0155),
                ('3Y', 0.0156),
                ('4Y', 0.0157),
                ('5Y', 0.0158),
                ('7Y', 0.0159),
                ('10Y', 0.016),
                ('15Y', 0.0161),
                ('20Y', 0.0162)]

    tenors = []
    zerorates = []
    interpolator1DType = mx.Interpolator1D.Linear
    extrapolator1DType = mx.Extrapolator1D.FlatForward

    for tr in tenor_rates:
        tenors.append(tr[0])
        zerorates.append(tr[1])

    fittingCurve = mx.ZeroYieldCurveExt(ref_date, tenors, zerorates, interpolator1DType, extrapolator1DType, 'irskrw_krccp')
    alphaCurve = mx.DeterministicParameter([1, 20, 100], [0.1, 0.15, 0.15])
    sigmaCurve = mx.DeterministicParameter([20, 100], [0.01, 0.015])

    hw1f = mx.HullWhite1FModel('hw1f', fittingCurve, alphaCurve, sigmaCurve)
    models = [hw1f]

    corrMatrix = mx.Matrix([[1.0]])

    timeGrid = mx.TimeEqualGrid(ref_date, 3, 365)

    # random 
    scenario_num = 5000
    dimension = (len(timeGrid) - 1)* len(models)
    seed = 100
    skip = 0
    isMomentMatching = False
    randomType = "crude"
    subType = "mersennetwister"
    randomTransformType = "invnormal"

    rsg = mx.Rsg(scenario_num, dimension, seed, skip, isMomentMatching, 
                randomType, subType, randomTransformType)
                
    scen = mx.ScenarioGenerator(models, corrMatrix, timeGrid, rsg, False, filename, False)
    scen.generate()

if __name__ == "__main__":
    
    test()
	#mx.npzee_view(filename)