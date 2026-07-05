products = ["Python Base", "Django MVP", "Asyncio Advanced", "PostgreSQL Admin"]
prices = [15000, 30000, 45000, 25000]

def lst_zip(x, y):

    mid_prices = sum(y)/len(y)

    lst = list(zip(x, y))
    result = dict(filter(lambda item: item[1] < mid_prices, lst))
    for product, price in result.items():
        print(f"Курс: {product}, Цена: {price}")

lst_zip(products,prices)