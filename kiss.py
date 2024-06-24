z = 1234567
w = 2345678
jsr = 3456789
jc = 4567890

def znew():
    global z
    z = 36969 * (z & 65535) + (0xffffffff & (z >> 16))
    return z

def wnew():
    global w
    w = 18000 * (w & 65535) + (0xffffffff & (w >> 16))
    return w
    
def MWC():
    return (0xffffffff & (znew() << 16)) + wnew()
    
def SHR3():
    global jsr
    jsr ^= (0xffffffff & (jsr << 17))
    jsr ^= (0xffffffff & (jsr >> 13))
    jsr ^= (0xffffffff & (jsr << 5))
    return jsr
    
def CONG():
    global jc
    jc = (0xffffffff & (69069 * jc)) + 1234567
    #jc = (0xffffffff & jc)
    return jc
    
def kiss():
    return ((MWC() ^ CONG()) + SHR3()) / 4294967296.0

f = open("datapizdata.txt", "w")
#c = 0

for i in range(10000):
        ##print(kiss() % 1)
        f.write(f"{round(kiss() % 1)}")
f.close()
        
#def kiss(z, w, jc, jsr):
    #z = 36969 * (z & 65535) + (0xffffffff & (z >> 16))
    #print(0xffffffff & (z << 16))
    #w = 18000 * (w & 65535) + (0xffffffff & (w >> 16))
    #jc = 69069 * jc + 1234567
    #jsr ^= (0xffffffff & (jsr << 17))
    #jsr ^= (0xffffffff & (jsr >> 13))
    #jsr ^= (0xffffffff & (jsr << 5))
    #return ((((0xffffffff & (z << 16)) + w) ^ jc) + jsr) / 4294967296.0

#for i in range(100):
    #print(kiss(1234567, 2345678, 3456789, 4567890))