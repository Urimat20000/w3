#def bbs(seed, p, q):
    #while True:
        #seed = pow(seed, 2) % (p * q)
        #yield seed

#f = open("data1.txt", "w")
#c = 0

#for i in bbs(1, 2, 6, 5000):
    #if c < 1000:
        ##f.write(f"{i}, ")
        #print(i)
    #else:
        #break
    #c += 1
##f.close()
    
def bbs(seed, p, q):
    while True:
        seed = pow(seed, 2) % (p * q)
        yield seed
        
#c = 0

#f = open("data5.txt", "w")
#for i in bbs(6599, 271, 870977):
    #if c < 59000:
        #f.write(f"{i % 2}")
        #print(i)
    #else:
        #break
    #c += 1
    
#f.close()