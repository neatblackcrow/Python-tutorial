#ID:5510405791
#Name:Voravut Nateluercha

from webshop_model import Customer, Product, Order, Customers, Products, Orders

class Webshop:

    def __init__(self):
        self.customers = Customers()
        self.products = Products()
        self.orders = Orders()

    def get_total_customers(self):
        """ Return total number of customers

        @rtype: integer
        """
        return len(self.customers)

    def get_total_products(self):
        """ Return total number of products

        @rtype: integer
        """
        return len(self.products)

    def get_total_orders(self):
        """ Return total number of orders

        @rtype: integer
        """
        return len(self.orders)

    def add_customer(self, email, first_name, last_name):
        """ Add new customer if he/she does not exist (identified by email)
        Return the new customer if successes otherwise None

        @param email: email address
        @type email: unicode string
        @param first_name: first name
        @type first_name: unicode string
        @param last_name: last name
        @type last_name: unicode string

        @rtype: Customer
        """
        if email not in self.customers:
            self.customers.add(email, Customer(email, first_name, last_name))
            return Customer(email, first_name, last_name)
        else:
            return None

    def add_product(self, sku, name, description, price_ex_vat):
        """ Add new product if it does not exist (identified by sku)
        Return the new product if successes otherwise None

        @param sku: SKU
        @type sku: unicode string
        @param name: name
        @type name: unicode string
        @param description: description
        @type description: unicode string
        @param price_ex_vat: price excluding vat
        @type price_ex_vat: float

        @rtype: Product
        """
        if sku not in self.products:
            self.products.add(sku, Product(sku, name, description, price_ex_vat))
            return  Product(sku,name ,description ,price_ex_vat)
        else:
            return None

    def add_order(self, order_code, customer, products):
        """ Add new order if it does not exist (identified by order_code)
        Return the new order if successes otherwise None

        @param order_code: unique code of each product
        @type order_code: unicode string
        @param customer: customer
        @type customer: Customer
        @param products: products
        @type products: list of Product

        @rtype: Order
        """
        if order_code not in self.orders:
            customer.add_order(Order(order_code, customer, products))
            self.customers[customer.email].add_order(Order(order_code, customer, products))
            self.orders.add(order_code, Order(order_code, customer, products))
            return Order(order_code, customer, products)
        else:
            return None

    def delete_customer(self, email):
        """ Delete the customer who has the given email
        Return True if successes otherwise False

        @param email: email address
        @type email: unicode string

        @rtype: boolean
        """
        if email in self.customers:
            self.customers.remove(email)
            return True
        else:
            return False

    def delete_product(self, sku):
        """ Delete the product which has the given sku
        Return True if successes otherwise False

        @param sku: SKU
        @type sku: unicode string

        @rtype: boolean
        """
        if sku in self.products:
            self.products.remove(sku)
            return True
        else:
            return False

    def delete_order(self, order_code):
        """ Delete the order which has the given order_code
        Return True if successes otherwise False

        @param order_code: unique code of each product
        @type order: unicode string

        @rtype: boolean
        """
        if order_code in self.orders:
            self.orders.remove(order_code)
            return True
        else:
            return False

    def get_products_in_price_range(self, min_price=None, max_price=None):
        """ Get products in the given range of price

        @rtype: list of Product
        """
        result = []
        if max_price == None:
            max_price = max(self.products.get_product_prices())
        for product in self.products.values():
            if (min_price <= product.price_ex_vat <= max_price):
                result.append(product)
        return result

    def get_best_customers(self):
        """ Return customers that have highest total price of orders

        @rtype: list of Customer
        """
        result = []
        temp_dict = {}
        for customer in self.customers.values():
            for order in customer.orders:
                if customer.email not in temp_dict.keys():
                    temp_dict[customer.email] = self.orders.total_prices_from_order(order)
                else:
                    temp_dict[customer.email] += self.orders.total_prices_from_order(order)
        max_value = max([price for price in temp_dict.values()])
        for email, price_count in temp_dict.items():
            if price_count == max_value:
                result.append(self.customers[email])
        return result

    def get_orders_of_customer(self, email):
        """ Get orders of the given customer

        @param email: email address
        @type email: unicode string

        @rtype: list of Order
        """
        return self.customers[email].orders

    def get_customers_who_ordered_product(self, sku):
        """ Get customers who ordered the given product

        @param sku: SKU
        @type sku: unicode string

        @rtype: list of Customer
        """
        result = []
        for order in self.orders.values():
            for product in order.products:
                if product.sku == sku:
                    result.append(order.customer)
        return result

    def get_cheapest_products(self):
        """ Return the cheapest products in the shop

        @rtype: list of Product
        """
        min_price = min(self.products.get_product_prices())
        min_price_product = self.products.get_products_from_price(min_price)
        return min_price_product

    def get_most_expensive_products(self):
        """ Return the most expensive products in the shop

        @rtype: list of Product
        """
        max_price = max(self.products.get_product_prices())
        max_price_product = self.products.get_products_from_price(max_price)
        return max_price_product

    def get_top_products(self, n):
        """ Return products that is ordered highest

        @param n: number of products
        @type n: integer

        @rtype: list of Product
        """
        temp_dict = {}
        result = []
        for order in self.orders.values():
            for product in self.orders.get_products_from_order(order):
                if product.sku not in temp_dict:
                    temp_dict[product.sku] = 1
                else:
                    temp_dict[product.sku] += 1
        i = 1
        while i <= n:
            max_value = max([item for item in temp_dict.values()])
            for key, value in temp_dict.items():
                if value == max_value:
                    result.append(self.products[key])
                    del temp_dict[key]
                    i += 1
        return result
