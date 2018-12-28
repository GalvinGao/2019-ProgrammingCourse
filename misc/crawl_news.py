import csv
import datetime
import re
import os
from urllib.parse import urljoin
from multiprocessing.dummy import Pool as ThreadPool
import requests as r
from bs4 import BeautifulSoup
import random

os.environ['NO_PROXY'] = 'best-intl-school.com'

THREADS = 128

url_template = {
    "news_detail": "http://www.best-intl-school.com/zongwu/news.php?id={news_id}",
    "news_list": "http://www.best-intl-school.com/zongwu/newslist.php?lb={news_category}&page={page}"
}


class Article:
    def __init__(self, id: int, title: str, date: str, district: str, content: str, images: list, url: str):
        self.id = id
        self.title = title
        self.date = date
        self.district = district
        self.content = content
        self.images = images
        self.url = url

        self._pre_compile()

    def _pre_compile(self):
        try:
            self.date = datetime.date(*[int(x) for x in self.date.split('-')])
        except TypeError:
            print(f"Date process error: expecting date string in {self.date}")

    def __str__(self):
        return f"[{self.date.isoformat()}] {self.title} <{self.district}>: {', '.join(self.content)[:256]}..."

    def get_preview(self, trim: int = 64, include_content: bool = True):
        if include_content:
            return f"[{self.date.isoformat()}] {self.title} <{self.district}>: {', '.join(self.content)[:trim]}..."
        else:
            return f"[{self.date.isoformat()}] {self.title} <{self.district}>"

    def get_data(self):
        return [self.id, self.title, self.date, self.district, "\\n".join(self.content), '|'.join(self.images), self.url]


global result, soup


all_articles = []

def parser(req):
    html = req.text
    url = req.url
    soup = BeautifulSoup(html, "html5lib")

    # === Content === #
    results = soup.findAll('table', align='center', border='0', cellpadding='0', cellspacing='0', class_='font1',
                           width='800')
    if len(results) == 1:
        result = results[0]
    elif len(results) == 0:
        print(f"Article Content is missing at {url}")
        result = None
    elif len(results) > 1:
        lengths = [len(el.prettify().replace("\n", "").replace("    ", "")) for el in results]
        result = results[sorted(lengths)[-1]]
    # Now we make it clean and neat.
    # REMOVE attribute 'style' !
    del result['style']
    # remove the table layout
    content = [re.sub(r"^(\s)+|(\s)+$", "", x.replace('\xa0', '')) for x in result.text.splitlines() if
               not re.match("^(\s)+$", x) and len(x) > 0]

    id = url.split("?id=")[-1]

    # === Title & Author === #
    title, author = re.findall(r"(.*)\-(.*)$", soup.head.title.text)[0]

    # === Date === #
    date = re.findall(r"\d{4}\-\d{2}\-\d{2}$",
                      soup.find("td", align="center", class_="font1", height="50", valign="middle").text.split(
                          "\u3000")[0])[0]

    # === Images === #
    images = [el['src'] for el in soup.find_all("img") if "img-news" in el['src']]

    article = Article(id, title, date, author, content, images, url)

    # result = "\n".join(paragraphs)
    return article


def get_links(category: str = "", page: int = 1):
    try:
        req = r.get(url_template["news_list"].format(news_category=category, page=page))
    except:
        req = r.get(url_template["news_list"].format(news_category=category, page=page))
    html = req.text
    url = req.url
    soup = BeautifulSoup(html, "html5lib")
    link_list = [html["href"] for html in
                 soup.find("table", width="900", border="0", align="center", cellpadding="0", cellspacing="0").findAll(
                     "a")]
    link_list = [urljoin(url, link) for link in link_list]
    return link_list


def crawl_list(category: str = "", page_range: range = range(1)):
    article_list = []
    with ThreadPool(THREADS) as p:
        p.map(per_list, page_range)

def per_list(page_index):
    for article_index, page_link in enumerate(get_links("", page_index + 1)):
        #print(f"[+ | page {page_index} | article {article_index} ] Crawling...")
        try:
            parse_result = parser(r.get(page_link))
        except:
            parse_result = parser(r.get(page_link))
        all_articles.append(parse_result)
        if random.randint(0, 4) == 0:
            print(f"Articles => {len(all_articles)}")
        #print(f"[+ | page {page_index} | article {article_index} ] Crawled. Preview: {parse_result.get_preview(include_content=False)}")


if __name__ == '__main__':
    crawl_list(page_range=range(1, 582 + 1))
    with open('articles.csv', 'w', newline='', encoding='utf8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerows([result.get_data() for result in all_articles])
