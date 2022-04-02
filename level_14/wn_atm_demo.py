# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     wn_atm_demo.py
   Description :  
   Author :       kirk
   date：          2022/3/21
-------------------------------------------------
   Change Activity:
                   2022/3/21
-------------------------------------------------
"""
"""
1.编写一个简单的蜗牛ATM的注册和登录功能，要求如下:

a.利用两个列表, -个存放用户名，-个存放密码，下标位置一-对应好。 注册时,判断用户名是否已存在,密码长度要大于等于6位，如果输入错误要有相应提示，并退出系统。

b.如果用户注册成功，则提示用户进行登录。要求用户输入用户名和密码，只有当用户名和密码均正确才能提示用户登录成功，否则提示用户名或密码错误，并退出系统。

2.在上题的基础上加入错误重试功能，不管是注册阶段还是登录阶段,一旦用户输入错误,都将提示用户重新输入,直到正确为止。

3.在前面的蜗牛ATM项目的基础上进一步进行改进， 要求使用一个二维列表来保存用户名和密码, 二维列表如: users = ['zhangsan', '123456'], [lisi', 'admin123'], ['admin', 'adminadmin']]并且添加如下操作主菜单,

******欢仰来到Woniu ATM********

*****请选择操作菜单..***

****1.注册2.登录3.退卡****

用户选择对应的菜单选项进行操作，每次操作完后继续进入主菜单，用户输入3之后可以结束并退出应用。

4.在3题项目的基础上进一步进行改进， 要求使用一个列表加字典的形式来保存用户的信息，并增加-个账户余额信息项。

用户信息的保存格式如下，

users_list = [
    {'user': 'zhangsan', 'password': '123456', 'balance': 1000},
    {'user': 'lisi', 'password': '111111', 'balance': 2500},
    {'user': 'wangwu', 'password': 'wangwu', 'balance': 100}
]

添加如下操作主菜单,

*****欢避来到Woniu ATM******

*****请选择操作菜单..*****

***1.注册2.登录3.查询余额4.退卡****

用户选择对应的菜单选项进行操作，每次操作完后继续进入主菜单，用户输入4之后可以结束并退出应用。用户注册成功后奖励3000元账户余额。

5.继续改进蜗牛ATM的功能，功能要求:

添加如下操作主菜单，

******欢迎来到Wn ATM******
********请选择操作菜单********
******1.注册 2.登陆 3.查询余额 4.存款 5.取款 6.转账 7.取卡 ***
实现增加的菜单的功能。
注意，存取款要求只能是100的整数倍。
"""

# 1
# user_name = ['zhangsan', 'lisi', 'wangwu']
# pass_word = ['111111', '222222', '333333']


# class WnATM:
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def register():
#         print('欢迎使用WN ATM系统')
#         user_n = input('[注册]请输入您的用户名：')
#         if user_n.strip() in user_name:  # 用户输入的用户名已经在用户列表内
#             print('用户已存在')
#             return False  # 当前函数结束
#         else:
#             pass_wd = input('[注册]请输入您的密码：')
#             if len(pass_wd) < 6:
#                 print('密码长度小于6位，请检查')
#                 return False
#             else:
#                 # 注册成功，将用户名和密码加入数据列表
#                 user_name.append(user_n)
#                 pass_word.append(pass_wd)
#                 print('恭喜您注册成功!')
#                 return True
#
#     @staticmethod
#     def login():
#         user_n_login = input('[登陆]请输入您的用户名：')
#         pass_wd_login = input('[登陆]请输入您的密码：')
#         if user_n_login in user_name:
#             i = user_name.index(user_n_login)
#             if pass_word[i] == pass_wd_login:
#                 print('恭喜您登陆成功！')
#                 return True
#             else:
#                 print('用户名或者密码错误！')
#         else:
#             print('用户名或者密码错误！')

# 2
# user_name = ['zhangsan', 'lisi', 'wangwu']
# pass_word = ['111111', '222222', '333333']

# class WnATM:
#     @staticmethod
#     def register():
#         print('欢迎使用WN ATM系统')
#         while True:
#             user_n = input('[注册]请输入您的用户名：')
#             if user_n.strip() in user_name:  # 用户输入的用户名已经在用户列表内
#                 print('用户已存在')
#             else:
#                 break
#
#         while True:
#             pass_wd = input('[注册]请输入您的密码：')
#             if len(pass_wd) < 6:
#                 print('密码长度小于6位，请检查')
#             else:
#                 break
#
#         # 注册成功，将用户名和密码加入数据列表
#         user_name.append(user_n)
#         pass_word.append(pass_wd)
#         print('恭喜您注册成功!')
#         return True
#
#     @staticmethod
#     def login():
#         while True:
#             user_n_login = input('[登陆]请输入您的用户名：')
#             pass_wd_login = input('[登陆]请输入您的密码：')
#             if user_n_login in user_name:
#                 i = user_name.index(user_n_login)
#                 if pass_word[i] == pass_wd_login:
#                     print('恭喜您登陆成功！')
#                     break
#                 else:
#                     print('用户名或者密码错误！')
#             else:
#                 print('用户名或者密码错误！')


# 3
# users = [['zhangsan', '123456'], ['lisi', 'admin123'], ['admin', 'adminadmin']]


# class WnATM:
#     @staticmethod
#     def register():
#         print('欢迎使用WN ATM系统')
#         while True:
#             user_n = input('[注册]请输入您的用户名：')
#             for item in users:
#                 if user_n.strip() == item[0]:  # 用户输入的用户名已经在用户列表内
#                     print('用户已存在')
#                     break
#             else:
#                 pass_wd = input('[注册]请输入您的密码：')
#                 if len(pass_wd) < 6:
#                     print('密码长度小于6位，请检查')
#                 else:
#                     # 注册成功，将用户名和密码加入数据列表
#                     users.append([user_n, pass_wd])
#                     print('恭喜您注册成功!')
#                     return True
#
#     @staticmethod
#     def login():
#         while True:
#             user_n_login = input('[登陆]请输入您的用户名：')
#             pass_wd_login = input('[登陆]请输入您的密码：')
#             if [user_n_login, pass_wd_login] in users:
#                 print('恭喜您登陆成功！')
#                 return
#             else:
#                 print('用户名或者密码错误！')
#
#     @staticmethod
#     def run_main():
#         man = """
#               ******欢迎来到Wn ATM******
#             ********请选择操作菜单********
#             ******1.注册 2.登陆 3.退卡 ***
#               """
#         while True:
#             print(man)
#             man_select = input('请输入您选择的操作项目:')
#             if man_select == '1':
#                 WnATM.register()
#             elif man_select == '2':
#                 WnATM.login()
#             elif man_select == '3':
#                 print('感谢您的使用，欢迎下次再来！')
#                 break
#             else:
#                 print('指令输入错误，请重新选择操作项目!')


# 4
# users_list = [
#     {'user': 'zhangsan', 'password': '123456', 'balance': 1000},
#     {'user': 'lisi', 'password': '111111', 'balance': 2500},
#     {'user': 'wangwu', 'password': 'wangwu', 'balance': 100}
# ]
#
# current_user = {}  # 记录当前登陆用户信息
#
#
# class WnATM:
#     @staticmethod
#     def register():
#         print('欢迎使用WN ATM系统')
#         while True:
#             user_n = input('[注册]请输入您的用户名：')
#             for item in users_list:
#                 if user_n.strip() == item.get('user'):  # 用户输入的用户名已经在用户列表内
#                     print('用户已存在')
#                     break
#             else:
#                 pass_wd = input('[注册]请输入您的密码：')
#                 if len(pass_wd) < 6:
#                     print('密码长度小于6位，请检查')
#                 else:
#                     # 注册成功，将用户名和密码加入数据列表
#                     users_list.append({'user': user_n, 'password': pass_wd, 'balance': 3000})
#                     print('恭喜您注册成功!')
#                     return True
#
#     @staticmethod
#     def login():
#         while True:
#             user_n_login = input('[登陆]请输入您的用户名：')
#             pass_wd_login = input('[登陆]请输入您的密码：')
#             for item in users_list:
#                 if item.get('user') == user_n_login and item.get('password') == pass_wd_login:
#                     print('恭喜您登陆成功！')
#                     global current_user
#                     current_user = item
#                     return True
#             else:
#                 print('用户名或者密码错误！')
#
#     @staticmethod
#     def check_balance():
#         if current_user:  # 代表当前已经登陆
#             print(f'当前用户：{current_user["user"]}， 余额为：{current_user["balance"]}')
#         else:
#             print('请先登陆后再进行查询余额操作!')
#
#     @staticmethod
#     def run_main():
#         man = """
#               ******欢迎来到Wn ATM******
#             ********请选择操作菜单********
#         ******1.注册 2.登陆 3.查询余额 4.退卡 ***
#               """
#         while True:
#             print(man)
#             man_select = input('请输入您选择的操作项目:')
#             if man_select == '1':
#                 WnATM.register()
#             elif man_select == '2':
#                 WnATM.login()
#             elif man_select == '3':
#                 WnATM.check_balance()
#             elif man_select == '4':
#                 print('感谢您的使用，欢迎下次再来！')
#                 break
#             else:
#                 print('指令输入错误，请重新选择操作项目!')


# 5
users_list = [
    {'user': 'zhangsan', 'password': '123456', 'balance': 1000},
    {'user': 'lisi', 'password': '111111', 'balance': 2500},
    {'user': 'wangwu', 'password': 'wangwu', 'balance': 100}
]

current_user = {}  # 记录当前登陆用户信息


class WnATM:
    @staticmethod
    def register():
        print('欢迎使用WN ATM系统')
        while True:
            user_n = input('[注册]请输入您的用户名：')
            for item in users_list:
                if user_n.strip() == item.get('user'):  # 用户输入的用户名已经在用户列表内
                    print('用户已存在')
                    break
            else:
                pass_wd = input('[注册]请输入您的密码：')
                if len(pass_wd) < 6:
                    print('密码长度小于6位，请检查')
                else:
                    # 注册成功，将用户名和密码加入数据列表
                    users_list.append({'user': user_n, 'password': pass_wd, 'balance': 3000})
                    print('恭喜您注册成功!')
                    return True

    @staticmethod
    def login():
        while True:
            user_n_login = input('[登陆]请输入您的用户名：')
            pass_wd_login = input('[登陆]请输入您的密码：')
            for item in users_list:
                if item.get('user') == user_n_login and item.get('password') == pass_wd_login:
                    print('恭喜您登陆成功！')
                    global current_user
                    current_user = item
                    return True
            else:
                print('用户名或者密码错误！')

    @staticmethod
    def check_balance():
        if current_user:  # 代表当前已经登陆
            print(f'当前用户：{current_user["user"]}， 余额为：{current_user["balance"]}')
            return
        else:
            print('请先登陆后再进行查询余额操作!')
            return

    @staticmethod
    def deposit():
        if current_user:
            deposit_money = input('请输入您想要存入的金额：')
            if deposit_money.isdigit():
                if int(deposit_money) % 100 == 0 and len(deposit_money) > 2:  # 说明输入的是100的整数倍
                    current_user['balance'] += int(deposit_money)
                    print(f'恭喜您存款成功，当前余额为：{current_user["balance"]}')
                else:
                    print("存款金额最小为100且必须为100的整数倍，请检查后重新输入")
            else:
                print("您的存款金额格式不正确，请检查后重新输入")
        else:
            print("您尚未登陆，请登陆后再进行相关操作！")

    @staticmethod
    def withdraw():
        if current_user:
            withdraw_money = input('请输入您想要取出的金额：')
            if withdraw_money.isdigit():
                if int(withdraw_money) % 100 == 0 and len(withdraw_money) > 2:  # 说明输入的是100的整数倍
                    if current_user['balance'] >= int(withdraw_money):
                        current_user['balance'] -= int(withdraw_money)
                        print(f'恭喜您取款成功，当前余额为：{current_user["balance"]}')
                        return
                    else:
                        print('您的余额不足，赶紧去搬砖吧！')
                else:
                    print("存款金额最小为100且必须为100的整数倍，请检查后重新输入")
            else:
                print("您的存款金额格式不正确，请检查后重新输入")
        else:
            print("您尚未登陆，请登陆后再进行相关操作！")

    @staticmethod
    def transfer():
        if current_user:
            transfer_user = input('请输入您想要转账的对方账号：')
            if transfer_user == current_user['user']:
                print('不能给自己转账，请检查后操作')
            else:
                for item in users_list:
                    if item.get('user') == transfer_user:  # 说明找到了一个有效账户
                        transfer_money = input('请输入您想要转账的金额：')
                        if transfer_money.isdigit():
                            if int(transfer_money) % 100 == 0 and len(transfer_money) > 2:  # 说明输入的是100的整数倍
                                if current_user['balance'] >= int(transfer_money):
                                    current_user['balance'] -= int(transfer_money)  # 自己账户余额减少
                                    item['balance'] += int(transfer_money)  # 对方账户余额增加
                                    print(f'恭喜您转账成功，当前您的账户余额为：{current_user["balance"]}')
                                    return
                                else:
                                    print('您的余额不足，无法转账， 赶紧去搬砖吧！')
                                    return

                            else:
                                print("存款金额最小为100且必须为100的整数倍，请检查后重新输入")
                                return
                        else:
                            print("您的存款金额格式不正确，请检查后重新输入")
                            return
                else:
                    print("您输入转账用户信息有误，请核对后重新操作")
        else:
            print("您尚未登陆，请登陆后再进行相关操作！")

    @staticmethod
    def run_main():
        man = """
            ******欢迎来到Wn ATM******
            ********请选择操作菜单********
******1.注册 2.登陆 3.查询余额 4.存款 5.取款 6.转账 7.取卡 ***
              """
        while True:
            print(man)
            man_select = input('请输入您选择的操作项目:')
            if man_select == '1':
                WnATM.register()
            elif man_select == '2':
                WnATM.login()
            elif man_select == '3':
                WnATM.check_balance()
            elif man_select == '4':
                WnATM.deposit()
            elif man_select == '5':
                WnATM.withdraw()
            elif man_select == '6':
                WnATM.transfer()
            elif man_select == '7':
                print('感谢您的使用，欢迎下次再来！')
                break
            else:
                print('指令输入错误，请重新选择操作项目!')


if __name__ == '__main__':
    wn_atm = WnATM()
    # if wn_atm.register():
    #     wn_atm.login()
    wn_atm.run_main()
