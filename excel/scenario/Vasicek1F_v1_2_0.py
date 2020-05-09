# python script for Vasicek1F_v1_2_0.xlsm file
# excel link : https://blog.naver.com/montrix/221378282753
# python link : https://blog.naver.com/montrix/***********

import sys, os
import mxdevtool as mx
import numpy as np

filename = 'D:/test_vasicek1f.npz'

def test():
	print('vasicek1f test...', filename)
	
	ref_date = mx.Date(2018, 9, 9)
	

	initialValue = 0.02
	meanReverting = 0.1
	longTermRate = 0.042
	volatility = 0.03

	vasicek1f = mx.Vasicek1FModel('gbm', initialValue, meanReverting, longTermRate, volatility)
	models = [vasicek1f]

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