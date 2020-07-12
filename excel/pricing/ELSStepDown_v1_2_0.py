# python script for MultipleModels_v1_2_0.xlsm file
# excel link : https://blog.naver.com/montrix/221361343611
# python link : https://blog.naver.com/montrix/***********

import sys, os
import mxdevtool as mx
import numpy as np

filename = 'D:/test_stepdown.npz'


class StepDownPayoff:
	def __init__(self, notional, issue_date, maturity_date, initial_values, ki, ki_flag, coupons):
		pass

	def value(self, multi_path, discount):
		min_s = min(multi_path[0], multi_path[1])

		for cpn in self.coupons:
			if min_s >= cpn.level:
				return cpn.rate
		
		

		return 1


class ScenarioValuationModel:
	def __init__(self):
		pass

	def value(self):
		pass


def build_stepdown():
	notional = 10000
	issue_date = mx.Date(2012,8,22)
	maturity_date = mx.Date(2012,8,22)

	initial_values = [387833, 27450]

	ki = 0.35
	ki_flag = False

	coupons = [(mx.Date(2013,2,13), 0.9, 0.06),
			(mx.Date(2013,8,13), 0.9, 0.12),
			(mx.Date(2014,2,13), 0.85, 0.18),
			(mx.Date(2014,8,13), 0.85, 0.24),
			(mx.Date(2015,2,13), 0.8, 0.30),
			(mx.Date(2015,8,13), 0.8, 0.36)]

	return StepDownPayoff(notional, issue_date, maturity_date, initial_values, ki, ki_flag, coupons)


def build_scenario():
	print('stepdown test...', filename)
	
	ref_date = mx.Date(2012,8,22)

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
	#print(results.multiPath(scenCount=10))
	
		
def pricing():
	results = mx.ScenarioResult(filename)

	payoff = build_stepdown()
	simulNum = results.simulNum()
	refDate = mx.Date(2012,8,22)
	discount_curve = mx.FlatForward(refDate, 0.0307, mx.Actual365Fixed())

	v = 0

	for i in range(simulNum):
		path = results.multiPath(i)

		v += payoff.value(path, discount_curve)

	print('value : ', v)


if __name__ == "__main__":
	
	# build_scenario()
	pricing()

	#mx.npzee_view(filename)