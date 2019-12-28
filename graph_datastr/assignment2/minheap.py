"""Min-heap implementation."""


class MinHeap:
    """Allows heap of single values or (value, label) tuples."""
    def __init__(self, values=None):
        self.h = []
        if values is not None:
            self.heapify(values)

    def __contains__(self, value):
        return value in self.h

    def __repr__(self):
        return repr(self.h)

    def _full_val(self, label):
        if label in self.h:
            return label
        found = [v for v in self.h if isinstance(v, tuple) and v[1] == label]
        if found:
            return found[0]
        else:
            return None

    def _val(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            return value[0]
        return value

    def _parent_index(self, index):
        return None if index == 0 else (index - 1) // 2

    def _left_child_index(self, index):
        lci = index * 2 + 1

        return lci if lci < len(self.h) else None

    def _right_child_index(self, index):
        rci = index * 2 + 2

        return rci if rci < len(self.h) else None

    def heapify(self, values):
        self.h = []
        for v in values:
            self.insert(v)

    def is_empty(self):
        return len(self.h) == 0

    def peek(self):
        return self.h[0] if len(self.h) > 0 else None

    def _sift_up(self, i=None):
        if i is None:
            i = len(self.h) - 1
        while i > 0 and self._val(self.h[i]) < self._val(self.h[self._parent_index(i)]):
            p = self._parent_index(i)
            self.h[i], self.h[p] = self.h[p], self.h[i]
            i = p
        return i

    def _go_left(self, i):
        self.h[i], self.h[self._left_child_index(i)] = (
        self.h[self._left_child_index(i)],
        self.h[i],
        )
        return self._left_child_index(i)

    def _go_right(self, i):
        self.h[i], self.h[self._right_child_index(i)] = (
        self.h[self._right_child_index(i)],
        self.h[i],
        )
        return self._right_child_index(i)

    def _sift_down(self, i=None):
        if i is None:
            i = 0

        while i < len(self.h) and (
            (
                self._left_child_index(i) is not None
                and self._val(self.h[i]) > self._val(self.h[self._left_child_index(i)])
            )
            or (
                self._right_child_index(i) is not None
                and self._val(self.h[i]) > self._val(self.h[self._right_child_index(i)])
            )
        ):
            if self._right_child_index(i) is not None and self._right_child_index(i) is not None:
                if self._val(self.h[i]) <= self._val(self.h[self._left_child_index(i)]) and self._val(self.h[i]) <= self._val(self.h[self._right_child_index(i)]):
                    break
                if self._val(self.h[self._left_child_index(i)]) < self._val(self.h[self._right_child_index(i)]) and self._val(self.h[i]) > self._val(self.h[self._left_child_index(i)]):
                    i = self._go_left(i)
                elif self._val(self.h[self._right_child_index(i)]) < self._val(self.h[self._left_child_index(i)]) and self._val(self.h[i]) > self._val(self.h[self._right_child_index(i)]):
                    i = self._go_right(i)
            elif self._left_child_index(i) is not None and self._val(self.h[i]) > self._val(self.h[self._left_child_index(i)]):
                i = self._go_left(i)
            elif self._right_child_index(i) is not None and self._val(self.h[i]) > self._val(self.h[self._right_child_index(i)]):
                i = self._go_right(i)

        return i

    def insert(self, value):
        if len(self.h) == 0:
            self.h.append(value)
            return 0
        self.h.append(value)
        return self._sift_up()

    def pop(self, value=None):
        # Pop last element by default
        if len(self.h) == 0:
            return None
        elif len(self.h) == 1:
            return self.h.pop()

        if value is None:
            i = 0
            value = self.h[0]
        else:
            value = self._full_val(value)
            # Value not in heap
            if value is None:
                return None
            i = self.h.index(value)

        # Last element
        if i == len(self.h) - 1:
            return self.h.pop()
        else:
            self.h[i] = self.h.pop()

        if i == 0 or self._val(self.h[i]) > self._val(self.h[self._parent_index(i)]):
            self._sift_down(i)
        else:
            self._sift_up(i)

        return value
