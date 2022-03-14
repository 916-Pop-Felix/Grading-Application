import unittest


class IterableObj:
    def __init__(self):
        self.list = []
        self.index = 0

    def __iter__(self):
        return iter(self.list)

    def __next__(self):
        if self.index == len(self.list):
            raise StopIteration
        else:
            self.index += 1
            return self.list[self.index - 1]

    def __len__(self):
        return len(self.list)

    def __setitem__(self, index, val):
        self.list[index] = val

    def __getitem__(self, index):
        return self.list[index]

    def append(self, x):
        self.list.append(x)

    def __delitem__(self, index):
        del self.list[index]

    def pop(self, id):
        self.list.pop(id)

    def clear(self):
        self.list.clear()


def filter(condition, list):
    final_list = []
    for i in list:
        if condition(i):
            final_list.append(i)
    return final_list


def sort(list, func, reverse):
    i = 0
    while i < len(list):
        if i == 0:
            i = i + 1
        if func(list[i]) >= func(list[i - 1]):
            i = i + 1
        else:
            list[i], list[i - 1] = list[i - 1], list[i]
            i = i - 1
    if reverse == False:
        return list
    return reversed(list)


class TestIterableStructure(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIterable(self):
        v = IterableObj()
        self.assertEqual(v.index, 0)
        t_val = False
        try:
            v.__next__()
        except StopIteration:
            t_val = True
        self.assertTrue(t_val)
        numbers = [3, 5, -2, 44, 8, 102, -22, 6, 1231]
        for num in numbers:
            v.append(num)
        self.assertEqual(v.__next__(), 3)
        self.assertEqual(v.__len__(), 9)
        v.__delitem__(7)
        self.assertEqual(v.__len__(), 8)
        v.__setitem__(7, 2312)
        self.assertEqual(v.__getitem__(7), 2312)
        v.pop(7)
        self.assertEqual(v.__len__(), 7)
        positive_list = filter(lambda x: x >= 0, v)
        self.assertEqual(len(positive_list), 5)
        sorted_list = sort(v, lambda x: x, reverse=False)
        self.assertEqual(len(sorted_list), 7)
        self.assertEqual(sorted_list[0], -22)
        sorted_list = sort(v, lambda x: x, reverse=True)
        v.clear()
        self.assertEqual(len(v), 0)
