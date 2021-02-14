from .products_info import products, update_product_quantity

orders = [
    {
        'product': 'chleb',
        'ordered_quantity': 25,
        'total_price': 75
    }
]

def create_new_order(product_name, ordered_quantity):
    available_quantity = products[product_name]["quantity"]

    if ordered_quantity > available_quantity:
        print(f'Brak takiej ilości towaru w sklepie. Maksymalnie możesz zamówić {available_quantity}')
        return None

    price = products[product_name]['price']
    total_price = price * ordered_quantity

    new_order = {
        'product': product_name,
        'ordered_quantity': ordered_quantity,
        'total_price': total_price
    }
    update_product_quantity(product_name, ordered_quantity)
    orders.append(new_order)

    return new_order