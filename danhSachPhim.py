from datetime import datetime
class Movie:
    def __init__(self, ma, dateproject, name, number, cartegory):
        self.ma = 'P{:03d}'.format(ma)
        self.name = name
        self.dateproject = datetime.strptime(dateproject, '%d/%m/%Y')
        self.number = number
        self.cartegory = cartegory

    def __str__(self):
        return f'{self.ma} {self.cartegory.name} {self.dateproject.strftime("%d/%m/%Y")} {self.name} {self.number}'


class Cartegory:
    def __init__(self, id, name):
        self.id = 'TL{:03d}'.format(id)
        self.name = name


if __name__ == '__main__':
    t = [int(x) for x in input().split()]
    cartegory = []
    for i in range(t[0]):
        a = Cartegory(i + 1, input())
        cartegory.append(a)
    # for item in cartegory:
    #     print(item.id , item.name)
    movies = []
    for i in range(t[1]):
        c = input()
        d = ''
        for item in cartegory:
            if item.id == c:
                d = item

        # print(d.id, d.name)
        b = Movie(i + 1, input(), input(), int(input()), d)
        movies.append(b)
    movies.sort(key=lambda x: (x.dateproject, x.name, x.number * (-1)))
    for item in movies:
        print(item)
