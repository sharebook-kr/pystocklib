import pystocklib.srim as srim
import pystocklib.srim.reader as srim_reader

k = srim_reader.get_5years_earning_rate()

print(srim.get_disparity("005930", k, w=0.7))
print(srim.get_disparity("023460", k, w=0.7))
