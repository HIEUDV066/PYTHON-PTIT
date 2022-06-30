def res(text):
    if len(text) ==0:
        return
    text = " ".join(text.split())
    print(text.capitalize().strip())

text = ""
while True:
    try:
        text += input().lower()+ " "
    except EOFError:
        break
text = text.replace("!",".")
text = text.replace("?",".")
for i in text.split("."):
    res(i)