def lcg(seed, a, c, m):
    while True:
        seed = (a * seed + c) % m
        yield seed

f = open("data1.txt", "w")
c = 0

for i in lcg(1, 2, 6, 5000):
    if c < 1000:
        f.write(f"{i}, ")
        print(i)
    else:
        break
    c += 1
f.close()