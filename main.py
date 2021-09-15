# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
import models.tax_slabs as models


def tax_slab_object_constructor(tax_slabs_input):
    tax_slabs = models.TaxSlabs()
    for key, val in tax_slabs_input.items():
        tax_slab = models.TaxSlab()
        tax_slab.set_tax_name(key)
        tax_slab.set_tax(val['tax'])
        minPrice = None
        if 'minPrice' in val:
            minPrice = val['minPrice']

        maxPrice = None
        if 'maxPrice' in val:
            maxPrice = val['maxPrice']
        tax_slab.set_range(minPrice, maxPrice)
        tax_slab.set_type(val['type'])
        tax_slabs.add_tax(tax_slab)
    return tax_slabs


def main():
    with open('resources/input_tax_slabs.json') as fp:
        tax_slabs_input = json.load(fp)

    tax_slabs = tax_slab_object_constructor(tax_slabs_input)

    with open('resources/input_products.json') as fp:
        products = json.load(fp)

    final_products_price = []
    for product in products:
        tax_amount = tax_slabs.calculate_total_taxes(product['basePrice'])
        if 'discount' in product:
            tax_amount = tax_amount - (product['discount'] * product['basePrice']) / 100
        final_prod = {
            'item': product['item'],
            'basePrice': product['basePrice'],
            'finalPrice': product['basePrice'] + tax_amount
        }
        final_products_price.append(final_prod)

    print(final_products_price)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
