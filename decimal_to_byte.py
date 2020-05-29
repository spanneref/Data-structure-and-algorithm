# coding:utf-8

import myStack
import sys


def decimal_to_byte(num):
	# 创建一个栈
	stack = myStack.Stack()
	# 计算二进制
	num = int(num)
	while num > 0:
		temp = num % 2
		num = num / 2
		stack.push(temp)  # 将每一次%2的结果入栈

	bytestr = ""
	while not stack.is_empty():
		bytestr += str(stack.pop())

	return bytestr


def main():
	num = sys.argv[1]
	print("%s 的二进制值为：%s" % (num, decimal_to_byte(num)))

if __name__ == '__main__':
	main()