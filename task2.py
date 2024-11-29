import types


def flat_generator(list_of_lists):
    for sublist in list_of_lists:  # Перебираем каждый список
        for item in sublist:       # Перебираем элементы внутри списка
            yield item             # Возвращаем элемент


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    # Проверяем, что генератор возвращает элементы в нужном порядке
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    # Проверяем преобразование генератора в список
    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    # Проверяем, что функция возвращает генератор
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
