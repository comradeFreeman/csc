import math
import os.path


file_name = input("Enter file name: ")
with open(file_name, 'r', encoding='utf-8') as text:
    freq = {}
    count = 0
    for line in text.readlines(): # читаем построчно (здорово экономит ОЗУ, если текст весит, например, 1 Гб)
        for sym in line: # "для каждого символа в строке"
            if sym not in freq.keys(): # если нет такого ключа - создаём
                freq[sym] = 1
            else:
                freq[sym] += 1 # иначе увеличиваем значение ключа
            count+=1 # заодно считаем символы

    for key, value in freq.items(): # перебираем ключи и значения (элементы) словаря
        print(f"{key}: %.10f" % (value)) # выводим ключ и его значение.
        freq[key]/=count # заодно меняем в словаре кол-во на частоту у каждого элемента
    print("Total symbols: " + str(count))

    #entropy = 0
    #for i in freq.keys():
    #    entropy+= -(freq[i] * math.log(freq[i], 2))

    entropy = sum([ -(freq[i] * math.log(freq[i], 2)) for i in freq.keys() ])

    # а можно и так посчитать энтропию. 3 строки против 1-ой, ощутимо :)
    # вначале мы используем генератор списка. его синтаксис в целом такой:
    # [ действие(элемент) for элемент in итерируемый_объект ]  --> список
    # по сути, это перебор элементов любого итерируемого объекта (списки, строки, словари и т.д),
    # совершение над ними каких-то действий (в нашем случае мы подставили элемент в формулу)
    # и занесение результата действий в новый список
    # ну а "sum" - это встроенная функция, которая позволяет посчитать сумму элементов итерируемого объекта.
    # то есть мы ей скормили список из значений формулы, в которую подставлялось каждое значение словаря частот

    print("Entropy: ", entropy)
    print("The quantity of information: ", (entropy * count)/8, "\nFile size: ", os.path.getsize(file_name))

