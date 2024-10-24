def jegyek_atlag(lista):
    atlag:float =0
    db:int=0
    while(db<len(lista)):
        atlag+=lista[db]
        db+=1
    atlag=atlag%db
    return atlag
        
                