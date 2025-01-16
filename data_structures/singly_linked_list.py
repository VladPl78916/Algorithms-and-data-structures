class Node:
    # Класс для представления узла односвязного списка
    def __init__(self, data):
        self.data = data # Данные узла
        self.next = None # Ссылка на следующий узел

class SinglyLinkedList:
    # Класс для представления односвязного списка
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
    
    def prepend(self, data):
        # Добавление нового узла в начало списка
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node_data, data):
        # Вставка нового узла после заданного узла
        current = self.head
        while current and current.data != prev_node_data:
            current = current.next
        
        if current is None:
            print(f"Узел с данными {prev_node_data} не найден.")
            return
        
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete(self, key):
        # Удаление узла по значению ключа
        current = self.head

        # Если узел для удаления - это head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        
        # Поиск узла для удаления
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # Узел не найден
        if current is None:
            return
        
        # Удаление узла
        prev.next = current.next
        current = None
    
    def find(self, key):
        # Поиск узла по значению ключа
        current = self.head
        while current and current.data != key:
            current = current.next
        return current  # Вернёт узел или None, если не найден
    
    def print_list(self):
        # Вывод содержимого списка
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Пример использования
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.print_list()  # Вывод: 1 -> 2 -> 3 -> None

    sll.prepend(0)
    sll.print_list()  # Вывод: 0 -> 1 -> 2 -> 3 -> None

    sll.insert_after(1, 1.5)
    sll.print_list()  # Вывод: 0 -> 1 -> 1.5 -> 2 -> 3 -> None

    sll.delete(2)
    sll.print_list()  # Вывод: 0 -> 1 -> 3 -> None

    node = sll.find(3)
    if node:
        print(f"Найден узел с данными: {node.data}")  # Вывод: Найден узел с данными: 3