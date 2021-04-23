all_data = {}

def create_new_user(*args, **kwargs):
    global all_data
    while True:
        login = input("Введите никнейм: ")
        if login in all_data.keys():
            print("Пользователь с таким никнеймом уже зарегистрирован. Введите другой.")
        else:
            break
    sex = input("Введите пол: ")
    height = float(input("Введите рост (см): ")) / 100
    mass = float(input("Введите массу (кг): "))
    all_data[login] = {"Пол": sex, "Рост": height, "Масса": mass}

    # Опционально:
    bmi = round(mass / height ** 2)
    graphic = ["...", "..."]
    for num in range(5, 46):
        if num % 5 == 0:
            graphic.insert(-1, str(num))
        else:
            graphic.insert(-1, "=")
    if bmi - 4 < 0:
        graphic.insert(0, "BMI")
    elif bmi - 4 > len(graphic) - 1:
        graphic.append("BMI")
    else:
        graphic[bmi - 4] = "BMI"
    for item in graphic:
        print(item, end = " ")
    print("\nВаш BMI:", str(bmi) + ". Данные сохранены.")
    if bmi <= 16:
        print("Вам необходимо либо срочно набирать массу, либо срочно набирать рост. Чего-то из этого вам категорически не хватает.")
    elif bmi in range(17, 20):
        print("До нормы не хватает совсем-совсем чуть-чуть. Съешьте там, например, булочку какую-нибудь или закажите пиццу.")
    elif bmi in range(20, 25):
        print("Вы абсолютно в норме. Вам не о чем беспокоиться.")
    elif bmi in range(25, 30):
        print("Ваши показатели слегка выше нормы. Попробуйте на денёк-другой отказаться от набирания массы или от набирания роста.")
    elif bmi in range(30, 35):
        print("Ещё не всё потеряно, но повод для беспокойства есть. Попробуйте поискать в интернете какую-нибудь удобную для вас диету.")
    elif bmi in range(35, 40):
        print("Всё плохо. Ваши показатели заставляют меня волноваться, несмотря на то, что я — компьютер, и я не умею волноваться.")
    else:
        print("Просто удивительно, что вы тратите время на советы компьютерной программы, когда должны тратить время на советы опытного специалиста.")

def list_all_data():
    global all_data
    if len(all_data.keys()) == 0:
        print("Зарегистрированных пользователей нет.")
    else:
        N = 1
        for key, value in all_data.items():
            print(str(N) + ")", key + ":")
            for subkey, subvalue in value.items():
                print(subkey + ":", subvalue)
            N += 1

def show_specific_user():
    global all_data
    specific_user = input("Введите никнейм пользователя, чьи данные вы хотите просмотреть:\n")
    if specific_user in all_data.keys():
        for key, value in all_data[specific_user].items():
            print(key + ":", value)
    else:
        print("Пользователь с таким никнеймом не зарегистрирован.")

def change_user():
    global all_data
    specific_user = input("Введите никнейм пользователя, чьи данные вы хотите изменить:\n")
    if specific_user in all_data.keys():
        while True:
            login = input("Введите никнейм: ")
            if login in all_data.keys():
                print("Пользователь с таким никнеймом уже зарегистрирован. Введите другой.")
            else:
                break
        sex = input("Введите пол: ")
        height = float(input("Введите рост (см): ")) / 100
        mass = float(input("Введите массу (кг): "))
        all_data[login] = {"Пол": sex, "Рост": height, "Масса": mass}
        del all_data[specific_user]
        print("Данные успешно обновлены.")
    else:
        print("Пользователь с таким никнеймом не зарегистрирован.")

def delete_user():
    global all_data
    specific_user = input("Введите никнейм пользователя, чьи данные вы хотите удалить:\n")
    if specific_user in all_data.keys():
        del all_data[specific_user]
        print("Данные успешно удалены.")
    else:
        print("Пользователь с таким никнеймом не зарегистрирован.")

def goodbye():
    print("До новых встреч.")

while True:
    print("Введите 1, чтобы добавить новые данные.")
    print("Введите 2, чтобы просмотреть список имеющихся данных.")
    print("Введите 3, чтобы просмотреть данные конкретного пользователя.")
    print("Введите 4, чтобы изменить данные конкретного пользователя.")
    print("Введите 5, чтобы удалить данные конкретного пользователя.")
    print("Введите 0, чтобы завершить работу с программой.")
    user_request = input()
    print("\n" + "- " * 21 + "\n")
    if user_request == "1":
        create_new_user()
    elif user_request == "2":
        list_all_data()
    elif user_request == "3":
        show_specific_user()
    elif user_request == "4":
        change_user()
    elif user_request == "5":
        delete_user()
    elif user_request == "0":
        goodbye()
        break
    else:
        print("Вы ввели какую-то ерунду.")
    print("\n" + "- " * 21 + "\n")