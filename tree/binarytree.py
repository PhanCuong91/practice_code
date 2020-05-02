
class BinaryTree:

    def __init__(self, root=None):
        self.root = root
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if self.left is None:
            self.left = newNode
        else:
            temp = self.left
            newNode.left = temp
            self.left = newNode

    def insertRight(self, newNode):
        if self.right is None:
            self.right = newNode
        else:
            temp = self.right
            newNode.left = temp
            self.right = newNode

    def getRootValue(self, node):
        return node.root

    def getLeft(self, node):
        return node.left

    def getRight(self, node):
        return node.right

    def convertArrayToBinaryTree(self, binarytree, index, array):
        """
        The function shall convert array as input to a binary tree as output.
        Ex:
        input -> array = [0,1,2,3,4,5,6]
        output -> binary tree:      0
                                1       2
                              3   4   5   6
        :param binarytree:empty binary tree
        :param index: get value from this index in array
        :param array: values of binary tree
        :return: binary tree which was inserted all elements in array
        """
        # base case
        if index * 2 + 1 >= len(array) or index * 2 + 2 >= len(array):
            return binarytree
        binarytree.insertLeft(BinaryTree(array[index * 2 + 1]))
        self.convertArrayToBinaryTree(binarytree.left, index * 2 + 1, array)
        binarytree.insertRight(BinaryTree(array[index * 2 + 2]))
        self.convertArrayToBinaryTree(binarytree.right, index * 2 + 2, array)
        return binarytree


class BinaryHeap:
    def __init__(self, binarytree):
        self.minheap_binarytree = binarytree
        self.maxheap_binarytree = binarytree
    @staticmethod
    def minValueOneNode(binarytree):
        """
        This function shall find min value in [binaryTree.root, binaryTree.left.root, binaryTree.right.root]
        then move it to binaryTree.root
        :param binarytree: input
        :return: binarytree after finding min value
        """
        if binarytree.root > binarytree.left.root:
            temp = binarytree.left.root
            binarytree.left.root = binarytree.root
            binarytree.root = temp
        if binarytree.root > binarytree.right.root:
            temp = binarytree.right.root
            binarytree.right.root = binarytree.root
            binarytree.root = temp
        return binarytree

    @staticmethod
    def maxValueOneNode(binarytree):
        """
        This function shall find max value in [binaryTree.root, binaryTree.left.root, binaryTree.right.root]
        then move it to binaryTree.root
        :param binarytree: input
        :return: binarytree after finding max value
        """
        if binarytree.root < binarytree.left.root:
            temp = binarytree.left.root
            binarytree.left.root = binarytree.root
            binarytree.root = temp
        if binarytree.root < binarytree.right.root:
            temp = binarytree.right.root
            binarytree.right.root = binarytree.root
            binarytree.root = temp
        return binarytree

    def minHeap(self, binarytree):
        """
        This function shall return min heap binary tree
        :param binarytree:
        :return:
        """
        # if both binarytree.left and binarytree.right are None,
        if binarytree.left is not None and binarytree.right is not None:
            # recurse left branch
            self.minHeap(binarytree.left)
            # find the minimum value in node, and put it in root of this node
            old_BinaryTreeRoot = binarytree.root
            binarytree = BinaryHeap.minValueOneNode(binarytree)
            # if the root was change, then recurse left branch
            if binarytree.root != old_BinaryTreeRoot:
                self.minHeap(binarytree.left)
            # recurse left branch
            self.minHeap(binarytree.right)
            # find the minimum value in node, and put it in root of this node
            old_BinaryTreeRoot = binarytree.root
            binarytree = BinaryHeap.minValueOneNode(binarytree)
            # if the root was change, then recurse left branch
            if binarytree.root != old_BinaryTreeRoot:
                self.minHeap(binarytree.right)
            return binarytree
        # base case
        # if at least one of binarytree.left and binarytree.right is None,
        # then return binary
        else:
            return binarytree

    def maxHeap(self, binarytree):
        """
        This function shall return max heap binary tree
        :param binarytree:
        :return:
        """
        # if both binarytree.left and binarytree.right are None,
        if binarytree.left is not None and binarytree.right is not None:
            # recurse left branch
            self.maxHeap(binarytree.left)
            # find the minimum value in node, and put it in root of this node
            old_BinaryTreeRoot = binarytree.root
            binarytree = BinaryHeap.maxValueOneNode(binarytree)
            # if the root was change, then recurse left branch
            if binarytree.root != old_BinaryTreeRoot:
                self.maxHeap(binarytree.left)
            # recurse left branch
            self.maxHeap(binarytree.right)
            # find the minimum value in node, and put it in root of this node
            old_BinaryTreeRoot = binarytree.root
            binarytree = BinaryHeap.maxValueOneNode(binarytree)
            # if the root was change, then recurse left branch
            if binarytree.root != old_BinaryTreeRoot:
                self.maxHeap(binarytree.right)
            return binarytree
        else:
            return binarytree

    def insert(self, max, value):
        pass

    def extract(self, max):
        """
        This function shall return the top root which is minimum or maximum, depend on max is false or true respectively
        :param max: if max is True, then extract max heap. if max is False, then extract min heap
        :return: return max or min heap root
        """
        if max:
            self.maxHeap(self.maxheap_binarytree)
            value = self.maxheap_binarytree.root
        else:
            self.minHeap(self.minheap_binarytree)
            value = self.minheap_binarytree.root
        return value


class BinaryTreeSearch:
    def __init__(self):
        self.binaryTree = None
        self.size = 0

    def insert(self, value, binaryTree):
        if binaryTree is None:
            binaryTree = BinaryTree(value)
            self.size += 1
        else:
            if value > binaryTree.root:
                if binaryTree.right is None:
                    binaryTree.right = BinaryTree(value)
                    self.size += 1
                    return binaryTree
                self.insert(value, binaryTree.right)
            else:
                if binaryTree.left is None:
                    binaryTree.left = BinaryTree(value)
                    self.size += 1
                    return binaryTree
                self.insert(value, binaryTree.left)

        return binaryTree

    def find(self, root_value, binaryTree):
        if binaryTree is None:
            return False
        else:
            if binaryTree.root == root_value:
                return True
            if self.find(root_value, binaryTree.left):
                return True
            if self.find(root_value, binaryTree.right):
                return True
            return False

    def remove(self, root_value, binaryTree, preBinaryTree=None, dir='left'):
        temp = self.size
        if binaryTree is None:
            return False
        else:
            if binaryTree.root == root_value:
                self.size -= 1
                if binaryTree.left is not None:
                    if dir == 'left':
                        preBinaryTree.left = binaryTree.left
                        if binaryTree.right is not None:
                            preBinaryTree.left.right = binaryTree.right
                    else:
                        preBinaryTree.right = binaryTree.left
                        if binaryTree.right is not None:
                            preBinaryTree.right.right = binaryTree.right
                elif binaryTree.right is not None:
                    if dir == 'left':
                        preBinaryTree.left = binaryTree.right
                    else:
                        preBinaryTree.right = binaryTree.right
                else:
                    if dir == 'left':
                        preBinaryTree.left = None
                    else:
                        preBinaryTree.right = None
                return True
            self.remove(root_value, binaryTree.left, binaryTree, 'left')
            self.remove(root_value, binaryTree.right, binaryTree, 'right')
            return temp != self.size


class TreeTraversals:
    """
    this class only support balanced binary tree
    """
    def __init__(self, binarytree):
        self.binarytree = binarytree
        self.out_in_oder = []
        self.out_pre_oder = []
        self.out_post_oder = []

    def InOder(self, binaryTree):
        """
        print [left,root, right]
        :return:
        """
        if binaryTree is not None:
            self.InOder(binaryTree.left)
            self.out_in_oder.append(binaryTree.root)
            self.InOder(binaryTree.right)
            return
        else:
            return

        # if binaryTree.left.left is None:
        #     self.out_in_oder.append(binaryTree.left.root)
        #     self.out_in_oder.append(binaryTree.root)
        #     self.out_in_oder.append(binaryTree.right.root)
        #     return
        # else:
        #     self.InOder(binaryTree.left)
        #     self.out_in_oder.append(binaryTree.root)
        # if binaryTree.right.left is None:
        #     if binaryTree.left.left is None:
        #         self.out_in_oder.append(binaryTree.left.root)
        #         self.out_in_oder.append(binaryTree.root)
        #     self.out_in_oder.append(binaryTree.right.root)
        #     return
        # else:
        #     self.InOder(binaryTree.right)

        pass

    def PreOder(self, binaryTree):
        """
        print [root, left, right]
        :return:
        """
        if binaryTree is not None:
            self.out_pre_oder.append(binaryTree.root)
            self.PreOder(binaryTree.left)
            self.PreOder(binaryTree.right)
            return
        else:
            return
        # self.out_pre_oder.append(binaryTree.root)
        # if binaryTree.left.left is None:
        #     # self.out_pre_oder.append(binaryTree.root)
        #     self.out_pre_oder.append(binaryTree.left.root)
        #     self.out_pre_oder.append(binaryTree.right.root)
        #     return
        # else:
        #     self.PreOder(binaryTree.left)
        #
        # if binaryTree.right.left is None:
        #     if binaryTree.left.left is None:
        #         self.out_pre_oder.append(binaryTree.left.root)
        #     self.out_pre_oder.append(binaryTree.right.root)
        #     return
        # else:
        #     self.PreOder(binaryTree.right)
        #
        # pass

    def PostOrder(self, binaryTree):
        """
        print [left, right, root]
        :return:
        """
        if binaryTree is not None:
            self.PostOrder(binaryTree.left)
            self.PostOrder(binaryTree.right)
            self.out_post_oder.append(binaryTree.root)
            return
        else:
            return
        # if binaryTree.left.left is None:
        #     self.out_post_oder.append(binaryTree.left.root)
        #     self.out_post_oder.append(binaryTree.right.root)
        #     self.out_post_oder.append(binaryTree.root)
        #     return
        # else:
        #     self.PostOrder(binaryTree.left)
        #
        # if binaryTree.right.left is None:
        #     if binaryTree.left.left is None:
        #         self.out_pre_oder.append(binaryTree.left.root)
        #     self.out_post_oder.append(binaryTree.right.root)
        #     self.out_post_oder.append(binaryTree.root)
        #     return
        # else:
        #     self.PostOrder(binaryTree.right)
        # self.out_post_oder.append(binaryTree.root)
        # pass


class SupportBinaryTree:
    """
    this class only support balanced binary tree
    """
    def __init__(self):
        self.path = []
        self.output = []

    def get_longest_path(self, binaryTree):
        """
        get the maximum root in binary tree
        :param binaryTree: input binary tree
        :return: maximum root of binary tree
        """
        max_root = 0
        if binaryTree.left is None and binaryTree.right is None:
            return 1
        if binaryTree.left is not None:
            num_root = 0
            num_root = 1 + self.get_longest_path(binaryTree.left)
            if num_root > max_root:
                max_root = num_root
        if binaryTree.right is not None:
            num_root = 0
            num_root = 1 + self.get_longest_path(binaryTree.right)
            if num_root > max_root:
                max_root = num_root
        return max_root

    @staticmethod
    def calculate_row(output, binaryTree, row):
        """
        This function shall get row of matrix with each root of binary tree
        :param output: [row, column, root] of all root in binary tree (with row and column are in matrix)
        :param binaryTree: balanced binary tree which need to be printed
        :param row: row in matrix
        :return: output array with row and value of root
        """
        if binaryTree is not None:
            output.append([row, 0, binaryTree.root])
            SupportBinaryTree.calculate_row(output, binaryTree.left, row+1)
            SupportBinaryTree.calculate_row(output, binaryTree.right, row+1)
            return output

    def calculate_column(self, output, binaryTree):
        """
        This function shall get row of matrix with each root of binary tree
        :param output: [row, column, root] of all root in binary tree (with row and column are in matrix)
        :param binaryTree: balanced binary tree which need to be printed
        :return: output array with column
        """
        n = self.get_longest_path(binaryTree)
        arr_space = []
        for i in range(n):
            arr_space.append(2 ** i)
        tmp_pos = []
        for i in range(n):
            tmp_pos.append(arr_space[n-i-1]-1)
            output[i][1] = arr_space[n-i-1]-1
        for i in range(n, len(output)):
            index = output[i][0]
            tmp_pos[index] += arr_space[n-index]
            output[i][1] = tmp_pos[index]
        return output

    def print_binary_tree(self, binaryTree):
        """
        This function shall get the binary tree then print it to console
        :param binaryTree: balanced binary tree which need to be printed
        :return: matrix which includes binary tree
        """
        n = self.get_longest_path(binaryTree)
        arr_space = []
        for i in range(n):
            arr_space.append(2 ** i)
        # print(arr_space)
        output = SupportBinaryTree.calculate_row([], binaryTree, 0)
        # print(f"output with row is {output}")
        output = self.calculate_column(output, binaryTree)
        number_of_column = arr_space[len(arr_space)-1] *2-1
        matrix = []
        for r in range(n):
            text = ''
            for c in range(number_of_column):
                add = True
                for o in output:
                    if r == o[0] and c == o[1]:
                        if o[2] < 10:
                            text += '0'
                        text += str(o[2])
                        add = False
                if add:
                    text += '--'
            matrix.append(text)
        return matrix


class SupportAllBinaryTree:
    """
    This class support printing binary tree
    """
    def get_longest_path(self, binaryTree):
        """
        get the maximum root in binary tree
        :param binaryTree: input binary tree
        :return: maximum root of binary tree
        """
        max_root = 0
        if binaryTree.left is None and binaryTree.right is None:
            return 1
        if binaryTree.left is not None:
            num_root = 0
            num_root = 1 + self.get_longest_path(binaryTree.left)
            if num_root > max_root:
                max_root = num_root
        if binaryTree.right is not None:
            num_root = 0
            num_root = 1 + self.get_longest_path(binaryTree.right)
            if num_root > max_root:
                max_root = num_root
        return max_root

    def binary_insert(self, array, left, right, inserted_value):
        """
        This function shall insert
        :param arr: array which value shall be inserted
        :param left: left index of array
        :param right: right index of array
        :param inserted_value: value which is sorted and inserted to array
        :return: index where value shall be inserted to array
        """
        # base case
        # size of array is 0 or 1, then just append 0 and 1 to array
        if len(array) == 0 or len(array) == 1:
            array.append(inserted_value)
            return len(array)-1
        mid = int((left+right)/2)
        # if the gap between left and right is 1, then follow 3 below cases
        if right - left == 1:
            # Case 1: if inserted value is smaller than left index of array,
            # then insert to left index of array
            if array[left] > inserted_value:
                array.insert(left, inserted_value)
                res = left
            # Case 2: if inserted value is larger than left index of array and smaller than right index of array,
            # then insert to left index plus 1 of array
            elif inserted_value < array[right]:
                array.insert(left+1, inserted_value)
                res = left+1
            # Case 3: if inserted value is larger than right index of array,
            # then insert to right index plus 1 of array
            else:
                # if right index is the last of array, then append value
                if right == len(array)-1:
                    array.append(inserted_value)
                # insert to right index plus 1 of array
                else:
                    array.insert(right+1, inserted_value)
                res = right+1
            # return index where shall be added value
            return res
        # if array[mid] > value, then assign right index to mid and find valid position
        if array[mid] > inserted_value:
            return self.binary_insert(array, left, mid, inserted_value)
        # if array[mid] < value, then assign left index to mid and find valid position
        else:
            return self.binary_insert(array, mid, right, inserted_value)

    def convert2arr(self, binaryTree, arr_index, arr_root, start_index):
        """
        This function shall describe binary tree to array of indices and array of root values
        example: binary tree
        --------------------------------16----------------------------
        --------------10------------------------------30--------------
        ------09--------------12--------------20--------------35------
        ------------------11------14----------------------------------
        ----------------------------15--------------------------------
        output: arr_index = [0,  1,  2, 3,  4,  5,  6,  9, 10, 22]
                arr_root = [16, 10, 30, 9, 12, 20, 35, 11, 14, 15]
        :param binaryTree:
        :param arr_index: array contain binary tree's indices which base on indices of array
        :param arr_root: array contain binary tree's root. the sequence of root with respective to arr_index
        :param start_index: start index shall be 0
        :return: [arr_index, arr_root]
        """
        # base case
        if binaryTree is None:
            return [arr_index, arr_root]
        else:
            # find valid index in array root and insert index of binary to array index
            insert_ind = self.binary_insert(arr_index, 0, len(arr_index)-1, start_index)
            if insert_ind == len(arr_root):
                arr_root.append(binaryTree.root)
            else:
                arr_root.insert(insert_ind, binaryTree.root)
            # convert next root
            self.convert2arr(binaryTree.left, arr_index, arr_root, 2*start_index+1)
            self.convert2arr(binaryTree.right, arr_index, arr_root, 2*start_index+2)
            return [arr_index, arr_root]

    def getRootPos(self, binaryTree):
        """
        This function shall find position of root of binary tree in matrix
        :param binaryTree:
        :return: matrix contains all root of binary tree
        """
        # get longest path of binary tree is the row of matrix which use print binary tree
        longest_path = self.get_longest_path(binaryTree)
        # get array of binary tree 's indices and 's root
        arr_index_root = self.convert2arr(binaryTree, [], [], 0)
        # print(arr_index_root)
        # initial array space, start position, and start index of each row
        # array space shall show how many space between to indices of respective each row
        # start position shall start position of respective each row
        # start index is the index of binary which shall be print first of respective each row
        arr_space = []
        start_pos = []
        start_index = []
        for i in range(longest_path):
            arr_space.append(2**(longest_path-1-i))
            start_pos.append(arr_space[i]-1)
            if i == 0:
                start_index.append(0)
            else:
                start_index.append(2*start_index[i-1]+1)
        # add start index of next row
        start_index.append((2*start_index[longest_path-1]+1))
        # print(arr_space)
        # print(start_pos)
        # print(start_index)
        # initial value for position array [[row, column], root value]
        pos_value = []
        r = 0
        while r < longest_path:
            ind = 0
            # search index in index array which is range start index of this row and next row
            while ind < len(arr_index_root[0]):
                if start_index[r] <= arr_index_root[0][ind] < start_index[r+1]:
                    if r != 0:
                        # if row is not zero, then column shall be
                        # (curent index - start index of the row) * array space of the row + start pos of the row
                        c = (arr_index_root[0][ind] - start_index[r]) * arr_space[r-1] + start_pos[r]
                    else:
                        # if row is 0, then set column to first of array space
                        c = arr_space[r]
                    pos_value.append([[r, c], arr_index_root[1][ind]])
                ind += 1
            r += 1
        # print(pos_value)
        return pos_value

    def print_bt(self, binaryTree):
        longest_path = self.get_longest_path(binaryTree)
        number_of_column = 2**longest_path - 1
        pos_value = self.getRootPos(binaryTree)
        matrix = []
        for r in range(longest_path):
            text = ''
            for c in range(number_of_column):
                add = True
                for root in pos_value:
                    if r == root[0][0] and c == root[0][1]:
                        if root[1] < 10:
                            text += '0'
                        text += str(root[1])
                        add = False
                if add:
                    text += '--'
            matrix.append(text)
        return matrix


if __name__ == "__main__":
    # set number of element in array
    n = 11
    arr_binary = [0]*n
    for i in range(n):
        arr_binary[i] = i
    # arr_binary = [25, 15, 50, 10, 22, 35, 70, 4, 12, 18, 24, 31, 44,]
    print(f"array binary tree is {arr_binary}")

    # convert array to binary tree
    bt_class = BinaryTree(0)
    bt = bt_class.convertArrayToBinaryTree(BinaryTree(arr_binary[0]), 0, arr_binary)

    # print all TreeTraversal
    tt = TreeTraversals(bt)
    tt.InOder(tt.binarytree)
    print(f"print in order {tt.out_in_oder}")
    print(len(tt.out_in_oder))
    tt.PreOder(tt.binarytree)
    print(f"print pre order {tt.out_pre_oder}")
    print(len(tt.out_pre_oder))
    tt.PostOrder(tt.binarytree)
    print(f"print post order {tt.out_post_oder}")
    print(len(tt.out_post_oder))

    bh = BinaryHeap(bt)
    s = SupportBinaryTree()

    print(f"original binary tree is ")
    bt = bt_class.convertArrayToBinaryTree(BinaryTree(arr_binary[0]), 0, arr_binary)
    m = s.print_binary_tree(bt)
    for i in m:
        print(i)

    min_heap_bt = bh.minHeap(bh.minheap_binarytree)
    print(f"min heap binary tree is ")
    s.output = []
    m = s.print_binary_tree(min_heap_bt)
    for i in m:
        print(i)
    print(bh.extract(True))

    max_heap_bt = bh.maxHeap(bh.maxheap_binarytree)
    print(f"max heap binary tree is ")
    s.output = []
    m = s.print_binary_tree(max_heap_bt)
    for i in m:
        print(i)
    print("Binary tree search")
    bts = BinaryTreeSearch()
    # bts.binaryTree = None
    bts.binaryTree = bts.insert(16, bts.binaryTree)
    bts.insert(10, bts.binaryTree)
    bts.insert(30, bts.binaryTree)
    bts.insert(12, bts.binaryTree)
    bts.insert(9, bts.binaryTree)
    bts.insert(35, bts.binaryTree)
    bts.insert(14, bts.binaryTree)
    bts.insert(11, bts.binaryTree)
    bts.insert(15, bts.binaryTree)
    bts.insert(20, bts.binaryTree)
    # m = s.print_binary_tree(bts.binaryTree)
    # for i in m:
        # print(i)
    print(bts.size)
    print(bts.find(14, bts.binaryTree))
    print(bts.find(9, bts.binaryTree))
    print(bts.find(19, bts.binaryTree))
    print(bts.find(16, bts.binaryTree))

    ar = []
    arr = []
    # print(convert2arr(bts.binaryTree,arr,ar, 0))
    print(s.get_longest_path(bts.binaryTree))
    sa = SupportAllBinaryTree()
    sa.print_bt(bts.binaryTree)
    m = sa.print_bt(bts.binaryTree)
    for i in m:
        print(i)
    print(bts.remove(21, bts.binaryTree))
    m = sa.print_bt(bts.binaryTree)
    for i in m:
        print(i)
    m = sa.print_bt(bt)
    for i in m:
        print(i)
    print("end")

