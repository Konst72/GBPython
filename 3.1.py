def my_f(s_1, s_2):
    try:
        s_1=int(s_1)
        s_2=int(s_2)
        dif=s_1/s_2
    except ValueError:
        return  "Не является числом"
    except ZeroDivisionError:
        return  "На ноль делить нельзя"
    return round(dif, 3)
print(my_f(input("Введите первое число :"),input("Введите второе число :")))


