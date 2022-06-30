def show_messages(messages):
    for message in messages:
        print(message)

def send_message(messages):

    great_messages = []


    while messages:
        message = messages.pop()
        great_message = message + ' tuyet!'
        great_messages.append(great_message)

 
    for great_message in great_messages:
        messages.append(great_message)

messages = ['hieu', 'hai', 'hiep']
show_messages(messages)

print("\n")
send_message(messages)
show_messages(messages)