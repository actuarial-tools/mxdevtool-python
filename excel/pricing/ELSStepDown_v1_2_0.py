# python script for MultipleModels_v1_2_0.xlsm file
# excel link : https://blog.naver.com/montrix/221361343611
# python link : https://blog.naver.com/montrix/***********

import sys, os
import mxdevtool as mx
import numpy as np

filename = 'D:/test_multiplemodels.npz'


class StepDownPayoff:
	def __init__(self, notional, issue_date, maturity_date, initial_values, ki, ki_flag, coupons):
		pass

	def payoff(self, path, discount):
		pass


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

	
		
def pricing():
	payoff = build_stepdown()
	
	v = 0

	for i in range(scenario_num):
		path = results.multiPath(i)
		v += payoff(path)

	# 해야할일은, stepdown product의 계산을 수행 함. - 이건 built-in으로 해도 될만큼 보편적이긴한데
	# 확장성을 위해서 scenario만들어서 pricing 하는 방식으로 함.
	# 우선 비교를 위해 예전에 했던 pricing 엑셀을 토대로 작성함. - 값이 비슷하게 나오면 성공.
	# greeks들 까지 어떻게 pricing을 하는지 틀을 잡아놔야함. 시나리오 생성만 되었으니까....
	# 우선 그 파일을 찾자.
	# 근데 이게 완성되었다고 해서, 어디다가 팔수 있는건 아니고, 응용할 만큼 예제가 많아야하는데, 작업량이
	# 적지 않을 듯하다.
	# 한번 만들어보면 느낌이 오겠지. 오늘 한시간정도 시간이 있으니까... 우선 한번 ㄱㄱ 생각만 하던거니까...


	
if __name__ == "__main__":
	
	build_scenario()

	#mx.npzee_view(filename)