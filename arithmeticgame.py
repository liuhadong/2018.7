import random
import operator
# operator模块是python中内置的操作符函数接口，它定义了一些算术和比较内置操作的函数

player= []
# 记录该次启动游戏后用户的名字和得分

def menu():  # 开始游戏界面
    print('==========欢迎来到算数小游戏===========')
    print('1.新建游戏')
    print('2.查看记录')
    print('3.删除记录')
    print('4.查看帮助信息')
    print('5.退出游戏')
    print('==========欢迎来到算数小游戏===========')

def game_list():  #  模式选择
    print('请选择模式:')
    print('1.加减法练习(30道)')
    print('2.乘除法练习(30道)')
    key = input('请输入选项:')
    if key == '1':
        start_game1()
    elif key == '2':
        start_game2()

def start_game1():  #  加减模式
    game_dict = {}   #  建立一个字典，用来记录每一个用户游戏的得分
    number = 0  # 题目的数量
    correct = 0  # 答对题目的数量
    wrong = 0  # 答错题目的数量
     
    while True:
        for i in range(2):   
            a = random.randint(1,100)
            b = random.randint(1,100)
         
        op = random.choice('+-')
        # random.choice()可以从任何序列，比如list列表中，选取一个随机的元素返回，可以用于字符串、列表、元组等
        if op == '+':
            num = operator.add(a,b)  # operator.add(a,b),返回a+b
        elif op == '-':
            num = operator.sub(a,b)   #  operator.sub(a,b),返回a–b 
        #  num表示正确的答案
        try:
            c = int(input('{}{}{}='.format(a,op,b)))
        #用户计算的答案

            number += 1
        # 每输入一次答案，题目的计数器就+1  
            if c == num:
                print('答案正确')
                correct += 1
            elif c != num:
                print('答案错误')
                wrong += 1
                if wrong == 10 or number == 30:
                    break
        #  判断输入的答案是否正确
        except:
            print('输入错误，请重新开始游戏')
            return
    game_dict[new_name] = correct  # 向字典里添加数据
    player.append(game_dict) # 把字典添加到列表中
    
    print('共练习{}题,答对{}题,答错{}题,得{}分'.format(number,correct,wrong,correct))
    if wrong/number > 0.5:
        print('继续加油哦')
        print('='*20)
    else:
        print('还不错，保持哦')
        print('='*20)
    
def start_game2():  # 乘除模式
    game_dict = {}
    number = 0
    correct = 0
    wrong = 0
    
    while True:
        for i in range(2):
            a = random.randint(1,100)
            b = random.randint(1,100)
        
        op = random.choice('*/')
        
        if op == '*':
            num = operator.mul(a,b)
        elif op == '/':
            num = ('%.2f'%operator.truediv(a,b))
        try:
            c = float(input('{}{}{}='.format(a,op,b)))
        
            number += 1
        
            if c == float(num):
                print('答案正确')
                correct += 1
            elif c != num:
                print('答案错误')
                wrong += 1
            if wrong == 10 or number == 30:
                break
        except:
            print('输入错误，请重新开始游戏')
            return
    
    game_dict[new_name] = correct
    player.append(game_dict)
    
    print('共练习{}题,答对{}题,答错{}题,得{}分'.format(number,correct,wrong,correct))
    
    if wrong/number > 0.5:
        print('继续加油哦')
        print('='*20)
    else:
        print('还不错，保持哦')
        print('='*20)

def new_game():  # 新建游戏
    global new_name  # 可以让new_name可以在全局被调用
    new_name = input('请输入新建游戏用户名:')
    print('创建成功')

    game_list()

def cat_record():  # 查看记录
    if len(player) == 0:
        print('没有记录')
        return
    else:
        print(player)

def del_record(): # 删除记录  
    del_number = int(input('请输入要删除的记录的序列号:'))-1
    del player[del_number]

def help_mation(): # 帮助信息
    print('游戏只提供基本的加减和乘除运算，旨在提高小朋友的算数能力，用户只需根据给出的题目作答即可')

def main():
    while True:
        menu()
        key = input('请输入选项序号:')
        if key == '1':
            new_game()
        elif key == '2':
            cat_record()
        elif key == '3':
            del_record()
        elif key == '4':
            help_mation()
        elif key == '5':
            print('退出游戏')
            break
        else:
            print('输入有误,请重新输入')

main()


