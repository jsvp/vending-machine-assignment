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
            id = int(input('\nPlease, select a product by ID (100 for random choice, 99 to cancel transaction): '))
        except ValueError:
            print('The id was not valid. Select "0" to see the product list again.')
            continue
        if id == 0:
            show_products()
        elif id == 99:
            return None
    if id == 100:
        return products.get_random_product()
    else:
        return products.get_product_by_id(id)

def get_money_inserted(product):
    """Ask the customer to insert money until the sum exceeds tho selected product's price."""
    sum = 0
    print('\nYour product ({}) costs {}€. Please insert cash into the machine until the sum exceeds product cost. To cancel transaction, insert a negative value.'.format(product.name, product.price))
    while sum < product.price:
        try:
            inserted = float(input('- Total sum: {}€. Insert more: '.format(sum)).replace(',', '.'))
            # If negative value, return current sum to indicate that the customer want's to cancel transaction.
            if inserted < 0:
                return sum
            sum += inserted
        except ValueError:
            print('Only numeric values are accepted.')
    return round(sum, 2)

def get_money_returned(inserted_sum, product_price):
    """Calculate the returned change."""
    return round(inserted_sum-product_price, 2)


def main():
    """Run the vending machine in a loop where each iteration stands for a single transaction."""
    while True:
        print('### Welcome to The Vending Machine! ###')
        show_products()

        product = select_product()
        if product is None:
            print('\nTransaction canceled.\n\n\n')
            continue

        # Continue by asking customer to insert money
        print('You selected the following product:')
        product.show()

        money_inserted = get_money_inserted(product)
        if money_inserted < product.price:
            print('\nTransaction canceled. The inserted money ({}€) is returned.\n\n\n'.format(money_inserted))
            continue

        # Continue and finish the transaction by returning the change.
        print('You inserted a total of {}€'.format(money_inserted))

        money_returned = get_money_returned(money_inserted, product.price)
        print('You will be returned {}€'.format(money_returned))

        print('\nTransaction completed. Thank you!\n\n\n')


# Start the vending machine
if __name__ == '__main__':
    print('Starting vending machine...\n\n')
    main()
