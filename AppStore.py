class AppStore:
    apps = []

    def add_application(self, app):
        AppStore.apps.append(app)

    def remove_application(self, app):
        AppStore.apps.remove(app)

    def block_application(self, app):
        for a in self.apps:
            if a is app:
                a.blocked = True
                return

    def total_apps(self):
        return len(self.apps)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)

print(store.total_apps())  # должно быть 1

# Блокируем
store.block_application(app_youtube)
print(app_youtube.blocked)  # должно быть True

# Удаляем
store.remove_application(app_youtube)
print(store.total_apps())  # должно быть 0
