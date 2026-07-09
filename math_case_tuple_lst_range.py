# t = (int, str, str, float, int)
# book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]
# match book:
#     case [str(author), str(title)]:
#         print('Yes')
#     case [_,str(author), str(title), float(price)]:
#         print('Yes')
#     case [_,str(author), str(title), float(price), int(year), *_]:
#         print('Yes')
#     case _:
#         print('No')


t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

match book:
    case [_, autor, title] if len(autor) >= 6 and len(title) >= 10:
        print('Yes')
    case [_, autor, title, price] if len(autor) >= 6 and price > 0:
        print('Yes')
    case [_, autor, title, year] if year >= 2020:
        print('Yes')
    case [_, autor, title, price, year] if year >= 2020 and price > 0:
        print('Yes')
    case _:
        print('No')