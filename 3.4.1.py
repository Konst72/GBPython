def my_f(x,y):
    try:
        x,y = float(x), int(y)
        if x<= 0 or y>0:
            return "Х должен быть больше 0, а Y - меньше. Попробуйте еще раз."
        else:
            res = 1
            for _ in range(abs(y)):
                res /=x
            return f"При возведении Х в степень получилось :{round(res,5)}"
    except ValueError:
        return "Вы ввели не число)"

n1 = input("Введите положительное значение Х -  ")
n2 = input("Введите степень: ")

print(my_f(n1,n2))





