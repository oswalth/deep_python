class Lister(list):
    def __init__(self, list_):
        self.list_ = list_

    def preprocess_lists(self, other_list):
        dif = len(self.list_) - len(other_list)
        if dif < 0:
            list_a = self.list_[:] + abs(dif) * [0]
            list_b = other_list[:]
        else:
            list_a = self.list_[:]
            list_b = other_list[:] + abs(dif) * [0]
        return list_a, list_b

    def __add__(self, other):
        if not isinstance(other, Lister):
            other = Lister(other)
        list_a, list_b = self.preprocess_lists(other.list_)
        return Lister([x + y for (x, y) in zip(list_a, list_b)])

    def __sub__(self, other):
        if not isinstance(other, Lister):
            other = Lister(other)
        list_a, list_b = self.preprocess_lists(other.list_)
        return Lister([x - y for (x, y) in zip(list_a, list_b)])

    def __eq__(self, other):
        if not isinstance(other, Lister):
            other = Lister(other)
        if sum(self.list_) == sum(other.list_):
            return True
        return False

    def __ne__(self, other):
        if not isinstance(other, Lister):
            other = Lister(other)
        if sum(self.list_) != sum(other.list_):
            return True
        return False

    def __lt__(self, other):
        if not isinstance(other, Lister):
            other = Lister(other)
        if sum(self.list_) < sum(other.list_):
            return True
        return False

    def __le__(self, other):
        if not isinstance(other, Lister):
            other = Lister(other)
        if sum(self.list_) <= sum(other.list_):
            return True
        return False

    def __gt__(self, other):
        if not isinstance(other, Lister):
            other = Lister(other)
        if sum(self.list_) > sum(other.list_):
            return True
        return False

    def __ge__(self, other):
        if not isinstance(other, Lister):
            other = Lister(other)
        if sum(self.list_) >= sum(other.list_):
            return True
        return False

    def __str__(self):
        return 'Magic list - {}'.format(self.list_)


a = Lister([1, 2, 3, 4])
# b = Lister([3, 6])
b = [3, 6]
c = a + b
d = a - b
eq = a == Lister([5, 2, 3])
ne = a != Lister([1, 2, 3, 4, 0])
lt = a < Lister([1, 2, 3, 5])
le = a <= Lister([1, 2, 3, 4, 0])
gt = a > Lister([5, 5])
ge = a >= [9, 0, 1, 0, -1]
