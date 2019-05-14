from abc import ABCMeta, abstractmethod
from random import randint

class Fighter(metaclass = ABCMeta):
	"""战斗者"""

	#通过__slots__魔法限定对象可以绑定的成员变量
	__slots__ = ('_name', '_hp')

	def __init__(self, name, hp):
		"""
		初始化方法

		:param name: 名字
		:param hp: 生命值
		"""
		self._name = name
		self._hp = hp

	@property
	def name(self):
		return self._name
	
	@property
	def hp(self):
		return self._hp
	
	@hp.setter
	def hp(self, hp):
		self._hp = hp if hp >=0 else 0

	@property
	def alive(self):
		return self._hp > 0

	@abstractmethod
	def attack(self, other):
		"""
		攻击

		:param other: 被攻击的对象
		"""
		pass

class Ultraman(Fighter):
	"""奥特曼"""

	__slots__ = ('_name', '_hp', '_mp')

	def __init__(self, name, hp, mp):
		"""
		初始化方法
		
		:param mp: 魔法值
		"""
