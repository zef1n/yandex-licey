# Самые большие
obch_mosh = 0
count = 0
while True:
    values = input()
    if values == "FINISH":
        break
    if values.replace(".", "", 1).isdigit():
        value = float(values)
        if value > 100:
            obch_mosh += value
            count += 1
    else:
        print("Ошибка ввода. Введите число или FINISH.")

if count > 0:
    sr_mosh = obch_mosh / count
    print(sr_mosh)
else:
    print("Не введено ни одного числа больше 100.")

# Космический лес
number_pl = int(input())
for number_pl2 in range(1, number_pl + 1):
    sever_str = input()
    yg_str = input()
    yg_luchs = list(map(int, yg_str.split(". ")))
    sever_luchs = list(map(int, sever_str.split(". ")))
    uniq_luchs = [
        ray for ray in yg_luchs if ray not in sever_luchs and ray <= sever_luchs[-1]
    ]
    if uniq_luchs:
        uniq_luchs = "; ".join(map(str, uniq_luchs))
        print(f"{number_pl2} platform: {uniq_luchs}")
    else:
        print(f"{number_pl2} platform:")
