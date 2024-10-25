import random
def jegyek_atlag(lista):
    atlag:float =0
    db:int=0
    while(db<len(lista)):
        atlag+=lista[db]
        db+=1
    atlag=atlag/db
    return atlag



def osztalyzat_db(lista,szam):
    db = 0
    for i in lista:
        if i== szam:
            db += 1
        i += 1
    return db



def elegtelen_sorszam(lista): #függvény
    i:int=0
    while(i<len(lista)):
        if lista[i] == 1:
            print(f" {i+1}. diák kapott 1-est.")
        i+=1



def savdiagarm(sav_lista): #eljaras
    i:int=0
    while(i<len(sav_lista)):
       print(f"{i}| {sav_lista[i]}")
       i+=1
    


def jegyek_kiir(lista): #eljaras
    i:int=0
    while(i<len(lista)):
        print(f"* {i+1}. diák: {lista[i]} *")
        print("***************")
        i+=1

def veletlen_jegyek(lista): #fuggveny
    lista=[]
    i:int=0
    while(i<17):
        jegy:int=int(random.random()*5+1)
        if(jegy==6):
            jegy=5
        lista.append(jegy)
        i+=1
    return lista


        
                
