class Node:
    # Класс для представления узла двусвязного списка 
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # Класс для представления двусвязного списка
    def __init__(self):
        self.head = None # Ссылка на первый узел списка
    
    def is_empty(self):
        # Проверка на пустоту списка
        return self.head is None
    
    def append(self, data):
        # Добавление нового узла в конец списка
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
    
    def prepend(self, data):
        # Добавление нового узла в начало списка
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insert_after(self, prev_node_data, data):
        # Вставка нового узла после узла с указанным значением данных
        current = self.head
        while current and current.data != prev_node_data:
            current = current.next
        
        if current is None:
            print(f"Узел с данными {prev_node_data} не найден.")
            return
        
        new_node = Node(data)
        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def insert_before(self, next_node_data, data):
        # Вставка нового узла перед узлом с указанным значением данных
        current = self.head
        while current and current.data != next_node_data:
            current = current.next

        if current is None:
            print(f"Узел с данными {next_node_data} не найден.")
            return
        
        new_node = Node(data)
        new_node.next = current
        new_node.prev = current.prev

        if current.prev:
            current.prev.next = new_node
        else:
            self.head = new_node
        current.prev = new_node

    def delete(self, key):
        # Удаление узла по значению ключа
        current = self.head
        while current and current.data != key:
            current = current.next

        if current is None:
            return
        
        # Если узел удаления это head
        if current == self.head:
            self.head = current.next
            if self.head:
                self.head.prev = None
        else:
            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next
        
        current = None

    def delete_first(self):
        # Удаление первого узла списка
        if self.is_empty():
            return
        
        self.head = self.head.next
        if self.head:
            self.head.prev = None
    
    def delete_last(self):
        # Удаление последнего узла списка
        if self.is_empty():
            return
        
        current = self.head
        while current.next:
            current = current.next

        if current.prev:
            current.prev.next = None
        else:
            self.head = None
    
    def access(self, index):
        # Доступ к элементу по индексу
        current = self.head
        count = 0

        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1
        
        print("Индекс вне диапазона")
        return None
    
    def print_list(self):
        # Вывод содержимого списка вперёд
        current = self.head 
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
    
    def print_reverse(self):
        # Вывод содержимого списка в обратном порядке
        current = self.head
        while current and current.next:
            current = current.next
        
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Пример использования
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.print_list()  # Вывод: 1 <-> 2 <-> 3 <-> None

    dll.prepend(0)
    dll.print_list()  # Вывод: 0 <-> 1 <-> 2 <-> 3 <-> None

    dll.insert_after(1, 1.5)
    dll.print_list()  # Вывод: 0 <-> 1 <-> 1.5 <-> 2 <-> 3 <-> None

    dll.insert_before(2, 1.75)
    dll.print_list()  # Вывод: 0 <-> 1 <-> 1.5 <-> 1.75 <-> 2 <-> 3 <-> None

    dll.delete_first()
    dll.print_list()  # Вывод: 1 <-> 1.5 <-> 1.75 <-> 2 <-> 3 <-> None

    dll.delete_last()
    dll.print_list()  # Вывод: 1 <-> 1.5 <-> 1.75 <-> 2 <-> None

    dll.delete(1.5)
    dll.print_list()  # Вывод: 1 <-> 1.75 <-> 2 <-> None

    print("Элемент с индексом 1:", dll.access(1))  # Вывод: Элемент с индексом 1: 1.75

    dll.print_reverse()  # Вывод: 2 <-> 1.75 <-> 1 <-> None