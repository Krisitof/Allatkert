#Hozz létre egy mappát. Ebbe a mappába rakd bele ezt a fájlt. Készíts mégegy mappát ezen a mappán belül adatbazis néven, abba a mappába pedig rakd bele a fajl1, 2, 3 és 4-et.

fajlhelye="i:\\Downloads\\sd\\"                                                                 #Megadjuk a fájl helyét, hogy ne kelljen mindig begépelni

bekeres_adatai=open(fajlhelye+"bekeres_adatai.txt","r",encoding="UTF-8")                        #Megnyitjuk az adatok fájlt. Olvasunk
jegyek_fajl=open(fajlhelye+"jegyek.txt","r",encoding="UTF-8")                                        #Megnyitjuk jegyket fájlt. Olvasunk
programok=open(fajlhelye+"programok.txt","r",encoding="UTF-8")                                  #Megnyitjuk programok fájlt. Olvasunk

id=1                                                                                            #Az id alapvetően 1, s ahány sor van a bekeres_adatai fájlban, annyival növeljük, mert annyi ember van ahány sor.
for x in bekeres_adatai: 
    id+=1

bekeres_adatai.close()                                                                          #Bezárjuk, mert több adatot nem olvasunk ki.
bekeres_adatai=open(fajlhelye+"bekeres_adatai.txt","a",encoding="UTF-8")                        #Megnyitjuk újra append módban, a fájl végére írunk majd.

print(id)

print("Üdvözöllek az Állatkert jegyvásárlási felületén!")
nev=input("Kérlek add meg a neved:").upper()                                                    #Megadhja a nevét, eltároljuk, capslockkal.
print(nev)
print("1, 2, 3, 4, 5, 6, 7")

nap=int(input("Kérlek add a hét hanyadik napján jönnél:"))                                      #Megadja hanyadik nap jönne.
while nap not in range(1,8):                                                                    #Ameddig a nap nem 1 és 7 között van, addig újra kérjük a napot.
    print("1, 2, 3, 4, 5, 6, 7")
    nap=int(input("Kérlek add a hét hanyadik napján jönnél:"))

print(nap)

hanyan=int(input("Kérlek add meg hány ember jönne:"))                                           #Megadhja hány ember.


print(hanyan)

programok_sorai=programok.readlines()                                                           #A programok_sorai beolvassuk a programok fájl összes sorát.
programok.close()

helyek=int(programok_sorai[nap-1].strip().split(",")[1])                                        #A helyek száma arra a napra: A fájlban 1-7. sor a napokat jelzi. Megnyitom azt az indexű sort amiben a nap van. nap-1. Erről leszedem a \n-t és feldarabolom, majd a darabolás 2. elemét veszem.
if hanyan<helyek:                                                                               #Ha a darabolás 2. eleme nagyobb mint a hanyan, akkor van elég hely.
    helyek -= hanyan                                                                            #A helyek számából levonjuk a hanyan értékét, mert annyi helyet foglalnak el.
    programok_sorai[nap-1] = str(nap)+","+str(helyek)+"\n"                                      #A programok_sorai nap-1. indexű sorát átírjuk az új, már levont helyek számával.

    jegyek_szama= 0                                                                                   #A jegyek_szama alapvetően 0, s amíg a jegyek_szama kisebb mint a hanyan, addig újra kérjük a jegy típusát.
    jegyek_kesz=[]                                                                                     
    hiba=True
    jegyek=jegyek_fajl.readlines()    

    while hiba == True:                                                                                    #Ameddig nem jó a jegyek megadása addig ismétlődjön.
        for _ in jegyek:                                                                                   #Végigmegyünk a jegyek fájl sorain.
            x=_.strip().split(",")                                                                         #Ezeket a sorokat egy változóba helyezzük.
            print("Hány",x[2],"típusú jegyre lenne szükség?")                                              #Ahogy haladunk a sorokon kiírjuk az aktuális sorban található jegy 3. elemét ami a nevét tartalmazza a jegynek.
            mennyiseg=int(input())                                                                         #Bekérjük, hogy az adott típusú jegyből mennyire van szükség.
            jegyek_szama+=mennyiseg                                                                        #Az összesítt jegyek számához hozzáadjuk a jelenlegi lefutáskor megadott mennyiséget
            if jegyek_szama == hanyan:                                                                     #Ha az összes jegy annyi amennyien jönnek hozzáadjuk a most megadott jegy adatait a jegyek_kesz listához, s befejezzük a bekérdezést.
                jegyek_kesz.append(str(x[0])+","+str(x[1])+","+str(x[2])+","+str(mennyiseg))                                               
                hiba = False                                                                    
                break
            if jegyek_szama > hanyan:                                                                      #Ha összesen így már több jegy van, mint amennyien jönnek elvileg jönnének akkor kérje be újra a mennyiséget addig, ameddig nem lesz jó.
                print("Úgy volt, hogy kevesebben jöttök... Kérlek indítsd újra a jegyvásárlást, vagy add meg a helyes számot, köszi!")
                jegyek_szama=0                                                                             #Nullázzuk a jegyek_szama-t
                break                                                                                      #A fájl beolvasás újra indul, mert ugyan ki break-elek belőle, a while ciklusom miatt újra kezdődik.
            if jegyek_szama < hanyan and mennyiseg>0:                                                      #Ha a jegyek_szama kisebb mint amennyien vannak és a mennyiség több mint 1, akkor a jegyek_kesz lista megkapja az adatokat
                jegyek_kesz.append(str(x[0])+","+str(x[1])+","+str(x[2])+","+str(mennyiseg))

    print(jegyek_kesz)
    
else:
    print("Sajnos nincs ennyi hely erre a napra... :(")                                         

programok=open(fajlhelye+"programok.txt","w",encoding="UTF-8")                                  #Megnyitjuk újra a programok fájlt, de most már írni fogunk bele, mert átírjuk a helyek számát. w módban minden korábbi adat törlődik.
programok.writelines(programok_sorai)                                                           #A programok_sorai összes sorát beleírjuk a programok fájlba, így átírva a helyek számát.          

bekeres_adatai.close()
jegyek_fajl.close()
programok.close()