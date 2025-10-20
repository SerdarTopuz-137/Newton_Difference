sayılar=[]

while True:
    k=float(input("değer gir: "))
    if type(k)!=float:
        print(type(k))
        break
    sayılar.append(k)
    a=input("bitir: ")
    if a=="a":
        break
print(sayılar)

def derecebulan(küme):
    k=0
    while True:
        n=len(küme)
        dizin=[]
        kontrolkümesi={""}
        kontrolkümesi.clear()
        for i in range(n-1):
            n=(küme[i+1]-küme[i])
            dizin.append(n)
            kontrolkümesi.add(n)
        küme=dizin
        k+=1
        if len(kontrolkümesi)==1:
            break
    return k

def dizi(küme):
    k=0
    asılküme=küme
    n=len(küme)
    kontrolkümesi={""}
    kontrolkümesi.clear()
    for i in range(n):
        x=küme[i]
        kontrolkümesi.add(x)
    if len(kontrolkümesi)==1:
        a=küme[0]
        print(f"eleman derecesi {0} katsayı {a}")
        dizix=[]
        return dizix
    while True:
        n=len(küme)
        dizin=[]
        kontrolkümesi={""}
        kontrolkümesi.clear()
        for i in range(n-1):
            x=(küme[i+1]-küme[i])
            dizin.append(x)
            kontrolkümesi.add(x)
        print(dizin)
        küme=dizin
        k+=1
        if len(kontrolkümesi)==1 or len(kontrolkümesi)==0:
            if len(kontrolkümesi)==0:
                break
            m=1
            for i in range(k):
               m*=(i+1)
            a=(float(dizin[0]))/m
            break
    print(f"eleman derecesi {k} katsayı {a}")
    dizix=[]
    n=len(asılküme)
    kontrolkümesi={""}
    kontrolkümesi.clear()
    for i in range(int(n)-1):
        dizix.append(int(asılküme[i])-a*((i+1)**k))
        kontrolkümesi.add(int(asılküme[i])-a*((i+1)**k))
    print(dizix)
    return dizix

def işlem(kümeler):
    k=0
    değişmişküme=dizi(kümeler)
    while k!=derecebulan(kümeler):
        değişmişküme=dizi(değişmişküme)
        dizi(değişmişküme)
        k+=1

işlem(sayılar)