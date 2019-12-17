# implement dynamic array
import ctypes


class DynamicArray(object):
    def __init__(self, array):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if not 0 <= index < self.n:
            return IndexError('cannot found index in array')
        return self.A[index]

    def make_array(self, capacity):
        return (capacity*ctypes.py_object)()

    def _resize(self, new_cap):
        B = self.make_array(new_cap)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = new_cap

    def append(self, element):
        if self.n == self.capacity:
            self._resize(self.capacity*2)
        self.A[self.n] = element
        self.n += 1


if __name__ == "__main__":
    dyn_arr = DynamicArray(int)
    for i in range(10):
        dyn_arr.append(i*2)
        print("len of array: {0}".format(dyn_arr.__len__()))
        print("value: {0}".format(dyn_arr.__getitem__(i)))
        print("array after appending: {0}".format(dyn_arr.A))
    print("value: {0}".format(dyn_arr.__getitem__(11)))
    for i in range(10):
        print("number of index {0}: {1}".format(i, dyn_arr[i]))