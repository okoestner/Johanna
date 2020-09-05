geheimnis = 1
versuch = -1
zeahler = 0

while versuch != geheimnis:
    versuch = int(input("du bist dran: "))
    if versuch < geheimnis:
        print("zu klein")

    if versuch > geheimnis:
        print( "zu groß")

    zeahler = zeahler + 1

print(" super, geschafft in ", zeahler, " versuchen.")