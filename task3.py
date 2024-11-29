class FlatIterator:
    def __init__(self, list_of_list):
        self.stack = [(list_of_list, 0)]  # Стек для отслеживания текущего списка и индекса

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            current_list, current_index = self.stack[-1]  # Берем текущий список и индекс из вершины стека
            if current_index >= len(current_list):  # Если индекс превышает длину текущего списка
                self.stack.pop()  # Убираем текущий список из стека
                continue
            self.stack[-1] = (current_list, current_index + 1)  # Увеличиваем индекс на 1
            item = current_list[current_index]
            if isinstance(item, list):  # Если элемент — список, добавляем его в стек
                self.stack.append((item, 0))
            else:
                return item  # Если элемент не список, возвращаем его
        raise StopIteration  # Если стек пустой, завершаем итерацию


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    print("Результат итерации через FlatIterator:")
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        print(flat_iterator_item, end=" ")  # Печатаем каждый элемент
        assert flat_iterator_item == check_item

    result_list = list(FlatIterator(list_of_lists_2))
    print("\nРезультат преобразования в список:", result_list)  # Печатаем итоговый список
    assert result_list == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
