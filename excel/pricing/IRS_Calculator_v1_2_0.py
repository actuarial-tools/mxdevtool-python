# python script for BK1F_v1_2_0.xlsm file
# excel link : https://blog.naver.com/montrix/221376083438
# python link : https://blog.naver.com/montrix/***********

import mxdevtool as mx

def test():
    print('irs pricing test...')

    #calendar = mx.NullCalendar()
    ref_date = mx.Date(2020, 3, 13)
    mx.Settings.instance().setEvaluationDate(ref_date)

    # ref_date
    marketQuotes = [('1D','Cash',0.012779015127),
                ('3M','Cash',0.0146),
                ('6M','Swap',0.014260714286),
                ('9M','Swap',0.014110714286),
                ('1Y','Swap',0.013975),
                ('18M','Swap',0.0138),
                ('2Y','Swap',0.013653571429),
                ('3Y','Swap',0.0137),
                ('4Y','Swap',0.013775),
                ('5Y','Swap',0.013814285714),
                ('6Y','Swap',0.013817857143),
                ('7Y','Swap',0.013835714286),
                ('8Y','Swap',0.013921428571),
                ('9Y','Swap',0.014042857143),
                ('10Y','Swap',0.014185714286),
                ('12Y','Swap',0.014360714286),
                ('15Y','Swap',0.014146428571),
                ('20Y','Swap',0.013175)]

    swap_quote_tenors = []
    swap_quote_types  = []
    swap_quote_values = []

    for q in marketQuotes:
        swap_quote_tenors.append(q[0])
        swap_quote_types.append(q[1])
        swap_quote_values.append(q[2])

    interpolator1DType = mx.Interpolator1D.Linear
    extrapolation = mx.FlatExtrapolation('forward')

    family_name = 'irskrw_krccp'
    forSettlement = True

    yield_curve = mx.BootstapSwapCurveCCP(ref_date, swap_quote_tenors, swap_quote_types, swap_quote_values, interpolator1DType, extrapolation, family_name, forSettlement)

    swaptype = mx.VanillaSwapExt.Receiver
    nominal = 10000000000
    #settlementDate = calendar.advance(ref_date, mx.Period('1D'))
    settlementDate = mx.Date(2020,3,16)

    maturityTenor = mx.Period('20Y')
    fixedRate = 0.013175
    iborIndexExt = mx.IborIndexExt('krwcd', '3M')
    spread = 0.0

    engine = mx.VanillaSwapExtEngine(yield_curve)
    swap = mx.VanillaSwapExt(swaptype, nominal, settlementDate, maturityTenor, fixedRate, iborIndexExt, spread, family_name, engine)

    print('npv : ', swap.NPV())
    print('rho : ', swap.rho(mx.LegResultType.Net))
    print('conv : ', swap.convexity(mx.LegResultType.Net))

    print('leg rho(Pay) : ', swap.rho(mx.LegResultType.Pay))
    print('leg rho(Rec) : ', swap.rho(mx.LegResultType.Receive))
    print('leg rho(Fix) : ', swap.rho(mx.LegResultType.Fixed))
    print('leg rho(Flo) : ', swap.rho(mx.LegResultType.Floating))

if __name__ == "__main__":
    test()