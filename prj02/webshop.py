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
        pass
        
    def get_total_products(self):
        """ Return total number of products
        
        @rtype: integer
        """
        pass

    def get_total_orders(self):
        """ Return total number of orders
        
        @rtype: integer
        """
        pass

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
        pass

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
        pass

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
        pass
        
    def delete_customer(self, email):
        """ Delete the customer who has the given email
        Return True if successes otherwise False
        
        @param email: email address
        @type email: unicode string
        
        @rtype: boolean
        """
        pass
            
    def delete_product(self, sku):
        """ Delete the product which has the given sku
        Return True if successes otherwise False

        @param sku: SKU
        @type sku: unicode string
        
        @rtype: boolean
        """
        pass
        
    def delete_order(self, order_code):
        """ Delete the order which has the given order_code
        Return True if successes otherwise False

        @param order_code: unique code of each product
        @type order: unicode string
        
        @rtype: boolean        
        """
        pass

    def get_products_in_price_range(self, min_price=None, max_price=None):
        """ Get products in the given range of price

        @rtype: list of Product
        """
        pass

    def get_best_customers(self):
        """ Return customers that have highest total price of orders

        @rtype: list of Customer
        """
        pass

    def get_orders_of_customer(self, email):
        """ Get orders of the given customer
        
        @param email: email address
        @type email: unicode string

        @rtype: list of Order
        """
        pass
        
    def get_customers_who_ordered_product(self, sku):
        """ Get customers who ordered the given product
        
        @param sku: SKU
        @type sku: unicode string
        
        @rtype: list of Customer
        """        
        pass
        
    def get_cheapest_products(self):
        """ Return the cheapest products in the shop
        
        @rtype: list of Product
        """
        pass
        
    def get_most_expensive_products(self):
        """ Return the most expensive products in the shop
        
        @rtype: list of Product
        """
        pass
        
    def get_top_products(self, n):        
        """ Return n products that is ordered highest
        
        @param n: number of products
        @type n: integer
        
        @rtype: list of Product
        """        
        pass
        
    