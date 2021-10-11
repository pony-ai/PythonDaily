import json

def add_f_num():
	f_number = input('please input your favorite number...')
	file_name = 'f_number.json'
	with open(file_name,'w') as f:
		json.dump(f_number,f)
	return f_number

def get_f_num():
	file_name = 'f_number.json'
	try:
		with open(file_name) as f:
			f_number = json.load(f)
	except:
		# print(f"{file_name} not exist")
		pass
	else:
		return f_number

def remeber_f_num():
	f_number = get_f_num()
	judge = ''
	if f_number:
		judge = input(f"current number is {f_number},please judge your favorite number!(yse/no)")
		if judge == 'yes':
			print(f"I know your favorite number! It's {f_number}.")
		else:
			f_number = add_f_num()
remeber_f_num()		
# add_f_num()
# f_number =  get_f_num()
# print(f_number)