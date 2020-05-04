import pricing.CCP_SwapCurve_v1_2_0 as ccpswap
import pricing.Interpolation_v1_2_0 as interp
import pricing.IRS_Calculator_v1_2_0 as irscalc
import pricing.OptionCalculator_v1_2_0 as optioncalc


if __name__ == "__main__":
    ccpswap.test()
    interp.test()
    irscalc.test()
    optioncalc.test()



