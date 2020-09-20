import pystocklib.srim as srim
import pystocklib.srim.reader as srim_reader
from pystocklib.common import *
import pandas as pd

# KOSPI code list
kospi = get_code_list_by_market(market=2)
kospi.to_excel("KOSPI.xlsx")

# KOSDAQ code list
kosdaq = get_code_list_by_market(market=3)
kosdaq.to_excel("KOSDAQ.xlsx")

# KOSPI+KOSDAQ
codes = pd.concat([kospi, kosdaq])

k = srim_reader.get_5years_earning_rate()

# error cases
#print(srim.estimate_price("344820", k))

code_list = list(codes.index)
#index = code_list.index("A318410")
#code_list = code_list[index: ]

for i, code in enumerate(code_list):
    print(f"{i}/{len(code_list)} {code}", end="\t")
    price = srim.estimate_price(code, k)
    print(price)


'''
# 삼성전자
code = "005930"
price0 = srim.estimate_price(code, k)
price1 = srim.estimate_price(code, k, w=0.9)
price2 = srim.estimate_price(code, k, w=0.8)
print("초과이익 지속      : ", price0[0])
print("초과이익 감소 (10%): ", price1[0])
print("초과이익 감소 (20%): ", price2[0])

code = "023460"
price0 = srim.estimate_price(code, k)
price1 = srim.estimate_price(code, k, w=0.9)
price2 = srim.estimate_price(code, k, w=0.8)
print("초과이익 지속      : ", price0[0])
print("초과이익 감소 (10%): ", price1[0])
print("초과이익 감소 (20%): ", price2[0])
'''
