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
import random

import xlrd
from xlutils.copy import copy
import xlwt
import datetime
import calendar


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
                        sheet.write(i, line, '晚班')
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
                            sheet.write(i, line, '晚班')
                            over_lines[line] += 1
                            break
                        else:
                            continue
                    else:
                        if sheet_old.cell(i, line).value != '休' and over_lines.get(line) < 2:
                            sheet.write(i, line, '晚班')
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
                        sheet.write(i, line, '晚班')
                        over_lines[line] += 1
                        break
                    else:
                        continue
    # 保存Excel
    workbook.save(excel_name_)


if __name__ == '__main__':
    pass
    """
    name_list填写值，请区分主管列，员工列，新人列
    对应name_list = [[主管列],员工列,[新人列]]
    没有新人，可以不用加最后的中括号，例如[[主管],员工]
    """
    name_list = [['x'], 'y']
    result = write_online_table(name_list)
    change_over_work_value(result[0], result[-1])
