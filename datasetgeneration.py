from bbs import bbs
from kiss import kiss

#Генерация датасетов с помощью алгоритма блюм блюм шуба
for i in range(20):
    f = open(f"data\\bbs\\bbsdata{i}.txt", "w")
    c = 0
    for i in bbs(6599, 271, 870977):
        if c < 50000:
            f.write(str(i % 2))
        else:
            break
        c += 1
    f.close()

#Генерация датасетов с помощью алгоритма kiss
for j in range(20):
    f = open(f"data\\kiss\\kissdata{j}.txt", "w")
    for i in range(50000):
        f.write(str(round(kiss() % 1)))
    f.close()
    
#Условие о диапазоне в 5000 между случайными числами можно восполнить в генераторе kiss
#умножением на некоторую константу