from Class import FlatIterator

def flat_generator(nested_list):
    i = 0
    while len(nested_list) > i:
        k = 0
        try:
            len_el = len(nested_list[i])
            while len_el > k:
             yield nested_list[i][k]
             k += 1
        except TypeError:
            yield nested_list[i]
        i += 1


if __name__ == '__main__':
    #Задание №1
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for item in FlatIterator(nested_list):
        print(item)  #

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    print('===========================================================')
    # Задание №2
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]

    for item in flat_generator(nested_list):
        print(item)
