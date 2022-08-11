class FlatIterator:

    def __init__(self, list):
        self.list = list

    def __iter__(self):
        self.num_item = -1
        self.result = iter([])
        self.len_list = len(self.list)
        return self

    def __next__(self):
        try:
            item = next(self.result)
        except StopIteration:
            self.num_item += 1
            if self.num_item >= self.len_list:
                raise StopIteration
            try:
                self.result = iter(self.list[self.num_item])
                item = next(self.result)
            except TypeError:
                item = self.list[self.num_item]
        return item