import unittest
from project.tests.AT_tests.test_env.Driver import Driver
from project.tests.AT_tests import ATsetUP
import jsonpickle

class purchase_products_by_purchase_types(unittest.TestCase):
    def setUp(self):
        self.service = Driver.make_bridge()
        ATsetUP.setup(self.service)
        res = jsonpickle.decode(self.service.searchProduct("Banana"))
        first_store_id = list(res)[0]
        self.service.add_product(first_store_id, jsonpickle.encode(res.get(first_store_id)[0]), 2)
        self.service.buy()

    def test_buy_by_type_purchase_happy(self):
        result = jsonpickle.decode(self.service.get_purchase_history())
        self.assertEqual(list(result[0].products)[0], "Banana")

    def test_buy_by_type_purchase_sad(self):
        result = jsonpickle.decode(self.service.get_purchase_history())
        self.assertNotIn("apple", result[0].products.keys())

    def test_buy_by_type_purchase_bad(self):
        result = jsonpickle.decode(self.service.get_purchase_history())
        self.service.logout()
        self.assertIn("Banana", result[0].products.keys())



if __name__ == '__main__':
    unittest.main()
