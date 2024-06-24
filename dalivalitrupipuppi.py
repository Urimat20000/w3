import math
import scipy
import random
import matplotlib.pyplot as plt
import time

from bbs import bbs
from kiss import kiss

c = 0
temp = []
temp1 = []
tmparr = [[], []]

#Подсчёт времени генерации случайных чисел алгоритмом Блюм Блюм Шуба
start = time.time()
for i in bbs(6599, 271, 870977):
    if c < 1000000:
        temp1.append(i)
        if (c == 1000) or (c == 2000) or (c == 5000) or (c % 10000 == 0):
            tmparr[0].append(time.time() - start)
    else:
        break
    c += 1
    
start = time.time()
time.sleep(1)
#print(time.time() - start)

#Подсчёт времени генерации случайных чисел алгоритмом KISS
start = time.time()
for i in range(1000000):
    temp.append(kiss() % 1)
    if (i == 1000) or (i == 2000) or (i == 5000) or (i % 10000 == 0):
        tmparr[1].append(time.time() - start)    

#print(len(tmparr[0]), len(tmparr[1]))
##f = open("datatt.txt", "a")
#for i in range(1000000):
    #f.write(f"{int(temp[i] % 1 * 10000000 % 2)}")

#for j in range(1000000):
    #f.write(f"{round(temp[j] % 1)}")
#f.close()

#Хи-квадрат с равновероятными отрезками
def mychi2(l):
    N = len(l)
    k = round(1 + math.log(N, 2))
    maxx = max(l)
    arra = []
    arrb = [0 for i in range(k)]
    for i in range(1, k+1):
        arra.append(maxx / k * i)
    arra = [0] + arra
    print()
    #print(arra)
    #print(len(arra))
    #print(arrb)
    #print(k)
    for j in range(k):
        for i in range(N):
            if arra[j] <= l[i] <= arra[j + 1]:
                arrb[j] += 1
    #print(arrb)
    #print(k)
    #print()
    return [1/N*sum(list(map(lambda a: pow(a, 2)/(1/k), arrb))) - N, k]

def mychi2b(l1):
    N = len(l1)
    k = 2
    for i in range(len(l1)):
        #l1[i] = l1[i] % 2
        l1[i] = int(temp[i] % 1 * 10000000 % 2)
    #print(N)
    #print(1/N*sum(list(map(lambda a: pow(a, 2)/(1/2), [l1.count(0), l1.count(1)]))) - N)
    return [1/N*sum(list(map(lambda a: pow(a, 2)/(1/2), [l1.count(0), l1.count(1)]))) - N, k]

res = mychi2(temp[0:50000])
print(res[0]) #Значение статистики хи-квадрат
print(res[1]) #Количество интервалов
print(scipy.stats.chi2.cdf(res[0], res[1] - 1)) #Квантиль

print()

mm = sum(temp) / len(temp) #Выборочное среднее
dd = sum(list(map(lambda a: pow(a - mm, 2), temp)))/len(temp) #Дисперсия
co = pow(dd, 1/2) #Среднеквадратичное отклонение
print(mm, dd, co)

print()

res = mychi2b(temp)
#print(res[0])
#print(res[1])
#print(scipy.stats.chi2.cdf(res[0], res[1] - 1))

#tmtmp = []
#start = time.time()
#for i in range(1000):
    #temp.append(kiss())
#tmtmp.append(time.time() - start)

#start = time.time()
#for i in range(10000):
    #temp.append(kiss())
#tmtmp.append(time.time() - start)

#start = time.time()
#for i in range(50000):
    #temp.append(kiss())
#tmtmp.append(time.time() - start)

#start = time.time()
#for i in range(100000):
    #temp.append(kiss())
#tmtmp.append(time.time() - start)

#start = time.time()
#for i in range(200000):
    #temp.append(kiss())
#tmtmp.append(time.time() - start)

#start = time.time()
#for i in range(500000):
    #temp.append(kiss())
#tmtmp.append(time.time() - start)

#start = time.time()
#for i in range(1000000):
    #temp.append(kiss())
#tmtmp.append(time.time() - start)

#tmtmp1 = []
#c = 0
#start = time.time()
#for i in bbs(6599, 271, 870977):
    #if (c == 1000) or (c == 10000) or (c == 50000) or (c == 100000) or (c == 200000) or (c == 500000):
        #tmtmp1.append(time.time() - start)
        #start = time.time()
    #elif (c == 1000000):
        #tmtmp1.append(time.time() - start)
        #break
    #c += 1
    
#plt.plot([1000, 10000, 50000, 100000, 200000, 500000, 1000000], tmtmp, [1000, 10000, 50000, 100000, 200000, 500000, 1000000], tmtmp1)
#plt.legend(["Blum Blum Shub", "KISS"])
#plt.show()

#print(tmparr[0][0], tmparr[0][25], tmparr[0][52], tmparr[0][77], tmparr[0][102])
#print(tmparr[1][0], tmparr[1][25], tmparr[1][52], tmparr[1][77], tmparr[1][102])
plt.plot([1000, 2000, 5000] + [i for i in range(10000, 1000001, 10000)], tmparr[0], [1000, 2000, 5000] + [i for i in range(10000, 1000001, 10000)], tmparr[1])
plt.legend(["Blum Blum Shub", "KISS"])
plt.show()