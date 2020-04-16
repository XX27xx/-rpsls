#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ������
���ڣ�2020/4/11
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
	"""
	����Ϸ�����Ӧ����ͬ������
	"""
	if name=='ʯͷ':
			x=0
	elif name=='ʷ����':
			x=1
	elif name=='ֽ':
			x=2
	elif name=='����':
			x=3
	elif name=='����':
			x=4
	else:
			print("Error: No Correct Name")
	return x
    
			
	


def number_to_name(number):
	"""
	������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
	"""
	if number==0:
		 x='ʯͷ'
	elif number==1:
	     x='ʷ����'
	elif number==2:
		 x='ֽ'
	elif number==3:
		 x='����'
	elif number==4:
			x='����'    
	return x     
		    

    


def rpsls(player_choice):
	"""
	�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
	"""	

	print("--------")
	print("����ѡ��Ϊ��",player_choice)
	player_choice_number = name_to_number(player_choice)
	comp_number = random.randrange(0,5)
	comp_choice = number_to_name(comp_number)
	print("����������ѡ��Ϊ��",comp_choice)
	if player_choice_number-comp_number in range(1,5):
		print("��Ӯ��!")
	elif player_choice_number-comp_number in range(-4,0):
		print("�����Ӯ��!")
	elif player_choice_number-comp_number==0:
		print("���ͼ��������һ����!")
		

   


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


