products = {
    "chleb": {
        'name': 'chleb',
        'price': 3,
        'quantity': 100
    },
    "mleko": {
        'name': 'mleko',
        'price': 2,
        'quantity': 50
    },
    "kawa": {
        'name': 'kawa',
        'price': 25,
        'quantity': 10
    }
}

def update_product_quantity(product_name, ordered_quantity):
    products[product_name]["quantity"] -= ordered_quantity
    quantity = products[product_name]["quantity"]
    print(f'Zostalo {quantity} sztuk')