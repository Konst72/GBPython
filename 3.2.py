def my_list(**kwargs):
    return " ".join(kwargs.values())

print(my_list(имя=input("Имя :"), фамилия =input("фамилия :"), отчество=input("отчество :"),город=input("город :"),страна=input("страна :")))