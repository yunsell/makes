class FourCal:
    def __init__(self, first=1, second=1):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

    def div(self):
        if self.second == 0:
            return 0
        else:
            result = self.first / self.second
            return result


a = MoreFourCal(4, 2)
b = FourCal(3, 8)
c = FourCal()

print(a.pow())
print(b.add())
print(c.mul())
