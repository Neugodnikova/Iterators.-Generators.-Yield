class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.outer_index = 0  # индекс для внешнего списка
        self.inner_index = 0  # индекс для внутреннего списка

    def __iter__(self):
        return self

    def __next__(self):
        while self.outer_index < len(self.list_of_list):  # проверяем, не вышли ли за пределы внешнего списка
            if self.inner_index < len(self.list_of_list[self.outer_index]):  # проверяем, есть ли элементы во внутреннем списке
                item = self.list_of_list[self.outer_index][self.inner_index]
                self.inner_index += 1  # перемещаемся к следующему элементу внутреннего списка
                return item
            else:
                self.outer_index += 1  # переходим к следующему списку
                self.inner_index = 0  # сбрасываем индекс внутреннего списка
        raise StopIteration  # если элементы закончились, вызываем исключение


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    print("Результат итерации через FlatIterator:")
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        print(flat_iterator_item, end=" ")
        assert flat_iterator_item == check_item

    result_list = list(FlatIterator(list_of_lists_1))
    print("\nРезультат преобразования в список:", result_list)
    assert result_list == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
