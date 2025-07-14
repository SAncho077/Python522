from bs4 import BeautifulSoup
import requests


class Parserss:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        news = self.html.find_all("div", class_ = "short-news")
        for item in news:
            time = item.find("span", class_="time").text
            text = item.find("a", class_="short-text")["title"]
            self.res.append({
                'time': time,
                'text': text,

            })


    def save(self, num):
        with open(self.path, 'a', encoding='utf-8') as fw:
            i = 1
            fw.write(f'Страница: {num}\n')
            for item in self.res:
                fw.write(f"Новость №{i}\n\nВремя: {item["time"]}\nТекст: {item["text"]}\n\n{'*' * 40}\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save(1)