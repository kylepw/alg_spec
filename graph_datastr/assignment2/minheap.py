"""Min-heap implementation."""


class MinHeap:
    """Allows heap of single values or (value, label) tuples."""
    def __init__(self, values=None):
        self.h = []
        # Track current index of labels.
        self.index = {}
        if values is not None:
            self.heapify(values)

    def __contains__(self, value):
        return value in self.h

    def __len__(self):
        return len(self.h)

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

    def _label(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            return value[1]
        return value

    def _val(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            return value[0]
        return value

    def _parent_index(self, index):
        return (index - 1) // 2

    def _left_child_index(self, index):
        return index * 2 + 1

    def _right_child_index(self, index):
        return index * 2 + 2

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

        p = self._parent_index(i)

        while p >= 0 and self._val(self.h[p]) > self._val(self.h[i]):
            self.h[i], self.h[p] = self.h[p], self.h[i]
            # Update label indices.
            self.index[self._label(self.h[i])], self.index[self._label(self.h[p])] = self.index[self._label(self.h[p])], self.index[self._label(self.h[i])]
            i = p
            p = self._parent_index(i)
        return i

    def _sift_down(self, i=None):
        if i is None:
            i = 0

        while True:
            l = self._left_child_index(i)
            r = self._right_child_index(i)

            smallest = i

            if l < len(self.h) and self._val(self.h[i]) > self._val(self.h[l]):
                smallest = l
            elif r < len (self.h) and self._val(self.h[i]) > self._val(self.h[r]):
                smallest = r

            if smallest != i:
                self.h[i], self.h[smallest] = self.h[smallest], self.h[i]
                # Update label indices.
                self.index[self._label(self.h[i])], self.index[self._label(self.h[smallest])] = self.index[self._label(self.h[smallest])], self.index[self._label(self.h[i])]
                smallest = i
            else:
                return i

    def insert(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            label = value[1]
        else:
            label = value

        self.h.append(value)

        # Add index.
        self.index[label] = len(self.h) - 1

        return self._sift_up()

    def update_min(self, value, label):
        if label not in self.index:
            return False
        i = self.index[label]
        current_val = self._val(self.h[i])
        if value < current_val:
            self.h[i] = (value, label)
        return True



    def pop(self, label=None):
        if label is not None and label not in self.index:
            return None
        # Pop last element by default
        if len(self.h) == 0:
            return None
        elif len(self.h) == 1:
            self.index = {}
            return self.h.pop()

        if label is None:
            label = self._label(self.h[-1])
            i = 0
            value = self.h[0]
        else:
            i = self.index[label]
            value = self.h[i]

        del self.index[label]

        # Last element
        if i == len(self.h) - 1:
            return self.h.pop()

        self.index[self._label(self.h[-1])] = i
        self.h[i] = self.h.pop()

        if i == 0 or self._val(self.h[i]) > self._val(self.h[self._parent_index(i)]):
            self._sift_down(i)
        else:
            self._sift_up(i)

        return value
