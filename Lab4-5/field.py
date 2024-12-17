def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) == 1:
            value = item.get(args[0])
            if value is not None:
                yield value
        else:
            result = {}
            for key in args:
                value = item.get(key)
                if value is not None:
                    result[key] = value
            if result:
                yield result


goods = [
   {'title': 'Ковер', 'price': 2000, 'color': 'green'},
   {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]
test1 = field(goods, 'title')
for i in test1:
    print(i)

test2 = field(goods, 'title', 'price')
for i in test2:
    print(i)