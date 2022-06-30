n = int(input())
for i in range(n):
    s = input()
    k = 1
    stack = []
    for i in s:
        if i == '(':
            stack.append(k)
            print(k,end=" ")
            k += 1
        elif i ==')':
            print(stack.pop(),end=" ")
    print("")