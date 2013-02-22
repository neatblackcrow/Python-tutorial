class Customer(object):

    def __init__(self, email, firstname, lastname):
        self.email = email
        self.first_name = firstname
        self.last_name = lastname
        self.orders = []

    def add_order(self, order):
        self.orders += [order]

class Product(object):

    def __init__(self, sku, name, description, price_ex_vat):
        self.sku = sku
        self.name = name
        self.description = description
        self.price_ex_vat = price_ex_vat

class Order(object):

    def __init__(self, order_code, customer, products):
        self.order_code = order_code
        self.customer = customer
        self.products = products

class CustomCollector(dict):

    def __init__(self):
        super(CustomCollector, self).__init__()

    def add(self, key, value):
        super(CustomCollector, self).__setitem__(key, value)

    def remove(self, key):
        super(CustomCollector, self).__delitem__(key)

    def update(self, key, value):
        super(CustomCollector, self).update({key: value})

class Customers(CustomCollector):

    pass

class Products(CustomCollector):

    def get_products_from_price(self, price):
        result = []
        for product in self.values():
            if product.price_ex_vat == price:
                result.append(product)
        return result

    def get_product_prices(self):
        return [product.price_ex_vat for product in self.values()]

class Orders(CustomCollector):

    def get_products_from_order(self, order):
        return [product for product in self[order.order_code].products]

    def total_prices_from_order(self, order):
        result = 0
        for product in self[order.order_code].products:
            result += product.price_ex_vat
        return result
