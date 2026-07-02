lst_in = ['смартфон:120000',
          'яблоко:2',
          'сумка:560',
          'брюки:2500',
          'линейка:10',
          'бумага:500']

lst_dict = {int(idx): val for item in lst_in for val, idx in [item.split(":")]}

def srtd_dict(d):
    result = [d[k] for k in sorted(d)]
    return result[:3]


print(*srtd_dict(lst_dict))