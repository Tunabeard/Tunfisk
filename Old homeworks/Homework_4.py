def check_if_admin(funcname):
    def wrapper_decorator(*args, **kwargs):
        if args[0] == "admin":
            funcname()
        else:
            print("Отказано в доступе.")
    return wrapper_decorator

@check_if_admin
def cash(*args, **kwargs):
    print("На счёте лежит два денег.")

username = input("Введите логин: ")
cash(username)