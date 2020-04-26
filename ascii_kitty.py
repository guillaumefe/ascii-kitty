import time

msg1 = "world!"
msg2= "hello"
duration = 1
max = 100

chat1 = f"\n             ^  ^  {msg1}\n            ( ô.ô)___(\n             //||-//||"
chat2 = f"\n             ^   ^  {msg2}\n            (ù.ù )___(\n             //||-//||"

chat = chat1

for a in range(1,max):
    print(chr(27) + "[2J")
    if chat == chat1:
        chat = chat2
    else:
        chat = chat1
    print(chat)
    time.sleep(duration)
