import unittest
from webshop import Webshop
from webshop_model import Product, Customer, Order, Products, Customers, Orders

class TestWebshop(unittest.TestCase):

    def setUp(self):
        self.webshop = Webshop()

    def test_add_customer1(self):
        n = self.webshop.get_total_customers()
        assert self.webshop.add_customer(u'test1@example.com',u'test',u'test') != None
        assert self.webshop.get_total_customers() - n == 1

    def test_add_customer2(self):
        n = self.webshop.get_total_customers()
        assert self.webshop.add_customer(u'test1@example.com',u'test',u'test') != None
        assert self.webshop.add_customer(u'test1@example.com',u'test',u'test') == None
        assert self.webshop.get_total_customers() - n == 1

    def test_add_product1(self):
        n = self.webshop.get_total_products()
        assert self.webshop.add_product(u'T-0001', u'test', u'test', 0.99) != None
        assert self.webshop.get_total_products() - n == 1

    def test_add_product2(self):
        n = self.webshop.get_total_products()
        assert self.webshop.add_product(u'T-0001', u'test', u'test', 0.99) != None
        assert self.webshop.add_product(u'T-0001', u'test', u'test', 0.99) == None
        assert self.webshop.get_total_products() - n == 1

    def test_add_order1(self):
        n = self.webshop.get_total_orders()
        customer = self.webshop.add_customer(u'test1@example.com',u'test',u'test')
        product1 = self.webshop.add_product(u'T-0001', u'test1', u'test', 0.99)
        product2 = self.webshop.add_product(u'T-0002', u'test2', u'test', 1.99)
        product3 = self.webshop.add_product(u'T-0003', u'test3', u'test', 2.99)
        order = self.webshop.add_order(u'R-00001', customer, [product1, product2, product3])
        assert order != None
        assert self.webshop.get_total_orders() - n == 1
        assert len(customer.orders) == 1
        assert len(order.products) == 3
        assert order.customer.email == customer.email

    def test_add_order2(self):
        n = self.webshop.get_total_orders()
        customer = self.webshop.add_customer(u'test1@example.com',u'test',u'test')
        product1 = self.webshop.add_product(u'T-0001', u'test1', u'test', 0.99)
        product2 = self.webshop.add_product(u'T-0002', u'test2', u'test', 1.99)
        product3 = self.webshop.add_product(u'T-0003', u'test3', u'test', 2.99)
        assert self.webshop.add_order(u'R-00001', customer, [product1, product2, product3]) != None
        assert self.webshop.add_order(u'R-00001', customer, [product1, product2, product3]) == None
        assert self.webshop.get_total_orders() - n == 1

    def test_delete_customer1(self):
        self.webshop.add_customer(u'test1@example.com',u'test',u'test')
        assert self.webshop.delete_customer(u'test1@example.com') == True
        assert self.webshop.get_total_customers() == 0

    def test_delete_customer2(self):
        self.webshop.add_customer(u'test1@example.com',u'test',u'test')
        assert self.webshop.delete_customer(u'test2@example.com') == False
        assert self.webshop.get_total_customers() == 1

    def test_delete_product1(self):
        self.webshop.add_product(u'T-0001', u'test', u'test', 0.99)
        assert self.webshop.delete_product(u'T-0001') == True
        assert self.webshop.get_total_products() == 0

    def test_delete_product2(self):
        self.webshop.add_product(u'T-0001', u'test', u'test', 0.99)
        assert self.webshop.delete_product(u'T-00002') == False
        assert self.webshop.get_total_products() == 1

    def test_delete_order1(self):
        n = self.webshop.get_total_orders()
        customer = self.webshop.add_customer(u'test1@example.com',u'test',u'test')
        product1 = self.webshop.add_product(u'T-0001', u'test1', u'test', 0.99)
        product2 = self.webshop.add_product(u'T-0002', u'test2', u'test', 1.99)
        product3 = self.webshop.add_product(u'T-0003', u'test3', u'test', 2.99)
        products = Products()
        self.webshop.add_order(u'R-00001', customer, [product1, product2, product3])
        assert self.webshop.delete_order(u'R-00001') == True
        assert self.webshop.get_total_orders() == 0
        assert self.webshop.get_total_customers() == 1
        assert self.webshop.get_total_products() == 3

    def test_delete_order2(self):
        n = self.webshop.get_total_orders()
        customer = self.webshop.add_customer(u'test1@example.com',u'test',u'test')
        product1 = self.webshop.add_product(u'T-0001', u'test1', u'test', 0.99)
        product2 = self.webshop.add_product(u'T-0002', u'test2', u'test', 1.99)
        product3 = self.webshop.add_product(u'T-0003', u'test3', u'test', 2.99)
        self.webshop.add_order(u'R-00001', customer, [product1, product2, product3])
        self.webshop.add_order(u'R-00002', customer, [product1, product1, product2, product3])
        assert self.webshop.delete_order(u'R-00003') == False
        assert self.webshop.get_total_orders() == 2
        assert self.webshop.get_total_customers() == 1
        assert self.webshop.get_total_products() == 3

    def test_get_products_in_price_range(self):
        self.webshop.add_product(u'T-0001', u'test', u'test', 0.99)
        self.webshop.add_product(u'T-0002', u'test', u'test', 1.99)
        self.webshop.add_product(u'T-0003', u'test', u'test', 10.99)
        self.webshop.add_product(u'T-0004', u'test', u'test', 20.99)
        self.webshop.add_product(u'T-0005', u'test', u'test', 40.99)
        self.webshop.add_product(u'T-0006', u'test', u'test', 100.99)
        self.webshop.add_product(u'T-0007', u'test', u'test', 300.99)
        self.webshop.add_product(u'T-0008', u'test', u'test', 500.99)
        assert len(self.webshop.get_products_in_price_range()) == 8
        assert len(self.webshop.get_products_in_price_range(min_price=5)) == 6
        assert len(self.webshop.get_products_in_price_range(min_price=50)) == 3
        assert len(self.webshop.get_products_in_price_range(max_price=50)) == 5
        assert len(self.webshop.get_products_in_price_range(max_price=10)) == 2
        assert len(self.webshop.get_products_in_price_range(min_price=30, max_price=400)) == 3

    def test_get_best_customers(self):
        customer1 = self.webshop.add_customer(u'test1@example.com',u'test1',u'test')
        customer2 = self.webshop.add_customer(u'test2@example.com',u'test2',u'test')
        customer3 = self.webshop.add_customer(u'test3@example.com',u'test3',u'test')
        product1 = self.webshop.add_product(u'T-0001', u'test1', u'test', 0.99)
        product2 = self.webshop.add_product(u'T-0002', u'test2', u'test', 1.99)
        product3 = self.webshop.add_product(u'T-0003', u'test3', u'test', 2.99)
        product4 = self.webshop.add_product(u'T-0004', u'test4', u'test', 20.99)
        product5 = self.webshop.add_product(u'T-0005', u'test5', u'test', 40.99)
        product6 = self.webshop.add_product(u'T-0006', u'test6', u'test', 100.99)
        product7 = self.webshop.add_product(u'T-0007', u'test7', u'test', 300.99)
        product8 = self.webshop.add_product(u'T-0008', u'test8', u'test', 500.99)
        self.webshop.add_order(u'R-00001', customer1, [product1, product2, product1, product2])
        self.webshop.add_order(u'R-00002', customer2, [product1, product5, product1, product2])
        self.webshop.add_order(u'R-00003', customer3, [product1, product2, product1, product2])
        self.webshop.add_order(u'R-00004', customer1, [product8, product2, product1, product2])
        assert self.webshop.get_best_customers()[0].email == u'test1@example.com'

    def test_get_orders_of_customer(self):
        customer = self.webshop.add_customer(u'test1@example.com',u'test',u'test')
        product1 = self.webshop.add_product(u'T-0001', u'test1', u'test', 0.99)
        product2 = self.webshop.add_product(u'T-0002', u'test2', u'test', 1.99)
        product3 = self.webshop.add_product(u'T-0003', u'test3', u'test', 2.99)
        self.webshop.add_order(u'R-00001', customer, [product1, product2, product3])
        self.webshop.add_order(u'R-00002', customer, [product1, product2])
        self.webshop.add_order(u'R-00003', customer, [product2, product3])

        orders = self.webshop.get_orders_of_customer(u'test1@example.com')
        assert len(orders) == 3

        order_codes = map(lambda x:x.order_code, orders)
        order_codes.sort()
        assert order_codes[0] == u'R-00001'
        assert order_codes[1] == u'R-00002'
        assert order_codes[2] == u'R-00003'

    def test_get_customers_who_ordered_product(self):
        customer1 = self.webshop.add_customer(u'test1@example.com',u'test1',u'test1')
        customer2 = self.webshop.add_customer(u'test2@example.com',u'test2',u'test2')
        customer3 = self.webshop.add_customer(u'test3@example.com',u'test3',u'test3')
        product1 = self.webshop.add_product(u'T-0001', u'test1', u'test', 0.99)
        product2 = self.webshop.add_product(u'T-0002', u'test2', u'test', 1.99)
        product3 = self.webshop.add_product(u'T-0003', u'test3', u'test', 2.99)
        self.webshop.add_order(u'R-00001', customer1, [product1, product2, product3])
        self.webshop.add_order(u'R-00002', customer2, [product1, product2])
        self.webshop.add_order(u'R-00003', customer3, [product2, product3])
        customers = self.webshop.get_customers_who_ordered_product(u'T-0001')
        assert len(customers) == 2

        emails = map(lambda x:x.email, customers)
        emails.sort()
        assert emails[0] == u'test1@example.com'
        assert emails[1] == u'test2@example.com'


    def test_get_cheapest_products(self):
        product1 = self.webshop.add_product(u'T-0001', u'test1', u'test', 0.99)
        product2 = self.webshop.add_product(u'T-0002', u'test2', u'test', 1.99)
        product3 = self.webshop.add_product(u'T-0003', u'test3', u'test', 2.99)
        product4 = self.webshop.add_product(u'T-0004', u'test4', u'test', 0.99)
        product5 = self.webshop.add_product(u'T-0005', u'test5', u'test', 40.99)
        product6 = self.webshop.add_product(u'T-0006', u'test6', u'test', 100.99)
        product7 = self.webshop.add_product(u'T-0007', u'test7', u'test', 300.99)
        product8 = self.webshop.add_product(u'T-0008', u'test8', u'test', 500.99)

        products = self.webshop.get_cheapest_products()
        assert len(products) == 2
        for product in products:
            assert product.price_ex_vat == 0.99


    def test_get_most_expensive_products(self):
        product1 = self.webshop.add_product(u'T-0001', u'test1', u'test', 0.99)
        product2 = self.webshop.add_product(u'T-0002', u'test2', u'test', 1.99)
        product3 = self.webshop.add_product(u'T-0003', u'test3', u'test', 2.99)
        product4 = self.webshop.add_product(u'T-0004', u'test4', u'test', 20.99)
        product5 = self.webshop.add_product(u'T-0005', u'test5', u'test', 40.99)
        product6 = self.webshop.add_product(u'T-0006', u'test6', u'test', 200.99)
        product7 = self.webshop.add_product(u'T-0007', u'test7', u'test', 300.99)
        product8 = self.webshop.add_product(u'T-0008', u'test8', u'test', 500.99)

        products = self.webshop.get_most_expensive_products()
        assert len(products) == 1
        for product in products:
            assert product.price_ex_vat == 500.99

    def test_get_top_products(self):
        customer1 = self.webshop.add_customer(u'test1@example.com',u'test1',u'test1')
        customer2 = self.webshop.add_customer(u'test2@example.com',u'test2',u'test2')
        customer3 = self.webshop.add_customer(u'test3@example.com',u'test3',u'test3')
        product1 = self.webshop.add_product(u'T-0001', u'test1', u'test', 0.99)
        product2 = self.webshop.add_product(u'T-0002', u'test2', u'test', 1.99)
        product3 = self.webshop.add_product(u'T-0003', u'test3', u'test', 2.99)
        product4 = self.webshop.add_product(u'T-0004', u'test4', u'test', 20.99)
        product5 = self.webshop.add_product(u'T-0005', u'test5', u'test', 40.99)
        product6 = self.webshop.add_product(u'T-0006', u'test6', u'test', 200.99)
        product7 = self.webshop.add_product(u'T-0007', u'test7', u'test', 300.99)
        product8 = self.webshop.add_product(u'T-0008', u'test8', u'test', 500.99)

        self.webshop.add_order(u'R-00001', customer1, [product1, product2, product3, product4, product7])
        self.webshop.add_order(u'R-00002', customer2, [product1, product2, product8])
        self.webshop.add_order(u'R-00003', customer3, [product2, product3, product5, product8])
        self.webshop.add_order(u'R-00004', customer1, [product2, product3, product4, product7])
        self.webshop.add_order(u'R-00005', customer2, [product1, product2, product7])
        self.webshop.add_order(u'R-00006', customer3, [product2, product4, product5, product8])
        self.webshop.add_order(u'R-00007', customer1, [product1, product2, product3, product4, product5])
        self.webshop.add_order(u'R-00008', customer2, [product1, product2, product8])
        self.webshop.add_order(u'R-00009', customer3, [product2, product3, product5, product8])

        products = self.webshop.get_top_products(4)
        assert len(products) == 4
        skus = map(lambda x:x.sku, products)
        skus.sort()

        assert skus[0] == u'T-0001'
        assert skus[1] == u'T-0002'
        assert skus[2] == u'T-0003'
        assert skus[3] == u'T-0008'

if __name__ == '__main__':
    unittest.main()
