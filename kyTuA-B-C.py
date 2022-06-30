from itertools import product
from sys import stdin, stdout

readint = lambda: int(stdin.readline().rstrip())
writelist = lambda l: stdout.write("\n".join(map(str, l)) + "\n")


def main():
    n = readint()
    a = ["A", "B", "C"]
    res = []
    for j in range(n + 1):
        if j < 3:
            continue
        for i in product(a, repeat=j):
            ca = i.count("A")
            cb = i.count("B")
            cc = i.count("C")
            if ca > 0 and ca <= cb and cb <= cc:
                res.append("".join(map(str, i)))
    writelist(res)
    return


if __name__ == "__main__":
    main()