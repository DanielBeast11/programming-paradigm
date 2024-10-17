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
