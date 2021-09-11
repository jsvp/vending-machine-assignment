import csv
import random


class Products:

    def __init__(self):
        self.products = []
        self.read_products()

    def read_products(self):
        """Read available products from file"""
        with open('products.csv', newline='') as f:
            for row in csv.DictReader(f, delimiter='|'):
                p = Product(
                    row['id'],
                    row['name'],
                    row['price'],
                    row['description'],
                )
                self.products.append(p)
        print('{} products initialized.'.format(len(self.products)))

    def show(self):
        for p in self.products:
            p.show()

    def get_product_ids(self):
        return [p.id for p in self.products]
    
    def get_product_by_id(self, id):
        return next((p for p in self.products if p.id == id), None)

    def get_product_by_name(self, name):
        return next((p for p in self.products if p.name == name), None)
        
    def get_random_product(self):
        return self.products[random.randint(0, len(self.products)-1)]



class Product:

    def __init__(self, id, name, price, description=''):
        self.id = int(id)
        self.name = name
        self.price = round(float(price), 2)
        self.description = description or '<No description>'

    def show(self, return_string=False):
        msg = '{id} \t {name:<10s} \t {price} \t {desc}'.format(id=self.id, name=self.name, price=self.price, desc=self.description)
        if return_string:
            return msg
        else:
            print(msg)


if __name__ == '__main__':
    products = Products()
    
    print('\nCurrent available products:')
    products.show()

    print('\nProduct by id:')
    products.get_product_by_id(2).show()

    print('\nProduct by id:')
    products.get_product_by_name('Fanta').show()

    print('\nRandom product:')
    products.get_random_product().show()