from minheap import MinHeap
import unittest


class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.h = MinHeap()
        self.h.h = [2, 4, 5, 12, 13, 6, 10]

    def test_parent_index(self):
        self.assertLess(self.h._parent_index(0), 0)
        self.assertEqual(self.h._parent_index(1), 0)
        self.assertEqual(self.h._parent_index(2), 0)
        self.assertEqual(self.h._parent_index(4), 1)
        self.assertEqual(self.h._parent_index(6), 2)

    def test_left_child_index(self):
        self.assertGreaterEqual(self.h._left_child_index(3), len(self.h))
        self.assertGreaterEqual(self.h._left_child_index(5), len(self.h))
        self.assertEqual(self.h._left_child_index(0), 1)
        self.assertEqual(self.h._left_child_index(1), 3)
        self.assertEqual(self.h._left_child_index(2), 5)

    def test_right_child_index(self):
        self.assertGreaterEqual(self.h._right_child_index(3), len(self.h))
        self.assertGreaterEqual(self.h._right_child_index(6), len(self.h))
        self.assertEqual(self.h._right_child_index(0), 2)
        self.assertEqual(self.h._right_child_index(1), 4)
        self.assertEqual(self.h._right_child_index(2), 6)

    def test_is_empty(self):
        self.assertFalse(self.h.is_empty())
        self.assertTrue(MinHeap().is_empty())

    def test_peek(self):
        self.assertEqual(self.h.peek(), self.h.h[0])
        self.assertIsNone(MinHeap().peek())

    def test_heapify_init(self):
        values = [2, 4, 5, 6, 10, 12, 13]
        h = MinHeap(values)
        self.assertEqual(h.h, [2, 4, 5, 6, 10, 12, 13])

    def test_heapify_after_init(self):
        values = [2, 4, 5, 6, 10, 12, 13]
        h = MinHeap()
        self.assertEqual(h.h, [])
        h.heapify(values)
        self.assertEqual(h.h, [2, 4, 5, 6, 10, 12, 13])

    def test_insert_1(self):
        self.assertEqual(self.h.insert(1), 0)
        self.assertEqual(self.h.h, [1, 2, 5, 4, 13, 6, 10, 12])

    def test_insert_3(self):
        self.assertEqual(self.h.insert(3), 1)
        self.assertEqual(self.h.h, [2, 3, 5, 4, 13, 6, 10, 12])

    def test_insert_10(self):
        self.assertEqual(self.h.insert(10), 3)
        self.assertEqual(self.h.h, [2, 4, 5, 10, 13, 6, 10, 12])

    def test_insert_15(self):
        self.assertEqual(self.h.insert(15), 7)
        self.assertEqual(self.h.h, [2, 4, 5, 12, 13, 6, 10, 15])

    def test_pop_empty(self):
        h = MinHeap()
        self.assertIsNone(h.pop())
        self.assertEqual(h.h, [])

    def test_pop_value_not_in_heap(self):
        before = self.h.h
        self.assertIsNone(self.h.pop(20))
        self.assertEqual(before, self.h.h)

    def test_pop_2(self):
        self.assertEqual(len(self.h.h), 7)
        self.assertEqual(self.h.pop(2), 2)
        self.assertEqual(len(self.h.h), 6)
        self.assertEqual(self.h.h, [4, 10, 5, 12, 13, 6])

    def test_pop_5(self):
        self.assertEqual(len(self.h.h), 7)
        self.assertEqual(self.h.pop(5), 5)
        self.assertEqual(len(self.h.h), 6)
        self.assertEqual(self.h.h, [2, 4, 6, 12, 13, 10])

    def test_pop_10(self):
        self.assertEqual(len(self.h.h), 7)
        self.assertEqual(self.h.pop(10), 10)
        self.assertEqual(len(self.h.h), 6)
        self.assertEqual(self.h.h, [2, 4, 5, 12, 13, 6])

class TestMinHeapSort(unittest.TestCase):
    def setUp(self):
        self.h = MinHeap(values=[(4, 101), (12, 9), (13, 5), (2, 1), (6, 1001), (5, 45), (10, 121)])

    def test_correct_order(self):
        self.assertEqual(self.h.h, [(2, 1), (4, 101), (5, 45), (12, 9), (6, 1001), (13, 5), (10, 121)])

    def test_insert_99_1(self):
        self.assertEqual(self.h.insert((1, 99)), 0)
        self.assertEqual(self.h.h, [(1, 99), (2, 1), (5, 45), (4, 101), (6, 1001), (13, 5), (10, 121), (12, 9)])

    def test_pop(self):
        self.assertEqual(len(self.h.h), 7)
        self.assertEqual(self.h.pop(), (2, 1))
        self.assertEqual(self.h.pop(), (4, 101))
        self.assertEqual(self.h.pop(), (5, 45))
        self.assertEqual(self.h.pop(), (6, 1001))
        self.assertEqual(len(self.h.h), 3)
        self.assertEqual(self.h.h, [(10, 121), (13, 5), (12, 9)])

    def test_pop_2_1_val(self):
        self.assertEqual(len(self.h.h), 7)
        self.assertEqual(self.h.pop((2, 1)), (2, 1))
        self.assertEqual(len(self.h.h), 6)
        self.assertEqual(self.h.h, [(4, 101), (10, 121), (5, 45), (12, 9), (6, 1001), (13, 5)])

    def test_pop_label_101(self):
        self.assertEqual(len(self.h.h), 7)
        self.assertEqual(self.h.pop(101), (4, 101))
        self.assertEqual(len(self.h.h), 6)
        self.assertEqual(self.h.h, [(2, 1), (6, 1001), (5, 45), (12, 9), (10, 121), (13, 5)])

if __name__ == '__main__':
    unittest.main()
