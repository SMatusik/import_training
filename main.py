from products.complete_order import create_new_order

def run_shop():
    print('Witaj w sklepie')
    product_name = input('Co chcesz zamowic (chleb, mleko, kawa)?')
    quantity = int(input('Ile sztuk?'))

    result = create_new_order(product_name, quantity)

    if result is not None:
        total_price = result['total_price']
        print(f'laczny koszt wyniesie: {total_price}')

if __name__ == '__main__':
    run_shop()