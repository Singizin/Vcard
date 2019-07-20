def simple(c):
    sostav ={2:0}
    i = 2
    while True:
        if c % i == 0:
            sostav.update({i:sostav.get(i)+1})
            #print(i,c)
            if c == i:
                break
            c = c / i
            continue
        else:
            i = i + 1
            sostav.update({i:0})
    #print(sostav)
    return sostav
def razlozh(a,b):
    if a % b == 0:
        return a
    if b % a == 0:
        return b
    m = max(a,b)
    l = min(a,b)
    lsimple = simple(l)
    msimple = simple(m)
    for i in lsimple:
        if i not in msimple:
            msimple.update({i:1})
        else:
            if msimple.get(i)<lsimple.get(i):
                msimple.update({i:msimple.get(i)+1})
    #print(msimple)
    return msimple
def nok(a,b):
    sostav = razlozh(a,b)
    otvet = 1
    for i in sostav.keys():
        print(i,sostav.get(i))
        otvet = otvet * i**sostav.get(i)
    return otvet

print(nok(6,8))