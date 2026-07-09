def require_admin(func):
    def wrapper(user_role):
        if user_role == 'admin':
            return func(user_role)
        else:
            print('Доступ не предоставлен')
            return None
    return wrapper



@require_admin
def delete_database(user_role):
    print("База данных успешно удалена!")
    return "Успех"


print("--- Проверка 1: Заходит админ ---")
result1 = delete_database(user_role="admin")
print(f"Результат функции: {result1}\n")

print("--- Проверка 2: Заходит обычный пользователь ---")
result2 = delete_database(user_role="user")
print(f"Результат функции: {result2}\n")