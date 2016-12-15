import unittest

def my_sort_v1(s_list):
    was_swap = True
    while was_swap:
        was_swap = False
        for i in range(len(s_list)-1):
            if s_list[i] > s_list[i+1]:
                s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
                was_swap = True
    return s_list


def my_sort_v2(s_list):
    if len(s_list) <=1:
        return s_list
    base_elem = s_list[0]
    less_then = [elem for elem in s_list if elem < base_elem]
    larger_then = [elem for elem in s_list if elem > base_elem]
    return my_sort(less_then) + [base_elem] + my_sort(larger_then)

def my_sort(s_list):
    return sorted(set(s_list))


class MyListTest(unittest.TestCase):
    def test_normal(self):
        res = my_sort([1, 4, 6, 2, 87,15, 2, 1])
        self.assertEqual(res, [1, 2, 4, 6, 15, 87])

    def test_empty(self):
        res = my_sort([])
        self.assertEqual(res, [])

    def test_single(self):
        res = my_sort([1])
        self.assertEqual(res, [1])

    def test_negative(self):
        res = my_sort([1, -6, 8, -16])
        self.assertEqual(res, [-16, -6, 1, 8])

    def test_abc(self):
        res = my_sort(['a', 'c', 'b', 'a'])
        self.assertEqual(res, ['a', 'b', 'c'])


if __name__ == '__main__':
    unittest.main()
