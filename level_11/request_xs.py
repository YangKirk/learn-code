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


def get_chapters(target):
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    chapter_bs = BeautifulSoup(html, 'html.parser')
    chapters = chapter_bs.find('div', id='list')
    chapters = chapters.find_all('a')
    return chapters


def download_xs(chapter_list, server, book_name):
    for chapter in tqdm(chapter_list):
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')


def gui_download_xs():
    import PySimpleGUI as Psg

    layout = [
        [Psg.Text("请输入此小说所在笔趣阁网站的首页地址:(例如：https://www.xsbiquge.com)", size=(40, 2)), Psg.Input()],
        [Psg.Text("请输入需要下载的小说名:(例如：诡秘之主.txt)", size=(40, 1)), Psg.Input()],
        [Psg.Text("请在笔趣阁找到此小说的章节目录，复制网址输入:(例如：https://www.xsbiquge.com/15_15338/)", size=(40, 2)),
         Psg.Input()],
        [Psg.Button("开始下载")],
    ]

    window = Psg.Window("笔趣阁小说下载脚本", layout)

    while True:
        event, values = window.read()
        server = values[0]
        book_name = values[1]
        target = values[2]
        if event == '开始下载':
            Psg.popup('等待下载完成')
            window.close()
            download_xs(get_chapters(target), server, book_name)
        else:
            break


if __name__ == '__main__':
    # server = 'https://www.xsbiquge.com'
    # book_name = '诡秘之主.txt'
    # target = 'https://www.xsbiquge.com/15_15338/'
    gui_download_xs()
