num_init = int(input("Введите целое положительное число: "))
max_dig = 0
num = num_init
while num > 0:
    digit = num % 10
    if digit > max_dig:
        max_dig = digit
        if max_dig ==9:
            break
    num = num // 10
print(f"Наибольшая цифра в числе {num_init} равно {max_dig}")

