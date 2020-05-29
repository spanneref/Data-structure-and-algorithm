# coding=utf-8

# 线性表的链式结构的实现python


class Node(object):
	# 节点类
	def __init__(self, data, to=None):
		self.data = data  # 节点的数据域
		self.to = to  # 节点的指针域


class LinkList(object):
	# 链式线性表类\
	
	def __init__(self):
		self.root = None  # 根节点
		self.length = 0  # 链表长度

	def create_list(self, list):
		# 创建线性表
		# 校验传入的list。
		if len(list) < 0:
			print(u'数据错误')
			return False

		elif len(list) == 1: # 只有一个节点是时候
			self.root = Node(list[0])
			self.length = 1
			return 'OK'

		else:  # 有多个节点
			# 创建根节点
			self.root = Node(list[0])
			self.length = 1
			# 保存当前节点
			temp = self.root 
			for item in list[1: len(list)]:
				temp.to = Node(item)  # 创建节点并将当前节点的指针域修改为新节点的引用
				temp = temp.to  # 修改当前节点为新的节点
				self.length += 1
			return 'OK'  
	
	def get_item(self, num):
		# 获取元素数据
		if 0 < num < self.length:
			if num == 0:
				return self.root.data
			else:
				temp = self.root
				for i in range(1, self.length):
					if i == num:
						return temp.to.data
					else:
						temp = temp.to

	def get_all(self):
		# 获取所有元素
		linklist = list()
		current_node = self.root
		for i in range(self.length):
			# print(self.length)
			linklist.append(current_node.data)
			current_node = current_node.to
		print(linklist)

	def insert_items(self, list, num):
		# 插入数据
		if len(list) < 0:
			print(u'数据错误')
			return False

		if num <= 0 or num > self.length:
			print('插入的位置超出范围，目前插入的范围为：1-%d' % self.length)
			return False
		print('要在第%d位插入列表[%s]' % (num, ", ".join(list)))

		if num == 1:  # 头结点插入
			if len(list) == 1:  # 头结点插入一个节点
				old_node = self.root
				self.root = Node(list[0])
				self.root.to = old_node
				self.length += 1
				return 'OK'

			else:  # 头结点插入多个
				old_node = self.root
				self.root = Node(list[0])
				self.length += 1
				temp = self.root
				for item in list[1: len(list)]:
					temp.to = Node(item)
					temp = temp.to
					self.length += 1
				temp.to = old_node  # 将最后插入的节点接回之前的节点
				return 'OK'

		else:  # 非头部插入节点
			current_node = self.root
			for i in range(2, self.length+1):
				if i == num:
					for item in list:
						temp = Node(item)
						temp.to = current_node.to
						current_node.to = temp
						current_node = temp
						self.length += 1
					return 'OK'

				else:
					current_node = current_node.to

	def delete_item(self, num):
		# 单个删除
		if num <= 0 or num > self.length:
			print('删除的节点位置超出范围，当前节点的范围是：1-%d' % self.length)
			return False

		current_node = self.root
		if num == 1:  # 删除头结点
			print('要删除的是第1位的%s元素' % current_node.data)
			self.root = current_node.to
			self.length -= 1
			del current_node
			return 'ok'
		else:
			for i in range(2, self.length+1):
				if num == i:
					print('要删除的是第%d位的%s元素' % (i,current_node.to.data))
					q = current_node.to  # 当前要删除的节点
					current_node.to = q.to	# 当前节点的后继改为下下个节点
					self.length -= 1
					del q
					return 'ok'
				else:
					current_node = current_node.to


if __name__ == '__main__':
	l = ['a', 'b', 'c']
	l2 = ['e', 'f', 'g']
	linkli = LinkList()
	linkli.create_list(l)
	linkli.insert_items(l2, num=2)
	linkli.get_all()
	linkli.delete_item(6)
	linkli.get_all()


