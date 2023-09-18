class BinaryTree:
    """
    Класс BinaryTree создает бинарное дерево, которому характерно наличии двух потомков,
    где левый меньше родителя, а правый – больше.
    """
    __slots__ = '__root', '__count'  # Запрещает создавать другие переменные

    def __init__(self, root_value):
        self.__root = Node(root_value)
        self.__count = 1

    def __str__(self):
        return f"{self.__root}"

    @property
    def count(self):
        """
        Свойство, которое возвращает общее количество узлов в бинарном дереве.
        """
        return f'Общее количество узлов в бинарном дереве равно {self.__count}'

    def add(self, value):
        """
        Добавляет звено в дерево
        """
        if self.__root:
            search_node, parent_node = self.search(self.__root, value)
            if search_node is None:
                new_node = Node(value)
                if value > parent_node.data:
                    parent_node.right = new_node
                else:
                    parent_node.left = new_node
                self.__count += 1
            else:
                print(f"Число {value} уже есть в дереве")
        else:
            self.__root = Node(value)
            self.__count += 1

    def delete(self, value):
        """
        Поиск и удаление звена дерева по значению.
        """
        search_node, parent_node = self.search(self.__root, value)
        if search_node and isinstance(search_node, Node):
            if search_node.left is None and search_node.right is None:  # если удаляемое звено листок
                self.__delete_node_without_child(search_node, parent_node)
            elif search_node.left and search_node.right:                # если удаляемое звено имеет 2 детей
                self.__delete_node_with_two_children(search_node)
            else:                                                       # если удаляемое звено имеет только 1 ребенка
                self.__delete_node_with_single_child(search_node, parent_node)
            self.__count -= 1
        else:
            print(f"Число {value} не найдено в дереве")

    def __delete_node_with_two_children(self, delete_node):
        """
        Удаление звена с 2 детьми
        """
        min_value_node, parent_min_value_node = self.__find_min_value(delete_node.right)
        if parent_min_value_node is None:
            parent_min_value_node = delete_node
        delete_node.data = min_value_node.data
        if min_value_node.right:
            self.__delete_node_with_single_child(min_value_node, parent_min_value_node)
        else:
            self.__delete_node_without_child(min_value_node, parent_min_value_node)

    def __delete_node_without_child(self, delete_node, parent_node):
        """
        Удаление звена без детей
        """
        if parent_node:
            if parent_node.left == delete_node:
                parent_node.left = None
            else:
                parent_node.right = None
        else:
            self.__root = None

    def __delete_node_with_single_child(self, delete_node, parent_node):
        """
        Удаление звена с 1 ребенком
        """
        child_node = delete_node.left or delete_node.right
        if parent_node:
            if parent_node.left == delete_node:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
        else:
            self.__root = child_node

    def search(self, node, value, parent=None):
        """
        Рекурсивный поиск значения в дереве.
        Если найдено звено со входящем значением, то возврашает это звено и его родителя.
        Иначе возвращает None и ближайшее звено по входящему значению.
        """
        if node is None or value == node.data:
            return node, parent
        if value > node.data:
            return self.search(node.right, value, node)
        if value < node.data:
            return self.search(node.left, value, node)

    def __find_min_value(self, node):
        """
        Поиск звена по минимальному значению
        """
        cur_node = node
        parent_node = None
        while cur_node.left:
            parent_node = cur_node
            cur_node = cur_node.left
        return cur_node, parent_node


class Node:
    """
    Класс Node, которое создает звено бинарного дерева
    """
    __slots__ = 'data', 'left', 'right'  # Запрещает создавать другие переменные

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
