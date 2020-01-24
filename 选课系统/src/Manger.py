#-*-coding:utf-8-*-
# Author:Lu Wei
from lib import user_choice
import os,sys

base_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
User_path=os.path.join(base_path,r'db\User-db')
Course_path=os.path.join(base_path,r'db\Course-db')
S_Course_path=os.path.join(base_path,r'db\S_Course-db')
def Start():
    while True:
        print('管理员系统'.center(30, '*'))
        print("""
            　　　　  1、创建课程
        　　　　　　　2、创建学生学生账号
        　　　　　　　3、查看所有课程
        　　　　　　　4、查看所有学生
        　　　　　　　5、查看所有学生的选课情况
        　　　　　　　6、退出程序(N)
            """)
        Mlist = {'1': C_Course, '2': C_Student, '3': S_Course, '4': S_Student, '5': S_Student_Chioce}
        func = user_choice.User_Choice(Mlist)
        if func:
            func()
        else:
            return


def C_Course():
    while True:
        with open(Course_path,mode='a',encoding='utf-8') as f:
            print('创建课程'.center(30,'*'))
            course_name=input('course_name(N-exit):')
            if course_name.upper()=='N':
                return
            course_time=input('course_time:')
            course_pice=input('course_pice:')
            course_teacher=input('course_teacher:')
            Course={'course_name':course_name,'course_time':course_time,'course_pice':course_pice,'course_teacher':course_teacher}
            f.write(str(Course)+'\n')


def C_Student():
    while True:
        with open(User_path,mode='a',encoding='utf-8') as f:
            print('创建学生学生账号'.center(30,'*'))
            username=input('username(N-exit):')
            if username.upper()=='N':
                return
            password=input('password:')
            role=input('role(M/S):').upper()
            Stu={'username':username,'password':password,'role':role}
            f.write('\n'+str(Stu))


def S_Course():
    with open(Course_path, mode='r', encoding='utf-8') as f:
            count=1
            print('查看所有课程'.center(30,'*'))
            print('序号'.ljust(10,' '),'course_name'.ljust(10,' '),'course_time'.ljust(10,' '),'course_pice'.ljust(10,' '),'course_teacher'.ljust(10,' '))
            for i in  f:
                line=eval(i.strip())
                print(count,' '.ljust(10,' '),line['course_name'].ljust(10,' '),line['course_time'].ljust(10,' '),line['course_pice'].ljust(10,' '),line['course_teacher'].ljust(10,' '))
                count+=1

def S_Student():
    with open(User_path, mode='r', encoding='utf-8') as f:
        print('查看学生学生账号'.center(30,'*'))
        print('student username:')
        count=1
        for i in f:
            line=eval(i.strip())
            if line['role']=='S':
                print(count,':',line['username'])
                count+=1
def S_Student_Chioce():
    with open(User_path, mode='r', encoding='utf-8') as f:
        print('查看所有学生的选课情况'.center(30,'*'))
        print('student username'.ljust(20,' '),'Course name'.ljust(20,' '))
        for i in f:
            line=eval(i.strip())
            print(line['username'].ljust(20,' '),line['Coursename'].ljust(20,' '))


