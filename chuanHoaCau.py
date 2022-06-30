def process(A):
    A = " ".join(A.split())
    if A[len(A)-1] != '.' and A[len(A)-1] != '?' and A[len(A)-1] != '!':
        A += '.'
    A = A.replace(" ?","?")
    A = A.replace(" !","!")
    A = A.replace(" .",".")
    A = A.replace(".",".;")
    A = A.replace("!","!;")
    A = A.replace("?","?;")
    for i in A.split(";"):
        if i == "":
            continue
        i = i.rstrip().lstrip()
        print(f"{i.upper()[0]}{i.lower()[1:len(i)]}")
inputText = ''
while (True):
    try:
        strInput = input()+ ";"
        inputText += strInput
        if strInput == "quit;":
            break
    except EOFError:
        break
inputText = inputText.split(";")
ans = list()
for i in inputText:
    if i == "":
        continue
    process(i)