# _______________________________1 задание____ НИЖЕ ОСНОВНАЯ ВЕРСИЯ ________________________________
# numbers = []
#
# def add_number(num):
#     if num in numbers:
#         print("Число уже существует в списке.")
#     else:
#         numbers.append(num)
#         print("Число добавлено в список.")
#
# def remove_number(num):
#     if num in numbers:
#         numbers.remove(num)
#         print("Число удалено из списка.")
#     else:
#         print("Число не найдено в списке.")
#
# def show_menu():
#     print("Меню:")
#     print("1. Добавить новое число в список")
#     print("2. Удалить все вхождения числа из списка")
#     print("3. Показать список чисел")
#     print("4. Выйти из программы")
#
# while True:
#     show_menu()
#     choice = input("Выберите пункт меню: ")
#
#     if choice == '1':
#         num = int(input("Введите число для добавления: "))
#         add_number(num)
#     elif choice == '2':
#         num = int(input("Введите число для удаления: "))
#         remove_number(num)
#     elif choice == '3':
#         print("Список чисел:", numbers)
#     elif choice == '4':
#         print("Программа завершена.")
#         break
#     else:
#         print("Некорректный выбор. Попробуйте снова.")



# _____________________________ ИСПРАВЛЕННАЯ ВЕРСИЯ_______________________

from collections import deque 
 
def print_menu(): 
    printnМеню:") 
    print("1. Добавить новое число в список") 
    print("2. Удалить все вхождения числа из списка") 
    print("3. Показать содержимое списка") 
    print("4. Проверить наличие значения в списке") 
    print("5. Заменить значение в списке") 
    print("6. Выход") 
 
def add_number(dq): 
    num = int(input("Введите число для добавления: ")) 
    if num in dq: 
        print("Число уже существует в списке.") 
    else: 
        dq.append(num) 
        print("Число добавлено.") 
 
def remove_number(dq): 
    num = int(input("Введите число для удаления: ")) 
    count = dq.count(num) 
    for _ in range(count): 
        dq.remove(num) 
    print(f"Число {num} удалено {count} раз.") 
 
def show_list(dq): 
    order = input("Показать список с начала или с конца? (начало/конец): ").lower() 
    if order == 'начало': 
        print("Содержимое списка:", list(dq)) 
    elif order == 'конец': 
        print("Содержимое списка:", list(dq)[::-1]) 
    else: 
        print("Неверный выбор.") 
 
def check_number(dq): 
    num = int(input("Введите число для проверки наличия: ")) 
    if num in dq: 
        print("Число есть в списке.") 
    else: 
        print("Числа нет в списке.") 
 
def replace_number(dq): 
    old_num = int(input("Введите число для замены: ")) 
    new_num = int(input("Введите новое число: ")) 
    choice = input("Заменить только первое вхождение или все? (первое/все): ").lower() 
 
    if choice == 'первое': 
        try: 
            index = dq.index(old_num) 
            dq[index] = new_num 
            print("Первое вхождение числа заменено.") 
        except ValueError: 
            print("Число для замены не найдено.") 
    elif choice == 'все': 
        replaced = False 
        for i in range(len(dq)): 
            if dq[i] == old_num: 
                dq[i] = new_num 
                replaced = True 
        if replaced: 
            print("Все вхождения числа заменены.") 
        else: 
            print("Число для замены не найдено.") 
    else: 
        print("Неверный выбор.") 
 
def main(): 
    dq = deque() 
    while True: 
        print_menu() 
        choice = input("Выберите пункт меню: ") 
        if choice == '1': 
            add_number(dq) 
        elif choice == '2': 
            remove_number(dq) 
        elif choice == '3': 
            show_list(dq) 
        elif choice == '4': 
            check_number(dq) 
        elif choice == '5': 
            replace_number(dq) 
        elif choice == '6': 
            print("Выход из программы.") 
            break 
        else: 
            print("Неверный выбор. Попробуйте снова.") 
 
if name == "__main__": 
    main()












#  _______________________________2 задание____________________________________
#
#
# #
# class StringStack:
#     def __init__(self, max_size):
#         self.max_size = max_size
#         self.stack = []
#
#     def push(self, string):
#         if len(self.stack) < self.max_size:
#             self.stack.append(string)
#         else:
#             print("Стек полон, невозможно добавить строку.")
#
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             print("Стек пуст, невозможно вытолкнуть строку.")
#             return None
#
#     def size(self):
#         return len(self.stack)
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def is_full(self):
#         return len(self.stack) == self.max_size
#
#     def clear(self):
#         self.stack = []
#
#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         else:
#             print("Стек пуст, невозможно получить верхнюю строку.")
#             return None
#
# def display_menu():
#     print("Меню:")
#     print("1. Добавить строку в стек")
#     print("2. Вытолкнуть строку из стека")
#     print("3. Подсчитать количество строк в стеке")
#     print("4. Проверить, пустой ли стек")
#     print("5. Проверить, полный ли стек")
#     print("6. Очистить стек")
#     print("7. Получить верхнюю строку без выталкивания")
#     print("0. Выйти")
# #
# def main():
#     max_size = int(input("Укажите максимальный размер стека: "))
#     stack = StringStack(max_size)
#
#     while True:
#         display_menu()
#         choice = input("Выберите операцию: ")
#
#         if choice == '1':
#             string = input("Введите строку: ")
#             stack.push(string)
#         elif choice == '2':
#             print("Вытолкнутая строка: ", stack.pop())
#         elif choice == '3':
#             print("Количество строк в стеке: ", stack.size())
#         elif choice == '4':
#             print("Стек пустой: ", stack.is_empty())
#         elif choice == '5':
#             print("Стек полный: ", stack.is_full())
#         elif choice == '6':
#             stack.clear()
#             print("Стек очищен.")
#         elif choice == '7':
#             print("Верхняя строка: ", stack.peek())
#         elif choice == '0':
#             print("Выход из программы.")
#             break
#         else:
#             print("Неверный выбор, попробуйте еще раз.")
#
# if __name__ == "__main__":
#     main()



# ---------------------------------------------------

# class DbIList:
#     class Node:
#         previous_node = None
#         next_node =None
#         element = None
#
#         def __init__(self, element, next_node = None, previous_node = None)-> None:
#             self.element = element
#             self.next_node = next_node
#             self.previous_node = previous_node
#
#     head = None
#     tail = None
#     length = 0
#
#     def add(self, element):
#         if not self.head:
#             self.head = self.Node(element)
#             return element
#         elif not self.tail:
#             self.tail = self.Node(element, None, self.head)
#             self.head.next_node = self.tail
#             return element
#         else:
#             self.tail = self.Node(element, None,self.tail)
#             self.tail.previous_node.next_node = self.tail
#             return element
#
#     def _del(self, index, reverse = False):
#         if index == 0:
#                 el = self.head.element
#                 if self.head.next_node:
#                     self.head = self.head.next_node
#                     self.head.previous_node = None
#                 else:
#                     self.head = None
#                 return el
#         elif index == self.length-1:
#             el = self.tail.element
#             self.tail = self.tail.previous_node
#             self.tail.next_node = None
#             return el
#         elif reverse:
#                 i = self.length -1
#                 node = self.tail
#
#                 while i != index:
#                     node = node.previous_node
#                     i -= 1
#                 el = node.element
#                 node.previous_node.next_node, node.next_node.previous_node = node.next_node,node.previous_node
#                 del node
#
#
#                 return el
#         else:
#                 i = 0
#                 node = self.head
#
#                 while i != index:
#                     node = node.next_node
#                     i += 1
#                 el = node.element
#                 node.previous_node.next_node, node.next_node.previous_node = node.next_node, node.previous_node
#                 del node
#
#                 return el
#
#
#     def delete(self, index):
#         if self.head:
#             if index > self.length // 2:
#                 el = self._del(index, reverse = True)
#             elif index <= self.length // 2:
#                 el = self._del(index, reverse = False)
#             self.length -= 1
#             return el
#
#         def _assign(self,index, element, reverse = False):
#             if index == 0:
#                 self.head.element = element
#             elif index == self.length - 1:
#                 self.tail.element = element
#             elif reverse:
#                 i = self.length - 1
#                 node = self.tail
#
#             while i != index:
#                 node = node.previous_node
#                 i -= 1
#
#                node.element = element
#         else:
#             i = 0
#             node = self.head
#
#             while i != index:
#                 node = node.next_node
#                 i += 1
#
#                 node.element = element
#
#
# def delete(self, index):
#     if self.head:
#         if index > self.length // 2:
#                 el = self._del(index, reverse=True)
#         elif index <= self.length // 2:
#                 el = self._del(index, reverse=False)
#             self.length -= 1
#         return el
#
#     def is_empty(self):
#         return self.length == 0
#
#     def assign(self, index, element):
#         if self.head:
#             if index > self.length // 2:
#                    self._assing(index, element, reverse=True)
#             elif index <= self.length // 2:
#                    self._assing(index, element, reverse=False)
#
#         def __iter__(self):
#             node = self.head
#
#         while node:
#             yield node.element
#             node = node.next_node
#
#
# if __name__ == '__main__':
#     dbIList = DbIList()
#
#     # dbIList.add(4)
#     dbIList.delete(0)
#
#     # dbIList.add(-3)
#     # dbIList.add(1)
#     # dbIList.add(25)
#     # dbIList.add(0)
#     # dbIList.add(10)
#     #
#     # dbIList.assign(0, 1000)
#
# for e in dbIList:
#     print(e)
# print(dbIList.is_empty())
#
