from pystocklib.common import *
import pystocklib.srim as srim
import time
import pandas as pd

# kospi + kosdaq
df = get_code_list_by_market()
#print(df.head())

data = []
index = 0
for acode in df.index:
    name = df.loc[acode, "nm"]
    disparity = srim.get_disparity(acode, w=0.7)
    data.append({'code': acode, 'name': name, 'disparity': disparity})
    time.sleep(3)
    print(index, "/", len(df.index))

    #if index == 5:
    #    break
    index += 1

# sorting
df = pd.DataFrame(data=data)
df = df.set_index('code')
df2 = df.sort_values(by='disparity')
df2.to_excel("srim.xlsx")

