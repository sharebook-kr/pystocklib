import pystocklib.srim.reader as reader


def estimate_company_value(code, w=1):
    net_worth = reader.get_net_worth(code)
    roe = reader.get_roe(code)
    k = reader.get_5years_earning_rate()

    if w == 1:
        value = net_worth + (net_worth * (roe - k)) / k
    else:
        excess_earning = net_worth * (roe - k) * 0.01
        mul = w / (1.0 + k * 0.01 - w)
        value = net_worth + excess_earning * mul
    return value


def estimate_price(code, w=1):
    value = estimate_company_value(code, w)
    shares = reader.get_shares(code)
    price = value / shares
    return price


def get_disparity(code, w=1):
    est_price = estimate_price("005930", w)
    cur_price = reader.get_current_price(code)

    try:
        disparity = (cur_price / est_price) * 100
    except:
        disparity = 1000
    return disparity


if __name__ == "__main__":
    #price_w = estimate_price("005930")
    #price_w_10 = estimate_price("005930", w=0.9)
    #price_w_20 = estimate_price("005930", w=0.8)
    print(get_disparity("005930", w=0.3))



