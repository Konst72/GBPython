list = [2.5, 'alfa', 15,complex(6, 8),[2, 4, 'k'], (7, 1.9),{'prima',2}, False, {1:'one', 9:'nine'} ]
print(list)
for i,v in enumerate (list,1):
    print(f"{i}, {v} - {type(v)}")

