import random
import time
print("SMC Calculator v1.3.5")
print("Загрузка технологий...")
print()
modules = [
    "SevenMemoryCells (SMC)",
    "Memory All Delete (MAD)",
    "NotebookMemoryCell (NMC)",
    "Константы: π, e, τ, φ, c, g",
    "Графический интерфейс загрузки"
]
total = len(modules)
for i, module in enumerate(modules, 1):
    bar = "█" * i + "░" * (total - i)
    print(f"\r[{bar}] {i}/{total} {module}", end="")
    time.sleep(1) 
print()
print("\n✅ Все технологии загружены!")
print()
print("""
╔═══════════════════════════════════════════════════╗
║     SMC Calculator                               ║
║     SevenMemoryCells Technology (SMC)            ║
║     + MAD (Memory All Delete)                    ║
║     + NMC (NotebookMemoryCell)                   ║
║     + NMCD (NotebookMemoryCellDelete)            ║
╚═══════════════════════════════════════════════════╝
""")
dzl=' '
di=0
d=0
dqk=0
dck=0
ds=0
dp=0
dr=0
ls=299792458
g=9.80665
fi=1.618033988749895
pi= 3.141592653589793
e=2.718281828459045
tay=6.283185307179586
def zam(text):
    text=text.replace('пи' , str(pi))
    text=text.replace('фи' , str(fi))
    text=text.replace('тау' , str(tay))
    text=text.replace('же' , str(g))
    text=text.replace('скорость света' , str(ls))
    text=text.replace('е' , str(e)) 
    text=text.replace('память степени' , str(ds))
    text=text.replace('память десятичная' , str(di))
    text=text.replace('память' , str(d))
    text=text.replace('память рандом' , str(dr))
    text=text.replace('память корня квадрата' , str(dqk))
    text=text.replace('память корня куба' , str(dck))
    text=text.replace('память процент' , str(dp))
    text=float(eval(text))
    return text
while True:
    a=input("режим I перевод дроби в десятичную S возведение в степень R рандом U обычный QK корень квадрата CK корень куба % проценты M посмотреть память MAD очистка всей памяти Z заметки  ZD очистка заметок E выход")
    if a=="S":
        bi=input("число:")
        ps=input("степень:")
        b=zam(bi) 
        p=zam(ps)
        ds=(b**p)
        print(ds)
    elif a == "I":
        bi=input ('числитель можно использовать число пи тау фи же скорость света и ейлера(е)')
        b=zam(bi)
        ps=input ("знаменатель можно использовать число пи тау фи же скорость света и ейлера(е)")
        p=zam(ps)
        di=b/p
        print(di)
    elif a == "Z":
        if dzl == " ":  
            dzl = input('заметки:')
        else:
            print(dzl)
    elif a=="ZD":
        dzl=' '
        print('заметки очищены')
    elif a=="R":
        c=random.randint(0,10000)
        print (c)
        dr=c
    elif a=='%':
        bi=input ("число:")
        b=zam(bi)
        ps=input ("процент")
        p=zam(ps)
        dp=b*p/100
        print(dp)
    elif a=="U":
        bi=input ("пример можно использовать число пи тау фи же скорость света и ейлера(е)")
        b=zam(bi)
        print (b)
        d=b
    elif a=="QK":
        bi=input ("можно использовать число пи тау фи же скорость света и ейлера(е)")
        b=zam(bi)
        if b>0:
            dqk=(b**0.5)
            print (dqk)
        else:
            print("ошибка отрицательное число")
    elif a=="CK":
        bi=input ("можно использовать число пи тау фи же скорость света и ейлера(е)")
        b=zam(bi)
        dck=(b**(1/3))
        print (dck)
    elif a=='M':
        print('память:', d, 'память рандом:', dr, 'память степени:', ds, 'память процент:', dp, 'память корня квадрата:', dqk, 'память корня куба:', dck,'память десятичная:', di)
    elif a=='MAD':
        d=0
        dr=0
        di=0
        ds=0
        dp=0
        dqk=0
        dck=0
        print('память очищена')
    elif a=="67":
        print ("67"*10000)
    elif a=="E":
        break
    else:
        print ("ошибка")
