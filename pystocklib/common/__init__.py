import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_element_by_css_selector(url, selector, rawdata=False):
    try:
        resp = requests.get(url)
        html = resp.text
        soup = BeautifulSoup(html, "html5lib")
        tag = soup.select(selector)[0]

        if rawdata:
            return tag.text
        else:
            return float(tag.text.replace(",", ""))
    except:
        return None


def get_elements_by_css_selector(url, selector):
    try:
        resp = requests.get(url)
        html = resp.text
        soup = BeautifulSoup(html, "html5lib")
        tags = soup.select(selector)
        return [float(tag.text.replace(",", "")) for tag in tags]
    except:
        return None


def get_code_list_by_market(market=1):
    """
    get listed company information such as code and name
    :param market: 1: all, 2: kospi, 3: kosdaq
    :return: DataFrame
    """
    url = f"http://comp.fnguide.com/SVO2/common/lookup_data.asp?mkt_gb={market}&comp_gb=1"
    resp = requests.get(url)
    data = resp.json()
    df = pd.DataFrame(data)
    df = df.set_index('cd')
    return df


if __name__ == "__main__":
    df = get_code_list_by_market(market=3)
    print(df.head())

