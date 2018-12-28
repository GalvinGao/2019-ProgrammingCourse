import os

import pymysql
import requests as r
from multiprocessing.dummy import Pool as ThreadPool

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='kinglee-info',
                             charset='utf8mb4')

def do(fetch_single_result):
    article_index, pictures = fetch_single_result
    # print(f"Article {article_index}, {len(pictures[0].split('|'))} files contained.")
    for pic_index, picture in enumerate(pictures[0].split("|")):
        try:
            if len(picture) > 0 and "http" in picture:
                # print(f"Downloading {picture}")
                binary = r.get(picture)
                file_name = f"article{article_index}_pic{pic_index}.{picture.split('.')[-1].lower()}"
                with open(f"nosync_news_picture_mttry\\{file_name}", "bw") as file:
                    file.write(bytes(binary.content))
            else:
                print(f"DLERROR: {picture} is not a valid url.")
        except:
            print(f"SYSERROR: During the process of downloading {picture}, an error has occurred.")

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `images` FROM `articles`"
        cursor.execute(sql)
        fetch_results = cursor.fetchall()
        print(f"fetched data. len: {len(fetch_results)}")
        with ThreadPool(24) as p:
            p.map(do, enumerate(fetch_results))

finally:
    connection.close()
