import datetime
# file_name = 'pi_digits.txt'
# file_name = 'pi_million_digits.txt'

# with open(file_name) as file_object:
# 	# contents = file_object.read()
# 	contents = file_object.readlines()
# 	# for line in file_object:
# 	# 	print(line.rstrip())
# pi_string = ''
# for content in contents:
# 	# print(content.rstrip())
# 	pi_string += content.strip()
# # print(pi_string)
# birthday = input('please input your birthday...')
# if birthday in pi_string:
# 	print('yes')
# else:
# 	print('no')

# guess = input('name:')
# with open('guess.txt','w') as file_object:
# 	file_object.write(f"{guess}\n")

while True:
	guest = input('name:')
	if guest == 'quit':
		break
	else:
		with open('guest_book.txt','a') as file_object:
			current_time = datetime.datetime.today()
			file_object.write(f"{guest} {current_time}\n")
with open('guest_book.txt') as guest_object:
	contents = guest_object.read()
print(contents)