# n = input().split()
#
#
# lst_abs = [ [n[i], int(n[i+1])] for i in range(0, len(n), 2) ]
#
# print(lst_abs)
# print('\n'.join(['*' * (i + 1) for i in range(N)]))
# from this import d


# 1 a = [(i,j) for i in range(3) for j in range(4)]
# print(a)
#
# 2 matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# a = [y
#      for x in matrix
#      for y in x]
#
# print(a)


# M, N = 3, 4
#
# matrix = [[a for a in range(M)] for b in range(N)]
#
# print(matrix)


# A = [[1,2,3],[4,5,6],[7,8,9]]
#
# A = [ [ x**2 for x in row] for row in A ]
#
# print(A)

# A = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
#
# A = [[row [i] for row in A] for i in range(len(A[0]))]
#
# print(A)


# g = [u**2 for u in [x + 1 for x in range(5)]]
# print(g)


# N = int(input())
#
# N = [' '.join('1' if i == j else '0' for j in range(N)) for i in range(N)]
# N = '\n'.join(N)
# print(N)

# List = [[1,2,4],[5,6,7],[8,9,10],[1,2,3]]
#
# N = [' '.join(map(str, j[::-1])) for j in List[::-1]]
#
# print(*N)

# N = list(map(int, input().split()))
# n = int(len(N) ** 0.5)
# lst = [N[i:i+n] for i in range(0, len(N), n)]
#
# print(lst)


# t = ["– Скажи-ка, дядя, ведь не даром",
#      "Я Python выучил с каналом",
#      "Балакирев что раздавал?",
#      "Ведь были ж заданья боевые,",
#      "Да, говорят, еще какие!",
#      "Недаром помнит вся Россия",
#      "Как мы рубили их тогда!"
#      ]
#
# lst = [[j for j in i.split() if len(j) > 3] for i in t]
#
# print(lst)


# lst_in = [[10,20,30],[40,50,60],[7,80,9]]
#
# A = [[j[i] for j in lst_in] for i in range(len(lst_in[0]))]
#
# for row in A:
#     print(*row)
#

# d[[True]] = 'истина'


# D = input().split()
#
# d = [[int(i.split('=')[0]), i.split('=')[1]]for i in D]
# d = dict(d)
# print(*sorted(d.items()))


# D = input().split()
# d = {}
# for item in D:
#     if '=' in item:
#         key, value = item.split('=', 1)
#         d[key] = value
#
# required = {'house', 'True', '5'}
# if required.issubset(d.keys()):
#     print('ДА')
# else:
#     print('НЕТ')


# Задача Эйлера 1:

# d = [i for i in range(1000) if i%5 == 0 or i%3==0]
# s = 0
# for i in d:
#     s+=i
# print(s)

# Задача Эйлера 2:


# a, b = 1, 2
# fib_list = []
#
# while a <= 4000000:
#     fib_list.append(a)
#     a, b = b, a + b
# fib_list = [i for i in fib_list if i%2==0]
#
# s = 0
#
# for i in fib_list:
#     s = s + i
#
# print(s)


# D = input().split()
#
# d = [[i.split('=')[0], i.split('=')[1]] for i in D]
# d = dict(d)
# while 'False' in d:
#     d.pop('False')
# while '3' in d:
#     d.pop('3')
# print(*sorted(d.items()))


#
# A = input()
# B = input()
# C = input()
# D = input()
# print(f"{B}{A}{C}{A}{D}")


# import sys
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# d = {}
#
# for line in lst_in:
#     if not line:
#         continue
#     phone, name = line.rsplit(' ',1)
#     if name in d:
#         d[name].append(phone)
#     else:
#         d[name] = [phone]
#
# print(*sorted(d.items()))


# temperatures = [23, 19, 25, 21]
#
#
# for i in temperatures:
#     if i > 20:
#         print(f"Сегодня {i} градусов, тепло")
#     else:
#         print(f"Сегодня {i} градусов, прохладно")
# print("Погода переменчива!")


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:       # каждый row — это список (строка)
#     for item in row:     # перебираем элементы внутри строки
#         print(item, end=' ')
#     print()  # переход на новую строку


#
# new_lst = [i for i in range(1,20) if i % 2 == 0 and i % 3 == 0]
# print(new_lst)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# new_matrix = [[j[i] for j in matrix] for i in range(len(matrix))]
#
#
# print(new_matrix)


# m = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f'],
#     ['g', 'h', 'i']
# ]
#
# print(m[1][2], m[2], m[0][1],m[-1][-1], sep='\n')


# cache = {}
#
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     else:
#         if n in cache:
#             print(f'значение из кэша: {cache[n]:.2f}')
#         else:
#             sqrt_n = n**0.5
#             cache[n] = sqrt_n
#             print(round(sqrt_n, 2))


# lst_in = [
#     "ustanovka-i-zapusk-yazyka",
#     "ustanovka-i-poryadok-raboty-pycharm",
#     "peremennyye-operator-prisvaivaniya-tipy-dannykh",
#     "arifmeticheskiye-operatsii",
#     "ustanovka-i-poryadok-raboty-pycharm"
# ]
#
# cache = {}
#
# for url in lst_in:
#     if url not in cache:
#         page = f"HTML-страница для адреса {url}"
#         print(page)
#         cache[url] = page
#     else:
#         cached_page = cache[url]
#         print(f"Взято из кэша: {cached_page}")


# lst = ['+6','+7','+5','+4']
#
# a = dict.fromkeys(lst, 'Код страны')
# print(a)


# char =  {".-": "а", "-...": "б", ".--": "в", "--.": "г", "-..": "д", ".": "е", "...-": "ж", "--..": "з", "..": "и", ".---": "й", "-.-": "к", ".-..": "л", "--": "м", "-.": "н", "---": "о", ".--.": "п", ".-.": "р", "...": "с", "-": "т", "..-": "у", "..-.": "ф", "....": "х", "-.-.": "ц", "---.": "ч", "----": "ш", "--.-": "щ", ".--.-": "ъ", "-.--": "ы", "-..-": "ь", "...-...": "э", "..--": "ю", ".-.-": "я", "-...-": " "}
#
# words = input().split()
#
# codes = []
# for word in words:
#     if word in char:
#         codes.append(char[word])
# print(*codes, sep='')


# s = list(map(int, input().split()))
#
# codes = []
# for i in s:
#     if i in codes:
#         continue
#     else:
#         codes.append(i)
#
# print(*codes)


# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
#
#
# wt = int (input()) * 1000
# wha = []
# things_sorted = dict(sorted(things.items(), key=lambda item: item[1], reverse=True))
# for i in things_sorted:
#     if things_sorted[i] > wt:
#         continue
#     else:
#         wha.append(i)
#         wt -= things_sorted[i]
# print(*wha)


# a = int(input())
# b = int(input())
#
# print(3 * ((a + b) * (a + b) * (a + b))  + 275 * (b * b) - 127 * a - 41 )


# Следующее за числом <текущее число> число: <следующее число>
# Для числа <текущее число> предыдущее число: <предыдущее число>

# a = int(input())
# b = int(input())
# c = int(input())
#
# print(a+b*(c-1))


# x = int(input())
# print(*[x * i for i in range(1,6)], sep='---')

# a = 82 // 3**2 % 7
# print(a)


# b1 = int(input())
# q = int(input())
# n = int(input())
#
# print(b1 * q**(n - 1))

# a = int(input())
# print(a // 100)

#
# a = int(input())
# b = int(input())
#
# print(b//a)
# print(b%a)


# a = int(input())
#
# print (int((a+2-1)/2))

# a = int(input())
#
# print(f"{a} мин - это {a//60} час {a%60} минут.")


# a = int(input())
# print(f'Сумма цифр = {a//100+ (a // 10) % 10 + a%10}\nПроизведение цифр = {(a//100) * ((a // 10) % 10) * (a%10)}')


# a = int(input())
# print(f'{a//100}{(a // 10) % 10}{a%10}\n{a//100}{a%10}{(a // 10) % 10}\n{(a // 10) % 10}{a//100}{a%10}\n{(a // 10) % 10}{a%10}{a//100}\n{a%10}{a//100}{(a // 10) % 10}\n{a%10}{(a // 10) % 10}{a//100}')


# a = int(input())
#
# print(f'Цифра в позиции тысяч равна {a//1000}\nЦифра в позиции сотен равна {(a//100)%10}\nЦифра в позиции десятков равна {(a//10)%10}\nЦифра в позиции единиц равна {a%10}')


# print("Told you not to worry", "But maybe that's a lie", sep=' :) ')
#
#
#
# print("The world's a little blurry", "Or maybe it's my eyes", end='!!!', sep=' :) ')
#
# print("Honey, what's your hurry", end='?')


#
# _a3 = input()
# print(_a3)


# s = 13
# k = -5
# d = s + 2
# s = d
# k = 2 * s
# print(s + k + d)


# a = 17 // (23 % 7)
# b = 34 % a * 5 - 29 % 4 * 3
# print(a * b)


# a = '*'
#
# print(f"{a*17}\n{a}{' '*15}{a}\n{a}{' '*15}{a}\n{a*17}")


# a = int(input())
# b = int(input())
#
# print(f"Квадрат суммы {a} и {b} равен {(a + b)**2}\nСумма квадратов {a} и {b} равна {a**2 + b**2}")


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# print(a**b + c**d)


# n = int(input())
# if 1 <= n <= 9:
#     print(n + (10 * n + n)+(100 * n + 10 * n + n))


# t = tuple(input())
# print(t)


# a = {'это': 'тоже кортеж'}
#
# print(a)


# t = (3.4, -56.7)
# t += tuple(map(int, input().split()))
#
# print(t)


# city = list(map(str, input().split()))
# moscow = "Ульяновск"
#
# if moscow in city:
#     city.remove(moscow)
#     city = tuple(city)
#     print(*city)
# else:
#     city = tuple(city)
#     print(*city)


# students = list(map(str.lower, input().split()))
# result = list()
#
# for name in students:
#     if 'ва' in name:
#         result.append(name)
# result = tuple(result)
# print(*result)


# lst = list(map(int, input().split()))
# lst_nw = tuple()
#
# for i, v in enumerate(lst):
#     cnt = lst.count(v)
#     if cnt > 1:
#         lst_nw = lst_nw + (i,)
#
# print(*lst_nw)


# t = ((1, 0, 0, 0, 0),
#      (0, 1, 0, 0, 0),
#      (0, 0, 1, 0, 0),
#      (0, 0, 0, 1, 0),
#      (0, 0, 0, 0, 1))
# N = int(input())
# t2 = [' '.join('1' if i == j else '0' for j in range(N)) for i in range(N)]
# t2 = '\n'.join(t2)
# print(t2)


# import sys
#
# from forEducational import result

# считывание списка из входного потока
# lst_in = [
#     "Главная home",
#     "Python learn-python",
#     "Java learn-java",
#     "PHP learn-php"
# ]
#
# menu = tuple(tuple(item.split()) for item in lst_in)
#
# print(menu)


# s = set(map(float, input().split()))
#
# print(*sorted(s))


# print(len(set(input().lower().split())))


# st = set()
# for i in input():
#     if i.isdigit():
#         st.add(int(i))
#
#
# if len(st) == 0:
#     print('НЕТ')
# else:
#     print(*sorted(st))


# import sys
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# b = set(lst_in)
#
# print(len(b))


# lst_in = ["EvgeniyK: спасибо большое!", "LinaTroshka: лайк и подписка!", "Sergey Karandeev: крутое видео!", "Евгений Соснин: обожаю", "EvgeniyK: это повтор?", "Sergey Karandeev: нет, это новое видео"]
# st = set()
# for i in lst_in:
#     parts = i.split(':',1)
#     st.add(parts[0])
# print(len(st))

# cities = set()
#
# while True:
#     city = input()
#     if city == 'q':
#         break
#     cities.add(city)
#
# print(len(cities))


# language = 'Русский'
#
# if language != 'English' != 'Español':
#     print('Язык по умолчанию не является ни английским, ни испанским')
#
# if language != 'English' != 'Русский':
#     print('Язык по умолчанию не является ни английским, ни русским')


# setA = {1,2,3,4}
# setB = {3,4,5,6,7}
# res = setA & setB
# res2 = setA | setB
# print(res, res2, sep='\n')


# setA = set(map(int, input().split()))
# setB = set(map(int, input().split()))
#
# print(*sorted(setA.intersection(setB)))

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
#
# diff = num2 - num1
#
# if num2 == num1 + diff and num3 == num2 + diff:
#     print('YES')
# else:
#     print('NO')


# num = input()
#
# if int(num[0]) + int(num[3]) == int(num[1]) - int(num[2]):
#     print('ДА')
# else:
#     print('НЕТ')


# num1, num2, num3 = int(input()), int(input()), int(input())
# ct = 0
#
# for i in (num1, num2, num3):
#     if i >= 0:
#         ct += i
# print(ct)


# age = int(input())
#
# if age <= 13:
#     print('детство')
# elif 14 <= age <= 24:
#     print('молодость')
# elif 25 <= age <= 59:
#     print('зрелость')
# elif 60 <= age:
#     print('старость')


# print(min(int(input()) for _ in range(4)))


# setA = set(input().split())
# setB = set(input().split())
#
# if setA == setB:
#     print("ДА")
# else:
#     print("НЕТ")


# grade = set(map(int, input().split()))
#
# if  2 in grade:
#     print('НЕ ДОПУЩЕН')
# else:
#     print('ДОПУЩЕН')


# cites1 = set(map(str, input().split()))
# cites2 = set(map(str, input().split()))
#
# if cites2 & cites1 == cites1:
#     print("ДА")
# else:
#     print("НЕТ")


# num = int(input())
#
# st1 = set()
# i = 2
# while num > 1:
#     while num % i == 0:
#         st1.add(i)
#         num //= i
#     i += 1
#
# if 2 in st1 and 3 in st1 and 5 in st1:
#     print('ДА')
# else:
#     print('НЕТ')


# m = {'неудовл.': 2, 'удовл.': 3, 'хорошо': '4', 'отлично': '5' }
# n = {int(y): x.upper() for x, y in m.items()}
#
# print(n)


# grade = input().split()
#
# out_gr = {i: word for i, word in enumerate(grade[1:], int(grade[0]))}
#
# print(out_gr[4])


#
# lst = ["Е220СК", "А120МВ", "В101АА", "Е220СК", "А120МВ"]
#
# a = {x for x in lst}
# print(len(a))


# lst = input().split()
# lst_out = {i.lower() for i in lst if len(i) >= 3}
#
# print(len(lst_out))

#
# lst = input().split().lower()
#
# a = {i: lst.count(i) for i in lst}
#
# print(a.get('и',0))


# lst_in = [
#     "Пушкин: Сказка о рыбаке и рыбке",
#     "Есенин: Письмо к женщине",
#     "Тургенев: Муму",
#     "Пушкин: Евгений Онегин",
#     "Есенин: Русь"
# ]
#
# d = {}
# for item in lst_in:
#     author, title = item.split(': ', 1)
#     if author not in d:
#         d[author] = set()
#     d[author].add(title)
# print(d)


# d = {}
# val = d.setdefault('a', 0)   # val = 0, d = {'a': 0}
# val = d.setdefault('b', 100) # val = 0 (потому что ключ уже есть)
# print(d)


# lst = [
#     row1 := [1, 2, 3],
#     row2 := [-1, 12, -13],
#     row3 := [7, 8, 2],
# ]
#
# row1, row3 = row3, row1
#
# print(lst)


# lst_in = [[4,3,2,-1],[-1,-1,-2,-3]]
#
# res = [m for n in lst_in for m in n if m < 0]
#
# print(*res)


# t = (4, 3, -1, 10, 9, 3)
#
# s = 0
# lst = [s := s + x for x in t]
# print(*lst)


# s = 0
# while (d := int(input())) != 0:
#     if d % 2 == 0:
#         s += d
# print(s)


# s = 1
# while (d := int(input())) > 0:
#     if d % 3 == 0:
#         s *= d
# print(s)


# def send_print():
#     text = 'Привет, привет'
#     print(text)
#
#
# send_print()


# def send_massage(x):
#     print(f"Min = {min(x)}, max = {max(x)}, sum = {sum(x)}")
#
#
# send_massage(list(map(int, input().split())))


# def perimeter(a, b):
#     per = 2 * (a + b)
#     print(f"Периметр прямоугольника, равен {per}")
#
#
# perimeter(*map(int, input().split()))


# def check_email(email):
#     rus_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя!?#$&*+=^%"
#     has_russian = any(char.lower() in rus_alphabet for char in email)
#
#     if email.count('@') != 1 or email.count('.') != 1 :
#         print('НЕТ')
#     elif has_russian:
#         print('НЕТ')
#     else:
#         print('ДА')
#
# check_email(input())


# def reverse_words(text):
#     words = text.split(' ')
#     reversed_words = [word[::-1] for word in words]
#
#     return ' '.join(reversed_words)
#
# reverse_words('This is an example!')


# def get_sqrt(x):
#     res = None if x < 0 else x ** 0.5
#     return res
#
#
# a = get_sqrt(49)
# print(a)


# def f(a, b):
#     if a > b:
#
#         return a - b
#
#     elif a == b:
#
#         return a
#
#     else:
#
#         return b - a
#
#
# print(f(5, 6))


# def get_sq(x):
#     return x**2
#
# print(get_sq(float(input())))


# def is_triangle(a, b, c):
#     if a < b + c and b < c + a and c < b + a:
#         return True
#     else:
#         return False
#
# print(is_triangle(3, 4, 5))


# def is_large(string):
#     if len(string) >= 3:
#         return True
#     return False
#
# print(is_large('Мы'))


# def main(x):
#     if x % 2 == 0:
#         print(x)
#
# x = 0
# while x != 1:
#     x = int(input())
#     main(x)


# def is_odd(x):
#     return x % 2 != 0
#
#
# lst_d = list(map(int, input().split()))
# lst = [i for i in lst_d if is_odd(i)]
#
# print(*lst)


# tp = input().strip()
#
# #здесь продолжайте программу
#
# if tp == 'RECT':
#     def get_sq(a , b):
#         return a * b
# if tp != 'RECT':
#     def get_sq(a):
#         return a*a
#
#
# print(get_sq(10))


# def bool_check(city):
#     if len(city) < 6:
#         return False
#     else:
#         return True
#
#
# cities = list(map(str, input().split()))
#
# lst = [i for i in cities if bool_check(i)]
# print(*lst)


# def main(i):
#     return (i, len(i))
#
# cities = list(map(str, input().split()))
#
# d = {i : l for i, l in map(main, cities)}
#
# a = sorted(d, key=d.get)
# print(d)

#
# digs = list(map(int, input().split()))
#
# def min_an_max(a, b):
#     return a * b
#
# print(min_an_max(max(digs), min(digs)))


# import time
#
# def get_nod(a,b):
#     while a != b:
#         if a > b:
#             a -= b
#         elif a < b:
#             b -= a
#     return a
#
#
# def test_nod(func):
#     a = 28
#     b = 35
#     res = func(a, b)
#     if res == 7:
#         print("test1 = ok")
#     else:
#         print("test1 = fail")
#
#
#     a = 100
#     b = 1
#     res = func(a, b)
#     if res == 1:
#         print("test2 = ok")
#     else:
#         print("test2 = fail")
#
#
#     a = 2
#     b = 100000000
#     st = time.time()
#     res = func(a, b)
#     et = time.time()
#     dt = et - st
#     if res == 2 and dt < 1:
#         print("test3 = ok")
#     else:
#         print("test3 = fail")
#
# test_nod(get_nod)


# import time
#
# def get_nod(a,b):
#     while min(a,b) > 0:
#         a, b = b, a%b
#     return max(a,b)
#
#
# def test_nod(func):
#     a = 28
#     b = 35
#     res = func(a, b)
#     if res == 7:
#         print("test1 = ok")
#     else:
#         print("test1 = fail")
#
#
#     a = 100
#     b = 1
#     res = func(a, b)
#     if res == 1:
#         print("test2 = ok")
#     else:
#         print("test2 = fail")
#
#
#     a = 2
#     b = 100000000
#     st = time.time()
#     res = func(a, b)
#     et = time.time()
#     dt = et - st
#     if res == 2 and dt < 1:
#         print("test3 = ok")
#     else:
#         print("test3 = fail")
#
# test_nod(get_nod)


# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
# a, b = map(int, input().split())
# print(gcd(a, b))


# def get_rect_value(l, w, tp = 0):
#     if tp == 0:
#         return 2 * (l + w)
#     else:
#         return l * w


#
# def check_password(string, chars = '$%!?@#'):
#     if any(char in chars for char in string) and len(string) >= 8:
#         return True
#     else:
#         return False
#
#
# print(check_password(string ='12345678!'))


# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# def translit(string, sep='-'):
#    result = []
#    for c in string:
#        if c in t:
#            result.append(t[c])
#        else:
#            result.append(c)
#    return ''.join(result).replace(' ', sep)
#
#
# res = input().lower()
# print(translit(res))
# print(translit(res,sep='+'))


# def tagify(string, tag = "h1",up = True):
#     if up:
#         tag1 = '<' + tag.upper() + '>'
#         tag2 = '</' + tag.upper() + '>'
#     else:
#         tag1 = '<' + tag + '>'
#         tag2 = '</' + tag + '>'
#     result = f"{tag1}{string}{tag2}"
#     return result
#
# res = input()
# print(tagify(res, tag = "div"))
# print(tagify(res, tag = "div", up = False))


# def get_even(*numbers):
#     return [n for n in numbers if n % 2 == 0]
#
# print(*get_even(*map(int, input().split())))


# def get_biggest_city(*cities):
#     return max(cities, key=lambda city: len(city))
#
# print(get_biggest_city(*map(str, input().split())))


# def get_data_fig(*N, **kwargs):
#     res = [sum(N)]
#     if 'tp' in kwargs:
#         res.append(kwargs['tp'])
#     if 'color' in kwargs:
#         res.append(kwargs['color'])
#     if 'closed' in kwargs:
#         res.append(kwargs['closed'])
#     if 'width' in kwargs:
#         res.append(kwargs['width'])
#     return tuple(res)
#
#
# n = list(map(int, input().split()))
#
# print(get_data_fig(*n))
# print(*get_data_fig(*n, tp = True ))
# print(*get_data_fig(*n, tp = True, color = 7))
# print(*get_data_fig(*n, tp = True, color = 7, closed = False, width = 2.0))


# def verify(lst2D):
#     N = len(lst2D)
#     M = len(lst2D[0]) if N > 0 else 0
#
#     is_isolate = True
#
#     for y in range(N):
#         for x in range(M):
#             if lst2D[y][x] == 1:
#                 has_neighbor = False
#
#                 if y + 1 < N and lst2D[y+1][x] == 1:
#                     has_neighbor = True
#                 if x + 1 < M and lst2D[y][x+1] == 1:
#                     has_neighbor = True
#                 if y + 1 < N and x + 1 < M and lst2D[y + 1][x + 1] == 1:
#                     has_neighbor = True
#                 if y > 0 and lst2D[y - 1][x] == 1:
#                     has_neighbor = True
#                 if x > 0 and lst2D[y][x - 1] == 1:
#                     has_neighbor = True
#                 if y > 0 and x > 0 and lst2D[y - 1][x - 1] == 1:
#                     has_neighbor = True
#
#                 if has_neighbor:
#                     is_isolate = False
#                     return is_isolate
#
#     return is_isolate
#
# print(verify([[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]))


# *lst, x, y, z = list(map(int, input().split()))
# print(*lst)


# cities = input().split()
# cities = *cities,
# print(cities)

#
# a, b = input().split()
#
# print(*range(int(a), int(b) + 1))


# s = map(float,(input().split()))
# c = input().split()
#
# print(*s, *c)


# menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# lst_in = ['Города=about-cities', 'Машины=read-of-cars', 'Самолеты=airplanes']
# menu = {**menu, **dict([i.split("=") for i in lst_in])}
#
#
# gallows_states = [
#     # 0 ошибок: пусто
#     [
#         "   ____",
#         "  |    |",
#         "  |",
#         "  |",
#         "  |",
#         "  |",
#         "__|__"
#     ],
#     # 1 ошибка: голова
#     [
#         "   ____",
#         "  |    |",
#         "  |    O",
#         "  |",
#         "  |",
#         "  |",
#         "__|__"
#     ],
#     # 2 ошибки: туловище
#     [
#         "   ____",
#         "  |    |",
#         "  |    O",
#         "  |    |",
#         "  |",
#         "  |",
#         "__|__"
#     ],
#     # 3 ошибки: левая рука
#     [
#         "   ____",
#         "  |    |",
#         "  |    O",
#         "  |   /|",
#         "  |",
#         "  |",
#         "__|__"
#     ],
#     # 4 ошибки: правая рука
#     [
#         "   ____",
#         "  |    |",
#         "  |    O",
#         "  |   /|\\",
#         "  |",
#         "  |",
#         "__|__"
#     ],
#     # 5 ошибок: левая нога
#     [
#         "   ____",
#         "  |    |",
#         "  |    O",
#         "  |   /|\\",
#         "  |   /",
#         "  |",
#         "__|__"
#     ],
#     # 6 ошибок: правая нога (полная виселица)
#     [
#         "   ____",
#         "  |    |",
#         "  |    O",
#         "  |   /|\\",
#         "  |   / \\",
#         "  |",
#         "__|__"
#     ]
# ]


# import  math
#
# def box_nd(a, b, c, *args, perimetr = True):
#     if perimetr:
#         return sum((a, b, c, *args)) * 2 ** (len((a, b, c, *args)) - 1)
#     else:
#         return math.prod((a, b, c, *args))
#
#
# res1 = box_nd(5, 7, 3)
# res2 = box_nd(5, 7, 3, 5, 2)
# res3 = box_nd(5, 7, 3, 5, 2, perimetr = False)
#
#
# print(res1, res2, res3)


#
# def compare_str(s1, s2, *, ignore_case=True):
#     if ignore_case:
#         return s1.lower() == s2.lower()
#     else:
#         return s1 == s2
#
#
# res1 = compare_str("Python", "python")
# res2 = compare_str(s2="Go", s1="go", ignore_case=False)


# def str_min(s1, s2):
#     if ord(s1[0]) < ord(s2[0]):
#         return s1
#     elif ord(s1[0]) > ord(s2[0]):
#         return s2
#     else:
#         if ord(s1[1]) < ord(s2[1]):
#             return s1
#         else:
#             return s2
#
#
# def str_min3(s1, s2, s3 ):
#     return str_min(str_min(s1, s2), s3)
#
#
# def str_min4(s1, s2, s3, s4 ):
#     return str_min(str_min(str_min(s1, s2), s3), s4)
#
#
# print(str_min("значимый", "подвиг"))
# print(str_min3("это", "заметный", "подвиг"))
# print(str_min4("я", "выполнил", "значимый", "подвиг"))


# def most_popular(people, *,case_sens=False):
#     prepared_people = [i if case_sens else i.lower() for i in people]
#     counts = {}
#     for name in prepared_people:
#         counts[name] = counts.get(name, 0) + 1
#     winner = max(counts, key=counts.get)
#     return (winner, counts[winner])
#
#
# writers = input().split()
# result = most_popular(writers, case_sens=True)


# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False


# i = [5, 10, 3, 8]
# total = 0
# res = [ total := total + n for n in i]
# print(total)


# def max3(a, b, c):
#     return max(a, b, c)


# i = ["кот", "пёс", "кот", "кот", "пёс"]
# count = {}
# for word in i:
#     if word in count :
#         count[word] += 1
#     else:
#         count[word] = 1
# print(count)


# def sum_of_squares(n):
#     sq = [i**2 for i in range(n+1)]
#     return sum(sq)
#
# print(sum_of_squares(4))


# numbers = [4, 7, 1, 9, 3, 8, 5, 2, 6, 10]
# mid_arf = 0
# j = [mid_arf := mid_arf + i for i in numbers]
#
# print(mid_arf/len(numbers))


# str = "Привет мир! Это тестовая строка с пробелами и гласными."
# vowels = "аеёиоуыэюя"
# result = ""
#
# for i in str.lower():
#     if i in vowels:
#         i = '*'
#     if i == ' ':
#         i = '-'
#     result += i
#
# print(result)


# def count_chars(s, chars, return_type= tuple, ignore_case= True):
#     result = []
#     for char in chars:
#         count = 0
#         for i in s:
#             if ignore_case:
#                 if i.lower() == char.lower():
#                     count += 1
#
#             else:
#                 if i == char:
#                     count += 1
#         result.append(count)
#
#     return return_type(result)
#
# print(count_chars("Python is an easy to learn, powerful programming language.", "aouvei", return_type=list, ignore_case= True))


# def merge_dicts(*dict1, ignored_keys=None):
#     if ignored_keys is None:
#         ignored_keys = []
#     result = {}
#
#     for d in dict1:
#         for key, value in d.items():
#             if key not in ignored_keys:
#                 result[key] = value
#     return result
#
# d1 = {"id": 1, "title": "Белая ночь", "author": "Михаил Боярский"}
# d2 = {"id": 2, "name": "Группа крови", "author": "Виктор Цой"}
# d3 = {"id": 3, "track": "На заре", "author": "Альянс"}
#
# songs = merge_dicts(d1, d2, d3, ignored_keys=('id',))


# def symbol_upper(msg, indx=0, *, ignore_indx, to_upper=True):
#     if indx in ignore_indx:
#         return msg
#
#     new_char = msg[indx].upper() if to_upper else msg[indx].lower()
#     msg = msg[:indx] + new_char + msg[indx+1:]
#
#     return msg
#
#
# res1 = symbol_upper("Python is the best language.", ignore_indx=(3, 6))
# res2 = symbol_upper("Python is the best language.", 2, ignore_indx=(3, 6))
#
#
# print(res1)
# print(res2)


# def model(x, w, /, bias=0.0, scale=1.0):
#     predict = sum(_x * _w for _x, _w in zip(x, w)) + bias
#     return predict * scale
#
#
# x = [1, 0.4, -2.5]
# w = [0.4, -1.5, 0.2]
#
# res1 = model(x, w)
# res2 = model(x, w, scale=2.0, bias=-1.5)
# res3 = model(x, w, 0.5)


# def is_right_tr (a,b,c,/,precision=0.001):
#     diff = abs(c ** 2 - (a ** 2 + b ** 2))
#     diff2 = abs(a ** 2 - (b ** 2 + c ** 2))
#     diff3 = abs(b ** 2 - (a ** 2 + c ** 2))
#
#     return min(diff,diff2,diff3) < precision
#
# side_a, side_b, side_c = map(float, input().split())
#
# result = (is_right_tr(side_a,side_b,side_c))

#
# def verify_password(psw, /,chars = "@#!*", min_length=8):
#     if len(psw) < min_length:
#         return False
#     if not any(c in chars for c in psw):
#         return False
#     ru_litter = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя"
#     if any(c in ru_litter for c in psw.lower()):
#         return False
#
#     return True
#
# password = input()
# result = verify_password(password, chars="0123456789", min_length=10)

# phone_number = input()
# def check_phone(phone, format_phone="8(xxx)xxx-xx-xx" , /,format_symbol='x' ):
#     if len(phone) != len(format_phone):
#         return False
#
#     for num_phone, num_format in zip(phone, format_phone):
#         if num_format == format_symbol:
#             if not num_phone.isdigit():
#                 return False
#         else:
#             if num_phone != num_format:
#                 return False
#
#     return True
#
#
# result = check_phone(phone_number, '+7(***)*** ****', '*')


# def rcs(x): # Изначально вызывается первая функция
#     print(f"down: x = {x}")
#     rcs2(x - 1) # Отсюда вызывается rcs2
#     print(f"up: x = {x}")
#
#
# def rcs2(x):
#     print(f"down: x = {x}")
#     rcs3(x - 1) # Отсюда вызывается rcs3
#     print(f"up: x = {x}")
#
#
# def rcs3(x):
#     print(f"down: x = {x}")
#     print(f"up: x = {x}")
#
#
# rcs(3)


# def rcs(x):
#     print(f"down: x = {x}")
#     if x > 1:
#         rcs(x - 1)
#     print(f"up: x = {x}")
#
# rcs(3)


# def get_rec_N(N):
#     if N > 1:
#         get_rec_N(N - 1)
#     print(N)
#
# get_rec_N(10)


# def get_rec_sum(nums):
#     if not nums:
#         return 0
#     return nums[0] + get_rec_sum(nums[1:])
#
#
# numbers = list(map(int, input().split()))
# print(get_rec_sum(numbers))

# N = int(input())
#
# def fib_rec(N, f):
#     if N  > len(f):
#         f.append(f[-1] + f[-2])
#         fib_rec(N, f)
#     return f
#
# result = fib_rec(N, [1, 1])
# print(result)


# def largest_prime_factor(num):
#     d = 2
#     while d * d <= num:
#         if num % d == 0:
#             num //= d
#         else:
#             d += 1
#     return num
#
#
# print(largest_prime_factor(20))


# palin = max(l * i for l in range(999, 99, -1) for i in range(999, 99, -1) if (s := str(l * i)) == s[::-1])
#
# print(palin)


#
# n = 20
# while not all(n % i == 0 for i in range(1, 21)):
#     n += 20
# print(n)


# n = int(input())
#
# def fact_rec(n, a = 1):
#     if n <= 1:
#         return a
#     return fact_rec(n - 1, a * n)
#
#
# print(fact_rec(n))


# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
#
#
# def get_line_list(d,a=None):
#     if a is None:
#         a = []
#     for k in d:
#         if type(k) is list:
#             get_line_list(k,a)
#         else:
#             a.append(k)
#     return a
#
# print(get_line_list(d))

#
# n = int(input())
#
# def get_path(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return get_path(n-1) + get_path(n-2)
#
#
# print(get_path(n))


# lst = list(map(int, input().split()))
#
# def merge_sort(lst):
#     result = []
#     i = j = 0
#     if len(lst) <= 1:
#         return lst
#     else:
#         mid = len(lst) // 2
#         left, right = lst[:mid], lst[mid:]
#         left = merge_sort(left)
#         right = merge_sort(right)
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 result.append(left[i])
#                 i = i + 1
#             else:
#                 result.append(right[j])
#                 j = j + 1
#         result += left[i:]
#         result += right[j:]
#     return result
# print(*merge_sort(lst))

#
# get_sq = lambda a: a * a
#
# print(get_sq(10))


# get_div = lambda a, b: a / b if b > 0 else None
#
# print(get_div(6, 5))
# print(get_div(1, 2))

# x = float(input())
# a = lambda x: abs(x)
# print(a(x))

# s = input()
# check = lambda s: True if 'ra' in s else False
#
# print(check(s))

# s = list(map(int, input().split()))
#
# def filter_lst(it, key=None):
#     if key is None:
#         return tuple(it)
#
#     res = ()
#     for x in it:
#         if key(x):
#             res += (x,)
#
#     return res
#
#
# print(*filter_lst(s))
# print(*filter_lst(s, lambda x: x < 0))
# print(*filter_lst(s, lambda x: x >= 0))
# print(*filter_lst(s, lambda x: 3 <= x <= 5))


# WIDTH = int(input())
#
#
# def func1():
#     global WIDTH
#     WIDTH += 1
#     return WIDTH
#
#
# print(func1())


# def func1():
#     msg = input()
#
#
#     def func2():
#         nonlocal msg
#         msg = input()
#         print(msg)
#
#
#     func2()
#     print(msg)
#
#
# func1()


#
# def create_global(x):
#     global TOTAL
#     TOTAL = x


# def counter_add():
#     def counter_sub(i):
#         return i + 5
#     return counter_sub
# x = counter_add()
# k = int(input())
# print(x(k))

#
# def counter_add(n):
#     def counter_sub(i):
#         return i + n
#     return counter_sub
#
#
# k = int(input())
# cnt = counter_add(k)
# print(cnt(2))


# def say_name(name):
#     def say_tag(tag):
#         print(f"<{tag}>{name}</{tag}>")
#
#     return say_tag
#
# y = input()
# x = input()
# f = say_name(x)
# f(y)


#
# def str_collection(tp):
#     numbers = [int(x) for x in tp]
#     def list_or_tuple(x):
#         if x == 'list':
#             print(numbers)
#         else:
#             print(tuple(numbers))
#     return list_or_tuple
#
#
# z = input()
# y = input().split()
#
# f = str_collection(y)
# f(z)


#
# def get_sq(width, height):
#     return width * height
#
#
# def func_show(func):
#     def wrapper(w, h):
#         res = func(w, h)
#         print(f"Площадь прямоугольника: {res}")
#         return res
#     return wrapper
#


# menu = input()
#
# def show_menu(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         for i, item in enumerate(result):
#             print(f'{i + 1}. {item}')
#
#
#     return wrapper
#
#
# @show_menu
# def get_menu(s):
#     items = s.split()
#     return items
#
#
# get_menu(menu)


# def lst_dec(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         lst = sorted([i for i in result])
#         return lst
#     return wrapper
#
#
# @lst_dec
# def get_list(s):
#     items = s.split()
#     return [int(x) for x in items]
#
#
# s = input()
# lst = get_list(s)
# print(*lst)

#
# def reverse_words(text):
#     new_text = [i[::-1] for i in text.split(' ')]
#     return " ".join(new_text)
#
# print(reverse_words(input()))


# import math
#
#
# def square_area(a):
#     return (4 * pow(a,2))/ pow(math.pi,2)
#
#
# print(square_area(2))
# print(square_area(0))
# print(square_area(14.05))
# print(square_area(1))


# def jumping_number(number):
#     number = int(number)
#     if number < 10:
#         return 'Jumping!!'
#     if number >= 10:
#         x = list(map(int, str(number)))
#         for i in range(len(x) - 1):
#             if abs(x[i] - x[i + 1]) == 1:
#                 continue
#             else:
#                 return 'Not!!'
#         return 'Jumping!!'
#     else:
#         return 'Not!!'
#
# print(jumping_number(9))
# print(jumping_number(79))
# print(jumping_number(23))
# print(jumping_number(556847))
# print(jumping_number(432101212))


# def jumping_number(number):
#     digits = list(map(int, str(number)))
#     new_num = all(abs(a - b) == 1 for a, b in zip(digits, digits[1:]))
#     if new_num:
#         return 'Jumping!!'
#     else:
#         return 'Not!!'

# str1 = input(str)
# str2 = input(str)
#
# def decorator(func):
#     def wrapper(*args,**kwargs):
#         result = func(*args,**kwargs)
#         return dict(result)
#     return wrapper
#
# @decorator
# def my_func(str1, str2):
#     new_str = [(a, b) for a, b in zip(str1.split(), str2.split())]
#     return new_str
#
#
# d = my_func(str1, str2)
# print(*sorted(d.items()))

#
# s = input().lower()
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         while '--' in result:
#             result = result.replace('--', '-')
#         return result
#
#     return wrapper
#
# @decorator
# def convert_ru_to_eng(s,t):
#     new_s = [t[i] if i in t else i for i in s]
#     return ''.join(new_s).replace(' ', '-')
#
# print(convert_ru_to_eng(s,t))


#
# def two_sort(array):
#     array = sorted(array)
#     return '***'.join(array[0])
#
# print(two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"]))

# from math import ceil
#
# fl = float(input())
# print(ceil(fl))


# from math import floor
#
# fl = float(input())
#
# print(floor(fl))


# from math import factorial as fact
#
#
# def factorial(n):
#     p = 1
#     for i in range(2, n+1):
#         p *= i
#
#     print("my factorial")
#     return p


# from random import seed, randint
#
# seed(1)
# print(randint(10, 50))
#

# from random import random as rnd, seed
#
# seed(10)
# print(round(rnd(), 2))


# def find_quarter_notes(time_signature):
#     from math import floor
#     up_quarter, down_quarter = map(int, time_signature.split('/'))
#     if down_quarter <= 0 or (down_quarter & (down_quarter - 1)) != 0:
#         return None
#     else:
#         result_quarter = floor(up_quarter * 4 / down_quarter)
#         return result_quarter


# def vert_mirror(strng):
#     new_strng =  strng.split('\n')
#     reversed_strng = [i[::-1] for i in new_strng]
#     return "\n".join(reversed_strng)
#
#
#
# def hor_mirror(strng):
#     new_strng =  strng.split('\n')
#     reversed_strng = new_strng[::-1]
#     return "\n".join(reversed_strng)
#
# def oper(fct, s):
#     return fct(s)
#
#
# print(vert_mirror('abcd\nefgh\nijkl\nmnop'), hor_mirror('abcd\nefgh\nijkl\nmnop'))


#
# var_a = 5
# var_b = 7
# var_c = sum(var_a, var_b)


#
# total = 5
# count = -4.3
#
# total += 3
# count -=  1.2


# x, y = map(int, input().split())
#
# x /= 2
# y *= 3
#
# import random
# import string
#
# def generate_password(length = 8):
#     alphabet = string.ascii_letters + string.digits
#     result = ''.join(random.choices(alphabet, k=length))
#     return result
#
#
# print(generate_password(10))


# nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# unique_nums = [i**2 for i in list(set(nums))]
#
# print(unique_nums)
#

#
# class Point:
#     def __init__(self, x, y):
#         self.x = x


# f_log = open('log.dat', encoding='utf-8')
# header = f_log.read(3)
# last_data = f_log.readline()
# f_log.close()
# try:
#     with open('diagnostics.csv', encoding = 'utf-8') as file:
#         success_open_file = True
#         header = file.readline()
#         row = file.readline()
# except FileNotFoundError:
#     success_open_file = False


# success_open_file = True
# success_file_operations = True
# last_row = None
#
# try:
#     with open('images/targets.dat', encoding='UTF-8') as filed:
#         last_row = filed.readlines()[-1]
# except FileNotFoundError:
#     success_open_file = False
# except Exception:
#     success_file_operations = False

# try:
#     with open('python/course_text.txt', encoding = 'windows-1251') as file_w:
#         target = 'python'
#
#         while True:
#             current_pos = file_w.tell()
#             chunk = file_w.read(len(target))
#             if not chunk:
#                 break
#             if chunk.lower() == target:
#                 file_w.seek(current_pos)
#                 break
#             file_w.seek(current_pos + 1)
#
# except FileNotFoundError:
#     pass
# msg = input()
# with open('work_data/log_stats.txt', 'a+', encoding='UTF-8') as file:
#     file.write(msg)
#     file.seek(0)
#     header = file.readline().strip()


# a = (x ** 2 for x in range(6))
# print(next(a))
# print(next(a))
# print(next(a))


# gen = (x for x in range(2,10001))
#
# for x in gen:
#     print(x)


# a, b = map(int, input().split())
#
# gen = (x ** 2 for x in range(a, b + 1))
# tp = tuple(gen)
# print(tp)


# a, b = map(int, input().split())
#
# gen = (abs(x) for x in range(a, b + 1))
#
# for idx, x in enumerate(gen):
#     print(x)
#     if idx > 3:
#         break


# a = int(input())
#
# gen = (x ** 3 for x in range(-a, a + 1))
# i = []
# for idx, x in enumerate(gen):
#     i.append(abs(x))
#     if idx == 3:
#         break
#
# print(*i)
#
#
# from string import ascii_lowercase
#
# gen = (i + j for i in ascii_lowercase for j in ascii_lowercase)
# for idx, letter in enumerate(gen):
#     print(letter,  end = ' ')
#     if idx == 49:
#         break
#
# N = int(input())
#
#
# def get_sum(total):
#     for x in range(1,total + 1):
#         yield sum(range(1, x + 1))
#
#
# a = get_sum(N)
# for x in a:
#     print(x)
# def get_list():
#     for x in [1, 2, 3, 4]:
#         yield x
#
#
# d = get_list()
# print(next(d))
# print(next(d))


# N = int(input())
#
# def balak_seq(max_len):
#     balak_1, balak_2, balak_3 = 1, 1, 1
#     idx = 0
#     while idx <= max_len:
#         yield balak_1
#         idx += 1
#         if idx == max_len:
#             break
#         yield balak_2
#         idx += 1
#         if idx == max_len:
#             break
#         yield balak_3
#         idx += 1
#         if idx == max_len:
#             break
#         balak_1 = balak_2 + balak_1 + balak_3
#         balak_2 = balak_1 + balak_2 + balak_3
#         balak_3 = balak_2 + balak_1 + balak_3
# a = balak_seq(N)
# my_list = []
# for x in a:
#     my_list.append(x)
#
# print(*my_list, sep = " ")
#
# import random
# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
#
# def gen_pass(psw_length):
#     for _ in range(5):
#         password = "".join(random.choices(chars, k=psw_length))
#         yield password
#
# N = int(input())
# a = gen_pass(N)
# lst_psw = []
# for _ in a:
#     lst_psw.append(_)


# from string import ascii_lowercase, ascii_uppercase
# chars = ascii_lowercase + ascii_uppercase
# import random
# random.seed(1)
#
# def rndm_mail(max_size):
#     while True:
#         email_chars = []
#         for _ in range(max_size):
#             indx = random.randint(0, len(chars) - 1)
#             email_chars.append(chars[indx])
#         yield "".join(email_chars) + "@mail.ru"
# N = int(input())
# a = rndm_mail(N)
# lst_psw = []
# for _ in range(5):
#     lst_psw.append(next(a))
# print(*lst_psw, sep="\n")


# b = map(int, ['1', '2', '3', '4', '5'])
#
# for _ in b:
#     print(_, end = " ")


# numbers = map(float, input().split())
#
# lst_fl = []
# for _ in range(3):
#     lst_fl.append(next(numbers))
#
# print(*lst_fl)


# numbers = map(lambda x: abs(int(x)), input().split())
# lst = list(numbers)
# print(*lst)
#
#
# lst_in = [
#     '8 11 -5',
#     '3 4 10',
#     '-1 -2 3',
#     '-4 5 6'
# ]
#
# lst2D = list(map(lambda row: list(map(int, row.split())), lst_in))
# print(lst2D)


#
# fvltr = filter(lambda _ : len(_) > 5, cities)
#
# print(*(next(fvltr) for _ in range(3)))
# a = 0o54
#
#
#
#
# print(a)


# s = "Привет мир!"
# second = "Привет мир!"
# print(id(s), id(second))  # Одинаковые
#
# # Но если создать строку динамически:
# third = "Привет " + "мир!"
# print(id(s), id(third))

# s = "Привет мир!" * 10000
# second = "Привет мир!"
# print(id(s), id(second))
#
# seen = {s, second, 321, "dsdasd", [1, 2, 3]}


# def function(a):
#     # a.append(1)
#     # print(a, args, kwargs)
#     # a = [] if a is None else 0
#     # a = 34
#     #
#     # def func ():
#     #     print(a)
#     #     function()
#     # func()
#     #print(a())
#
#
# def default():
#     return True
#
#
#
# function(default)


# result = [x ** 2 for x in string]
# print(result)
# string = [1, 2, 3, 4]
# a = map(lambda x: x ** 2, string)
# print(*a)


# def default():
#     return int(input())
#
# def func(default):
#     def wrapper():
#         a = 'Hello'
#         b = 'Poka'
#         c = default()
#         print(a * c, b * c)
#     return wrapper
#
# my_func = func(default)
# my_func()


#
# d = {}
# d["cat"] = "кот"
# print(hash("cat"))
# print(d["cat"])
# print(hash(42),
# hash((1, 2)))

#
# table_size = 5
# hash_cat = hash("cat")
# hash_dog = hash("dog")
#
# print(f"Хэш cat: {hash_cat}, индекс: {hash_cat % table_size}")
# print(f"Хэш dog: {hash_dog}, индекс: {hash_dog % table_size}")
#
#
# d = {"a": 1}
# print(hash(d))


# def func(len):
#     return [x for x in range(len) if x % 2 == 0]
#
#
# print(func(10))
#
#
# def test():
#     assert func(10) == [0, 2, 4, 6, 8]
#
# print(test())

#
# import random
#
# a = random.randint(1,10)
#
# print(a)


lst = [3, 4, 5, -4, 0, 3, 4, 0]

# i = []
# v = []
# for x in lst:
#     if x == 0:
#         i.append(x)
#     else:
#         v.append(x)
#
#
# print(v + i)
# def func(f):
#     null = [x for x in f if x == 0]
#     new_lst = [x for x in f if x != 0]
#     return new_lst + null
# print(func(lst))

#
#
# def some_foo(int_list):
#     new_list = []
#     counter_zero = 0
#     for i in int_list:
#         if i == 0:
#             counter_zero += 1
#         else:
#             new_list.append(i)
#     for i in range(counter_zero):
#         new_list.append(0)
#     return new_list


# cmd = 'top'
#
# match cmd:
#     case 'top':
#         print("вверх")


# def some_foo(int_list):
#     new_list = []
#     counter_zero = 0
#     for i in int_list:
#         match i:
#             case 0:
#                 counter_zero += 1
#             case _:
#                 new_list.append(i)
#     for i in range(counter_zero):
#         new_list.append(0)
#     return new_list
# print(some_foo([1,3,4,0,3,-1,-3,0,3,1]))
# i, j = 1, 2
# while i < 4:
#     while j < 4:
#         print(i, j)
#         j += 1
#     i += 1
