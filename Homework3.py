# Аналог односвязного LinkedList-a, созданного на семинаре
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        """
        Функция для вывода элементов
        node - элементы линкед листа
        :return: преобразование из списка в строку
        """
        node = self.head
        nodes = list()
        while node is not None:
            nodes.append(node.data)
            node = node.next
            if node == self.head:
                break
        return " ".join(nodes)

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def add_last(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def remove_first(self):
        if self.head is None: raise Exception("List is empty")
        node = self.head
        self.head = node.next
        return

    def remove_last(self):
        if self.head is None: raise Exception("List is empty")

        current_node = self.head
        if not current_node.next:
            self.head = None
            return

        pre_node = None

        while current_node.next:
            pre_node = current_node
            current_node = current_node.next

        if not current_node: return
        pre_node.next = current_node.next


    def contains(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def reverse_itr(self):
        """
        Разворот односвязного списка через итерацию
        """
        previous, current = None, self.head
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        self.head = previous

    def reverse_rec(self):
        """
        Разворот односвязного списка через рекурсию
        """

        def reverse(previous, current):
            if current:
                reverse(current, current.next)
                current.next = previous
            else:
                self.head = previous

        reverse(previous=None, current=self.head)

    def find_element(self, n):
        """
        Поиск n-го элемента Ll без узнавания длины
        """
        p = q = self.head

        count = 0
        while q:
            count += 1
            if count >= n: break
            q = q.next

        if not q: print(str(n) + "больше длины связного списка!")

        while p and q.next:
            p = p.next
            q = q.next
        return p.data

llist = LinkedList()
llist.add_first("a")
print(llist)
llist.add_last("b")
llist.add_last("c")
llist.add_last("d")
print(llist)
print("Head:", llist.head)
llist.reverse_itr()
print("Итеративный разворот: ", llist)
print("Head:", llist.head)
llist.reverse_rec()
print("Рекурсивный разворот: ", llist)
print("Head:", llist.head)
print(llist.find_element(int(input("Введите искомый индекс: "))))