#Hozz létre egy mappát. Ebbe a mappába rakd bele ezt a fájlt. Készíts mégegy mappát ezen a mappán belül adatbazis néven, abba a mappába pedig rakd bele a fajl1, 2, 3 és 4-et.

bekeres_adatai=open("C:\\Users\\sinko.kristof\\Downloads\\csapatmunka_05.18\\adatbazis\\bekeres_adatai.txt","r",encoding="UTF-8")
jegyek=open("C:\\Users\\sinko.kristof\\Downloads\\csapatmunka_05.18\\adatbazis\\jegyek.txt","r",encoding="UTF-8")
programok=open("C:\\Users\\sinko.kristof\\Downloads\\csapatmunka_05.18\\adatbazis\\programok.txt","r",encoding="UTF-8")

id=1
for x in bekeres_adatai: 
    id+=1

bekeres_adatai.close()
bekeres_adatai=open("C:\\Users\\sinko.kristof\\Downloads\\csapatmunka_05.18\\adatbazis\\bekeres_adatai.txt","a",encoding="UTF-8")

print(id)

print("Üdvözöllek az Állatkert jegyvásárlási felületén!")
nev=input("Kérlek add meg a neved:").upper()
print(nev)
print("1, 2, 3, 4, 5, 6, 7")

nap=int(input("Kérlek add a hét hanyadik napján jönnél:"))
while nap not in range(1,8):
    print("1, 2, 3, 4, 5, 6, 7")
    nap=int(input("Kérlek add a hét hanyadik napján jönnél:"))

print(nap)

hanyan=int(input("Kérlek add meg hány ember jönne:"))

print(hanyan)

programok_sorai=programok.readlines()
programok.close()

helyek=int(programok_sorai[nap-1].strip().split(",")[1])
if hanyan<helyek:
    helyek -= hanyan

    programok_sorai[nap-1] = str(nap)+","+str(helyek)+"\n"
    
else:
    print("Sajnos nincs ennyi hely erre a napra... :(")

programok=open("C:\\Users\\sinko.kristof\\Downloads\\csapatmunka_05.18\\adatbazis\\programok.txt","w",encoding="UTF-8")
programok.writelines(programok_sorai)

bekeres_adatai.close()
jegyek.close()
programok.close()