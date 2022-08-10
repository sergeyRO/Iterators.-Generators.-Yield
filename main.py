from Class import FlatIterator

if __name__ == '__main__':
    # Задание №1
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    for item in FlatIterator(nested_list):
        print(item)  #

    print('----------------------------------------------')
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    # Задание №2
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]

    
    # for item in flat_generator(nested_list):
    #     print(item)