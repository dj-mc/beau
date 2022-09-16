import requests
from bs4 import BeautifulSoup


def parse_price(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    price = soup.find(
        "span", {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}
    ).text
    return price


def parse(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    return soup


if __name__ == "__main__":
    # print(parse_price("https://finance.yahoo.com/quote/META?p=META"))
    print(parse("https://www.amazon.com/gp/product/B07V4GCFP9"))
