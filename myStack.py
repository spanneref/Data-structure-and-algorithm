# coding:utf-8


class Stack(object):  # 栈的顺序结构
	
	def __init__(self):  # 初始化
		self.__list = list()

	def is_empty(self):  # 判断是否为空栈
		return len(self.__list) <= 0

	def push(self, data):  # 入栈
		self.__list.append(data)

	def pop(self):  # 出栈
		if self.is_empty():
			return "stack is empty"
		else:
			return self.__list.pop()

	def get_top(self):  # 获取栈顶数据元素
		if self.is_empty():
			return "stack is empty"
		else:
			return self.__list[-1]
	def clear(self):  # 清空栈
		self.__list.clear()

if __name__ == '__main__':
	stack = Stack()
	stack.push(1)
	stack.push(2)
	stack.push(3)

	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.is_empty())
	print(stack.pop())


