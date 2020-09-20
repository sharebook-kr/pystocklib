import pystocklib.srim as srim
import pystocklib.srim.reader as srim_reader
from pystocklib.common import *
import pandas as pd

# 단일 종목 조회
k = srim_reader.get_5years_earning_rate()
print(srim.get_disparity("005930", k, w=0.7))
print(srim.get_disparity("023460", k, w=0.7))

# 전 종목 조회
# KOSPI code list
kospi = get_code_list_by_market(market=2)
kospi.to_excel("KOSPI.xlsx")

# KOSDAQ code list
kosdaq = get_code_list_by_market(market=3)
kosdaq.to_excel("KOSDAQ.xlsx")

# KOSPI+KOSDAQ
codes = pd.concat([kospi, kosdaq])
index = 0
total = len(codes)
for code in codes.index:
    print(index, code, end="\t")
    disparity = srim.get_disparity(code, k, w=0.7)
    print(disparity)
    index += 1

