from pystocklib.common import *


def get_5years_earning_rate():
    url = "https://www.kisrating.com/ratingsStatistics/statics_spread.do"
    selector = "#con_tab1 > div.table_ty1 > table > tbody > tr:nth-child(11) > td:nth-child(9)"
    ret = get_element_by_css_selector(url, selector)
    return ret


def get_net_worth(code):
    url = f"http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A{code}"
    selector = "#highlight_D_A > table > tbody > tr:nth-child(10) > td:nth-child(4)"
    ret = get_element_by_css_selector(url, selector)
    return ret * 100000000

def get_roe(code):
    url = f"http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A{code}"
    selector = "#highlight_D_A > table > tbody > tr:nth-child(18) > td"
    vals = get_elements_by_css_selector(url, selector)
    roe3 = vals[:3]

    # uptrend or downtrend
    if roe3[0] <= roe3[1] <= roe3[2] or roe3[0] >= roe3[1] >= roe3[2]:
        roe = roe3[2]
    else:
        roe = (roe3[0] + roe3[1] * 2 + roe3[2] * 3) / 6     # weighting average
    return roe


def get_shares(code):
    url = f"http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A{code}"
    selector = "#svdMainGrid1 > table > tbody > tr:nth-child(7) > td:nth-child(2)"
    total_shares = get_element_by_css_selector(url, selector, rawdata=True)
    total_shares = total_shares.split("/")[0]
    total_shares = total_shares.replace(",", "")
    total_shares = float(total_shares)

    selector = "#svdMainGrid5 > table > tbody > tr:nth-child(5) > td:nth-child(3)"
    self_hold_shares = get_element_by_css_selector(url, selector)
    if self_hold_shares is None:
        self_hold_shares = 0

    return total_shares - self_hold_shares


def get_current_price(code):
    url = f"http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A{code}"
    selector = "#svdMainChartTxt11"
    return get_element_by_css_selector(url, selector)


if __name__ == "__main__":
    print(get_5years_earning_rate())
    print(get_net_worth("005930"))
    print(get_roe("005930"))
    print(get_shares("005930"))
    print(get_current_price("005930"))