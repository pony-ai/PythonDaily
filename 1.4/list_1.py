#遍历列表
# magicians = ['liu','xue','xiao']
# for magician in magicians:
# 	# print(magician)
# 	print(f"{magician.title()},that was a great trick.")

#创建数值列表
# numbers = list(range(1,6))
# print(numbers)

#打印1-10的平方数
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)
# 简单运算
# print('最大值为',max(squares))
# print('最小值为',min(squares))
# print('数组和为',sum(squares))

# 立方解析
# squares = [value**3 for value in range(1,11)]
# print(squares)

# 切片
# print(squares[0:2])
# print(squares[-3:])
# 遍历切片
# for value in squares[3:]:
# 	print(value)