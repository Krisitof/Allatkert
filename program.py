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
        for _ in jegyek[:5]:                                                                               #Végigmegyünk a jegyek fájl sorain.
            x=_.strip().split(",")                                                                         #Ezeket a sorokat egy változóba helyezzük.
            print("Hány",x[2],"típusú jegyre lenne szükség?")                                              #Ahogy haladunk a sorokon kiírjuk az aktuális sorban található jegy 3. elemét ami a nevét tartalmazza a jegynek.
            mennyiseg=int(input())                                                                         #Bekérjük, hogy az adott típusú jegyből mennyire van szükség.
            jegyek_szama+=mennyiseg                                                                        #Az összesítt jegyek számához hozzáadjuk a jelenlegi lefutáskor megadott mennyiséget
            if jegyek_szama == hanyan:                                                                     #Ha az összes jegy annyi amennyien jönnek hozzáadjuk a most megadott jegy adatait a jegyek_kesz listához, s befejezzük a bekérdezést.
                jegyek_kesz.append(str(x[0])+","+str(x[1])+","+str(x[2])+","+str(mennyiseg))               #Az x lista elemeit egyesével üsszefüzzük, így egy darab sorként majd újra bonthatóak és nem egy listát teszünk a listába.                                
                hiba = False                                                                    
                break
            if jegyek_szama > hanyan:                                                                      #Ha összesen így már több jegy van, mint amennyien jönnek elvileg jönnének akkor kérje be újra a mennyiséget addig, ameddig nem lesz jó.
                print("Úgy volt, hogy kevesebben jöttök... Kérlek indítsd újra a jegyvásárlást, vagy add meg a helyes számot, köszi!")
                jegyek_szama=0                                                                             #Nullázzuk a jegyek_szama-t
                break                                                                                      #A fájl beolvasás újra indul, mert ugyan ki break-elek belőle, a while ciklusom miatt újra kezdődik.
            if jegyek_szama < hanyan and mennyiseg>0:                                                      #Ha a jegyek_szama kisebb mint amennyien vannak és a mennyiség több mint 1, akkor a jegyek_kesz lista megkapja az adatokat
                jegyek_kesz.append(str(x[0])+","+str(x[1])+","+str(x[2])+","+str(mennyiseg))
        if hiba == True:                                                                                   #Ha egyszer végigmentünk az összes lehetőségen és még mindig hiba van írjuk ki, hogy mennyi jegy hiányzik még.
            print("Nem adtad meg az összes esetet, az eddig hozzáadott személyek száma:",jegyek_szama,"/",hanyan)

    print(jegyek_kesz)
    ar=0                                                                                                    #Az ar változót alapvetően 0-ra állítjuk
    for _ in jegyek_kesz:                                                                                   #A jegyek_kesz elemein végigmegyünk, ugye ebben van mindegyik jegytípus és a mennyiség
        x=_.strip().split(",")                                                                              #Szépen feldarabolom az elemeket
        szorzat=int(x[1])*int(x[-1])                                                                        #Összeszorzom a sor 2. elemét az utolsóval a 2. elem az ár, az utolsó, hogy hány ilyen jegy van.
        ar+=szorzat
    print(ar,"Ft a végösszeg.")

    program_bool=input("Szeretnétek programokra menni? Igen/Nem").upper()                                   #Szeretnénk-e programra menni. Addig kérzedem ameddig igen vagy nem a válasz.
    while program_bool != "IGEN" and program_bool != "NEM":
        program_bool=input("Szeretnétek programokra menni? Igen/Nem").upper()
    
    program_nincs=[]                                                                                        #A program_nincs tárolja azokat a sorokat ahol a férőhely x[-1] nulla
    program_ferohely=[]                                                                                     #A program_ferohely tárolja az összes többi program számát és a férőhelyeket
    if program_bool == "IGEN":                                                                              
        print("Az aznap elérhető programok azonosítőja, időpontja, neve és a férőhelyek száma:")
        for _ in programok_sorai:                                                                           #A programok sorait végig lefuttatom
            x=_.strip().split(",")                                                                                  
            if int(x[0]) > nap*10 and int(x[0])<nap*10+10:                                                  #Ha az első elem nagyobb mint a nap*10, de kisebb mint nap*10+10 akkor jó részt vizsgálok. pl. 1. nap 10-20 id-k között nézi, ami jó is, mert 11-19-ig vannak a hétfői programok számozva.
                print(x)
                if int(x[-1]) == 0:                                                                         #Ha a sor utolsó eleme 0 (a ferőhelyek száma), akkor megy a program_nincs listára az id-je
                    program_nincs.append(int(x[0]))
                else:
                    id_ferohely=x[0],x[-1]                                                                  #Ha van férőhely akkor az id és a férőhelyek száma megy a program_ferohely listába.
                    program_ferohely.append(id_ferohely)
        
        program_melyik=int(input("Kérlek add meg annak a programnak a számát amelyikre menni szeretnétek:"))
        while program_melyik in program_nincs:                                                              #Ha a program id-je a program_nincs-ben van akkor nincs férőhely, újra bekérünk.
            print("Akkor nincsen program/teljesen betelt...")
            program_melyik=int(input("Kérlek add meg annak a programnak a számát amelyikre menni szeretnétek:"))

        program_hanyan=int(input("Kérlek add meg mennyien mennétek erre a programra:"))                     #Ha kiválaszotta a programot megkérdezzük hanyan szeretnének jönni, itt van több buktató is, ezeket szűrjük ki.
        while program_hanyan > hanyan:                                                                      #Ha többen szeretnének jönni, mint amennyien vannak akkor az nem jó.
            print("Ennyien nem is jöttök...")
            program_hanyan=int(input("Kérlek add meg mennyien mennétek erre a programra:"))

        program_max=0                                                                                       #A következőben azt fogjuk vizsgálni, hogy van-e elég hely a programon. 
        for x in program_ferohely:                                                                          #Végigmegyek a program_ferohely listán.
            if int(x[0]) == program_melyik:                                                                 #Ha az sor 1. eleme ugyan az, mint a kiválaszott id akkor meg van a program.
                program_max+=int(x[1])                                                                      #Ennek a sornak a 2. elemét hozzáadom a program_max-hoz.

        while program_hanyan > program_max:                                                                 #Ha többen szeretnének jönni mint ahány hely van, akkor az nem jó, addig kérjük ameddig jó nem lesz.
            print("Nincs ennyi férőhely...")
            program_hanyan=int(input("Kérlek add meg mennyien mennétek erre a programra:"))

        for _ in programok_sorai:                                                                           #Végigmegyek a programok_sorai-n.
            x=_.strip().split(",")
            if int(x[0]) == program_melyik:                                                                 #Ha a sor első eleme megyegyezik a programom id-jével akkor meg van a kiválasztott program.
                programok_sorai[program_melyik-1] = str(x[0])+","+str(x[1])+","+str(x[2])+","+str(int(x[-1])-program_hanyan)+"\n"   #Azt a sort ami az id-1. helyen van kicserélem a régi adatokra, de az utoló férőhelyeket tartalmazó elemből kivonom azt amennyien mennének rá.

        print("Köszönjük, itt a jegyetek:")
        
    else:
        print("A jegyed:") #Tartalmazza a nevet, a napot, s az árat.

else:
    print("Sajnos nincs ennyi hely erre a napra... :(")                                         

programok=open(fajlhelye+"programok.txt","w",encoding="UTF-8")                                  #Megnyitjuk újra a programok fájlt, de most már írni fogunk bele, mert átírjuk a helyek számát azon a napon, programon. W módban minden korábbi adat törlődik.
programok.writelines(programok_sorai)                                                           #A programok_sorai összes sorát beleírjuk a programok fájlba, így átírva a helyek számát.          

bekeres_adatai.close()
jegyek_fajl.close()
programok.close()