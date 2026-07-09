# class Point:
#     color = 'red'
#     circle = 2
#
#
#
# Point.color = 'black'
# Point.circle = 4
#
# print(Point.__dict__)
#
# a = Point()
#
#
# print(getattr(Point, 'color', False))
#
#
# print(hasattr(Point,'prop'))


# class Point:
#     color = 'green'
#     radius = 3
#
# a = Point()
#
# setattr(a, 'color', 'white')
# if hasattr(a, 'color'):
#     print(Point.color)
#     print(a.color)
#     delattr(a, 'color')
#     print(a.color)



class DataBase:
    pk = 1
    title = "Классы и объекты"
    author = "Сергей Балакирев"
    views = 14356
    comments = 12


class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024

setattr(Goods, 'price', 2048)

Goods.inflation = 100


class Car:
    pass


setattr(Car, 'model', 'Тойота')
setattr(Car, 'color', 'Розовый')
setattr(Car, 'number', 'П111УУ77')

class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2

class Dictionary:
    rus = "Питон"
    eng = "Python"


# print(getattr(Dictionary, 'rus_word', False))

class TravelBlog:
    total_blogs = 0
tb1 = TravelBlog()

tb1.name = 'Франция'
tb1.days = 6
TravelBlog.total_blogs += 1

tb2 = TravelBlog()
tb2.name = 'Италия'
tb2.days = 5
TravelBlog.total_blogs += 1


class Figure:
    type_fig = 'ellipse'
    color = 'red'

fig1 = Figure()

fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'

delattr(fig1, 'color')

# print(*fig1.__dict__.keys())


class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'

p1 = Person()
print('job' in p1.__dict__)


