def sum_num():
    s = 0
    while True:
        m_l = input("Введите числа с пробелами, или z для выхода: ").split()
        for num in m_l:
            if num.lower() == "z":
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print("Для выхода из программы нажмите - z ")
        print(f"Сумма чисел = {s}")
print(sum_num())
