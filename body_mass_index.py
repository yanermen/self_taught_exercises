body_weight = float(input("Please type your weight: "))
body_height = float(input("Please type your height: "))
bdi = (body_weight / (body_height / 100 * body_height / 100))


def body_mass_index():
    return bdi


print(body_mass_index())

if bdi > 20 and bdi <= 25:
    print("Не стоит волноваться: у вас нормальный вес, который находится в гармонии с миром")
elif bdi >= 26 and bdi <= 30:
    print(
        "Вам стоит начать заботиться о своем организме; у вас имеется небольшой избыток веса. Дальнейшее накопление жира увеличивает риск развития различных болезней и ухудшения общего состояния здоровья")
elif bdi >= 31 and bdi <= 35:
    print(
        "Вы имеете явную склонность к ожирению, поэтому необходимо приложить все усилия, чтобы снизить этот показатель")
else:
    print("У вас ожирение; пора бить тревогу и начинать активно работать над восстановлением былой формы")

body_mass_index()
