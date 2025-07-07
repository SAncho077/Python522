from bs4 import BeautifulSoup
import requests

import csv

def get_html(url):
    r = requests.get(url)
    return r.text



def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\r')
        writer.writerow([data['name'], data['price']])


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    plugins = soup.find_all("div", class_="template-preview-wrapper")
    for plugin in plugins:
        try:
            name = plugin.find("span", class_="template-preview-wrapper-descr").text.strip()
        except AttributeError:
            name = ""
        price = plugin.find("div", class_="template-preview-price")
        data = {"name": name, "price": price}
        write_csv(data)


def main():
    url = "https://tobiz.net/templates/"
    get_data(get_html(url))

if __name__ == '__main__':
    main()