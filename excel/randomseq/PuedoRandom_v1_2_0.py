# python script for PuedoRandom_v1_2_0.xlsm file
# excel link : https://blog.naver.com/montrix/221359670804
# python link : https://blog.naver.com/montrix/***********

import mxdevtool as mx

def test():
	print('puedo random test...')

	scenario_num = 5000
	dimension = 100
	seed = 100
	skip = 0
	isMomentMatching = False
	randomType = "crude"
	subType = "mersennetwister"
	randomTransformType = "invnormal"

	rsg = mx.Rsg(scenario_num, dimension, seed, skip, isMomentMatching, 
				randomType, subType, randomTransformType)

	print(rsg.nextSequence())

if __name__ == "__main__":
    test()