def check_if_admin(funcname):
    def wrapper_decorator(login, *args, **kwargs):
        admins_logins_list = ["admin", "admin001", "the_boss", "sysadmin", "director", "john"]
        if login in admins_logins_list:
            funcname(login, *args, **kwargs)
        else:
            print("Отказано в доступе.")
    return wrapper_decorator

@check_if_admin
def cash(login, *args, **kwargs):
    print("Добро пожаловать, " + login + ". На счёте лежит два денег.")

username = input("Введите логин: ")
cash(username)