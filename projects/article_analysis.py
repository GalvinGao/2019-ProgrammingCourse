import csv
import datetime


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

    def __repr__(self):
        return f"[#{self.id}] [{self.date.isoformat()}] {self.title} <{self.district}>: {', '.join(self.content)[:64]}..."

    def get_preview(self, trim: int = 64, include_content: bool = True):
        if include_content:
            return f"[{self.date.isoformat()}] {self.title} <{self.district}>: {', '.join(self.content)[:trim]}..."
        else:
            return f"[{self.date.isoformat()}] {self.title} <{self.district}>"

    def get_data(self):
        return [self.id, self.title, self.date, self.district, "\\n".join(self.content), '|'.join(self.images),
                self.url]


table = csv.reader(open('articles_181202.csv', newline='', encoding='utf8'))

articles = []
for row in table:
    articles.append(Article(row[0], row[1], row[2], row[3], row[4].split('\\n'), row[5].split('|'), row[6]))
