class BinaryTree:
    __slots__ = '__root', '__count'     # Запрещает создавать другие переменные

    def __init__(self, root_value):
        self.__root = Node(root_value)
        self.__count = 1

    def __str__(self):
        return f"{self.__root}"

    @property
    def count(self):
        return f'Общее количество узлова в бинарном дереве равно {self.__count}'

    def add(self, value):
        temp_value = value.data if isinstance(value, Node) else value
        if self.__root:
            res = self.search(self.__root, temp_value)
            if res[0] is None:
                new_node = value if isinstance(value, Node) else Node(value)
                if temp_value > res[1].data:
                    res[1].right = new_node
                else:
                    res[1].left = new_node
                self.__count += 1
            else:
                print(f"Число {value} уже есть в дереве")
        else:
            self.__root = Node(value)

    def __count_nodes(self, node=None):
        if node is None:
            node = self.__root
            self.__count = 0
        if node:
            self.__count += 1
            if node.left:
                self.__count_nodes(node.left)
            if node.right:
                self.__count_nodes(node.right)

    def delete(self, value):
        if self.__root.data == value:
            self.__root = None
            self.__count = 0
        else:
            res = self.search(self.__root, value)
            if res[0]:
                if res[1].left == res[0]:
                    res[1].left = None
                if res[1].right == res[0]:
                    res[1].right = None
                self.__count_nodes()
            else:
                print(f"Число {value} не найдено в дереве")

    def search(self, node, value, parent=None):
        """
        Рекурсивный поиск значения в дереве.
        Возвращает tuple из звена дерава и его предка.
        """
        if node is None or value == node.data:
            return node, parent
        if value > node.data:
            return self.search(node.right, value, node)
        if value < node.data:
            return self.search(node.left, value, node)


class Node:
    __slots__ = 'data', 'left', 'right'     # Запрещает создавать другие переменные

    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        """
        Рекурсивный вывод узла и его детей
        """
        res = f'значение нашего узла: {self.data}'
        if self.left:
            res += f' значение левого: {self.left.data}'
        if self.right:
            res += f' значение правого: {self.right.data}'
        if self.left:
            res += f'\n{self.left}'
        if self.right:
            res += f'\n{self.right}'
        return res
