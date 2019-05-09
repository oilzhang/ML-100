def flower():
	"""
	寻找水仙花----是指一个三位数，它的个位，十位，百位的立方和等于它本身
	"""
	for i in range(100,1000):
		first_num, second_num, thrid_num = int(str(i)[0]), int(str(i)[1]), int(str(i)[2])

		if first_num ** 3 + second_num ** 3 + thrid_num ** 3 == i:
			print(i)




def perfect_num(n):
	"""
	寻找完美数---是指一个数除本身之外的所有因子（约数）之和等于这个数本身
	"""
	for i in range(1,n+1):
		
		result = [a for a in range(1, m+1) if m % a == 0]
		sum_result = 0
		
		for j in range(len(result)-1):
			sum_result += result[j]

		if sum_result == i:
			print(i)


def buy_chick(chick_num, money):
	"""
	百千百鸡----公鸡5钱一只，母鸡3钱一只，小鸡1钱3只，现有100钱需买100只鸡
	"""
	max_cock = money // 5 #全买成公鸡，最多能买多少只
	max_hen = money // 3 #全买成母鸡，最多能买多少只

	for cock in range(max_cock + 1): 
		
		for hen in range(max_hen + 1): 
			
			chick = chick_num - cock - hen
			if cock * 5 + hen * 3 + chick / 3 == chick_num:
				print('公鸡：%d,母鸡：%d,小鸡：%d' % (cock, hen, chick)) 


def Fibonacci_sequence(n):
	"""
	斐波那契数列---从第三项开始，每一项都等于前两项之和
	"""
	result = [1, 1]
	i, j = 0, 0
	while i < n:
		i = result[j] + result[j+1]
		if i < n:
			result.append(i)
			j += 1

	return result

def crap():
	"""
	Craps赌博游戏
	玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
	如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
	玩家再次要色子 如果摇出7点 庄家胜
	如果摇出第一次摇的点数 玩家胜
	否则游戏继续 玩家继续摇色子
	玩家进入游戏时有1000元的赌注 全部输光游戏结束
	"""
	from random import randint

	money = 1000
	while money > 0:
		print('你的总资产为：',money)
		
		need_go_on = False #设置一个开关---判断是否需要继续
		
		while True:
			debt = int(input('请下注：'))
			if debt > 0 and debt <= money:
				break
		
		first = randint(1,6) + randint(1,6)
		print('玩家第一次摇出%d点'%(first))

		if first == 7 or first == 11:
			print('玩家胜')
			money += debt

		elif first == 2 or first == 3 or first == 12:
			print('庄家胜')
			money -= debt
		
		else:
			need_go_on = True
		
		while need_go_on:  #当玩家和庄家都没赢时，游戏继续
			
			current = randint(1,6) + randint(1,6)
			print('玩家摇出%d点'%(current))
			
			if current == first:
				print('玩家胜')
				money += debt
				need_go_on = False  #玩家胜，退出当前循环

			elif current == 7:
				print('庄家胜')
				money -= debt
				need_go_on = False # 庄家胜，退出当前循环
			else:
				need_go_on = True # 玩家和庄家都没赢时，游戏继续

	print('你破产了')
			


