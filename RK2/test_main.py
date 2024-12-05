import unittest
from main import *

class Test(unittest.TestCase):

    def setUp(self):
        self.details = [
            Detail(1, 'Тормозная колодка', 1000, 1),
            Detail(2, 'Свеча зажигания', 4000, 3),
            Detail(4, 'Решетка радиатора', 8000, 2),
            Detail(3, 'Подшипник', 2500, 2),
            Detail(5, 'Топливный бак', 5000, 3),
        ]

        self.suppliers = [
            Supplier(1, 'Автотрейд'),
            Supplier(2, 'Берг'),
            Supplier(3, 'Автопитер')
        ]

        self.details_suppliers = [
            DetailSupplier(1, 1),
            DetailSupplier(2, 3),
            DetailSupplier(4, 2),
            DetailSupplier(3, 2),
            DetailSupplier(5, 3),
        ]

    def test_task1(self):
        one_to_many_data = one_to_many(self.details, self.suppliers)
        result = task1(one_to_many_data)
        expected = [('Топливный бак', 'Автопитер'), ('Тормозная колодка', 'Автотрейд')]
        self.assertEqual(result, expected)

    def test_task2(self):
        one_to_many_data = one_to_many(self.details, self.suppliers)
        result = task2(one_to_many_data, self.suppliers)
        expected = [('Автотрейд', 1000), ('Берг', 2500), ('Автопитер', 4000)]
        self.assertEqual(result, expected)

    def test_task3(self):
        many_to_many_data = many_to_many(self.details, self.suppliers, self.details_suppliers)
        result = task3(many_to_many_data, self.suppliers)
        expected = {
            'Автотрейд': ['Тормозная колодка'],
            'Берг': ['Подшипник', 'Решетка радиатора'],
            'Автопитер': ['Свеча зажигания', 'Топливный бак']
        }
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()