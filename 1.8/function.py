from send_messages import *
# def display_message():
# 	# 打印字符串
# 	print('今天学习python函数的使用')
# display_message()

# def favorite_book(title):
# 	print(f"My favorite book is {title}")
# favorite_book('stoner')

# def make_shirt(size,logo = 'i love python'):
# 	print(f"This shirt size:{size} logo:{logo}")
# make_shirt('M','DayDayUp')
# # make_shirt(logo = 'DayDayUp',size = 'M')
# # make_shirt('M')


# def discribe_city(city,country):
# 	# print(f"{city} belongs to {country}")
# 	full_name = f"{city},{country}"
# 	return full_name.title()
# cities = {'beijing':'china','paris':'france'}
# for city,country in cities.items():
# 	city_country = discribe_city(city,country)
# 	print(city_country)

messages = ['hello','hi','nece to meet you','fine','thank you']
# def show_message(messages):
# 	for message in messages:
# 		print(f"\n{message}")
# show_message(messages)
# def send_messages(messages):
# 	print(messages)
# 	while messages:
# 		current_message = messages.pop()
# 		print(f"sent message:{current_message}")
# 		sent_message.append(current_message)
# 	print(sent_message)
send_messages(messages[:])