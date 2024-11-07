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

details = [
    Detail(1, 'Тормозная колодка', 1000, 1),
    Detail(2, 'Свеча зажигания', 4000, 3),
    Detail(4, 'Решетка радиатора', 8000, 2),
    Detail(3, 'Подшипник', 2500, 2),
    Detail(5, 'Топливный бак', 5000, 3),
]

suppliers = [
    Supplier(1, 'Автотрейд'),
    Supplier(2, 'Берг'),
    Supplier(3, 'Автопитер')
]

details_suppliers = [
    DetailSupplier(1, 1),
    DetailSupplier(2, 3),
    DetailSupplier(4, 2),
    DetailSupplier(3, 2),
    DetailSupplier(5, 3),
]

def main():
    one_to_many = [(d.name, d.price, s.name)
        for s in suppliers
        for d in details
        if d.id_supplier == s.id
    ]

    many_to_many_temp = [(s.name, ds.id_supplier, ds.id_detail)
        for s in suppliers
        for ds in details_suppliers
        if s.id == ds.id_supplier
    ]

    many_to_many = [(d.name, d.price, supplier_name)
        for supplier_name, id_supplier, id_detail in many_to_many_temp
        for d in details if d.id == id_detail
    ]

    print('Задание В1')
    res_11 = sorted(
        [(name, supplier) for name, _, supplier in one_to_many if name.startswith('Т')],
        key=itemgetter(1)
    )
    print(res_11)

    print('\nЗадание В2')
    res_12_unsorted = []
    for s in suppliers:
        s_details = list(filter(lambda i: i[2] == s.name, one_to_many))
        if s_details:
            min_price = min([price for _, price, _ in s_details])
            res_12_unsorted.append((s.name, min_price))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1))
    print (res_12)

    print('\nЗадание В3')
    res_13 = {}
    for s in suppliers:
        s_details = list(filter(lambda i: i[2] == s.name, many_to_many))
        s_details_names = [x for x, _, _ in s_details]
        res_13[s.name] = sorted(s_details_names)
    print (res_13)

if __name__ == '__main__':
    main()