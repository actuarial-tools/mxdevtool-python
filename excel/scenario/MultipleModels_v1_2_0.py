# python script for MultipleModels_v1_2_0.xlsm file
# excel link : https://blog.naver.com/montrix/221361343611
# python link : https://blog.naver.com/montrix/***********

import sys, os
import mxdevtool as mx
import numpy as np

filename = 'D:/test_multiplemodels.npz'

def test():
	print('multiplemodels test...', filename)
	
	ref_date = mx.Date(2018, 9, 9)

	initialValue = 10000
	riskFree = 0.032
	dividend = 0.01
	volatility = 0.15

	gbmconst1 = mx.GBMConstModel('gbmconst', initialValue, riskFree, dividend, volatility)
	gbmconst2 = mx.GBMConstModel('gbmconst', initialValue, riskFree, dividend, volatility)
	models = [gbmconst1, gbmconst2]

	corrMatrix = mx.Matrix([[1.0, 0.0],[0.0, 1.0]])

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