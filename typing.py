import msvcrt
import random
import PyQt5

#hs harf sayısı
def word():
    kelime=""
    hs=random.randint(2,5)
    while hs>0:
        asdf=["a","s","d","f"];
        harf=(asdf[random.randint(0,3)])
        hs-=1
        kelime+=harf
    kelime+=" "
    return kelime
satir=""
for i in range(10):

    satir+=word()


def oyun(text):
    print(text)
    i=0
    while i<len(text):
        key = msvcrt.getch()
        if ord(key) == ord(text[i]):
            i+=1
            print("+1")
oyun(satir)
            
            
