import math


class triangle:

    def __init__(self, a, b, c):

        self.triangleSide1 = a
        self.triangleSide2 = b
        self.triangleSide3 = c

        if (a + b) <= c or (a + c) <= b or (b + c) <= a:
            print('Can`t create this triangle!!')
            exit(1)

    def square(self):
        p = (self.triangleSide1 + self.triangleSide2 + self.triangleSide3) * 0.5
        s = math.sqrt((p * (p - self.triangleSide1) * (p - self.triangleSide2) * (p - self.triangleSide3)))
        return s

    def perimeter(self):
        sum = self.triangleSide1 + self.triangleSide2 + self.triangleSide3

        return sum

    def showSides(self):
        return [self.triangleSide1, self.triangleSide2, self.triangleSide3]


p = triangle(6, 6, 5)

print(p.perimeter())
print(p.showSides())
print(p.square())