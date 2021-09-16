def my_func(x,y):
    try:
        x, y = float(x), int(y)
        a = x ** y
        if y >=0:
            return "Y должен быть целым отрицательным числом "
        else:
            return f"X в степени Y равен : {(a)} "
    except ValueError:
        return "Y должен быть числом "
    return f"Результат равен:{(a)}"

n1 = input("Введите положительное значение Х -  ")
n2 = input("Введите степень: ")

print(my_func(n1,n2))