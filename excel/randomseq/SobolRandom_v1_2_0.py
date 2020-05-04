# python script for SobolRandom_v1_2_0.xlsm file
# excel link : https://blog.naver.com/montrix/221371425358
# python link : https://blog.naver.com/montrix/***********

import mxdevtool as mx

def test():
	print('puedo random test...')

	scenario_num = 1000
	dimension = 365
	seed = 0
	skip = 1024
	isMomentMatching = False
	randomType = "sobol"
	subType = "joekuod7"
	randomTransformType = "invnormal"

	rsg = mx.Rsg(scenario_num, dimension, seed, skip, isMomentMatching, 
				randomType, subType, randomTransformType)

	print(rsg.nextSequence())

if __name__ == "__main__":
    test()