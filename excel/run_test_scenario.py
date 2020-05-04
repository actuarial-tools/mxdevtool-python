import scenario.BK1F_v1_2_0 as bk1f
import scenario.CIR1F_v1_2_0 as cir1f
import scenario.GBM_v1_2_0 as gbm
import scenario.GBMConst_v1_2_0 as gbmconst
import scenario.GTwoExt_v1_2_0 as gtwoext
import scenario.Heston_v1_2_0 as heston
import scenario.HullWhite1F_v1_2_0 as hw1f
import scenario.MultipleModels_v1_2_0 as multimodels
import scenario.Vasicek1F_v1_2_0 as vasicek1f


if __name__ == "__main__":
    bk1f.test()
    cir1f.test()
    gbm.test()
    gbmconst.test()
    gtwoext.test()
    heston.test()
    hw1f.test()
    multimodels.test()
    vasicek1f.test()



