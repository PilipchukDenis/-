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



# _____________________________ОСНОВНАЯ ВЕРСИЯ_______________________
#
# def show_menu():
#     print("Меню: ")
#     print("1. Добавить новое число в список")
#     print("2. Удалить все вхождения числа из списка")
#     print("3. Показать содержимое списка")
#     print("4. Проверить, есть ли значение в списке")
#     print("5. Заменить значение в списке")
#     print("6. Выйти из программы")
#
#
# def add_number(lst):
#     num = int(input("Введите число для добавления: "))
#     if num in lst:
#         print(f"Число {num} уже существует в списке.")
#     else:
#         lst.append(num)
#         print(f"Число {num} добавлено в список.")
#
#
# def remove_number(lst):
#     num = int(input("Введите число для удаления: "))
#     if num in lst:
#         lst[:] = [x for x in lst if x != num]
#         print(f"Все вхождения числа {num} удалены из списка.")
#     else:
#         print(f"Число {num} не найдено в списке.")
#
#
# def show_list(lst):
#     direction = input("Вывести список с начала или с конца? (начало/конец): ").strip().lower()
#     if direction == "начало":
#         print("Содержимое списка: ", lst)
#     elif direction == "конец":
#         print("Содержимое списка: ", lst[::-1])
#     else:
#         print("Неверный выбор. Попробуйте снова.")
#
#
# def check_number(lst):
#     num = int(input("Введите число для проверки: "))
#     if num in lst:
#         print(f"Число {num} найдено в списке.")
#     else:
#         print(f"Число {num} не найдено в списке.")
#
#
# def replace_number(lst):
#     old_num = int(input("Введите число для замены: "))
#     new_num = int(input("Введите новое число: "))
#     all_occurrences = input("Заменить все вхождения или только первое? (все/первое): ").strip().lower()
#
#     if old_num not in lst:
#         print(f"Число {old_num} не найдено в списке.")
#         return
#
#     if all_occurrences == "все":
#         lst[:] = [new_num if x == old_num else x for x in lst]
#         print(f"Все вхождения числа {old_num} заменены на {new_num}.")
#     elif all_occurrences == "первое":
#         for i in range(len(lst)):
#             if lst[i] == old_num:
#                 lst[i] = new_num
#                 print(f"Первое вхождение числа {old_num} заменено на {new_num}.")
#                 break
#     else:
#         print("Неверный выбор. Попробуйте снова.")
#
#
# def main():
#     lst = list(map(int, input("Введите набор чисел, разделённых пробелами: ").split()))
#
#     while True:
#         show_menu()
#
#         choice = input("Выберите пункт меню: ").strip()
#
#         if choice == '1':
#             add_number(lst)
#         elif choice == '2':
#             remove_number(lst)
#         elif choice == '3':
#             show_list(lst)
#         elif choice == '4':
#             check_number(lst)
#         elif choice == '5':
#             replace_number(lst)
#         elif choice == '6':
#             print("Завершение программы.")
#             break
#         else:
#             print("Неверный выбор. Попробуйте снова.")
#
#
# if __name__ == "__main__":
#     main()












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