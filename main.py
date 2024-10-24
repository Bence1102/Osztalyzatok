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
feladatok.savdiagram(programozas_jegyek)
print("")

print("6. feladat:")
feladatok.jegyek_kiir(programozas_jegyek)
print("")

print("7. feladat:")
feladatok.veletlen_jegyek(programozas_jegyek)


