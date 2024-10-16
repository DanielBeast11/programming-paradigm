def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) == 1:
            value = item[args[0]]
            if value is not None:
                yield value
        else:
            result = {}
            for key in args:
                value = item[args[key]]
                if value is not None:
                    result[key] = value
            if result:
                yield result
            