# request = {'url': 'https://proproprogs.ru/', 'method': 'GET', 'timeout': 1000}
#
# match request:
#     case {'url': url, 'method': method}:
#         print(f"Запрос: url: {url}, method: {method}")
#     case _:
#         print('Неверный запрос')
from datetime import date


# primary_keys = {1, 2, 3}
#
# match primary_keys:
#     case set(keys):
#         print(f"primary_keys: {keys}")


# def parse_json(data):
#     match data:
#         case {'access': bool(access), 'data': [date, *_]}:
#             return (access, date)
#
#         case {'id': ids, 'data': [_, {'login': login}, _, _]}:
#             return ids, login
#
#     return None
#
#
# json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}
#
# print(parse_json(json_data))


def parse_json(data):
    match data:
        case {'access': True, 'data': [_, {'login': str(login), 'email': str(email)}, *_]}:
            return login, email

    return None


json_data = {'id': 2, 'access': True, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}
print(parse_json(json_data))