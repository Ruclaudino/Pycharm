woord = input("Voer het woord in: ")
variant = input("Encryptie of Decryptie : ")
shift = int((input("Voer shift in:")))
lengte = int(len(woord))
woord_2 = ""
decryptie = ord(variant.lower()) == ord("d")
encryptie = ord(variant.lower()) == ord("e")

# For the first letter
for i in range(0, 1):
    # transformating letters into numbers
    var_1 = ord(woord.lower()[i])
    spatie = var_1 == 32
    if decryptie:        # if spatie continue else ( isso é oque quero escrever mas nao esta a ter efeito)
            decryption = var_1 - shift

            # within_limits a-z ?
            if ord("a") <= decryption <= ord("z"):
                resultaat = chr(decryption)
                woord_2 += resultaat
            # smaller than a?
            if decryption < ord("a"):
                n = ord("a") - decryption
                resultaat = chr(123 - n)
                woord_2 += resultaat
    if encryptie:
        encryption = var_1 + shift

        if ord("a") <= encryption <= ord("z"):
            resultaat = chr(encryption)
            woord_2 += resultaat

            # bigger than z?
        if ord("z") < encryption:
            n = encryption - ord("z")
            resultaat = chr(96 + n)
            woord_2 += resultaat

# For other letters
for i in range(1, lengte):
    var_1 = ord(woord.lower()[i])
    if decryptie:      #if spatie: continue else
            # shift every time plus 1
            shift = shift + 1
            decryption = var_1 - shift

            if ord("a") <= decryption <= ord("z"):
                resultaat_2 = chr(decryption)
                woord_2 += resultaat_2

            if ord("a") > decryption > 32:     #  ???? transpforms isnt heving effect
                n = ord("a") - decryption
                resultaat = chr(123 - n)
                woord_2 += resultaat
    if encryptie:
        shift = shift + 1
        encryption = var_1 + shift
        if ord("a") <= encryption <= ord("z"):
            resultaat = chr(encryption)
            woord_2 += resultaat
        elif encryption > ord("z"):
            n = encryption - ord("z")
            resultaat = chr(96 + n)
            woord_2 += resultaat
print("Resultaat:", woord_2)
