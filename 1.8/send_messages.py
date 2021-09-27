sent_message = []
def send_messages(messages):
	print("used module")
	print(messages)
	while messages:
		current_message = messages.pop()
		print(f"sent message:{current_message}")
		sent_message.append(current_message)
	print(sent_message)