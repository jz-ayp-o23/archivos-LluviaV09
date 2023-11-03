f = open("beatles.txt","r",enconding="utf8")
for line in f:
    for caracter in line:
        print(repr(caracter), end="")
f.close()
