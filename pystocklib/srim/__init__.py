import pystocklib.srim.reader as reader


def estimate_company_value(code, k, w=1):
    """
    estimate company value
    :param code: stock code
    :param k: expected earning rate
    :param w:
    :return: (Value, NetWorth, ROE, Excess Earning)
    """
    net_worth = reader.get_net_worth(code)
    roe = reader.get_roe(code)
    excess_earning = net_worth * (roe - k) * 0.01

    if w == 1:
        value = net_worth + (net_worth * (roe - k)) / k
    else:
        excess_earning = net_worth * (roe - k) * 0.01
        mul = w / (1.0 + k * 0.01 - w)
        value = net_worth + excess_earning * mul

    return value, net_worth, roe, excess_earning


def estimate_price(code, k, w=1):
    """
    calculate reasonable price
    :param code:
    :param k:
    :param w:
    :return: Reasonable Price, Shares, Value, NetWorth, ROE, Excess Earning
    """
    value, net_worth, roe, excess_earning = estimate_company_value(code, k, w)
    shares = reader.get_shares(code)
    price = value / shares
    return price, shares, value, net_worth, roe, excess_earning


def get_disparity(code, k, w=1):
    """
    get disparity that is calculated by (cur_price / est_price ) * 100
    :param code:
    :param k:
    :param w:
    :return:
    """
    est_price, shares, value, net_worth, roe, excess_earning = estimate_price(code, k, w)
    cur_price = reader.get_current_price(code)

    try:
        disparity = (cur_price / est_price) * 100
    except:
        disparity = None
    return disparity, cur_price, est_price, shares, value, net_worth, roe, excess_earning


if __name__ == "__main__":
    k = reader.get_5years_earning_rate()

    #price_w = estimate_price("005930")
    #price_w_10 = estimate_price("005930", w=0.9)
    #price_w_20 = estimate_price("005930", w=0.8)
    #k = reader.get_5years_earning_rate()
    #print(get_disparity("005930", k, w=0.3))

    print(estimate_price("023460", k))



