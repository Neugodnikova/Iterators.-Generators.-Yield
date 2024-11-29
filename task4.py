import types

def flat_generator(list_of_list):
    for item in list_of_list:
        if isinstance(item, list):  # Если элемент — список, рекурсивно обрабатываем его
            yield from flat_generator(item)
        else:
            yield item  # Если элемент не список, возвращаем его

def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    print("Результат итерации через flat_generator:")
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        print(flat_iterator_item, end=" ")  # Печатаем каждый элемент
        assert flat_iterator_item == check_item

    result_list = list(flat_generator(list_of_lists_2))
    print("\nРезультат преобразования в список:", result_list)  # Печатаем итоговый список
    assert result_list == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)

if __name__ == '__main__':
    test_4()
