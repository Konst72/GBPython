my_ctr = input("Введите несколько слов через пробел: ").split()
for i, word in enumerate(my_ctr, 1):
    print(f"{i}. {word[:10]}")
