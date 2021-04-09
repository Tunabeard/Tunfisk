height = float(input("Введите ваш рост (см): ")) / 100
mass = float(input("Введите вашу массу (кг): "))
bmi = round(mass / height ** 2)
print("20" + "=" * (bmi - 21) + "|" + "=" * (49 - bmi) + "50")