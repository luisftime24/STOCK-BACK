EEUU_GROWTH = 0.03
COMPANY_GROWTH = 0.05
DISCOUNT_RATE = 0.09

def calculate_company_value(fcf, tc, td, crecimiento_eeuu):
    suma = (1+tc)*fcf/((1+td)) + (1+tc)**2*fcf/((1+td)**2)+ (1+tc)**3*fcf/((1+td)**3)+ (1+tc)**4*fcf/((1+td)**4)+ (1+tc)**5*fcf/((1+td)**5)+ (1+tc)**6*fcf/((1+td)**6)+ (1+tc)**7*fcf/((1+td)**7)+ (1+tc)**8*fcf/((1+td)**8)+ (1+tc)**9*fcf/((1+td)**9)+ (1+tc)**10*fcf/((1+td)**10)
    valor_diez = (1+tc)**10*fcf
    tv = valor_diez*(crecimiento_eeuu+1)/(td-crecimiento_eeuu)
    dtv = tv/(1+td)**10
    total = dtv + suma
    return total

def calculate_expected_return(stock, fair_value):
    if stock.currentPrice != None:
        return round((100 * ((fair_value * 0.7) - stock.currentPrice) / stock.currentPrice), 2)
    return 0

def fair_value_calculator(stock):

    free_cash_flow = stock.freeCashflow if stock.freeCashflow else 0
    total_cash = stock.totalCash if stock.totalCash else 0
    total_debt = stock.totalDebt if stock.totalDebt else 0
    shares_out = stock.sharesOutstanding if stock.sharesOutstanding else 0

    if free_cash_flow == 0 or total_cash == 0 or total_debt == 0 or shares_out == 0:
        return 0

    fair_value = round((calculate_company_value(free_cash_flow,COMPANY_GROWTH, DISCOUNT_RATE, EEUU_GROWTH)+total_cash-total_debt)/shares_out, 2)
    return fair_value