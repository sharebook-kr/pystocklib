from pystocklib.common import *
import pystocklib.srim as srim
import pystocklib.srim.reader as srim_reader
import time
import pandas as pd

# KOSPI code list
kospi = get_code_list_by_market(market=2)
kospi.to_excel("KOSPI.xlsx")

# KOSDAQ code list
kosdaq = get_code_list_by_market(market=3)
kosdaq.to_excel("KOSDAQ.xlsx")

# KOSPI+KOSDAQ
df = pd.concat([kospi, kosdaq])
#print(df.head())

# k
k = srim_reader.get_5years_earning_rate()

data = []
index = 0
for acode in df.index:
    name = df.loc[acode, "nm"]
    disparity, *others = srim.get_disparity(acode, k, w=0.7)
    roe = others[5]
    data.append({'code': acode, 'name': name, 'disparity': disparity, 'roe': roe})
    time.sleep(3)
    print(index, "/", len(df.index))
    if index == 20:
        break
    index += 1

# filtering the company (ROE > k)
df = pd.DataFrame(data=data)
df = df.set_index('code')
cond = df['roe'] > k
df = df[cond]

# sorting
df2 = df.sort_values(by='disparity')
df2.to_excel("srim.xlsx")

