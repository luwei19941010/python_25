#-*-coding:utf-8-*-
# Author:Lu Wei

def User_Choice(list):
    while True:
        user_choice = input('清输入(N-EXIT):')
        if user_choice.upper() == 'N':
            return
        func=list.get(user_choice,None)
        if func:
            return func
        else:
            print('输入有误，请重新输入')
            continue