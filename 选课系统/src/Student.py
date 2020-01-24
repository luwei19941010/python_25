#-*-coding:utf-8-*-
# Author:Lu Wei

from lib import user_choice
import os,sys
base_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
User_path=os.path.join(base_path,r'db\User-db')
Course_path=os.path.join(base_path,r'db\Course-db')
S_Course_path=os.path.join(base_path,r'db\S_Course-db')
def Start(username):
    while True:
        print("""
        　　　　　　　1、查看所有课程
        　　　　　　　2、选择课程
        　　　　　　　3、查看所选课程
        　　　　　　　4、退出程序(N)
            """)
        Slist = {'1': S_Course, '2': C_Course, '3': S_Choice_Course}
        func = user_choice.User_Choice(Slist)
        if func:
            func(username)
        else:
            return

def S_Course(username):
    with open(Course_path, mode='r', encoding='utf-8') as f:
            count=1
            print('查看所有课程'.center(30,'*'))
            print('序号'.ljust(10,' '),'course_name'.ljust(10,' '),'course_time'.ljust(10,' '),'course_pice'.ljust(10,' '),'course_teacher'.ljust(10,' '))
            for i in  f:
                line=eval(i.strip())
                print(count,' '.ljust(10,' '),line['course_name'].ljust(10,' '),line['course_time'].ljust(10,' '),line['course_pice'].ljust(10,' '),line['course_teacher'].ljust(10,' '))
                count+=1

def C_Course(username):
    flog=False
    data_list = []
    new_dict={}
    Course_list=[]
    with open(S_Course_path, mode='r', encoding='utf-8') as f:
        S_Course(username)
        Course_name = input('属于选择课程(N-EXIT):')
        for i in f:
            line=eval(i.strip())
            data_list.append(line)
        for i in data_list:
            if username == i['username']:
                flog=True
        if flog:
            with open(S_Course_path, mode='w', encoding='utf-8') as fw:
                for i in data_list:
                    if username == i['username']:
                        i['course'].append(Course_name)
                        fw.write(str(i) + '\n')
                        continue
                    fw.write(str(i) + '\n')
        else:
            with open(S_Course_path, mode='w', encoding='utf-8') as fw:
                Course_list.append(Course_name)
                new_dict['username']=username
                new_dict['course']=Course_list
                data_list.append(new_dict)
                for i in data_list:
                    fw.write(str(i) + '\n')



def S_Choice_Course(username):
    data_list=[]
    with open(S_Course_path, mode='r', encoding='utf-8') as f:
        print('查看选课情况'.center(30,'*'))
        print('student username'.ljust(20,' '),'Course name'.ljust(20,' '))
        for i in f:
            line=eval(i.strip())
            # data_list.append(line)
            print(line[username].ljust(20,' '),line['course'])

