#-*-coding:utf-8-*-
# Author:Lu Wei
import os,sys,json
base_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_path)
from src import Student
from src import Manger
User_path=os.path.join(base_path,r'db\User-db')
def Login():
    while True:
        username = input('username:')
        if username.upper() == 'N':
            print('exit')
            return
        password = input('password:')
        User_list = []
        Flog = False
        Role = None
        with open(User_path,mode='r',encoding='utf-8') as f:
            for i in f:
                User_list.append(eval(i.strip('\n')))
            for i in User_list:
                if username==i['username'] and password==i['password']:
                    Role=i['role']
                    Flog=True
            if Flog:
                print('login ok')
                if Role=='M':
                    if __name__=='__main__':
                       Manger.Start()
                elif Role=='S':
                    if __name__ == '__main__':
                       Student.Start()
            else:
                print('login error')

Login()