lst_in = ['зонт=1000',
          'палатка=10000',
          'спички=22',
          'котелок=543']

products = {}
for item in lst_in:
    name, price_str = item.split('=')
    products[name.strip()] = int(price_str.strip())

fltr = filter(lambda x: x[1] > 500, products.items())
expensive_products = dict(fltr)

print(*list(expensive_products.keys()))