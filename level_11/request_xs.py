# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     request_xs
   Description :
   Author :       kirk
   date：          2021/7/15
-------------------------------------------------
   Change Activity:
                   2021/7/15
-------------------------------------------------
"""
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup


def get_content(target):
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'html.parser')
    texts = bf.find('div', id='content')
    content = texts.text.strip().split('\xa0' * 4)
    return content


def get_chapters():
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    chapter_bs = BeautifulSoup(html, 'html.parser')
    chapters = chapter_bs.find('div', id='list')
    chapters = chapters.find_all('a')
    return chapters


def download_xs(chapter_list):
    for chapter in tqdm(chapter_list):
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')


if __name__ == '__main__':
    server = 'https://www.xsbiquge.com'
    book_name = '诡秘之主.txt'
    target = 'https://www.xsbiquge.com/15_15338/'
    download_xs(get_chapters())
