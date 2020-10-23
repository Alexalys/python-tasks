km = 0
dist = ""
dist1 = ""
dict1 = {'центральный':0,"северный":1,"восточный":2,"южный":1,"западный":2,"лесной":3,"окружная":3,"гидропарк":3}
office=input("Введите название отделение ")
if office=="центральный":
    print("Вы указали центральный офис")
else:
    print("Расстояние до центрального офиса",dict1[office])

km=dict1[office]
if office!="центральный":
    print("Отделения на таком же расстоянии: ")
    for dist in dict1:
        if dict1.get(dist)==km and office!=dist:
            print(dist)

