szamok=[12,10,32,3,66,17,42,99,20]
#kiíratas
print(szamok)
#lista bejárása
for elem in szamok:
      print(elem)
#lista számainak négyzete
print('Négyzetük:')
for pista in szamok:
      print(pista*pista)
#lista számainak összege: összegzés tétele
osszeg=0
for szam in szamok:
      osszeg=osszeg+szam
print('A lista számainak összege:',osszeg, sep=' ')
#lista elemeinek szorzata
szorzat=1
for ede in szamok:
      szorzat=szorzat*ede
print('A lista számainak szorzata:',szorzat, sep=' ')
#lista elemeinek átlaga
#1. módszer
elemszam=len(szamok)
atlag=osszeg/elemszam
print('A lista számainak átlaga:',atlag,sep=' ')
#2. egyszerűbben
print('Átlaguk:')
print(sum(szamok)/len(szamok))













