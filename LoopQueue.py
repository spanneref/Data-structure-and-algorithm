# coding:utf-8

class Loopqueue(object):

	def __init__(self, length):
		self.MAXSIZE = length
		self.__list = [None for i in range(self.MAXSIZE)]  # 初始化一个长度为length的列表，每一项都为None
		self.front = 0  # 头指针
		self.rear = 0  # 尾指针

	def queue_len(self):  # 获取当前队列的长度
		return (self.rear - self.front + self.MAXSIZE) % self.MAXSIZE

	def is_full(self):  # 判断队列是否满
		return (self.rear + 1) % self.MAXSIZE == self.front

	def is_empty(self):  # 判断是否为空
		return self.front == self.rear

	def enter_queue(self, data):  # 入队
		if self.is_full():
			return 'queue was full'
		else:
			self.__list[self.rear] = data
			self.rear = (self.rear + 1) % self.MAXSIZE
			return 'ok! %s has inserted into the queue' % data

	def quit_queue(self):  # 离队
		if self.is_empty():
			return 'queue was empty'
		else:
			data = self.__list[self.front]
			self.__list[self.front] = None
			self.front = (self.front + 1) % self.MAXSIZE
			return data

if __name__ == '__main__':
	loopqueue = Loopqueue(6)
	test_list = [chr(i) for i in range(97, 103)]
	for i, item in enumerate(test_list):
		print(loopqueue.enter_queue(item))

	for i in range(6):
		print(loopqueue.quit_queue())

	for i in ["f", "g"]:
		print(loopqueue.enter_queue(i))

	print(loopqueue.quit_queue())
