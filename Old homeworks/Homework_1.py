text = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"

print("1) Количество символов:\n" + str(len(text)))
print("2) Развёрнутый вид:\n" + text[::-1])
print("3) Каждое слово с большой буквы:\n" + text.title())
print("4) Весь текст прописными буквами:\n" + text.lower())
print("5) Количество вхождений \"нд\", \"ам\" и \"о\" соответственно:\n" + str(text.lower().count("нд")) + ", " + str(text.lower().count("ам")) + ", " + str(text.lower().count("о")))
print("6.1) Начинается ли строка с \"Hello, world!\":\n" + str(text.lstrip().startswith("Hello, world!")))
print("6.2) Заканчивается ли строка на \"!\":\n" + str(text.rstrip().endswith("!")))
print("6.3) Где в строке находится слово \"Лондон\":\n" + "Start index:", str(text.find("Лондон")) + ", Finish index:", text.find("Лондон") + len("Лондон"))
print("6.4) Менее дружелюбная строка:\n" + text.replace("друг", "враг"))
print("6.5) Строка для техъ, кому по душе старыйъ языкъ:\n" + "ъ ".join(text.split()).replace(",ъ", "ъ,").replace(".ъ", "ъ.").replace("!ъ", "ъ!").replace("—ъ", "—"))
print("7) Исходная строка:\n" + text)