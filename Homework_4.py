def check_if_admin(funcname):
    def wrappler_decorator(*args, **kwargs):
        if args[0] == "admin":
            funcname()
        else:
            print("Отказано в доступе.")
    return wrappler_decorator

@check_if_admin
def cash(*args, **kwargs):
    print("На счёте лежит два денег.")

username = input("Введите логин: ")
cash(username)