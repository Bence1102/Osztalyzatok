import feladatok

programozas_jegyek=[5,2,3,4,4,5,5,5,1,2,2,3,4,5,5,5,4,3,3]

print("1.feladat:")
print(f"Jegyek átlaga: {feladatok.jegyek_atlag(programozas_jegyek)}")
print("")

print("2-3-as feladat:")
print(f" 5-ös osztálzatok:{feladatok.osztalyzat_db(programozas_jegyek,5)}")
print("")

print("2-3-as feladat:")
print(f" 1-es osztálzatok:{feladatok.osztalyzat_db(programozas_jegyek,1)}")
print("")

print("5. feladat:")
def savdiagarm_segitoFgv(programozas_jegyek): #függvény
    x:int=1
    savdiagaram_lista=[]
    while(x<6):
        x_jegy_db = feladatok.osztalyzat_db(programozas_jegyek,x)
        csillag:str="*"*x_jegy_db
        savdiagaram_lista.append(csillag)
        x+=1
    return savdiagaram_lista
feladatok.savdiagarm(savdiagarm_segitoFgv)
print("")

print("6. feladat:")
feladatok.jegyek_kiir(programozas_jegyek)
print("")

print("7. feladat:")
uj_lista = feladatok.veletlen_jegyek(programozas_jegyek)
print(uj_lista)


