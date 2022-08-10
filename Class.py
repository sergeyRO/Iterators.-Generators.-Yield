class FlatIterator:
    new_list = list()
    def __init__(self, list):
        self.list = [x for l in list for x in l]
        self.i = -1
        self.len_list = len(self.list)

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i >= self.len_list:
            raise StopIteration
        return self.list[self.i]
