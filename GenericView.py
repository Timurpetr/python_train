# class HotDog:
#     def __init__(self):
#         self.ingredients = ["Сосиска", "Булочка", "Кетчуп", "Горчица"]
#
#     def __getattribute__(self, item):
#         print(type(item))
#         return object.__getattribute__(self, item)
#
#     def __getattr__(self, item):
#         return "Нет"
#
#     def __setattr__(self, key, value):
#         if not isinstance(key, str):
#             raise TypeError("Неверный тип данных")
#
#         # Если присваивают значение в add_ingredient, добавляем его в список
#         if key == "add_ingredient":
#             if isinstance(value, str):
#                 self.ingredients.append(value)
#                 return  # Выходим, чтобы не создавать сам атрибут 'add_ingredient' в объекте
#             else:
#                 raise TypeError("Ингредиент должен быть строкой")
#
#         # Для всех остальных атрибутов сохраняем стандартное поведение
#         object.__setattr__(self, key, value)
#
#
# hd = HotDog()
# hd.add_ingredient = "adsdas"
# hd.add_ingredient = "32233"
# print(hd.ingredients)
# class GenericView:
#     def __init__(self, methods=("GET",)):
#         self.methods = methods
#
#     def get(self, request):
#         return ""
#
#     def post(self, request):
#         pass
#
#     def put(self, request):
#         pass
#
#     def delete(self, request):
#         pass
#
#
# class DetailView(GenericView):
#     def get(self, request):
#         if not isinstance(request, dict):
#             raise TypeError("request не является словарем")
#         if "url" not in request:
#             raise TypeError("request не содержит обязательного ключа url")
#         return f"url: {request['url']}"
#
#     def render_request(self, request, method):
#         if method.upper() not in self.methods:
#             raise TypeError("данный запрос не может быть выполнен")
#         return getattr(self, method.lower())(request)
#
#
# dv = DetailView()
# html = dv.render_request({"url": "https://site.ru/home"}, "GET")
# print(html)


# class CommandHandler:
#     def start(self, data):
#         return f"Запуск: {data}"
#
#     def stop(self, data):
#         return f"Остановка: {data}"
#
#     def pause(self, data):
#         return f"Пауза: {data}"
#
#
# class MyHandler(CommandHandler):
#     def execute(self, command, data):
#         if command not in ("START", "PAUSE", "STOP"):
#             raise TypeError("Неизвестная команда")
#         return getattr(self, command.lower())(data)
#
#
# h = MyHandler()
#
# result = h.execute("START", "двигатель")
# print(result)
# res2 = h.execute("ASSD", "музыка")
# print(res2)
class GenericView:
    def __init__(self, methods=("GET",)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def get(self, request):
        if not isinstance(request, dict):
            raise TypeError("request не является словарем")
        if "url" not in request:
            raise TypeError("request не содержит обязательного ключа url")
        return f"url: {request['url']}"

    def render_request(self, request, method):
        if method not in self.methods:
            raise TypeError("данный запрос не может быть выполнен")
        return getattr(self, method.lower())(request)


dv = DetailView()
html = dv.render_request({"url": "https://site.ru/home"}, "GET")
print(html)
