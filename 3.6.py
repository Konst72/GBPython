def int_func():
    for word in input("Введите буквы на латинице :\n").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <=122:
                chars += 1
        print(word.title() if chars == len(word) else f"{word} -  не являются буквами латинского алфавита!")
int_func()
