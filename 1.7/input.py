# input函数获取用户输入
# message = input("please input your name:")
# print(f"\nhello {message}")

# int将字符串转换成数值
# height = input("height:")
# height = int(height)

# if height >= 120:
# 	print("you can play")
# else:
# 	print("no")

# 判断输入数值是否是10的整数倍
# num = input("please input nummber:")
# num = int(num)
# if num%10 == 0:
# 	print("yes")
# else:
# 	print("no")

# 添加配料
# burdenning = []
# message = input("Dear,please input your burdening what you want:")
# while True:
# 	if message == 'quit':
# 		break
# 	else:
# 		burdenning.append(message)
# 		for bur in burdenning:
# 			print(f"Add {bur}")
# 			continue
# 		message = input("Dear,please continue input your burdening what you want:")

sandwich_order = ['a','b','c','d','b','e','b']
finished_sandwiches = []
active = True
print('b sell out')
while 'b' in sandwich_order:
	sandwich_order.remove('b')
print(sandwich_order)
while sandwich_order:
	sandwich = sandwich_order.pop()
	print(f"I made your tuna sandwich:{sandwich}")	
	finished_sandwiches.append(sandwich)
print("\nAll sandwich already finished:")
for sandwiches in sorted(finished_sandwiches):
	print(sandwiches)