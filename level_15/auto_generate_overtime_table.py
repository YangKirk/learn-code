# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     auto_generate_overtime_table.py
   Description :  
   Author :       kirk
   date：          2022/3/30
-------------------------------------------------
   Change Activity:
                   2022/3/30
-------------------------------------------------
"""
import json
import os
import random

import xlrd
from xlutils.copy import copy
import xlwt
import datetime
import calendar
from tkinter import ttk, Tk, StringVar

RESOURCE_DIR = os.path.dirname(__file__)


def get_leader_work_list(list_count: int):
    relax_times = 0
    item_list = ['白班', '休']
    relax_skip = 0
    work_list = []
    while True:
        for _ in range(list_count):
            write_data = random.choice(item_list)
            if write_data == '白班':
                relax_skip += 1
            else:
                if relax_skip >= 3:
                    relax_times += 1
                    relax_skip = 0
                    if relax_times == 5:
                        item_list.remove('休')
                else:
                    write_data = '白班'
                    relax_skip += 1
            work_list.append(write_data)
        if work_list.count('休') >= 5:
            return work_list
        else:
            work_list.clear()


def get_date_list(year_: int, month_: int):
    """
    根据传入的年月获取日期列表和星期列表
    :param month_: 传入的排班表月份
    :param year_: 传入的排班表年份
    :return: tuple(date_list, week_list)
    """
    date_list = []  # 日期列表
    week_list = []  # 星期列表
    week_list_ = []  # 星期的数字列表
    week_dict = {0: '星期一',
                 1: '星期二',
                 2: '星期三',
                 3: '星期四',
                 4: '星期五',
                 5: '星期六',
                 6: '星期天'}
    # 获取传入月份的天数
    local_month_days = calendar.monthrange(year_, month_)[-1]

    # 获取月份第一天的星期
    month_first_week = calendar.monthrange(year_, month_)[0]

    # 生成星期的数字列表
    for _ in range(1, local_month_days + 1):
        if month_first_week == 7:
            month_first_week = 0
        week_list_.append(month_first_week)
        month_first_week += 1
        date_list.append('{}月{}日'.format(month_, _))

    for _ in week_list_:
        week_list.append(week_dict.get(_))

    return date_list, week_list


def write_online_table(name_list_: list):
    """
    根据传入的名字列表，编写排班表
    :param name_list_: 传入的名字列表
    :return: None
    """
    # 获取值班表年份
    table_year = datetime.date.today().year if (datetime.date.today().month + 1) != 13 \
        else datetime.date.today().year + 1

    # 获取值班表月份
    table_month = datetime.date.today().month + 1 if (datetime.date.today().month + 1) != 13 else 1

    # 创建workbook
    # encoding:设置字符编码，一般要这样设置：w = Workbook(encoding=’utf-8’)，就可以在excel中输出中文了。默认是ascii
    # style_compression:表示是否压缩，不常用。
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    # 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格
    # 其中的值班表是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False
    sheet = workbook.add_sheet('值班表', cell_overwrite_ok=True)

    # 第一行数据列表
    first_line_list = ['日期', '星期']
    first_line_list.extend(name_list_[0])
    if type(name_list_[-1]) is list:
        first_line_list.extend(name_list_[1:-1])
        first_line_list.extend(name_list_[-1])
    else:
        first_line_list.extend(name_list_[1:])

    # 向表中添加第一行数据
    first_line_count = 0
    for item in first_line_list:
        sheet.write(0, first_line_count, item)  # 其中的'0-行, first_line_count-列'指定表中的单元，item是向该单元写入的内容
        first_line_count += 1

    # 获取日期列表
    tup_r = get_date_list(table_year, table_month)
    date_list = tup_r[0]

    # 获取星期列表
    week_list = tup_r[-1]

    # 向表中添加第一列数据
    first_row_count = 1  # 除开第一行标题行
    for date in date_list:
        sheet.write(first_row_count, 0, date)
        first_row_count += 1

    # 向表中添加第二列数据
    second_row_count = 1
    for week in week_list:
        sheet.write(second_row_count, 1, week)
        second_row_count += 1

    # 向表中灌数据
    if type(name_list_[-1]) is list:
        max_row = len(name_list_[1:-1]) + len(name_list_[0]) + len(name_list_[-1]) + 2
    else:
        max_row = len(name_list_[0]) + len(name_list_[1:]) + 2
    for i in range(2, max_row):
        index = 0
        write_data_list = get_leader_work_list(len(date_list))
        for j in range(1, len(date_list) + 1):
            sheet.write(j, i, write_data_list[index])
            index += 1

    # 保存
    excel_name = fr'{table_year}年{table_month}月值班表.xlsx'
    workbook.save(excel_name)
    return excel_name, name_list_


def change_over_work_value(excel_name_: str, name_list_: list):
    # 读取Excel内容
    workbook_old = xlrd.open_workbook(excel_name_)
    workbook = copy(workbook_old)

    # 读取所有的sheet name
    sheet_old = workbook_old.sheet_by_name('值班表')
    sheet = workbook.get_sheet(0)

    # cols_max & rows_max
    # print(sheet_old.ncols)    # 打印最大列数
    # print(sheet_old.nrows)    # 打印最大行数

    # 获取主管列
    leader_col_start = 0
    for i in range(sheet_old.ncols):
        if sheet_old.cell_value(0, i) == name_list_[0][-1]:
            leader_col_start = i
            break

    # 获取当月天数
    date_count = sheet_old.nrows - 1

    # 添加晚班样式
    style = xlwt.XFStyle()

    pattern = xlwt.Pattern()

    pattern.pattern = xlwt.Pattern.SOLID_PATTERN

    pattern.pattern_fore_colour = xlwt.Style.colour_map['tan']  # 设置单元格背景色为棕褐色色

    style.pattern = pattern

    # 给员工灌晚班数据
    # 有新员工
    if type(name_list_[-1]) is list:
        over_lines = dict.fromkeys(range(leader_col_start + 1, sheet_old.ncols), 0)
        over_max = 5
        # 给普通员工加晚班
        for i in range(1, 16):
            for _ in range(100):
                line = random.randint(leader_col_start + 1, sheet_old.ncols - len(name_list_[-1]) - 1)
                if '晚班' not in sheet_old.row_values(i, leader_col_start + 1, sheet_old.ncols):
                    if sheet_old.cell(i, line).value != '休' and over_lines.get(line) < over_max:
                        sheet.write(i, line, '晚班', style=style)
                        over_lines[line] += 1
                        break
                    else:
                        continue

        # 给新员工和普通员工一起加晚班
        for i in range(16, sheet_old.nrows):
            for _ in range(100):
                line = random.randint(leader_col_start + 1, sheet_old.ncols - 1)
                if '晚班' not in sheet_old.row_values(i, leader_col_start + 1, sheet_old.ncols):
                    if line < sheet_old.ncols - len(name_list_[-1]):
                        if sheet_old.cell(i, line).value != '休' and over_lines.get(line) < over_max:
                            sheet.write(i, line, '晚班', style=style)
                            over_lines[line] += 1
                            break
                        else:
                            continue
                    else:
                        if sheet_old.cell(i, line).value != '休' and over_lines.get(line) < 2:
                            sheet.write(i, line, '晚班', style=style)
                            over_lines[line] += 1
                            break
                        else:
                            continue

    # 没有新员工
    else:
        over_lines = dict.fromkeys(range(leader_col_start + 1, sheet_old.ncols), 0)
        over_count = date_count - date_count % len(name_list_[1:])
        over_max = date_count // len(name_list_[1:])
        for i in range(1, over_count + 1):
            for _ in range(100):
                line = random.randint(leader_col_start + 1, sheet_old.ncols - 1)
                if '晚班' not in sheet_old.row_values(i, leader_col_start + 1, sheet_old.ncols):
                    if sheet_old.cell(i, line).value != '休' and over_lines.get(line) < over_max:
                        sheet.write(i, line, '晚班', style=style)
                        over_lines[line] += 1
                        break
                    else:
                        continue
    # 保存Excel
    workbook.save(excel_name_)


def get_name_list():
    conf_file_path = RESOURCE_DIR + "/write_table.json"
    conf = None
    # 如果json配置文件存在就读取字典到conf
    if os.path.isfile(conf_file_path):
        with open(conf_file_path, 'r') as data:
            conf = json.load(data)
    name_list_ = [[], ]
    dic_list = []
    for value in conf.values():
        dic_list.append(value)
    for value in dic_list[0:4]:
        if value not in ["", None]:
            name_list_[0].append(value)
    for value in dic_list[4:14]:
        if value not in ["", None]:
            name_list_.append(value)
    new_list = []
    for value in dic_list[14:]:
        if value not in ["", None]:
            new_list.append(value)
    if len(new_list) != 0:
        name_list_.append(new_list)
    print(name_list_)
    return name_list_


def gui_for_create_online_table():
    root = Tk()
    root.title('值班表生成工具(按提示填好名字保存退出即可)')

    conf_file_path = RESOURCE_DIR + "/write_table.json"
    conf = None
    # 如果json配置文件存在就读取字典到conf
    if os.path.isfile(conf_file_path):
        with open(conf_file_path, 'r') as data:
            conf = json.load(data)

    # 设定文本框默认值
    e1_default = StringVar()
    e1_default.set("" if conf is None else conf.get("e1"))
    e2_default = StringVar()
    e2_default.set("" if conf is None else conf.get("e2"))
    e3_default = StringVar()
    e3_default.set("" if conf is None else conf.get("e3"))
    e4_default = StringVar()
    e4_default.set("" if conf is None else conf.get("e4"))
    n1_default = StringVar()
    n1_default.set("" if conf is None else conf.get("n1"))
    n2_default = StringVar()
    n2_default.set("" if conf is None else conf.get("n2"))
    n3_default = StringVar()
    n3_default.set("" if conf is None else conf.get("n3"))
    n4_default = StringVar()
    n4_default.set("" if conf is None else conf.get("n4"))
    n5_default = StringVar()
    n5_default.set("" if conf is None else conf.get("n5"))
    n6_default = StringVar()
    n6_default.set("" if conf is None else conf.get("n6"))
    n7_default = StringVar()
    n7_default.set("" if conf is None else conf.get("n7"))
    n8_default = StringVar()
    n8_default.set("" if conf is None else conf.get("n8"))
    n9_default = StringVar()
    n9_default.set("" if conf is None else conf.get("n9"))
    n10_default = StringVar()
    n10_default.set("" if conf is None else conf.get("n10"))
    m1_default = StringVar()
    m1_default.set("" if conf is None else conf.get("m1"))
    m2_default = StringVar()
    m2_default.set("" if conf is None else conf.get("m2"))
    m3_default = StringVar()
    m3_default.set("" if conf is None else conf.get("m3"))
    m4_default = StringVar()
    m4_default.set("" if conf is None else conf.get("m4"))

    def btn1_clear_all():
        """
        清楚所有栏数据
        :return:
        """
        for _ in [e1, e2, e3, e4, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, m1, m2, m3, m4]:
            _.delete(0, len(_.get()))

    def btn2_save_and_exit():
        """
        保存输入并退出
        :return:
        """
        d = dict(e1=e1_default.get(), e2=e2_default.get(), e3=e3_default.get(), e4=e4_default.get(),
                 n1=n1_default.get(),
                 n2=n2_default.get(), n3=n3_default.get(), n4=n4_default.get(), n5=n5_default.get(),
                 n6=n6_default.get(),
                 n7=n7_default.get(), n8=n8_default.get(), n9=n9_default.get(), n10=n10_default.get(),
                 m1=m1_default.get(),
                 m2=m2_default.get(), m3=m3_default.get(), m4=m4_default.get())
        # 保存配置
        with open(conf_file_path, "w") as f:
            f.write(json.dumps(d))

        root.destroy()
        root.quit()

    # 生成主管列
    ttk.Label(root, text="经理名:", width=15).grid(row=0, sticky="W")
    e1 = ttk.Entry(root, width=20, textvariable=e1_default)
    e1.grid(row=0, column=1, sticky="E")

    ttk.Label(root, text="副经理名:", width=15).grid(row=1, sticky="W")
    e2 = ttk.Entry(root, width=20, textvariable=e2_default)
    e2.grid(row=1, column=1, sticky="E")

    ttk.Label(root, text="主管名1:", width=15).grid(row=2, sticky="W")
    e3 = ttk.Entry(root, width=20, textvariable=e3_default)
    e3.grid(row=2, column=1, sticky="E")

    ttk.Label(root, text="主管名2:", width=15).grid(row=3, sticky="W")
    e4 = ttk.Entry(root, width=20, textvariable=e4_default)
    e4.grid(row=3, column=1, sticky="E")

    # 生成员工列
    ttk.Label(root, text="\t员工名1:", width=20).grid(row=0, column=2, sticky="W")
    n1 = ttk.Entry(root, width=20, textvariable=n1_default)
    n1.grid(row=0, column=4, sticky="E")

    ttk.Label(root, text="\t员工名2:", width=20).grid(row=1, column=2, sticky="W")
    n2 = ttk.Entry(root, width=20, textvariable=n2_default)
    n2.grid(row=1, column=4, sticky="E")

    ttk.Label(root, text="\t员工名3:", width=20).grid(row=2, column=2, sticky="W")
    n3 = ttk.Entry(root, width=20, textvariable=n3_default)
    n3.grid(row=2, column=4, sticky="E")

    ttk.Label(root, text="\t员工名4:", width=20).grid(row=3, column=2, sticky="W")
    n4 = ttk.Entry(root, width=20, textvariable=n4_default)
    n4.grid(row=3, column=4, sticky="E")

    ttk.Label(root, text="\t员工名5:", width=20).grid(row=4, column=2, sticky="W")
    n5 = ttk.Entry(root, width=20, textvariable=n5_default)
    n5.grid(row=4, column=4, sticky="E")

    ttk.Label(root, text="\t员工名6:", width=20).grid(row=5, column=2, sticky="W")
    n6 = ttk.Entry(root, width=20, textvariable=n6_default)
    n6.grid(row=5, column=4, sticky="E")

    ttk.Label(root, text="\t员工名7:", width=20).grid(row=6, column=2, sticky="W")
    n7 = ttk.Entry(root, width=20, textvariable=n7_default)
    n7.grid(row=6, column=4, sticky="E")

    ttk.Label(root, text="\t员工名8:", width=20).grid(row=7, column=2, sticky="W")
    n8 = ttk.Entry(root, width=20, textvariable=n8_default)
    n8.grid(row=7, column=4, sticky="E")

    ttk.Label(root, text="\t员工名9:", width=20).grid(row=8, column=2, sticky="W")
    n9 = ttk.Entry(root, width=20, textvariable=n9_default)
    n9.grid(row=8, column=4, sticky="E")

    ttk.Label(root, text="\t员工名10:", width=20).grid(row=9, column=2, sticky="W")
    n10 = ttk.Entry(root, width=20, textvariable=n10_default)
    n10.grid(row=9, column=4, sticky="E")

    ttk.Label(root, text="\t新员工名1:", width=20).grid(row=0, column=6, sticky="W")
    m1 = ttk.Entry(root, width=20, textvariable=m1_default)
    m1.grid(row=0, column=8, sticky="E")

    ttk.Label(root, text="\t新员工名2:", width=20).grid(row=1, column=6, sticky="W")
    m2 = ttk.Entry(root, width=20, textvariable=m2_default)
    m2.grid(row=1, column=8, sticky="E")

    ttk.Label(root, text="\t新员工名3:", width=20).grid(row=2, column=6, sticky="W")
    m3 = ttk.Entry(root, width=20, textvariable=m3_default)
    m3.grid(row=2, column=8, sticky="E")

    ttk.Label(root, text="\t新员工名4:", width=20).grid(row=3, column=6, sticky="W")
    m4 = ttk.Entry(root, width=20, textvariable=m4_default)
    m4.grid(row=3, column=8, sticky="E")

    ttk.Button(root, text="清空所有栏", width=20, command=lambda: btn1_clear_all()).grid(row=9, column=0, sticky="W")
    ttk.Button(root, text="保存并退出", width=20, command=lambda: btn2_save_and_exit()).grid(row=9, column=8, sticky="W")

    # 居中
    root.update()  # 刷新窗口，用來獲取窗口大小
    window_left_top_point = (root.winfo_screenwidth() // 2 - root.winfo_width() // 2,
                             root.winfo_screenheight() // 2 - root.winfo_height() // 2)
    root.geometry('+{0}+{1}'.format(*window_left_top_point))
    root.update()
    root.mainloop()


"""
name_list填写值，请区分主管列，员工列，新人列
对应name_list = [[主管列],员工列,[新人列]]
没有新人，可以不用加最后的中括号，例如[[主管],员工]
"""
gui_for_create_online_table()
name_list = get_name_list()
if len(name_list) > 1:
    result = write_online_table(name_list)
    change_over_work_value(result[0], result[-1])
