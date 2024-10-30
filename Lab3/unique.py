from gen_random import gen_random

class Unique:
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.seen = set() 

    def __iter__(self):
        return self

    def __next__(self):
        for item in self.items:
            if self.ignore_case and isinstance(item, str):
                processed_item = item.lower()
            else:
                processed_item = item
            if processed_item not in self.seen:
                self.seen.add(processed_item)
                return item
        raise StopIteration
print("1)")
data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
for item in Unique(data):
    print(item)

print("\n2)")
data = gen_random(10, 1, 3)
for item in Unique(data):
    print(item)

print("\n3)")
data = ['a', 'A', 'b', "B", 'a', 'A', 'b', 'B']
for item in Unique(data):
    print(item)


print("\n4)")
data = ['a', 'A', 'b', "B", 'a', 'A', 'b', 'B']
for item in Unique(data, ignore_case=True):
    print(item)