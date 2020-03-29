#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      andela
#
# Created:     29.03.2020
# Copyright:   (c) andela 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
class Razlomak(object):
    '''Klasa razlomak'''
    def __init__(self, brojnik, nazivnik = 1):
        if nazivnik == 0: raise Exception('Nazivnik ne moze biti 0')
        self._brojnik = brojnik
        self._nazivnik = nazivnik
    def __str__(self):
        return '%d|%d' % (self._brojnik, self._nazivnik)
    def __inverz__(self):
        return Razlomak(self._nazivnik, self._brojnik)
    def stvori(realni_broj):
        a=str(realni_broj)
        t=a.find(".")
        k=len(a)-1
        n=1
        for i in range (1, k):
            n=n*10
        b=int(a.replace(".", ""))
        return Razlomak(b,n)
print('*** test2 ***')
r1 = Razlomak.stvori(3.14)
print(r1)
r2 = Razlomak.stvori(0.006021)
print(r2)
r3 = Razlomak.stvori(-75.204)
print(r3)

