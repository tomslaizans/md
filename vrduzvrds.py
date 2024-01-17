vards=input("Ievadit vardu:")
uzvards=input("ievadit uzvardu:")

kopa=f"{vards} {uzvards}"

with open("ziema.txt", "w", encoding="utf-8") as vrd:
    vrd.write(kopa)


