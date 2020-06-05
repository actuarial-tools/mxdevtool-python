# python script for GBM_v1_2_0.xlsm file
# excel link : https://blog.naver.com/montrix/221361343611
# python link : https://blog.naver.com/montrix/***********

import sys, os
import mxdevtool as mx
import numpy as np

filename = 'D:/test_gbm.npz'

def test():
    print('gbm test...', filename)

    ref_date = mx.Date(2018, 9, 9)

    initialValue = 10000

    # (period, rf, div)
    tenor_rates = [('3M', 0.0151, 0.01),
                ('6M', 0.0152, 0.01),
                ('9M', 0.0153, 0.01),
                ('1Y', 0.0154, 0.01),
                ('2Y', 0.0155, 0.01),
                ('3Y', 0.0156, 0.01),
                ('4Y', 0.0157, 0.01),
                ('5Y', 0.0158, 0.01),
                ('7Y', 0.0159, 0.01),
                ('10Y', 0.016, 0.01),
                ('15Y', 0.0161, 0.01),
                ('20Y', 0.0162, 0.01)]

    tenors = []
    rf_rates = []
    div_rates = []
    vols = []

    interpolator1DType = mx.Interpolator1D.Linear
    extrapolator1DType = mx.Extrapolator1D.FlatForward

    for tr in tenor_rates:
        tenors.append(tr[0])
        rf_rates.append(tr[1])
        div_rates.append(tr[2])
        
    rfCurve = mx.ZeroYieldCurveExt(ref_date, tenors, rf_rates, interpolator1DType, extrapolator1DType, 'irskrw_krccp')
    divCurve = mx.ZeroYieldCurveExt(ref_date, tenors, div_rates, interpolator1DType, extrapolator1DType, 'irskrw_krccp')
    volCurve = mx.BlackConstantVol(ref_date, 0.2, 'irskrw_krccp')

    gbm = mx.GBMModel('gbm', initialValue, rfCurve, divCurve, volCurve)
    models = [ gbm ]

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
    
    results = mx.ScenarioResult(filename)
    print(results.multiPath(scenCount=10))

if __name__ == "__main__":
	
	test()
	#mx.npzee_view(filename)