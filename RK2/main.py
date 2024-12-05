from operator import itemgetter

class Detail:
    def __init__(self, id, name, price, id_supplier):
        self.id = id
        self.name = name
        self.price = price
        self.id_supplier = id_supplier

class Supplier:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class DetailSupplier:
    def __init__(self, id_detail, id_supplier):
        self.id_detail = id_detail
        self.id_supplier = id_supplier

def one_to_many(details, suppliers):
    return [(d.name, d.price, s.name)
            for s in suppliers
            for d in details
            if d.id_supplier == s.id]

def many_to_many(details, suppliers, details_suppliers):
    temp = [(s.name, ds.id_supplier, ds.id_detail)
            for s in suppliers
            for ds in details_suppliers
            if s.id == ds.id_supplier]

    return [(d.name, d.price, supplier_name)
            for supplier_name, _, id_detail in temp
            for d in details if d.id == id_detail]

def task1(one_to_many_data):
    return sorted(
        [(name, supplier) for name, _, supplier in one_to_many_data if name.startswith('Т')],
        key=itemgetter(1)
    )

def task2(one_to_many_data, suppliers):
    result = []
    for s in suppliers:
        s_details = list(filter(lambda i: i[2] == s.name, one_to_many_data))
        if s_details:
            min_price = min([price for _, price, _ in s_details])
            result.append((s.name, min_price))
    return sorted(result, key=itemgetter(1))

def task3(many_to_many_data, suppliers):
    result = {}
    for s in suppliers:
        s_details = list(filter(lambda i: i[2] == s.name, many_to_many_data))
        s_details_names = [x for x, _, _ in s_details]
        result[s.name] = sorted(s_details_names)
    return result