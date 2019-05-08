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
	

