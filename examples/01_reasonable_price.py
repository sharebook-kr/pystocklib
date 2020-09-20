import pystocklib.srim as srim

price0 = srim.estimate_price("005930")
price1 = srim.estimate_price("005930", w=0.9)
price2 = srim.estimate_price("005930", w=0.8)

print("초과이익 지속      : ", price0)
print("초과이익 감소 (10%): ", price1)
print("초과이익 감소 (20%): ", price2)

