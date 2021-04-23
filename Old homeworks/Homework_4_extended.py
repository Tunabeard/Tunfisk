def check_if_admin(funcname):
    def wrapper_decorator(login, *args, **kwargs):
        admins_logins_list = ["admin", "admin001", "the_boss", "sysadmin", "director", "john"]
        if login in admins_logins_list:
            return funcname(login, *args, **kwargs)
        else:
            return "Отказано в доступе."
    return wrapper_decorator

@check_if_admin
def cash(login, valuta):
    return "Добро пожаловать, " + login + ". На счёте лежит 2 " + valuta + "."

@check_if_admin
def age(login, birtyear):
    age = birtyear - 2000
    return "Уважаемый " + login + ", ваш возраст: " + str(age) + " лет."

username = input("Введите логин: ")
print(cash(username, "USD"))
print(age(username, 2020))