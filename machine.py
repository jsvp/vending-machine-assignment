from products import Products


# Initialize vending machine products
products = Products()


def show_products():
    print('\nCurrently available products:')
    products.show()


def select_product():
    """Ask the customer to select the product he/she wants to buy."""
    id = -1
    while id not in products.get_product_ids() and id != 100:
        try:
            id = int(input('\nPlease, select a product by ID (100 for random choice): '))
        except ValueError:
            print('The id was not valid. Select "0" to see the product list again.')
            continue
        if id == 0:
            show_products()
    if id == 100:
        return products.get_random_product()
    else:
        return products.get_product_by_id(id)

def get_money_inserted(product):
    """Ask the customer to insert money until the sum exceeds tho selected product's price."""
    sum = 0
    print('\nYour product ({}) costs {}€. Please insert cash into the machine until the sum exceeds product cost.'.format(product.name, product.price))
    while sum < product.price:
        try:
            inserted = float(input('- Total sum: {}€. Insert more: '.format(sum)).replace(',', '.'))
            sum += inserted
        except ValueError:
            print('Only numeric values are accepted.')
    return round(sum, 2)

def get_money_returned(inserted_sum, product_price):
    """Calculate the returned change."""
    return round(inserted_sum-product_price, 2)


def transaction():
    """Run the vending machine in a loop, where each iteration stands for a single transaction. """
    while True:
        print('### Welcome to The Vending Machine! ###')
        show_products()

        product = select_product()
        print('You selected the following product:')
        product.show()

        money_inserted = get_money_inserted(product)
        print('You inserted a total of {}€'.format(money_inserted))

        money_returned = get_money_returned(money_inserted, product.price)
        print('You will be returned {}€'.format(money_returned))

        print('\nTransaction completed. Thank you!\n\n\n')


# Start the vending machine
if __name__ == '__main__':
    print('Starting vending machine...\n\n')
    transaction()
