#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：王玮璇
日期：2020/4/11
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
	"""
	将游戏对象对应到不同的整数
	"""
	if name=='石头':
			x=0
	elif name=='史波克':
			x=1
	elif name=='纸':
			x=2
	elif name=='蜥蜴':
			x=3
	elif name=='剪刀':
			x=4
	else:
			print("Error: No Correct Name")
	return x
    
			
	


def number_to_name(number):
	"""
	将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
	"""
	if number==0:
		 x='石头'
	elif number==1:
	     x='史波克'
	elif number==2:
		 x='纸'
	elif number==3:
		 x='蜥蜴'
	elif number==4:
			x='剪刀'    
	return x     
		    

    


def rpsls(player_choice):
	"""
	用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
	"""	

	print("--------")
	print("您的选择为：",player_choice)
	player_choice_number = name_to_number(player_choice)
	comp_number = random.randrange(0,5)
	comp_choice = number_to_name(comp_number)
	print("输出计算机的选择为：",comp_choice)
	if player_choice_number-comp_number in range(1,5):
		print("您赢了!")
	elif player_choice_number-comp_number in range(-4,0):
		print("计算机赢了!")
	elif player_choice_number-comp_number==0:
		print("您和计算机出的一样呢!")
		

   


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)


