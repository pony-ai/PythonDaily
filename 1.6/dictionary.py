# 创建字典
# friends_1 = {
#     'first_name':'chunhui',
#     'last_name':'Li',
#     'age':'25',
#     'city':'DaLian'
#     }
# friends_2 = {
#     'first_name':'xunan',
#     'last_name':'Zhao',
#     'age':'25',
#     'city':'DaLian'
#     }
# print(f"My favorite friend is {friends['last_name']}{friends['first_name']}")

# 练习6-3 词汇表
# terms = {
#     'list':'列表',
#     'tuple':'元组',
#     'dictionary':'字典',
#     'if':'条件语句',
#     'for':'循环语句',
#     }

# core = ['list','if','for']

# 遍历所有的键
# for key in terms.keys():
# 	print(key)

# 遍历所有的值
# for value in terms.values():
# 	print(value)

# for k,v in terms.items():
# 	if k in core:
# 		print(f"{k} in core.")
# 	if k not in core:
# 	    print(f"{k} not in core")

# print('over.')

# 列表中存储字典
# friends = [friends_1,friends_2]
# for fri in friends:
# 	print(fri)

# 字典中存储列表
favorite_city = {
	'Xiao':['ShenZ','BeiJ','ShangH'],
	'Li':['DaL','ShangH'],
	'Zhao':['ChangC','DaL','TianJ']
}
for name,cities in sorted(favorite_city.items()):
	print(f"\n{name} favorite cities:")
	for city in cities:
		print(f"{city}")
print('over.')
# 输出结果：
# Li favorite cities:
# DaL
# ShangH

# Xiao favorite cities:
# ShenZ
# BeiJ
# ShangH

# Zhao favorite cities:
# ChangC
# DaL
# TianJ
# over.
# [Finished in 160ms]