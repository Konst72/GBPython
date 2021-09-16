def int_func(word):
    eng = 'abcdefghijklmnopqrstuvwxyz'
    return word.title() if not set(word).difference(eng) else False
str = input("Введите строку из нескольких слов : ").split()
for a in str:
    res = int_func(a)
    if res:
        print(int_func(a), '')
